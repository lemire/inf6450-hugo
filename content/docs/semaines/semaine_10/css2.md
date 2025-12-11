---
title: "CSS (partie 2)"
weight: 42
---

# CSS (partie 2)

### Mais que se passe-t-il en cas de conflit ?

Plusieurs instructions peuvent s'appliquer en même temps : un texte peut être en rouge et souligné. Il peut arriver cependant que deux instructions CSS se contredisent. Par exemple, un texte ne peut être à la fois en rouge et en bleu. Dans ce cas, la sélection la plus spécifique l’emporte. Ainsi, dans l’exemple qui suit :

```css
* {
    color: black;
}
montant {
    color: red;
}
montant > montant {
    color: yellow;
}
```

les éléments « montant » seront en rouge, sauf s’ils sont immédiatement contenus dans un autre élément « montant », auquel cas ils seront en jaune.

Par ailleurs, si deux sélections de même spécificité sont rencontrées, c’est la dernière qui l’emporte. Ainsi, dans l’exemple qui suit :

```css
montant {
    color: red;
}
montant {
    color: black;
}
```

les éléments « montant » seront en noir.

On peut cependant forcer le navigateur à considérer une règle qui apparaît avant une autre comme ayant tout de même priorité (à spécificité égale). Il suffit d’utiliser la mention `!important` :

```css
montant {
    color: red !important;
}
montant {
    color: black;
}
```

les éléments « montant » seront en rouge.  
Notez que la mention `!important` permet souvent d’ignorer la spécificité de la règle : les règles avec cette mention l’emportent toujours sur les autres (sauf si une autre règle avec `!important` a une plus grande spécificité, elle aura alors priorité).

Les règles par défaut utilisées par votre navigateur dans le cas du HTML ou du XHTML sont lues en premier. De cette manière, toutes les règles que vous stipulez dans vos propres fichiers CSS ou directement dans le XML/HTML ont priorité pour une même spécificité. On peut considérer que les règles avec la mention `!important` sont lues en dernier dans la mesure où elles l’emportent toujours sur les autres.

