---
cuisine: [origine]           # japonaise, chinoise, française, thaï, etc.
type: [catégorie]            # plat-principal, dessert, soupe, entrée, etc.
temps_prep: [minutes]        # Temps de préparation uniquement
temps_cuisson: [minutes]     # Temps de cuisson uniquement
temps_total: [minutes]       # Temps total (inclut marinade/repos si nécessaire)
portions: [nombre]           # Nombre de portions
difficulté: [niveau]         # débutant, intermédiaire, avancé
protéine: [principale]       # poulet, porc, bœuf, poisson, fruits-de-mer, végétarien, vegan
source: [origine]            # Instagram, YouTube, livre, blog, etc.
url: [lien]                  # URL de la source si disponible
date_ajout: YYYY-MM-DD       # Date d'ajout au vault (format ISO)
tags:
  - #cuisine/[origine]
  - #type/[catégorie]
  - #protéine/[principale]
  - #temps/[express|rapide|moyen|long]
  - #cuisson/[méthode]
  - #difficulté/[niveau]
  # Ajouter 0-4 tags supplémentaires si pertinent
---

# [Titre de la Recette]

## Informations rapides

- 🌍 Cuisine : [origine]
- 🍽️ Type : [catégorie]
- ⏱️ Temps de préparation : [X] min
- 🔥 Temps de cuisson : [X] min
- 👥 Portions : [X]
- 📊 Difficulté : [niveau]
- 🥩 Protéine principale : [protéine]

## Ingredients

### [Section optionnelle si nécessaire]

- Quantité Ingrédient 1
- Quantité Ingrédient 2
- Quantité Ingrédient 3

### [Autre section si plusieurs groupes]

- Quantité Ingrédient 4
- Quantité Ingrédient 5

## Steps

1. Première étape avec description claire et précise
2. Deuxième étape
3. Troisième étape
4. Continue...

## Notes personnelles

*[Section optionnelle]*

- Note sur les modifications apportées
- Conseils de préparation
- Substitutions possibles
- Retours après avoir testé la recette

## Source

Link: [Titre de la source]([URL])

---

## Guide de Remplissage

### Champs YAML

**cuisine:**
- japonaise, chinoise, coréenne, thaï, vietnamienne
- française, italienne, grecque
- fusion, autre

**type:**
- plat-principal, entrée, dessert, soupe
- accompagnement, sauce, boisson

**protéine:**
- poulet, porc, bœuf, agneau
- poisson, fruits-de-mer
- végétarien, vegan

**difficulté:**
- débutant : recettes simples, techniques basiques
- intermédiaire : quelques techniques spécifiques
- avancé : techniques complexes, timing précis

### Tags

**Obligatoires (3) :**
- `#cuisine/[X]` - origine de la recette
- `#type/[X]` - catégorie du plat
- `#protéine/[X]` - protéine principale

**Recommandés (3-7) :**
- `#temps/express` (≤15min), `#temps/rapide` (15-30min), `#temps/moyen` (30-60min), `#temps/long` (>1h)
- `#temps/préparation-avance` - si marinade/repos nécessaire
- `#cuisson/[méthode]` - air-fryer, four, poêle, wok, bouilli, vapeur, sans-cuisson
- `#difficulté/[niveau]` - débutant, intermédiaire, avancé
- `#occasion/[contexte]` - semaine, weekend, festif, batch-cooking

**Optionnels :**
- `#diet/[restriction]` - sans-sucre, low-carb, léger, sans-gluten
- `#saveur/[profil]` - épicé, sucré-salé, umami, crémeux, acidulé
- `#équipement/[spécial]` - air-fryer, wok, moules-spéciaux

### Temps

- **temps_prep** : uniquement la préparation active
- **temps_cuisson** : uniquement le temps de cuisson
- **temps_total** : tout inclus (prep + cuisson + marinade + repos)

### Conseils

1. **Titre** : Utilisez le nom original ou français selon préférence
2. **Ingrédients** : Listez avec quantités précises
3. **Steps** : Numérotez et soyez précis
4. **Notes** : Ajoutez vos observations après avoir testé
5. **Source** : Créditez toujours l'origine de la recette
