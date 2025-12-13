---
title: "SVG"
weight: 50
---
<h1 class="">
 SVG
</h1>
<div class="">
 <p>
  Le Scalar Vector Graphics (SVG) est un format d'image vectorielle basé sur le langage XML, permettant de créer des graphiques évolutifs qui s'adaptent sans perte de qualité à toutes les tailles d'écran. Contrairement aux images matricielles (comme PNG ou JPEG), les SVG sont définis par des instructions textuelles décrivant des formes, des couleurs et des transformations, ce qui les rend légers, modifiables et idéaux pour le web. Grâce à leur intégration dans le HTML, les SVG peuvent être manipulés dynamiquement avec CSS ou JavaScript pour créer des animations ou des graphiques interactifs.
 </p>
 <p>
  On utilise de plus en plus la norme Scalar Vector Graphics (SVG)
        pour dessiner des figures en utilisant le XML. Vous pouvez déjà utiliser le format
        SVG avec plusieurs logiciels de bureautique ou tout simplement insérer
        un élément « svg » dans un document HTML comme nous allons le voir.
 </p>
 <p>
  La syntaxe SVG (Scalable Vector Graphics) repose sur un langage basé sur XML pour décrire des graphiques vectoriels bidimensionnels. Les principaux concepts incluent les éléments graphiques comme rect, circle, line, polygon ou path, qui définissent des formes géométriques. Ces éléments sont configurés via des attributs tels que x, y pour la position, width, height pour les dimensions, ou fill et stroke pour les couleurs et contours. Les transformations (via transform) permettent de déplacer, faire pivoter ou mettre à l’échelle les formes. SVG utilise un système de coordonnées où l’origine (0,0) est en haut à gauche, et les unités peuvent être absolues (px, cm) ou relatives (%). Enfin, les groupes (g) et les styles (via CSS ou l’attribut style) facilitent l’organisation et la personnalisation des éléments, rendant SVG flexible pour des graphiques interactifs et adaptatifs.
 </p>
 <p>
  Les attributs en SVG jouent un rôle clé pour définir les propriétés des éléments graphiques et contrôler leur apparence ou comportement. Parmi les attributs géométriques, on trouve x et y pour positionner un élément, width et height pour ses dimensions, ou cx et cy pour le centre d’un cercle. Les attributs de présentation comme fill déterminent la couleur de remplissage, stroke la couleur et stroke-width l’épaisseur du contour, tandis que opacity ajuste la transparence. Pour les formes complexes, path utilise l’attribut d pour décrire des trajectoires via des commandes comme M (move to), L (line to) ou C (courbe de Bézier). Les attributs de transformation, comme transform avec translate, rotate ou scale, modifient la position ou l’orientation. Enfin, des attributs comme id et class permettent d’identifier ou de styliser via CSS, et viewBox contrôle le cadre de visualisation pour un rendu adaptatif. Ces attributs offrent une grande précision pour personnaliser les graphiques SVG.
 </p>
 <h2>
  Principales balises et éléments SVG
 </h2>
 <p>
  Voici les éléments les plus couramment utilisés, avec leur rôle et un exemple simple.
 </p>
 <style>
  td {padding: 0.2em;}
 </style>
 <table border="1">
  <thead>
   <tr>
    <th>
     Élément
    </th>
    <th>
     Description
    </th>
    <th>
     Exemple d’utilisation
    </th>
    <th>
     Rendu approximatif
    </th>
   </tr>
  </thead>
  <tbody>
   <tr>
    <td>
     <code>
      &lt;svg&gt;
     </code>
    </td>
    <td>
     Conteneur racine obligatoire. Définit la zone de dessin avec
     <code>
      width
     </code>
     ,
     <code>
      height
     </code>
     et
     <code>
      viewBox
     </code>
     .
    </td>
    <td>
     <code>
      &lt;svg width="200" height="200" viewBox="0 0 200 200"&gt;&lt;/svg&gt;
     </code>
    </td>
    <td>
     Zone carrée 200×200
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;rect&gt;
     </code>
    </td>
    <td>
     Rectangle (coins éventuellement arrondis avec
     <code>
      rx
     </code>
     et
     <code>
      ry
     </code>
     ).
    </td>
    <td>
     <code>
      &lt;rect x="10" y="10" width="100" height="60" rx="10"/&gt;
     </code>
    </td>
    <td>
     Rectangle arrondi
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;circle&gt;
     </code>
    </td>
    <td>
     Cercle défini par centre (
     <code>
      cx
     </code>
     ,
     <code>
      cy
     </code>
     ) et rayon
     <code>
      r
     </code>
     .
    </td>
    <td>
     <code>
      &lt;circle cx="100" cy="100" r="80"/&gt;
     </code>
    </td>
    <td>
     Cercle centré
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;ellipse&gt;
     </code>
    </td>
    <td>
     Ellipse avec rayons horizontal
     <code>
      rx
     </code>
     et vertical
     <code>
      ry
     </code>
     .
    </td>
    <td>
     <code>
      &lt;ellipse cx="100" cy="70" rx="80" ry="40"/&gt;
     </code>
    </td>
    <td>
     Ovale
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;line&gt;
     </code>
    </td>
    <td>
     Segment de droite entre deux points.
    </td>
    <td>
     <code>
      &lt;line x1="0" y1="0" x2="200" y2="100"/&gt;
     </code>
    </td>
    <td>
     Diagonale
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;polyline&gt;
     </code>
    </td>
    <td>
     Série de segments connectés (liste de points).
    </td>
    <td>
     <code>
      &lt;polyline points="0,100 50,20 100,80 150,10 200,100"/&gt;
     </code>
    </td>
    <td>
     Ligne brisée
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;polygon&gt;
     </code>
    </td>
    <td>
     Polygone fermé (le dernier point est relié au premier).
    </td>
    <td>
     <code>
      &lt;polygon points="100,10 160,90 40,90"/&gt;
     </code>
    </td>
    <td>
     Triangle
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;path&gt;
     </code>
    </td>
    <td>
     Forme la plus puissante : courbes de Bézier, arcs, etc. via l’attribut
     <code>
      d
     </code>
     .
    </td>
    <td>
     <code>
      &lt;path d="M10 80 C 40 10, 65 10, 95 80 S 150 150, 180 80"/&gt;
     </code>
    </td>
    <td>
     Courbe cubique symétrique
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;text&gt;
     </code>
    </td>
    <td>
     Texte. Position avec
     <code>
      x
     </code>
     ,
     <code>
      y
     </code>
     ; rotation avec
     <code>
      transform
     </code>
     ou
     <code>
      rotate
     </code>
     .
    </td>
    <td>
     <code>
      &lt;text x="100" y="50" text-anchor="middle"&gt;Bonjour&lt;/text&gt;
     </code>
    </td>
    <td>
     Texte centré
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;tspan&gt;
     </code>
    </td>
    <td>
     Sous-élément de
     <code>
      &lt;text&gt;
     </code>
     pour changer de style ou position à l’intérieur d’un même texte.
    </td>
    <td>
     <code>
      &lt;text&gt;&lt;tspan font-weight="bold"&gt;Gras&lt;/tspan&gt; normal&lt;/text&gt;
     </code>
    </td>
    <td>
     Partie en gras
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;g&gt;
     </code>
    </td>
    <td>
     Groupe d’éléments. Permet d’appliquer des attributs ou transformations communes.
    </td>
    <td>
     <code>
      &lt;g fill="red"&gt;&lt;circle …/&gt;&lt;rect …/&gt;&lt;/g&gt;
     </code>
    </td>
    <td>
     Tous les enfants en rouge
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;defs&gt;
     </code>
    </td>
    <td>
     Définit des éléments réutilisables (gradients, patterns, symboles, clipPath…).
    </td>
    <td>
     <code>
      &lt;defs&gt;&lt;linearGradient id="grad"&gt;…&lt;/linearGradient&gt;&lt;/defs&gt;
     </code>
    </td>
    <td>
     —
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;use&gt;
     </code>
    </td>
    <td>
     Réutilise un élément défini dans
     <code>
      &lt;defs&gt;
     </code>
     ou ailleurs.
    </td>
    <td>
     <code>
      &lt;use href="#monSymbole" x="50" y="50"/&gt;
     </code>
    </td>
    <td>
     Instance du symbole
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;linearGradient&gt;
     </code>
     &amp;
     <code>
      &lt;radialGradient&gt;
     </code>
    </td>
    <td>
     Dégradés linéaire ou radial.
    </td>
    <td>
     <code>
      &lt;linearGradient id="g1"&gt;&lt;stop offset="0%" stop-color="gold"/&gt;&lt;stop offset="100%" stop-color="red"/&gt;&lt;/linearGradient&gt;
     </code>
    </td>
    <td>
     Dégradé or → rouge
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;pattern&gt;
     </code>
    </td>
    <td>
     Motif répétitif (carreaux, rayures, images…).
    </td>
    <td>
     <code>
      &lt;pattern id="dots" …&gt;&lt;circle cx="5" cy="5" r="3"/&gt;&lt;/pattern&gt;
     </code>
    </td>
    <td>
     Points répétés
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;marker&gt;
     </code>
    </td>
    <td>
     Flèches ou symboles aux extrémités de
     <code>
      &lt;path&gt;
     </code>
     ,
     <code>
      &lt;line&gt;
     </code>
     , etc.
    </td>
    <td>
     <code>
      &lt;marker id="fleche"&gt;&lt;path d="M0,0 L0,6 L9,3 z"/&gt;&lt;/marker&gt;
     </code>
    </td>
    <td>
     Flèche à la fin du trait
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;clipPath&gt;
     </code>
    </td>
    <td>
     Masque de découpage.
    </td>
    <td>
     <code>
      &lt;clipPath id="cercleClip"&gt;&lt;circle cx="100" cy="100" r="80"/&gt;&lt;/clipPath&gt;
     </code>
    </td>
    <td>
     Ne montre que l’intérieur du cercle
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;filter&gt;
     </code>
     + primitives (
     <code>
      &lt;feGaussianBlur&gt;
     </code>
     ,
     <code>
      &lt;feOffset&gt;
     </code>
     , etc.)
    </td>
    <td>
     Effets graphiques (ombre portée, flou, glow…).
    </td>
    <td>
     <code>
      &lt;filter id="ombre"&gt;&lt;feGaussianBlur stdDeviation="4"/&gt;&lt;/filter&gt;
     </code>
    </td>
    <td>
     Ombre floue
    </td>
   </tr>
  </tbody>
 </table>
 <br/>
 <p>
  Ces éléments couvrent la très grande majorité des besoins en illustration vectorielle, diagrammes, icônes animées et graphiques interactifs dans les pages web modernes. SVG est entièrement stylisable avec CSS et animable avec SMIL ou JavaScript.
 </p>
 <h2>
  Laboratoire
 </h2>
 <p>
  Je vous invite à éditer le code SVG au sein de la boîte suivante pour observer le résultat. Le SVG est notamment mis en forme à l'aide du CSS, un notion que nous
  allons explorer plus tard dans le cours.
 </p>
 <h2 style="text-align: center;">
  Code SVG
 </h2>
 <textarea id="svgCode" style="width: 100%; height: 300px; background: #f4f4f4; padding: 10px; border-radius: 5px; font-family: monospace; resize: vertical;">&lt;svg width="300" height="200" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg"&gt;
    &lt;rect x="20" y="20" width="100" height="60" style="fill: #3498db; stroke: #2c3e50; stroke-width: 2;" /&gt;
    &lt;circle cx="200" cy="50" r="30" style="fill: #e74c3c; stroke: #2c3e50; stroke-width: 2;" /&gt;
    &lt;line x1="20" y1="120" x2="280" y2="180" style="stroke: #27ae60; stroke-width: 4;" /&gt;
