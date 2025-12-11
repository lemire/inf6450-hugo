---
title: "CSS (partie 3)"
weight: 44
---

# CSS (partie 3)

### Quand le contenu excède le contenant

Il arrive qu’une image ou qu’un texte excède la taille de l’élément dans lequel il a été placé. Par défaut, ce contenu déborde visiblement (`overflow: visible`). La propriété `overflow: hidden` permet de contrôler ce comportement :

- `overflow: hidden` masque la partie qui dépasse.
- `overflow: scroll` ajoute des barres de défilement (même si le contenu tient dans la boîte).
- `overflow: auto` n’ajoute les barres que si nécessaire.

### Encodage des caractères

Il peut être utile de préciser l’encodage utilisé dans le fichier CSS en plaçant au tout premier ligne :

```css
@charset "UTF-8";
```

ou

```css
@charset "ISO-8859-1";
```

### Différentes règles pour différents médias

On peut appliquer des règles CSS différentes selon le type de média avec `@media` :

```css
@media print, handheld {
    img { display: none; }
    h1 { color: black; }
}

@media screen, tv {
    h1 { color: blue; }
}
```

Sans `@media`, la règle s’applique à tous les médias.

### Inclure d’autres fichiers CSS

Pour une approche modulaire, on peut importer d’autres feuilles de style avec `@import` (à placer après un éventuel `@charset`) :

```css
@import "mineure.css";
@import "print-mineure.css" print;
```

### Indentation de la première ligne d’un paragraphe

```css
p {
    text-indent: 1cm;
}
```

### Modifier la casse du texte

```css
h1 { text-transform: uppercase; }     /* TOUT EN MAJUSCULES */
h2 { text-transform: capitalize; } /* Première Lettre De Chaque Mot */
p  { text-transform: lowercase; }     /* tout en minuscules */
```

### Autres variantes des polices

Quelques propriétés courantes :

- `font-style: italic;` ou `oblique`
- `font-weight: bold;`, `bolder;`, `lighter`
- `font-family: serif;`, `sans-serif;`, `"Trebuchet MS", Arial, sans-serif`
- `font-size: small;`, `large;`, `120%;`, `1.2em`
- `text-decoration: underline;`, `overline;`, `line-through;`, `blink;`
- `cursor: pointer;` (main pour les liens), `text`, `wait`, etc.

### Ajouter des compteurs

Exemple 1 – numérotation romaine des paragraphes entre chaque `<h1>` :

```css
p { counter-increment: par-num; }
h1 { counter-reset: par-num; }
p:before { content: counter(par-num, upper-roman) ". "; }
```

Exemple 2 – numérotation simple des titres `<h1>` :

```css
h1 { counter-increment: h1-num; }
h1:before { content: counter(h1-num, decimal) ". "; }
```

### Traitement des retours de chariot

- `white-space: normal` → comportement par défaut (les retours à la ligne du source sont ignorés)
- `white-space: pre` → préserve tous les espaces et retours à la ligne (utile pour du code)
- `white-space: nowrap` → empêche tout retour à la ligne automatique

### Des nouveautés en CSS 3

CSS 3 introduit de nombreux nouveaux sélecteurs. Voici les plus utilisés :

| Sélecteur         | Signification                                                        | Niveau CSS |
|-------------------|----------------------------------------------------------------------|------------|
| *                 | tout élément                                                         | 2          |
| E                 | un élément de nom E                                                  | 1          |
| E[foo]            | élément E possédant l’attribut foo                                   | 2          |
| E[foo="bar"]      | attribut foo vaut exactement « bar »                                 | 2          |
| E[foo~="bar"]     | attribut foo contient le mot « bar » (séparé par espaces)            | 2          |
| E[foo^="bar"]     | attribut foo commence par « bar »                                    | 3          |
| E[foo$="bar"]     | attribut foo se termine par « bar »                                  | 3          |
| E[foo*="bar"]     | attribut foo contient la chaîne « bar »                              | 3          |
| E[foo|="bar"]     | attribut foo contient le mot « bar » (séparé par tirets)           | 2          |
| E F               | descendant F de E                                                    | 1          |
| E > F             | enfant direct F de E                                                 | 2          |
| E + F             | F immédiatement après un voisin E                                               | 2          |
| E ~ F             | F après un voisin quelconque E                                       | 3          |

Grâce à ces sélecteurs, on peut par exemple cibler tous les liens externes :

```css
a[href^="http"] { /* indique un lien externe */ }
```

CSS 3 permet aussi d’arrondir les coins :

```html
<span style="border: 2px solid blue; border-radius: 25px; padding: 2px;">
  Entoure-moi!
</span>
```

ou de transformer géométriquement le texte :

```css
p.rotated { transform: rotate(180deg); }
p.mirror  { transform: scale(-1, 1); }
```

### Optimisation des fichiers CSS

Un même effet peut souvent s’obtenir de façon plus concise en regroupant les déclarations communes :

```css
montant, nom, texte {
    background: white;
    font-style: normal;
}

montant {
    color: red;
    font-weight: bold;
    text-align: center;
}

nom {
    color: white;
    text-align: left;
}

texte {
    color: black;
    text-align: left;
}
```

Des outils comme CSSTidy peuvent automatiser ce genre d’optimisation.

### En terminant

La syntaxe CSS est extrêmement riche. Pour aller plus loin, consultez la référence officielle :  
[https://developer.mozilla.org/fr/docs/Web/CSS](https://developer.mozilla.org/fr/docs/Web/CSS)

### Livres de référence

- David Sawyer McFarland, *CSS: The Missing Manual*, O'Reilly Media, 2015, 718 pages.