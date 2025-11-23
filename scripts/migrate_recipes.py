#!/usr/bin/env python3
"""
Script de migration one-time pour déplacer les recettes de la racine vers les dossiers organisés
"""

import yaml
from pathlib import Path
import shutil

def migrate_recipes():
    base_path = Path(".")

    # Mapping des cuisines vers les dossiers
    cuisine_mapping = {
        'japonaise': 'recettes/asiatique/japonais',
        'chinoise': 'recettes/asiatique/chinois',
        'thaï': 'recettes/asiatique/thai',
        'coréenne': 'recettes/asiatique/coreen',
        'vietnamienne': 'recettes/asiatique/vietnamien',
        'française': 'recettes/europeen/francais',
        'italienne': 'recettes/europeen/italien',
        'grecque': 'recettes/europeen/grec',
    }

    # Fichiers à ignorer
    ignore_files = [
        'README.md', 'CLAUDE.md', 'Template - Recette.md',
        '📚 Index Recettes.md'
    ]

    # Dossiers à ignorer
    ignore_dirs = [
        '.obsidian', '.claude', 'commands', 'scripts', 'templates',
        'index', 'recettes', 'TO BE CLASSIFIED', 'docs'
    ]

    print("=" * 60)
    print("🚀 MIGRATION DES RECETTES")
    print("=" * 60 + "\n")

    # Trouver tous les fichiers .md à la racine
    recipe_files = []
    for md_file in base_path.glob("*.md"):
        if md_file.name not in ignore_files:
            recipe_files.append(md_file)

    print(f"📋 {len(recipe_files)} recettes trouvées à la racine\n")

    moved = 0
    skipped = 0
    errors = []

    for recipe_file in recipe_files:
        try:
            # Lire le fichier
            with open(recipe_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extraire le frontmatter YAML
            if not content.startswith('---'):
                print(f"⏭️  {recipe_file.name}: Pas de frontmatter YAML")
                skipped += 1
                continue

            yaml_end = content.find('---', 3)
            if yaml_end < 0:
                print(f"⏭️  {recipe_file.name}: Frontmatter YAML malformé")
                skipped += 1
                continue

            metadata = yaml.safe_load(content[3:yaml_end])
            if not metadata:
                print(f"⏭️  {recipe_file.name}: Métadonnées vides")
                skipped += 1
                continue

            # Extraire la cuisine
            cuisine = metadata.get('cuisine')
            if isinstance(cuisine, list):
                cuisine = cuisine[0] if cuisine else None

            if not cuisine:
                print(f"⏭️  {recipe_file.name}: Pas de champ 'cuisine'")
                skipped += 1
                continue

            # Déterminer le dossier de destination
            dest_folder = cuisine_mapping.get(cuisine, 'recettes/autres')
            dest_path = base_path / dest_folder

            # Créer le dossier de destination si nécessaire
            dest_path.mkdir(parents=True, exist_ok=True)

            # Chemin de destination complet
            dest_file = dest_path / recipe_file.name

            # Vérifier si le fichier existe déjà
            if dest_file.exists():
                print(f"⚠️  {recipe_file.name}: Existe déjà dans {dest_folder}")
                skipped += 1
                continue

            # Déplacer le fichier
            shutil.move(str(recipe_file), str(dest_file))
            print(f"✅ {recipe_file.name} → {dest_folder}")
            moved += 1

        except Exception as e:
            error_msg = f"{recipe_file.name}: {str(e)}"
            errors.append(error_msg)
            print(f"❌ {error_msg}")
            skipped += 1

    print("\n" + "=" * 60)
    print("✨ MIGRATION TERMINÉE")
    print("=" * 60)
    print(f"📊 Résumé:")
    print(f"   • Déplacées: {moved}")
    print(f"   • Ignorées: {skipped}")

    if errors:
        print(f"\n⚠️  Erreurs ({len(errors)}):")
        for error in errors[:10]:  # Afficher max 10 erreurs
            print(f"   - {error}")

    print()

if __name__ == "__main__":
    migrate_recipes()