&lt;/svg&gt;
            </textarea>
</div>
<div style="width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px;">
 <h2 style="text-align: center;">
  Rendu SVG
 </h2>
 <div id="svgRender">
  <svg height="200" viewbox="0 0 300 200" width="300" xmlns="http://www.w3.org/2000/svg">
   <rect height="60" style="fill: #3498db; stroke: #2c3e50; stroke-width: 2;" width="100" x="20" y="20">
   </rect>
   <circle cx="200" cy="50" r="30" style="fill: #e74c3c; stroke: #2c3e50; stroke-width: 2;">
   </circle>
   <line style="stroke: #27ae60; stroke-width: 4;" x1="20" x2="280" y1="120" y2="180">
   </line>
  </svg>
 </div>
 <script>
  const textarea = document.getElementById('svgCode');
        const renderDiv = document.getElementById('svgRender');
        textarea.addEventListener('input', () => {
            try {
                renderDiv.innerHTML = textarea.value;
            } catch (error) {
                console.error('Erreur SVG:', error);
            }
        });
 </script>
</div>
<p>
 Pour approfondir votre compréhension du SVG, essayez les activités suivantes dans la boîte de code ci-dessus :
</p>
<ol>
 <li>
  Changez la couleur du rectangle (par exemple, remplacez
  <code>
   fill: #3498db
  </code>
  par
  <code>
   fill: #f1c40f
  </code>
  ) ou ajustez le rayon du cercle (modifiez
  <code>
   r="30"
  </code>
  à
  <code>
   r="50"
  </code>
  ).
 </li>
 <li>
  Insérez un triangle en utilisant l'élément
  <code>
   &lt;polygon points="150,100 200,150 100,150" style="fill: #8e44ad; stroke: #2c3e50; stroke-width: 2;" /&gt;
  </code>
  à l'intérieur de la balise
  <code>
   &lt;svg&gt;
  </code>
  .
 </li>
 <li>
  Appliquez une rotation au rectangle en ajoutant
  <code>
   transform="rotate(45 70 50)"
  </code>
  à l'élément
  <code>
   &lt;rect&gt;
  </code>
  pour le faire pivoter autour de son centre.
 </li>
 <li>
  Combinez plusieurs formes (cercles, rectangles, lignes) pour dessiner une maison simple ou un autre objet de votre choix.
 </li>
 <li>
  Testez des propriétés CSS comme
  <code>
   fill-opacity: 0.5
  </code>
  ou
  <code>
   stroke-dasharray: 5,5
  </code>
  pour créer des effets de transparence ou de pointillés.
 </li>
</ol>
<p>
 On peut utiliser la norme SVG pour générer des graphiques dynamiques au sein de pages web scriptées.
</p>
<hr/>
