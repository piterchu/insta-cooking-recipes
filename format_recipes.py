#!/usr/bin/env python3
"""
Script to format recipe files with YAML frontmatter and structured content.
"""

import os
import re
from pathlib import Path

# Directory containing recipes to format
TO_BE_CLASSIFIED = Path(__file__).parent / "TO BE CLASSIFIED"

# Recipe metadata mapping based on content analysis
RECIPE_METADATA = {
    "Foie Gras Mi-Cuit, Gelée Vin Chaud": {
        "cuisine": "française",
        "type": "entrée",
        "temps_prep": 45,
        "temps_cuisson": 10,
        "temps_total": 300,  # includes 2h+ refrigeration
        "portions": 8,
        "difficulté": "avancé",
        "protéine": "fruits-de-mer",
        "tags": ["cuisine/française", "type/entrée", "protéine/fruits-de-mer", "temps/moyen", "cuisson/poêle", "difficulté/avancé", "occasion/festif", "saveur/riche", "temps/préparation-avance"]
    },
    "Foie gras poêlé aux pommes": {
        "cuisine": "française",
        "type": "plat-principal",
        "temps_prep": 15,
        "temps_cuisson": 15,
        "temps_total": 30,
        "portions": 4,
        "difficulté": "intermédiaire",
        "protéine": "fruits-de-mer",
        "tags": ["cuisine/française", "type/plat-principal", "protéine/fruits-de-mer", "temps/rapide", "cuisson/poêle", "difficulté/intermédiaire", "occasion/festif", "saveur/sucré-salé", "saveur/riche"]
    },
    "Tournedos de canard au foie gras poêlé": {
        "cuisine": "française",
        "type": "plat-principal",
        "temps_prep": 20,
        "temps_cuisson": 20,
        "temps_total": 40,
        "portions": 4,
        "difficulté": "intermédiaire",
        "protéine": "poulet",
        "tags": ["cuisine/française", "type/plat-principal", "protéine/poulet", "temps/moyen", "cuisson/poêle", "difficulté/intermédiaire", "occasion/festif", "saveur/riche"]
    },
    "Camembert festif de Noël": {
        "cuisine": "française",
        "type": "entrée",
        "temps_prep": 10,
        "temps_cuisson": 15,
        "temps_total": 25,
        "portions": 6,
        "difficulté": "débutant",
        "protéine": "végétarien",
        "tags": ["cuisine/française", "type/entrée", "protéine/végétarien", "temps/rapide", "cuisson/four", "difficulté/débutant", "occasion/festif", "saveur/crémeux"]
    },
    "Bûche de truite fumée et blinis pour Noël": {
        "cuisine": "française",
        "type": "entrée",
        "temps_prep": 20,
        "temps_cuisson": 0,
        "temps_total": 20,
        "portions": 8,
        "difficulté": "débutant",
        "protéine": "poisson",
        "tags": ["cuisine/française", "type/entrée", "protéine/poisson", "temps/rapide", "cuisson/sans-cuisson", "difficulté/débutant", "occasion/festif"]
    },
    "Gyoza Festifs aux Crevettes": {
        "cuisine": "japonaise",
        "type": "entrée",
        "temps_prep": 30,
        "temps_cuisson": 10,
        "temps_total": 40,
        "portions": 6,
        "difficulté": "intermédiaire",
        "protéine": "fruits-de-mer",
        "tags": ["cuisine/japonaise", "type/entrée", "protéine/fruits-de-mer", "temps/moyen", "cuisson/poêle", "difficulté/intermédiaire", "occasion/festif"]
    },
}


def extract_url(content):
    """Extract URL from recipe content."""
    url_match = re.search(r'Link:\s*<?([^>]+)>?', content)
    return url_match.group(1) if url_match else ""


def format_recipe(filepath, metadata):
    """Format a recipe file with YAML frontmatter."""

    # Read the original content
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract URL
    url = extract_url(content)

    # Extract title from filename
    title = filepath.stem

    # Extract ingredients and steps sections
    ingredients_match = re.search(r'### Ingredients\s*\n(.*?)### Steps', content, re.DOTALL)
    steps_match = re.search(r'### Steps\s*\n(.*?)Link:', content, re.DOTALL)

    ingredients = ingredients_match.group(1).strip() if ingredients_match else ""
    steps = steps_match.group(1).strip() if steps_match else ""

    # Create YAML frontmatter
    yaml = f"""---
cuisine: {metadata['cuisine']}
type: {metadata['type']}
temps_prep: {metadata['temps_prep']}
temps_cuisson: {metadata['temps_cuisson']}
temps_total: {metadata['temps_total']}
portions: {metadata['portions']}
difficulté: {metadata['difficulté']}
protéine: {metadata['protéine']}
source: Instagram
url: {url}
date_ajout: 2025-10-12
tags:
"""
    for tag in metadata['tags']:
        yaml += f"  - {tag}\n"
    yaml += "---\n\n"

    # Create formatted content
    cuisine_cap = metadata['cuisine'].capitalize()
    type_cap = metadata['type'].replace('-', ' ').capitalize()
    diff_cap = metadata['difficulté'].capitalize()
    prot_cap = metadata['protéine'].capitalize()

    info_rapides = f"""## Informations rapides

- 🌍 Cuisine : {cuisine_cap}
- 🍽️ Type : {type_cap}
- ⏱️ Temps de préparation : {metadata['temps_prep']} min
- 🔥 Temps de cuisson : {metadata['temps_cuisson']} min
- 👥 Portions : {metadata['portions']}
- 📊 Difficulté : {diff_cap}
- 🥩 Protéine principale : {prot_cap}
"""

    # Build complete content
    formatted = f"{yaml}# {title}\n\n{info_rapides}\n## Ingredients\n\n{ingredients}\n\n## Steps\n\n{steps}\n\n## Source\n\nLink: {url}\n"

    # Write formatted content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(formatted)

    print(f"✓ Formatted: {title}")


def main():
    """Process all recipes in TO BE CLASSIFIED directory."""
    for recipe_name, metadata in RECIPE_METADATA.items():
        filepath = TO_BE_CLASSIFIED / f"{recipe_name}.md"
        if filepath.exists():
            try:
                format_recipe(filepath, metadata)
            except Exception as e:
                print(f"✗ Error formatting {recipe_name}: {e}")
        else:
            print(f"✗ File not found: {recipe_name}")


if __name__ == "__main__":
    main()
