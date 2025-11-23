# 🏷️ Conventions de Tags

Guide complet du système de tags hiérarchiques pour l'organisation des recettes.

## 📋 Vue d'Ensemble

Chaque recette utilise un système de **tags hiérarchiques** pour faciliter la navigation et la recherche. Les tags sont organisés en catégories obligatoires et recommandées.

**Objectif :** Permettre une recherche multi-critères et une classification cohérente.

## ✅ Tags Obligatoires (3 minimum)

Ces tags DOIVENT être présents dans chaque recette :

### 1. `#cuisine/[origine]`

Indique l'origine géographique ou le style culinaire.

**Valeurs possibles :**
- `#cuisine/japonaise` - Cuisine japonaise
- `#cuisine/chinoise` - Cuisine chinoise
- `#cuisine/coréenne` - Cuisine coréenne
- `#cuisine/thaï` - Cuisine thaïlandaise
- `#cuisine/vietnamienne` - Cuisine vietnamienne
- `#cuisine/française` - Cuisine française
- `#cuisine/italienne` - Cuisine italienne
- `#cuisine/grecque` - Cuisine grecque
- `#cuisine/fusion` - Mélange de plusieurs cuisines
- `#cuisine/autre` - Autres origines

**Exemple :** `#cuisine/japonaise`

### 2. `#type/[catégorie]`

Indique le type de plat ou sa place dans le repas.

**Valeurs possibles :**
- `#type/plat-principal` - Plat principal
- `#type/entrée` - Entrée / Apéritif
- `#type/dessert` - Dessert
- `#type/soupe` - Soupe / Potage
- `#type/accompagnement` - Accompagnement / Side dish
- `#type/sauce` - Sauce / Condiment
- `#type/boisson` - Boisson

**Exemple :** `#type/plat-principal`

### 3. `#protéine/[principale]`

Indique la protéine principale du plat.

**Valeurs possibles :**
- `#protéine/poulet` - Volaille / Poulet
- `#protéine/porc` - Porc
- `#protéine/bœuf` - Bœuf
- `#protéine/agneau` - Agneau
- `#protéine/poisson` - Poisson
- `#protéine/fruits-de-mer` - Fruits de mer / Crustacés
- `#protéine/végétarien` - Sans viande (œufs/produits laitiers OK)
- `#protéine/vegan` - 100% végétal

**Exemple :** `#protéine/poulet`

## 📌 Tags Recommandés (3-7 tags)

Choisissez 3 à 7 tags supplémentaires parmi ces catégories pour enrichir la classification :

### 4. `#temps/[durée]`

Indique le temps total de préparation.

**Valeurs possibles :**
- `#temps/express` - ≤15 minutes (très rapide)
- `#temps/rapide` - 15-30 minutes (rapide)
- `#temps/moyen` - 30-60 minutes (moyen)
- `#temps/long` - >1 heure (long)
- `#temps/préparation-avance` - Nécessite marinade/repos

**Exemple :** `#temps/rapide`

**Note :** Si une recette nécessite une marinade de 24h mais seulement 15min de préparation active, utilisez :
- `#temps/express` (temps actif)
- `#temps/préparation-avance` (marinade requise)

### 5. `#cuisson/[méthode]`

Indique la méthode de cuisson principale.

**Valeurs possibles :**
- `#cuisson/air-fryer` - Air fryer / Friteuse sans huile
- `#cuisson/four` - Four traditionnel
- `#cuisson/poêle` - Poêle / Sauté
- `#cuisson/wok` - Wok / Sauté asiatique
- `#cuisson/bouilli` - Bouilli / Mijoté
- `#cuisson/vapeur` - Cuisson vapeur
- `#cuisson/sans-cuisson` - Pas de cuisson (desserts froids, salades, etc.)

**Exemple :** `#cuisson/poêle`

### 6. `#difficulté/[niveau]`

Indique le niveau de compétence requis.

**Valeurs possibles :**
- `#difficulté/débutant` - Techniques basiques, peu d'étapes
- `#difficulté/intermédiaire` - Techniques spécifiques, timing important
- `#difficulté/avancé` - Techniques complexes, précision requise

**Critères :**
- **Débutant** : Couper, mélanger, cuire simple
- **Intermédiaire** : Tempérage, émulsions, multiples étapes
- **Avancé** : Techniques professionnelles, timing précis

**Exemple :** `#difficulté/débutant`

### 7. `#occasion/[contexte]`

Indique le contexte d'utilisation de la recette.

**Valeurs possibles :**
- `#occasion/semaine` - Repas de semaine rapide
- `#occasion/weekend` - Repas du weekend plus élaboré
- `#occasion/festif` - Grandes occasions (fêtes, réceptions)
- `#occasion/batch-cooking` - Préparation en grande quantité

**Exemple :** `#occasion/semaine`

## 🎯 Tags Optionnels

Ces tags peuvent être ajoutés pour des besoins spécifiques :

### 8. `#diet/[restriction]`

Restrictions ou caractéristiques diététiques.

**Valeurs possibles :**
- `#diet/sans-sucre` - Sans sucre ajouté
- `#diet/low-carb` - Faible en glucides
- `#diet/léger` - Léger / Light
- `#diet/riche` - Riche / Indulgent
- `#diet/sans-gluten` - Sans gluten

