#!/usr/bin/env python3
"""
Génère automatiquement les fichiers d'index pour la navigation
À exécuter après avoir ajouté/modifié des recettes
"""

import yaml
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from urllib.parse import quote

class RecipeIndexGenerator:
    def __init__(self, base_path="."):
        self.base_path = Path(base_path)
        self.recipes = []

    @staticmethod
    def normalize_metadata_value(value, default=''):
        """Normalize metadata value - convert lists to first element, handle None"""
        if value is None:
            return default
        if isinstance(value, list):
            return value[0] if value else default
        return value

    @staticmethod
    def encode_url_path(path):
        """Encode file path for GitHub markdown compatibility"""
        # Convert Path object to string
        path_str = str(path)
        # Split into parts to encode each part separately
        parts = path_str.split('/')
        # Encode each part, keeping slashes unencoded
        encoded_parts = [quote(part, safe='') for part in parts]
        return '/'.join(encoded_parts)

    def parse_recipes(self):
        """Parse toutes les recettes et extrait les métadonnées"""
        print("🔍 Parsing des recettes...")

        for md_file in self.base_path.rglob("*.md"):
            # Ignorer certains fichiers
            if any(x in str(md_file) for x in ["README", "Template", "Index", "CLAUDE", "commands", "TO BE CLASSIFIED"]):
                continue

            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                if content.startswith('---'):
                    yaml_end = content.find('---', 3)
                    if yaml_end > 0:
                        metadata = yaml.safe_load(content[3:yaml_end])
                        if metadata:
                            # Extraire le titre (première ligne # après le frontmatter)
                            rest = content[yaml_end+3:].strip()
                            title = rest.split('\n')[0].replace('#', '').strip()

                            self.recipes.append({
                                'title': title,
                                'path': md_file.relative_to(self.base_path),
                                'metadata': metadata
                            })
            except Exception as e:
                print(f"⚠️  Erreur lors du parsing de {md_file}: {e}")

        print(f"✅ {len(self.recipes)} recettes trouvées\n")
        return self.recipes

    def generate_time_index(self):
        """Génère l'index par temps de préparation"""
        print("⏱️  Génération de l'index par temps...")

        time_groups = {
            'express': {'label': 'Express (≤15min)', 'recipes': []},
            'rapide': {'label': 'Rapide (15-30min)', 'recipes': []},
            'moyen': {'label': 'Moyen (30-60min)', 'recipes': []},
            'long': {'label': 'Long (>1h)', 'recipes': []}
        }

        for recipe in self.recipes:
            temps_total = recipe['metadata'].get('temps_total', 0)
            # Handle case where temps_total might be a list
            if isinstance(temps_total, list):
                temps_total = temps_total[0] if temps_total else 0
            # Convert to int if it's a string
            try:
                temps_total = int(temps_total)
            except (ValueError, TypeError):
                temps_total = 0

            if temps_total <= 15:
                time_groups['express']['recipes'].append(recipe)
            elif temps_total <= 30:
                time_groups['rapide']['recipes'].append(recipe)
            elif temps_total <= 60:
                time_groups['moyen']['recipes'].append(recipe)
            else:
                time_groups['long']['recipes'].append(recipe)

        content = "# 🕐 Index par Temps de Préparation\n\n"
        content += f"*Dernière mise à jour: {datetime.now().strftime('%Y-%m-%d')}*\n\n"

        for key, group in time_groups.items():
            content += f"## {group['label']}\n\n"
            content += f"**{len(group['recipes'])} recettes**\n\n"

            for recipe in sorted(group['recipes'], key=lambda x: x['title']):
                temps = recipe['metadata'].get('temps_total', '?')
                cuisine = recipe['metadata'].get('cuisine', 'autre')
                encoded_path = self.encode_url_path(recipe['path'])
                content += f"- [{recipe['title']}]({encoded_path}) - {temps}min - *{cuisine}*\n"
            content += "\n"

        output_path = self.base_path / "index" / "par-temps.md"
        output_path.write_text(content, encoding='utf-8')
        print(f"✅ {output_path}\n")

    def generate_protein_index(self):
        """Génère l'index par protéine"""
        print("🥩 Génération de l'index par protéine...")

        protein_groups = defaultdict(list)

        for recipe in self.recipes:
            protein = self.normalize_metadata_value(recipe['metadata'].get('protéine'), 'autre')
            protein_groups[protein].append(recipe)

        content = "# 🍖 Index par Protéine\n\n"
        content += f"*Dernière mise à jour: {datetime.now().strftime('%Y-%m-%d')}*\n\n"

        # Ordre préféré
        protein_order = ['poulet', 'porc', 'bœuf', 'poisson', 'fruits-de-mer', 'végétarien', 'vegan']

        for protein in protein_order + [k for k in protein_groups.keys() if k not in protein_order]:
            if protein not in protein_groups:
                continue

            recipes = protein_groups[protein]
            emoji = {
                'poulet': '🍗', 'porc': '🥓', 'bœuf': '🥩',
                'poisson': '🐟', 'fruits-de-mer': '🦐',
                'végétarien': '🥬', 'vegan': '🌱'
            }.get(protein, '🍽️')

            content += f"## {emoji} {protein.capitalize()}\n\n"
            content += f"**{len(recipes)} recettes**\n\n"

            for recipe in sorted(recipes, key=lambda x: x['title']):
                temps = recipe['metadata'].get('temps_total', '?')
                cuisine = recipe['metadata'].get('cuisine', 'autre')
                encoded_path = self.encode_url_path(recipe['path'])
                content += f"- [{recipe['title']}]({encoded_path}) - {temps}min - *{cuisine}*\n"
            content += "\n"

        output_path = self.base_path / "index" / "par-proteine.md"
        output_path.write_text(content, encoding='utf-8')
        print(f"✅ {output_path}\n")

    def generate_difficulty_index(self):
        """Génère l'index par difficulté"""
        print("👨‍🍳 Génération de l'index par difficulté...")

        diff_groups = {
            'débutant': {'emoji': '🟢', 'recipes': []},
            'intermédiaire': {'emoji': '🟡', 'recipes': []},
            'avancé': {'emoji': '🔴', 'recipes': []}
        }

        for recipe in self.recipes:
            diff = self.normalize_metadata_value(recipe['metadata'].get('difficulté'), 'débutant')
            if diff in diff_groups:
                diff_groups[diff]['recipes'].append(recipe)

        content = "# 🎯 Index par Difficulté\n\n"
        content += f"*Dernière mise à jour: {datetime.now().strftime('%Y-%m-%d')}*\n\n"

        for level, data in diff_groups.items():
            content += f"## {data['emoji']} {level.capitalize()}\n\n"
            content += f"**{len(data['recipes'])} recettes**\n\n"

            for recipe in sorted(data['recipes'], key=lambda x: x['title']):
                temps = recipe['metadata'].get('temps_total', '?')
                cuisine = recipe['metadata'].get('cuisine', 'autre')
                encoded_path = self.encode_url_path(recipe['path'])
                content += f"- [{recipe['title']}]({encoded_path}) - {temps}min - *{cuisine}*\n"
            content += "\n"

        output_path = self.base_path / "index" / "par-difficulte.md"
        output_path.write_text(content, encoding='utf-8')
        print(f"✅ {output_path}\n")

    def generate_cuisine_index(self):
        """Génère l'index par cuisine"""
        print("🌍 Génération de l'index par cuisine...")

        cuisine_groups = defaultdict(list)

        for recipe in self.recipes:
            cuisine = self.normalize_metadata_value(recipe['metadata'].get('cuisine'), 'autre')
            cuisine_groups[cuisine].append(recipe)

        content = "# 🌍 Index par Cuisine\n\n"
        content += f"*Dernière mise à jour: {datetime.now().strftime('%Y-%m-%d')}*\n\n"

        for cuisine in sorted(cuisine_groups.keys()):
            recipes = cuisine_groups[cuisine]
            emoji = {
                'japonaise': '🍜', 'chinoise': '🥡', 'coréenne': '🌶️',
                'thaï': '🍛', 'vietnamienne': '🥢',
                'française': '🥖', 'italienne': '🍝', 'grecque': '🫒'
            }.get(cuisine, '🍽️')

            content += f"## {emoji} {cuisine.capitalize()}\n\n"
            content += f"**{len(recipes)} recettes**\n\n"

            for recipe in sorted(recipes, key=lambda x: x['title']):
                temps = recipe['metadata'].get('temps_total', '?')
                protein = recipe['metadata'].get('protéine', '')
                encoded_path = self.encode_url_path(recipe['path'])
                content += f"- [{recipe['title']}]({encoded_path}) - {temps}min - *{protein}*\n"
            content += "\n"

        output_path = self.base_path / "index" / "par-cuisine.md"
        output_path.write_text(content, encoding='utf-8')
        print(f"✅ {output_path}\n")

    def generate_stats(self):
        """Génère des statistiques"""
        print("📊 Calcul des statistiques...")

        def get_temps(recipe):
            """Extract temps_total as int"""
            temps = recipe['metadata'].get('temps_total', 0)
            if isinstance(temps, list):
                temps = temps[0] if temps else 0
            try:
                return int(temps)
            except (ValueError, TypeError):
                return 0

        stats = {
            'total': len(self.recipes),
            'cuisines': len(set(self.normalize_metadata_value(r['metadata'].get('cuisine'), 'autre') for r in self.recipes)),
            'temps_moyen': sum(get_temps(r) for r in self.recipes) / len(self.recipes) if self.recipes else 0
        }

        return stats

    def run(self):
        """Exécute la génération de tous les index"""
        print("=" * 60)
        print("🚀 GÉNÉRATION DES INDEX")
        print("=" * 60 + "\n")

        self.parse_recipes()

        if not self.recipes:
            print("⚠️  Aucune recette trouvée avec métadonnées YAML\n")
            return

        self.generate_time_index()
        self.generate_protein_index()
        self.generate_difficulty_index()
        self.generate_cuisine_index()

        stats = self.generate_stats()

        print("=" * 60)
        print("✨ GÉNÉRATION TERMINÉE")
        print("=" * 60)
        print(f"📊 Statistiques:")
        print(f"   • Total: {stats['total']} recettes")
        print(f"   • Cuisines: {stats['cuisines']} origines")
        print(f"   • Temps moyen: {stats['temps_moyen']:.0f} minutes")
        print()

        return stats

if __name__ == "__main__":
    generator = RecipeIndexGenerator()
    generator.run()
