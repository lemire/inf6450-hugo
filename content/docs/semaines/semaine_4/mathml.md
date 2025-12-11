---
title: "MathML"
weight: 40
---
<h1>
 MathML
</h1>
<style>
 td {padding:0.1em;}
</style>
<div>
 <p>
  Le Mathematical Markup Language (MathML) est un langage basé sur XML conçu pour représenter et afficher des expressions mathématiques de manière structurée sur le web. Contrairement aux images statiques ou aux approximations textuelles, MathML permet de décrire la sémantique et la présentation des formules mathématiques, offrant une accessibilité accrue et une intégration dynamique avec HTML. Il est particulièrement utilisé dans les contextes éducatifs, scientifiques et techniques pour rendre des équations complexes de façon précise et adaptable.
 </p>
 <p>
  MathML gagne en popularité pour afficher des formules mathématiques dans des documents web ou des logiciels spécialisés. Vous pouvez intégrer des éléments MathML directement dans un document HTML, comme nous allons le voir.
 </p>
 <p>
  La syntaxe MathML repose sur deux approches principales : la présentation (pour l’affichage visuel) et le contenu (pour la sémantique). Les éléments de présentation, comme mrow, mfrac, msup ou msqrt, organisent visuellement les expressions, tandis que les éléments de contenu, comme apply ou plus, décrivent leur structure logique. Les formules sont construites à partir d’éléments comme mi (identifiants), mn (nombres) et mo (opérateurs), placés dans une balise math. Les attributs comme display (block ou inline) contrôlent le rendu, et les styles CSS peuvent personnaliser l’apparence. MathML utilise un modèle arborescent où chaque élément imbriqué définit une partie de l’expression, garantissant une grande précision pour des formules complexes.
 </p>
 <p>
  Les attributs en MathML jouent un rôle essentiel pour ajuster l’apparence et le comportement des expressions. Par exemple, l’attribut mathvariant permet de définir le style des identifiants (par exemple, italic pour les variables). Les attributs comme numalign ou denomalign dans mfrac contrôlent l’alignement des fractions. Pour les exposants ou indices (msup, msub), l’attribut scriptlevel ajuste la taille du texte. Les éléments de présentation comme mtable permettent de créer des matrices avec des attributs comme rowspacing ou columnalign pour l’espacement et l’alignement. Enfin, l’attribut id facilite l’interaction avec CSS ou JavaScript, et xmlns garantit la compatibilité XML. Ces attributs offrent une flexibilité pour un rendu précis et accessible.
 </p>
 <h2>
  Principales balises de présentation MathML
 </h2>
 <p>
  Voici une description détaillée des balises les plus couramment utilisées en MathML de présentation (MathML-Presentation). Toutes ces balises doivent être placées à l’intérieur de l’élément racine
  <code>
   &lt;math&gt;
  </code>
  .
 </p>
 <table border="1" style="border-collapse: collapse; width: 100%; margin: 20px 10px;">
  <thead>
   <tr style="background-color: #f0f0f0;">
    <th>
     Balise
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
      &lt;math&gt;
     </code>
    </td>
    <td>
     Élément racine obligatoire de toute expression MathML. L’attribut
     <code>
      display="block"
     </code>
     ou
     <code>
      "inline"
     </code>
     contrôle le mode d’affichage.
    </td>
    <td>
     <code>
      &lt;math display="block"&gt;…&lt;/math&gt;
     </code>
    </td>
    <td>
     —
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;mi&gt;
     </code>
    </td>
    <td>
     Identifiant (variable, constante, fonction). Par défaut en italique.
    </td>
    <td>
     <code>
      &lt;mi&gt;x&lt;/mi&gt;
     </code>
     ou
     <code>
      &lt;mi mathvariant="normal"&gt;sin&lt;/mi&gt;
     </code>
    </td>
    <td>
     x, sin
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;mn&gt;
     </code>
    </td>
    <td>
     Nombre.
    </td>
    <td>
     <code>
      &lt;mn&gt;123.45&lt;/mn&gt;
     </code>
    </td>
    <td>
     123.45
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;mo&gt;
     </code>
    </td>
    <td>
     Opérateur, symbole ou séparateur (+, −, ×, =, (, etc.). L’espacement est géré automatiquement.
    </td>
    <td>
     <code>
      &lt;mo&gt;+&lt;/mo&gt;
     </code>
     ou
     <code>
      &lt;mo fence="true"&gt;(&lt;/mo&gt;
     </code>
    </td>
    <td>
     + , (
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;mtext&gt;
     </code>
    </td>
    <td>
     Texte brut (non mathématique), utile pour les unités ou commentaires.
    </td>
    <td>
     <code>
      &lt;mtext&gt;kg&lt;/mtext&gt;
     </code>
    </td>
    <td>
     kg
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;mrow&gt;
     </code>
    </td>
    <td>
     Groupe horizontal d’éléments. Sert à structurer l’arbre sans effet visuel particulier.
    </td>
    <td>
     <code>
      &lt;mrow&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mo&gt;+&lt;/mo&gt;&lt;mi&gt;b&lt;/mi&gt;&lt;/mrow&gt;
     </code>
    </td>
    <td>
     a + b
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;mfrac&gt;
     </code>
    </td>
    <td>
     Fraction. Attributs utiles :
     <code>
      bevelled="true"
     </code>
     ,
     <code>
      numalign
     </code>
     ,
     <code>
      denomalign
     </code>
     .
    </td>
    <td>
     <code>
      &lt;mfrac&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;b&lt;/mi&gt;&lt;/mfrac&gt;
     </code>
    </td>
    <td>
     a/b
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;msqrt&gt;
     </code>
    </td>
    <td>
     Racine carrée.
    </td>
    <td>
     <code>
      &lt;msqrt&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;/msqrt&gt;
     </code>
    </td>
    <td>
     √x
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;mroot&gt;
     </code>
    </td>
    <td>
     Racine n-ième (indice en premier enfant).
    </td>
    <td>
     <code>
      &lt;mroot&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mn&gt;3&lt;/mn&gt;&lt;/mroot&gt;
     </code>
    </td>
    <td>
     ³√x
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;msup&gt;
     </code>
    </td>
    <td>
     Exposant.
    </td>
    <td>
     <code>
      &lt;msup&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/msup&gt;
     </code>
    </td>
    <td>
     x²
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;msub&gt;
     </code>
    </td>
    <td>
     Indice.
    </td>
    <td>
     <code>
      &lt;msub&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/msub&gt;
     </code>
    </td>
    <td>
     x₁
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;msubsup&gt;
     </code>
    </td>
    <td>
     Indice et exposant simultanés.
    </td>
    <td>
     <code>
      &lt;msubsup&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/msubsup&gt;
     </code>
    </td>
    <td>
     x₁²
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;munder&gt;
     </code>
    </td>
    <td>
     Élément placé sous le premier enfant (ex. limite).
    </td>
    <td>
     <code>
      &lt;munder&gt;&lt;mi&gt;lim&lt;/mi&gt;&lt;mrow&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mo&gt;→&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;/mrow&gt;&lt;/munder&gt;
     </code>
    </td>
    <td>
     lim sous x→0
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;mover&gt;
     </code>
    </td>
    <td>
     Élément placé au-dessus (ex. barre, vecteur).
    </td>
    <td>
     <code>
      &lt;mover&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mo&gt;→&lt;/mo&gt;&lt;/mover&gt;
     </code>
    </td>
    <td>
     x avec flèche au-dessus
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;munderover&gt;
     </code>
    </td>
    <td>
     Sous et au-dessus (ex. somme, intégrale).
    </td>
    <td>
     <code>
      &lt;munderover&gt;&lt;mo&gt;∑&lt;/mo&gt;&lt;mrow&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/mrow&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/munderover&gt;
     </code>
    </td>
    <td>
     ∑ avec i=1 en bas et n en haut
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;mtable&gt;, &lt;mtr&gt;, &lt;mtd&gt;
     </code>
    </td>
    <td>
     Tableau ou matrice. Fonctionne comme un tableau HTML.
    </td>
    <td>
     <code>
      &lt;mtable&gt;&lt;mtr&gt;&lt;mtd&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/mtd&gt;&lt;mtd&gt;&lt;/mtr&gt;&lt;/mtable&gt;
     </code>
    </td>
    <td>
     Matrice
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;mspace&gt;
     </code>
    </td>
    <td>
     Espace vide personnalisé (attributs width, height, depth).
    </td>
    <td>
     <code>
      &lt;mspace width="1em"/&gt;
     </code>
    </td>
    <td>
     —
    </td>
   </tr>
   <tr>
    <td>
     <code>
      &lt;menclose&gt;
     </code>
    </td>
    <td>
     Encadre ou décore une expression (longdiv, circle, box, etc.).
    </td>
    <td>
     <code>
      &lt;menclose notation="box"&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;/menclose&gt;
     </code>
    </td>
    <td>
     x encadré
    </td>
   </tr>
  </tbody>
 </table>
 <p>
  Cette liste couvre environ 90 % des besoins courants en MathML de présentation. Pour des cas plus avancés (opérateurs extensibles, annotations sémantiques, MathML-Content), il existe de nombreuses autres balises, mais celles-ci constituent la base indispensable pour commencer à écrire des formules complexes directement dans une page web.
 </p>
 <h2>
  Laboratoire en ligne
 </h2>
 <p>
  Je vous invite à éditer le code MathML dans la boîte suivante pour observer le résultat.
 </p>
 <h2>
  Code MathML
 </h2>
 <textarea id="mathmlCode" style="width:100%; height:400px">&lt;math xmlns="http://www.w3.org/1998/Math/MathML" display="block"&gt;
    &lt;mrow&gt;
        &lt;mi&gt;x&lt;/mi&gt;
        &lt;mo&gt;=&lt;/mo&gt;
        &lt;mfrac&gt;
            &lt;mrow&gt;
                &lt;mo&gt;-&lt;/mo&gt;
                &lt;mi&gt;b&lt;/mi&gt;
                &lt;mo&gt;±&lt;/mo&gt;
                &lt;msqrt&gt;
                    &lt;msup&gt;&lt;mi&gt;b&lt;/mi&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/msup&gt;
                    &lt;mo&gt;-&lt;/mo&gt;
                    &lt;mn&gt;4&lt;/mn&gt;
                    &lt;mi&gt;a&lt;/mi&gt;
                    &lt;mi&gt;c&lt;/mi&gt;
                &lt;/msqrt&gt;
            &lt;/mrow&gt;
            &lt;mrow&gt;
                &lt;mn&gt;2&lt;/mn&gt;
                &lt;mi&gt;a&lt;/mi&gt;
            &lt;/mrow&gt;
        &lt;/mfrac&gt;
    &lt;/mrow&gt;
&lt;/math&gt;
        </textarea>
</div>
<div class="render-container">
 <h2>
  Rendu MathML
 </h2>
 <div id="mathmlRender">
  <math display="block" xmlns="http://www.w3.org/1998/Math/MathML">
   <mrow>
    <mi>
     x
    </mi>
    <mo>
     =
    </mo>
    <mfrac>
     <mrow>
      <mo>
       -
      </mo>
      <mi>
       b
      </mi>
      <mo>
       ±
      </mo>
      <msqrt>
       <msup>
        <mi>
         b
        </mi>
        <mn>
         2
        </mn>
       </msup>
       <mo>
        -
       </mo>
       <mn>
        4
       </mn>
       <mi>
        a
       </mi>
       <mi>
        c
       </mi>
      </msqrt>
     </mrow>
     <mrow>
      <mn>
       2
      </mn>
      <mi>
       a
      </mi>
     </mrow>
    </mfrac>
   </mrow>
  </math>
 </div>
</div>
<script>
 const textarea = document.getElementById('mathmlCode');
    const renderDiv = document.getElementById('mathmlRender');
    textarea.addEventListener('input', () => {
        try {
            renderDiv.innerHTML = textarea.value;
        } catch (error) {
            console.error('Erreur MathML:', error);
        }
    });
</script>
