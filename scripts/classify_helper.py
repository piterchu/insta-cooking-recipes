#!/usr/bin/env python3
"""
Assistant de classification de recettes
Aide à analyser les recettes dans TO_BE_CLASSIFIED/ et suggère leur classification
"""

import yaml
from pathlib import Path
import re

class RecipeClassifier:
    def __init__(self, base_path="."):
        self.base_path = Path(base_path)
        self.to_classify_dir = self.base_path / "TO BE CLASSIFIED"

        # Mapping des cuisines vers les dossiers
        self.cuisine_mapping = {
            'japonaise': 'recettes/asiatique/japonais',
            'chinoise': 'recettes/asiatique/chinois',
            'thaï': 'recettes/asiatique/thai',
            'coréenne': 'recettes/asiatique/coreen',
            'vietnamienne': 'recettes/asiatique/vietnamien',
            'française': 'recettes/europeen/francais',
            'italienne': 'recettes/europeen/italien',
            'grecque': 'recettes/europeen/grec',
        }

    def find_unclassified_recipes(self):
        """Trouve toutes les recettes non classées"""
        if not self.to_classify_dir.exists():
            return []

        recipes = []
        for md_file in self.to_classify_dir.glob("*.md"):
            if "README" not in md_file.name:
                recipes.append(md_file)

        return recipes

    def analyze_recipe(self, recipe_path):
        """Analyse une recette et retourne ses métadonnées"""
        with open(recipe_path, 'r', encoding='utf-8') as f:
            content = f.read()

        metadata = None
        title = recipe_path.stem

        # Essayer d'extraire le frontmatter YAML
        if content.startswith('---'):
            yaml_end = content.find('---', 3)
            if yaml_end > 0:
                try:
                    metadata = yaml.safe_load(content[3:yaml_end])
                except:
                    pass

                # Extraire le titre
                rest = content[yaml_end+3:].strip()
                if rest:
                    first_line = rest.split('\n')[0]
                    title = first_line.replace('#', '').strip()

        return {
            'path': recipe_path,
            'title': title,
            'metadata': metadata,
            'has_metadata': metadata is not None
        }

    def suggest_destination(self, recipe_info):
        """Suggère un dossier de destination basé sur les métadonnées"""
        if not recipe_info['has_metadata']:
            return None, "Pas de métadonnées YAML trouvées"

        metadata = recipe_info['metadata']
        cuisine = metadata.get('cuisine', '')

        if cuisine in self.cuisine_mapping:
            dest_folder = self.cuisine_mapping[cuisine]
            return dest_folder, f"Basé sur cuisine: {cuisine}"
        else:
            return 'recettes/autres', f"Cuisine '{cuisine}' non mappée"

    def get_metadata_summary(self, recipe_info):
        """Résume les métadonnées d'une recette"""
        if not recipe_info['has_metadata']:
            return "❌ Aucune métadonnée"

        m = recipe_info['metadata']
        summary = []

        if 'cuisine' in m:
            summary.append(f"🌍 {m['cuisine']}")
        if 'type' in m:
            summary.append(f"🍽️ {m['type']}")
        if 'protéine' in m:
            summary.append(f"🥩 {m['protéine']}")
        if 'temps_total' in m:
            summary.append(f"⏱️ {m['temps_total']}min")
        if 'difficulté' in m:
            summary.append(f"🎯 {m['difficulté']}")

        return " | ".join(summary) if summary else "⚠️ Métadonnées incomplètes"

    def move_recipe(self, recipe_path, destination_folder):
        """Déplace une recette vers son dossier de destination"""
        dest_dir = self.base_path / destination_folder
        dest_dir.mkdir(parents=True, exist_ok=True)

        dest_path = dest_dir / recipe_path.name

        # Vérifier si le fichier existe déjà
        if dest_path.exists():
            return False, f"Le fichier existe déjà dans {destination_folder}"

        try:
            recipe_path.rename(dest_path)
            return True, f"Déplacé vers {dest_path.relative_to(self.base_path)}"
        except Exception as e:
            return False, f"Erreur: {e}"

    def interactive_classify(self):
        """Mode interactif pour classifier les recettes"""
        unclassified = self.find_unclassified_recipes()

        if not unclassified:
            print("✅ Aucune recette à classifier dans TO_BE_CLASSIFIED/\n")
            return

        print("=" * 60)
        print(f"📋 {len(unclassified)} RECETTES À CLASSIFIER")
        print("=" * 60 + "\n")

        for i, recipe_path in enumerate(unclassified, 1):
            recipe_info = self.analyze_recipe(recipe_path)

            print(f"\n{'─' * 60}")
            print(f"[{i}/{len(unclassified)}] {recipe_info['title']}")
            print(f"{'─' * 60}")
            print(f"📄 Fichier: {recipe_path.name}")
            print(f"📊 Métadonnées: {self.get_metadata_summary(recipe_info)}")

            dest_folder, reason = self.suggest_destination(recipe_info)

            if dest_folder:
                print(f"💡 Suggestion: {dest_folder}")
                print(f"   Raison: {reason}")
            else:
                print(f"⚠️  {reason}")

            print("\nOptions:")
            print("  [y] Accepter la suggestion")
            print("  [c] Choisir un autre dossier")
            print("  [s] Skip (passer)")
            print("  [v] Voir le contenu")
            print("  [q] Quitter")

            choice = input("\nVotre choix: ").lower().strip()

            if choice == 'q':
                print("\n👋 Classification interrompue\n")
                break
            elif choice == 's':
                print("⏭️  Recette ignorée")
                continue
            elif choice == 'v':
                with open(recipe_path, 'r', encoding='utf-8') as f:
                    print("\n" + "─" * 60)
                    print(f.read()[:500])  # Afficher les 500 premiers caractères
                    print("─" * 60)
                continue
            elif choice == 'y' and dest_folder:
                success, message = self.move_recipe(recipe_path, dest_folder)
                print(f"{'✅' if success else '❌'} {message}")
            elif choice == 'c':
                print("\nDossiers disponibles:")
                folders = list(self.cuisine_mapping.values()) + ['recettes/autres']
                for idx, folder in enumerate(folders, 1):
                    print(f"  [{idx}] {folder}")

                try:
                    folder_choice = int(input("\nNuméro du dossier: "))
                    if 1 <= folder_choice <= len(folders):
                        chosen_folder = folders[folder_choice - 1]
                        success, message = self.move_recipe(recipe_path, chosen_folder)
                        print(f"{'✅' if success else '❌'} {message}")
                except ValueError:
                    print("❌ Choix invalide")

        print("\n" + "=" * 60)
        print("✨ CLASSIFICATION TERMINÉE")
        print("=" * 60 + "\n")

    def batch_classify(self, dry_run=True):
        """Classifie automatiquement toutes les recettes avec métadonnées"""
        unclassified = self.find_unclassified_recipes()

        if not unclassified:
            print("✅ Aucune recette à classifier\n")
            return

        print("=" * 60)
        print(f"🤖 CLASSIFICATION AUTOMATIQUE {'(DRY RUN)' if dry_run else ''}")
        print("=" * 60 + "\n")

        moved = 0
        skipped = 0

        for recipe_path in unclassified:
            recipe_info = self.analyze_recipe(recipe_path)
            dest_folder, reason = self.suggest_destination(recipe_info)

            if dest_folder and recipe_info['has_metadata']:
                if dry_run:
                    print(f"🔍 {recipe_info['title']}")
                    print(f"   → {dest_folder}")
                    moved += 1
                else:
                    success, message = self.move_recipe(recipe_path, dest_folder)
                    if success:
                        print(f"✅ {recipe_info['title']} → {dest_folder}")
                        moved += 1
                    else:
                        print(f"❌ {recipe_info['title']}: {message}")
                        skipped += 1
            else:
                print(f"⏭️  {recipe_info['title']}: {reason}")
                skipped += 1

        print(f"\n📊 Résumé:")
        print(f"   • Déplacées: {moved}")
        print(f"   • Ignorées: {skipped}")

        if dry_run:
            print(f"\n💡 Exécutez avec --auto pour déplacer réellement les fichiers")

        print()

    def list_unclassified(self):
        """Liste simplement les recettes non classées"""
        unclassified = self.find_unclassified_recipes()

        if not unclassified:
            print("✅ Aucune recette à classifier\n")
            return

        print("=" * 60)
        print(f"📋 RECETTES NON CLASSÉES ({len(unclassified)})")
        print("=" * 60 + "\n")

        for recipe_path in unclassified:
            recipe_info = self.analyze_recipe(recipe_path)
            print(f"• {recipe_info['title']}")
            print(f"  {self.get_metadata_summary(recipe_info)}")
            print()

if __name__ == "__main__":
    import sys

    classifier = RecipeClassifier()

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "--list":
            classifier.list_unclassified()
        elif command == "--dry-run":
            classifier.batch_classify(dry_run=True)
        elif command == "--auto":
            classifier.batch_classify(dry_run=False)
        else:
            print("Usage:")
            print("  python classify_helper.py           # Mode interactif")
            print("  python classify_helper.py --list    # Lister les recettes")
            print("  python classify_helper.py --dry-run # Simulation")
            print("  python classify_helper.py --auto    # Classification auto")
    else:
        classifier.interactive_classify()