Calculer la [spécificité des règles](http://www.w3.org/TR/CSS21/cascade.html#specificity) n’est pas une mince affaire, mais c’est pourtant nécessaire dans certains cas difficiles. La spécificité se mesure avec une valeur à 4 chiffres (a,b,c,d). Lorsqu’on compare deux spécificités (a1,b1,c1,d1) et (a2,b2,c2,d2), on utilise l’ordre lexicographique pour déterminer laquelle est supérieure.

- La première valeur (a) vaut 1 si et seulement si la règle apparaît dans l’attribut `style` de l’élément lui-même.
- La seconde valeur (b) est le nombre de sélecteurs ID présents dans la règle.
- La troisième valeur (c) est le nombre d’autres sélecteurs d’attributs et de pseudo-classes.
- La quatrième valeur (d) est le nombre de sélecteurs de type élément et de pseudo-éléments.

Exemple concret :

```css
z[x] > a[i]         { color: blue; }           /* spécificité : 0,0,2,2 */
z z[x] a            { text-decoration: underline; } /* 0,0,1,3 */
z > z a , z z z + a { color: red ; }           /* deux règles : 0,0,0,3 et 0,0,0,4 */
```

### Le modèle de boîte CSS

En CSS, on peut spécifier la hauteur et la largeur d’un objet à l’aide des propriétés `width` et `height`. Par exemple, pour indiquer qu’un paragraphe ne doit avoir que 20 pixels de largeur :

```css
p {
    width: 20px;
}
```

Le CSS supporte de nombreuses unités : px, cm, in, %, em, rem, etc.

On peut ensuite définir une marge (margin) autour de tout objet. La marge est une zone transparente où rien ne peut apparaître ; elle ne fait pas partie de l’objet lui-même.

```css
p {
    margin-top: 10px;
    margin-bottom: 10px;
    margin-right: 10px;
    margin-left: 10px;
}
```

On peut aussi définir une région d’espacement interne (padding). Contrairement à la marge, le padding fait partie de l’objet : si vous définissez une couleur de fond, le padding sera coloré.

```css
p {
    padding-top: 10px;
    padding-bottom: 10px;
    padding-right: 10px;
    padding-left: 10px;
}
```

On peut enfin ajouter une bordure (border) qui se place entre le padding et la marge :

```css
p {
    border-color: black;
    border-width: medium;
}
```

Voici un diagramme qui résume le modèle de boîte CSS (le diagramme original étant en SVG, il n’est pas reproduit ici, mais il montre les zones suivantes de l’intérieur vers l’extérieur : contenu → padding → border → margin).




<svg height="350" width="1000" xmlns="http://www.w3.org/2000/svg">
 <g style="stroke-width:.025in; stroke:black; fill:none" transform="scale(0.07) translate(-1500,-300)">
  ../module3/box.pdf
  <defs>
   <pattern height="200" id="tile1" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 0 -100 200 16">
    </path>
    <path d="M 0 -60 200 56">
    </path>
    <path d="M 0 -20 200 96">
    </path>
    <path d="M 0 20 200 136">
    </path>
    <path d="M 0 60 200 176">
    </path>
    <path d="M 0 100 200 216">
    </path>
    <path d="M 0 140 200 256">
    </path>
    <path d="M 0 180 200 296">
    </path>
   </pattern>
   <pattern height="200" id="tile2" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 200 -100 0 16">
    </path>
    <path d="M 200 -60 0 56">
    </path>
    <path d="M 200 -20 0 96">
    </path>
    <path d="M 200 20 0 136">
    </path>
    <path d="M 200 60 0 176">
    </path>
    <path d="M 200 100 0 216">
    </path>
    <path d="M 200 140 0 256">
    </path>
    <path d="M 200 180 0 296">
    </path>
   </pattern>
   <pattern height="200" id="tile3" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 0 -100 200 16">
    </path>
    <path d="M 200 -100 0 16">
    </path>
    <path d="M 0 -60 200 56">
    </path>
    <path d="M 200 -60 0 56">
    </path>
    <path d="M 0 -20 200 96">
    </path>
    <path d="M 200 -20 0 96">
    </path>
    <path d="M 0 20 200 136">
    </path>
    <path d="M 200 20 0 136">
    </path>
    <path d="M 0 60 200 176">
    </path>
    <path d="M 200 60 0 176">
    </path>
    <path d="M 0 100 200 216">
    </path>
    <path d="M 200 100 0 216">
    </path>
    <path d="M 0 140 200 256">
    </path>
    <path d="M 200 140 0 256">
    </path>
    <path d="M 0 180 200 296">
    </path>
    <path d="M 200 180 0 296">
    </path>
   </pattern>
   <pattern height="200" id="tile4" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 100 0 200 100">
    </path>
    <path d="M 0 0 200 200">
    </path>
    <path d="M 0 100 100 200">
    </path>
   </pattern>
   <pattern height="200" id="tile5" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 100 0 0 100">
    </path>
    <path d="M 200 0 0 200">
    </path>
    <path d="M 200 100 100 200">
    </path>
   </pattern>
   <pattern height="200" id="tile6" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 100 0 200 100">
    </path>
    <path d="M 0 0 200 200">
    </path>
    <path d="M 0 100 100 200">
    </path>
    <path d="M 100 0 0 100">
    </path>
    <path d="M 200 0 0 200">
    </path>
    <path d="M 200 100 100 200">
    </path>
   </pattern>
   <pattern height="200" id="tile7" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 0 0 0 50">
    </path>
    <path d="M 0 50 200 50">
    </path>
    <path d="M 100 50 100 150">
    </path>
    <path d="M 0 150 200 150">
    </path>
    <path d="M 0 150 0 200">
    </path>
   </pattern>
   <pattern height="200" id="tile8" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 0 0 50 0">
    </path>
    <path d="M 50 0 50 200">
    </path>
    <path d="M 50 100 150 100">
    </path>
    <path d="M 150 0 150 200">
    </path>
    <path d="M 150 0 200 0">
    </path>
   </pattern>
   <pattern height="200" id="tile9" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 0 50 200 50">
    </path>
    <path d="M 0 150 200 150">
    </path>
   </pattern>
   <pattern height="200" id="tile10" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 50 0 50 200">
    </path>
    <path d="M 150 0 150 200">
    </path>
   </pattern>
   <pattern height="200" id="tile11" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 0 50 200 50">
    </path>
    <path d="M 0 150 200 150">
    </path>
    <path d="M 50 0 50 200">
    </path>
    <path d="M 150 0 150 200">
    </path>
   </pattern>
   <pattern height="200" id="tile12" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 0 0 25 50">
    </path>
    <path d="M 0 50 200 50">
    </path>
    <path d="M 100 50 125 150">
    </path>
    <path d="M 0 150 200 150">
    </path>
    <path d="M 0 150 25 200">
    </path>
   </pattern>
   <pattern height="200" id="tile13" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 200 0 175 50">
    </path>
    <path d="M 0 50 200 50">
    </path>
    <path d="M 100 50 75 150">
    </path>
    <path d="M 0 150 200 150">
    </path>
    <path d="M 200 150 175 200">
    </path>
   </pattern>
   <pattern height="200" id="tile14" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 0 0 50 25">
    </path>
    <path d="M 50 0 50 200">
    </path>
    <path d="M 50 100 150 125">
    </path>
    <path d="M 150 0 150 200">
    </path>
    <path d="M 150 0 200 25">
    </path>
   </pattern>
   <pattern height="200" id="tile15" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 0 25 50 0">
    </path>
    <path d="M 50 0 50 200">
    </path>
    <path d="M 50 125 150 100">
    </path>
    <path d="M 150 0 150 200">
    </path>
    <path d="M 150 25 200 0">
    </path>
   </pattern>
   <pattern height="200" id="tile16" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 0 50 A 50 50 0 1 0 100 50">
    </path>
    <path d="M 100 50 A 50 50 0 1 0 200 50">
    </path>
    <path d="M 50 100 A 50 50 0 1 0 150 100">
    </path>
    <path d="M 0 150 A 50 50 0 0 0 50 100">
    </path>
    <path d="M 150 100 A 50 50 0 1 0 200 50">
    </path>
    <path d="M 50 0 A 50 50 0 1 0 150 0">
    </path>
    <path d="M 150 0 A 50 50 0 0 0 200 50">
    </path>
    <path d="M 0 50 A 50 50 0 0 0 50 0">
    </path>
    <path d="M 0 150 A 50 50 0 1 0 100 150">
    </path>
    <path d="M 100 150 A 50 50 0 1 0 200 150">
    </path>
   </pattern>
   <pattern height="100" id="tile17" patternunits="userSpaceOnUse" width="100" x="0" y="0">
    <g transform="scale(0.5)">
     <path d="M 0 50 A 50 50 0 1 0 100 50">
     </path>
     <path d="M 100 50 A 50 50 0 1 0 200 50">
     </path>
     <path d="M 50 100 A 50 50 0 1 0 150 100">
     </path>
     <path d="M 0 150 A 50 50 0 0 0 50 100">
     </path>
     <path d="M 150 100 A 50 50 0 1 0 200 50">
     </path>
     <path d="M 50 0 A 50 50 0 1 0 150 0">
     </path>
     <path d="M 150 0 A 50 50 0 0 0 200 50">
     </path>
     <path d="M 0 50 A 50 50 0 0 0 50 0">
     </path>
     <path d="M 0 150 A 50 50 0 1 0 100 150">
     </path>
     <path d="M 100 150 A 50 50 0 1 0 200 150">
     </path>
    </g>
   </pattern>
   <pattern height="200" id="tile18" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <circle cx="100" cy="100" r="100">
    </circle>
   </pattern>
   <pattern height="200" id="tile19" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 0 50 45 0 105 0 140 50 200 50 ">
    </path>
    <path d="M 0 50 45 100 105 100 140 50 200 50">
    </path>
    <path d="M 0 150 45 100 105 100 140 150 200 150">
    </path>
    <path d="M 0 150 45 200 105 200 140 150 200 150">
    </path>
   </pattern>
   <pattern height="200" id="tile20" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 0 70 65 0 140 0 200 70 ">
    </path>
    <path d="M 0 70 0 130 65 200 140 200 200 130 200 70">
    </path>
   </pattern>
   <pattern height="200" id="tile21" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 50 0 75 25 100 0 M 150 0 175 25 200 0">
    </path>
    <path d="M 0 50 25 25 75 75 125 25 175 75 200 50">
    </path>
    <path d="M 0 100 25 75 75 125 125 75 175 125 200 100">
    </path>
    <path d="M 0 150 25 125 75 175 125 125 175 175 200 150">
    </path>
    <path d="M 0 200 25 175 75 225 125 175 175 225 200 200">
    </path>
   </pattern>
   <pattern height="200" id="tile22" patternunits="userSpaceOnUse" width="200" x="0" y="0">
    <path d="M 0 50 25 75 0 100 M 0 150 25 175 0 200">
    </path>
    <path d="M 50 0 25 25 75 75 25 125 75 175 50 200">
    </path>
    <path d="M 100 0 75 25 125 75 75 125 125 175 100 200">
    </path>
    <path d="M 150 0 125 25 175 75 125 125 175 175 150 200">
    </path>
    <path d="M 200 0 175 25 225 75 175 125 225 175 200 200">
    </path>
   </pattern>
  </defs>
  <!-- Line -->
  <path d="M 2700,1350 7650,1350 7650,3375 2700,3375 2700,1350 " style="stroke:#000000;stroke-width:75; fill:#00ffff; ">
  </path>
  <!-- Line -->
  <path d="M 2250,975 8250,975 8250,3825 2250,3825 2250,975 " style="stroke:#000000;stroke-width:15; stroke-dasharray:50 50; ">
  </path>
  <!-- Line -->
  <path d="M 8775,1575 " style="stroke:#000000;stroke-width:15; ">
  </path>
  <!-- Line -->
  <path d="M 7125,2925 7125,4425 " style="stroke:#000000;stroke-width:15; stroke-dasharray:10 10 10; ">
  </path>
  <!-- Line -->
  <path d="M 7125,2925 8850,2925 " style="stroke:#000000;stroke-width:15; stroke-dasharray:10 10 10; ">
  </path>
  <!-- Line -->
  <path d="M 7125,1800 8850,1800 " style="stroke:#000000;stroke-width:15; stroke-dasharray:10 10 10; ">
  </path>
  <!-- Line -->
  <path d="M 3300,4425 7050,4425 " style="stroke:#000000;stroke-width:15; ">
  </path>
  <!-- Arrowhead on endpoint -->
  <path d="M 6914 4455 7034 4425 6914 4395 6914 4455 Z " style="stroke:#000000;stroke-width:15; fill:white;">
  </path>
  <!-- Arrowhead on startpoint -->
  <path d="M 3436 4395 3316 4425 3436 4455 3436 4395 Z " style="stroke:#000000;stroke-width:15; fill:white;">
  </path>
  <!-- Line -->
  <path d="M 3300,3000 3300,4425 " style="stroke:#000000;stroke-width:15; stroke-dasharray:10 10 10; ">
  </path>
  <!-- Line -->
  <path d="M 8550,2850 8550,1800 " style="stroke:#000000;stroke-width:15; ">
  </path>
  <!-- Arrowhead on endpoint -->
  <path d="M 8580 1936 8550 1816 8520 1936 8580 1936 Z " style="stroke:#000000;stroke-width:15; fill:white;">
  </path>
  <!-- Arrowhead on startpoint -->
  <path d="M 8520 2714 8550 2834 8580 2714 8520 2714 Z " style="stroke:#000000;stroke-width:15; fill:white;">
  </path>
  <!-- Line -->
  <path d="M 3450,600 3450,1275 " style="stroke:#000000;stroke-width:15; ">
  </path>
  <!-- Arrowhead on endpoint -->
  <path d="M 3420 1138 3450 1258 3480 1138 " style="stroke:#000000;stroke-width:15; ">
  </path>
  <!-- Text -->
  <text fill="#ff0000" font-family="Times" font-size="214" font-style="normal" font-weight="normal" text-anchor="start" x="3300" y="3075">
   espacement (padding): espace laissé
  </text>
  <!-- Text -->
  <g transform="translate(7500,2850) rotate(-90)">
   <text fill="#000000" font-family="Times" font-size="214" font-style="normal" font-weight="normal" text-anchor="start" x="0" y="0">
    padding-right
   </text>
  </g>
  <!-- Text -->
  <text fill="#ff00ff" font-family="Times" font-size="214" font-style="normal" font-weight="normal" text-anchor="start" x="2850" y="3675">
   marge (margin): rien ne peut apparaître ici
  </text>
  <!-- Text -->
  <text fill="#000000" font-family="Times" font-size="214" font-style="normal" font-weight="normal" text-anchor="start" x="3975" y="4350">
   largeur de l'objet (width)
  </text>
  <!-- Text -->
  <text fill="#000000" font-family="Times" font-size="600" font-style="normal" font-weight="normal" text-anchor="start" x="3600" y="2700">
   Contenu ici
  </text>
  <!-- Text -->
  <text fill="#000000" font-family="Times" font-size="214" font-style="italic" font-weight="normal" text-anchor="start" x="4050" y="1650">
   padding-top
  </text>
  <!-- Text -->
  <g transform="translate(2475,2775) rotate(-90)">
   <text fill="#000000" font-family="Times" font-size="214" font-style="italic" font-weight="normal" text-anchor="start" x="0" y="0">
    margin-left
   </text>
  </g>
  <!-- Text -->
  <text fill="#000000" font-family="Times" font-size="214" font-style="italic" font-weight="normal" text-anchor="start" x="6300" y="3675">
   margin:bottom
  </text>
  <!-- Text -->
  <g transform="translate(8025,2550) rotate(-90)">
   <text fill="#000000" font-family="Times" font-size="214" font-style="italic" font-weight="normal" text-anchor="start" x="0" y="0">
    rmargin-right
   </text>
  </g>
  <!-- Text -->
  <text fill="#000000" font-family="Times" font-size="214" font-style="italic" font-weight="normal" text-anchor="start" x="4275" y="1200">
   margin-top
  </text>
  <!-- Text -->
  <text fill="#ff0000" font-family="Times" font-size="214" font-style="normal" font-weight="normal" text-anchor="start" x="3375" y="3300">
   vacant
  </text>
  <!-- Text -->
  <g transform="translate(9000,2850) rotate(-90)">
   <text fill="#000000" font-family="Times" font-size="214" font-style="normal" font-weight="normal" text-anchor="start" x="0" y="0">
    hauteur de l'objet (height)
   </text>
  </g>
  <!-- Text -->
  <text fill="#000000" font-family="Times" font-size="214" font-style="normal" font-weight="normal" text-anchor="start" x="3150" y="450">
   bordure (border)
  </text>
  <!-- Text -->
  <g transform="translate(3075,2775) rotate(-90)">
   <text fill="#000000" font-family="Times" font-size="214" font-style="italic" font-weight="normal" text-anchor="start" x="0" y="0">
    padding-left
   </text>
  </g>
  <!-- Line -->
  <path d="M 5625,1425 5625,1725 " style="stroke:#000000;stroke-width:15; ">
  </path>
  <!-- Arrowhead on endpoint -->
  <path d="M 5595 1656 5625 1716 5655 1656 5595 1656 Z " style="stroke:#000000;stroke-width:15; fill:white;">
  </path>
  <!-- Arrowhead on startpoint -->
  <path d="M 5655 1494 5625 1434 5595 1494 5655 1494 Z " style="stroke:#000000;stroke-width:15; fill:white;">
  </path>
  <!-- Line -->
  <path d="M 6600,3000 6600,3300 " style="stroke:#000000;stroke-width:15; ">
  </path>
  <!-- Arrowhead on endpoint -->
  <path d="M 6570 3231 6600 3291 6630 3231 6570 3231 Z " style="stroke:#000000;stroke-width:15; fill:white;">
  </path>
  <!-- Arrowhead on startpoint -->
  <path d="M 6630 3069 6600 3009 6570 3069 6630 3069 Z " style="stroke:#000000;stroke-width:15; fill:white;">
  </path>
  <!-- Line -->
  <path d="M 3300,1800 7125,1800 7125,2925 3300,2925 3300,1800 " style="stroke:#000000;stroke-width:15; stroke-dasharray:10 10 10; ">
  </path>
 </g>
</svg>



(Comme il se doit, ce diagramme est XML par l’entremise du SVG.)