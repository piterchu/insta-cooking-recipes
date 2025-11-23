# 🍳 Collection de Recettes

> Une collection de 108+ recettes du monde entier - Asie, Europe et plus

Cette collection organise des recettes de cuisine provenant de différentes sources (YouTube, Instagram, livres) dans une structure navigable et facilement consultable.

## 🔍 Navigation Rapide

### Par Cuisine

#### 🍜 Asiatique
- [Recettes Japonaises](recettes/asiatique/japonais/README.md) - Ramen, Gyoza, Donburi, etc.
- [Recettes Chinoises](recettes/asiatique/chinois/README.md) - Dim Sum, Wok, etc.
- [Recettes Thaï](recettes/asiatique/thai/README.md) - Pad Thai, Curry, etc.
- [Recettes Coréennes](recettes/asiatique/coreen/README.md) - Kimchi, BBQ, etc.
- [Recettes Vietnamiennes](recettes/asiatique/vietnamien/README.md) - Phở, Rouleaux de printemps, etc.

#### 🥖 Européenne
- [Recettes Françaises](recettes/europeen/francais/README.md) - Blanquette, Carbonade, Desserts, etc.
- [Recettes Italiennes](recettes/europeen/italien/README.md) - Pasta, Pizza, etc.
- [Recettes Grecques](recettes/europeen/grec/README.md) - Moussaka, etc.

#### 🌍 Autres
- [Autres Cuisines](recettes/autres/README.md) - Fusion et autres origines

### Par Critères

Consultez ces index pour trouver des recettes selon vos besoins :

- ⏱️ [Par Temps de Préparation](index/par-temps.md) - Express, Rapide, Moyen, Long
- 🥩 [Par Protéine](index/par-proteine.md) - Poulet, Porc, Bœuf, Poisson, Végétarien
- 👨‍🍳 [Par Difficulté](index/par-difficulte.md) - Débutant, Intermédiaire, Avancé
- 🌍 [Par Cuisine](index/par-cuisine.md) - Vue d'ensemble par origine

### Sélections Spéciales

- ⚡ **Recettes Express** (≤15min) - [Voir la liste](index/par-temps.md#express-15min)
- 🔥 **Air Fryer** - Recherchez le tag `#cuisson/air-fryer` ou `#équipement/air-fryer`
- 🌱 **Végétarien/Vegan** - [Options sans viande](index/par-proteine.md#végétarien)
- 🎉 **Recettes Festives** - Plats pour occasions spéciales

## 📊 Statistiques

- **Total :** 108+ recettes
- **Cuisines :** 8 origines différentes
- **Langues :** Français & English
- **Temps moyen :** ~35 minutes

## 🗂️ Organisation

Chaque recette contient :

- **Métadonnées complètes** (YAML frontmatter)
  - Cuisine, type, temps, portions, difficulté
  - Protéine principale, source, URL
  - Tags hiérarchiques pour navigation

- **Structure standardisée**
  - Informations rapides avec emojis
  - Liste d'ingrédients claire
  - Instructions étape par étape
  - Notes personnelles (optionnel)
  - Lien vers la source

## 🚀 Démarrage Rapide

### Pour Trouver une Recette

1. **Par envie :** Parcourez par [cuisine](recettes/) ou [protéine](index/par-proteine.md)
2. **Par contrainte de temps :** Consultez l'[index par temps](index/par-temps.md)
3. **Par niveau :** Filtrez par [difficulté](index/par-difficulte.md)

### Pour Ajouter une Recette

1. Placez votre recette dans [TO BE CLASSIFIED/](TO%20BE%20CLASSIFIED/)
2. Utilisez `/classify` pour formater et classifier
3. Les index seront régénérés automatiquement

Voir [TO BE CLASSIFIED/README.md](TO%20BE%20CLASSIFIED/README.md) pour plus de détails.

## 🛠️ Outils et Scripts

### Scripts Python

Situés dans [scripts/](scripts/) :

- **`generate_indexes.py`** - Régénère tous les index de navigation
- **`classify_helper.py`** - Aide à classifier les nouvelles recettes
- **`requirements.txt`** - Dépendances Python

### Installation

```bash
pip install -r scripts/requirements.txt
```

### Commandes

```bash
# Lister les recettes non classées
python scripts/classify_helper.py --list

# Classification interactive
python scripts/classify_helper.py

# Classification automatique (avec preview)
python scripts/classify_helper.py --dry-run
python scripts/classify_helper.py --auto

# Régénérer les index
python scripts/generate_indexes.py
```

Ou utilisez la commande intégrée : `/classify --help`

## 📝 Structure du Projet

```
recipe-collection/
├── README.md                  # Ce fichier
├── TO BE CLASSIFIED/          # Recettes non encore classées
├── recettes/                  # Toutes les recettes organisées
│   ├── asiatique/
│   │   ├── japonais/
│   │   ├── chinois/
│   │   └── ...
│   └── europeen/
│       ├── francais/
│       └── ...
├── index/                     # Fichiers d'index générés
│   ├── par-temps.md
│   ├── par-proteine.md
│   ├── par-difficulte.md
│   └── par-cuisine.md
├── scripts/                   # Outils Python
│   ├── generate_indexes.py
│   ├── classify_helper.py
│   └── requirements.txt
└── templates/                 # Templates pour nouvelles recettes
    └── recette-template.md
```

## 🏷️ Système de Tags

### Tags Obligatoires
- `#cuisine/[origine]` - japonaise, chinoise, française, etc.
- `#type/[catégorie]` - plat-principal, dessert, entrée, etc.
- `#protéine/[principale]` - poulet, porc, bœuf, végétarien, etc.

### Tags Recommandés
- `#temps/[durée]` - express, rapide, moyen, long
- `#cuisson/[méthode]` - air-fryer, four, poêle, wok, vapeur
- `#difficulté/[niveau]` - débutant, intermédiaire, avancé
- `#occasion/[contexte]` - semaine, weekend, festif, batch-cooking

Voir [docs/conventions-tags.md](docs/conventions-tags.md) pour la liste complète.

## 🤝 Contribution

Pour contribuer une nouvelle recette :

1. Utilisez le template dans [templates/recette-template.md](templates/recette-template.md)
2. Remplissez toutes les métadonnées YAML
3. Ajoutez 6-10 tags appropriés
4. Placez dans `TO BE CLASSIFIED/`
5. Exécutez `/classify` pour finaliser

## 📚 Ressources

- [Template de Recette](templates/recette-template.md)
- [Conventions de Tags](docs/conventions-tags.md)
- [Guide d'Utilisation de /classify](commands/classify.md)

## 📜 Licence

Collection personnelle de recettes pour usage privé.
Les recettes proviennent de diverses sources (créditées dans chaque recette).

---

**Dernière mise à jour :** 2025-11-23
**Version :** 1.0.0

*Bon appétit ! 👨‍🍳*