**Exemple :** `#diet/sans-sucre`

### 9. `#saveur/[profil]`

Profil de saveur dominant.

**Valeurs possibles :**
- `#saveur/épicé` - Plat épicé / Piquant
- `#saveur/sucré-salé` - Équilibre sucré-salé
- `#saveur/umami` - Riche en umami
- `#saveur/crémeux` - Texture crémeuse
- `#saveur/acidulé` - Notes acidulées

**Exemple :** `#saveur/umami`

### 10. `#équipement/[spécial]`

Équipement spécifique requis.

**Valeurs possibles :**
- `#équipement/air-fryer` - Air fryer nécessaire
- `#équipement/wok` - Wok recommandé
- `#équipement/moules-spéciaux` - Moules spécifiques (cannelés, etc.)

**Exemple :** `#équipement/air-fryer`

## 📊 Exemples Complets

### Exemple 1 : Gyoza Japonais

```yaml
tags:
  - #cuisine/japonaise          # Obligatoire - Origine
  - #type/plat-principal         # Obligatoire - Type
  - #protéine/porc               # Obligatoire - Protéine
  - #temps/moyen                 # Recommandé - 45min total
  - #cuisson/poêle               # Recommandé - Poêlé
  - #difficulté/intermédiaire    # Recommandé - Pliage
  - #occasion/weekend            # Optionnel - Préparation longue
  - #saveur/umami                # Optionnel - Saveur
```

**Total : 8 tags** ✓

### Exemple 2 : Fondant au Chocolat

```yaml
tags:
  - #cuisine/française           # Obligatoire - Origine
  - #type/dessert                # Obligatoire - Type
  - #protéine/végétarien         # Obligatoire - Pas de viande
  - #temps/rapide                # Recommandé - 25min
  - #cuisson/four                # Recommandé - Four
  - #difficulté/débutant         # Recommandé - Simple
  - #occasion/festif             # Optionnel - Dessert élégant
  - #diet/riche                  # Optionnel - Chocolat intense
  - #saveur/crémeux              # Optionnel - Texture
```

**Total : 9 tags** ✓

### Exemple 3 : Pad Thai

```yaml
tags:
  - #cuisine/thaï                # Obligatoire - Origine
  - #type/plat-principal         # Obligatoire - Type
  - #protéine/fruits-de-mer      # Obligatoire - Crevettes
  - #temps/rapide                # Recommandé - 20min
  - #cuisson/wok                 # Recommandé - Wok
  - #difficulté/intermédiaire    # Recommandé - Timing
  - #occasion/semaine            # Optionnel - Rapide
  - #saveur/sucré-salé           # Optionnel - Tamarind
  - #équipement/wok              # Optionnel - Wok requis
```

**Total : 9 tags** ✓

## ✅ Règles de Bonnes Pratiques

### Nombre de Tags

- **Minimum :** 6 tags (3 obligatoires + 3 recommandés)
- **Maximum :** 10 tags (éviter la sur-classification)
- **Optimal :** 7-8 tags

### Cohérence

- Utiliser **exactement** les tags listés ci-dessus
- Respecter la **casse** (minuscules)
- Respecter les **accents** (`#cuisine/thaï` pas `#cuisine/thai`)
- Utiliser les **tirets** (`#plat-principal` pas `#plat_principal`)

### Éviter

- ❌ Tags personnalisés non documentés
- ❌ Tags vagues (`#bon`, `#facile`)
- ❌ Doublons de sens (`#temps/express` + `#rapide`)
- ❌ Tags trop spécifiques (`#poulet/cuisse/désossé`)

## 🔍 Comment Choisir les Tags

### Étape 1 : Tags Obligatoires

1. **Cuisine** : D'où vient cette recette ?
2. **Type** : C'est quoi dans le repas ?
3. **Protéine** : Quel est l'ingrédient principal ?

### Étape 2 : Temps et Cuisson

4. **Temps** : Combien de temps total ?
5. **Cuisson** : Quelle méthode de cuisson ?

### Étape 3 : Contexte

6. **Difficulté** : Quel niveau requis ?
7. **Occasion** : Pour quel moment ?

### Étape 4 : Caractéristiques (Optionnel)

8-10. Ajouter 0-3 tags pour :
   - Restrictions diététiques
   - Profil de saveur
   - Équipement spécial

## 📝 Intégration dans le Frontmatter

Les tags doivent être ajoutés dans le frontmatter YAML en début de fichier :

```yaml
---
cuisine: japonaise
type: plat-principal
temps_prep: 30
temps_cuisson: 15
temps_total: 45
portions: 4
difficulté: intermédiaire
protéine: porc
source: YouTube
url: https://example.com
date_ajout: 2025-11-23
tags:
  - #cuisine/japonaise
  - #type/plat-principal
  - #protéine/porc
  - #temps/moyen
  - #cuisson/poêle
  - #difficulté/intermédiaire
  - #occasion/weekend
---
```

## 🔗 Navigation

- [Retour au README](../README.md)
- [Template de recette](../templates/recette-template.md)
- [Voir les index](../index/)

---

**Dernière mise à jour :** 2025-11-23
