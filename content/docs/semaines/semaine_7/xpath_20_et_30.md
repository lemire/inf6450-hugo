---
title: "XPath 2.0 et 3.0"
weight: 60
---
<h1 class="">
 XPath 2.0 et 3.0
</h1>
<div class="">
 <p>
 </p>
 <p>
  Jusqu'à présent, nous avons présenté XPath 1.0. Il s'agit de la version la plus largement supportée. Elle est la seule version supportée dans tous les grands navigateurs.
 </p>
 <p>
  XPath 2.0 ajoute de nombreuses
  <a href="http://www.w3.org/TR/xpath-functions/" shape="rect">
   fonctions et opérateurs
  </a>
  qui simplifient la vie du programmeur
        tels que empty, exists, intersect, except (pour calculer le complément),
        deep-equal (pour tester l'égalité entre deux séquences),
        index-of, reverse, subsequence, insert-before, remove, distinct-values,
        avg, max, min, etc. Alors que
        XPath 1.0 ne traite que des nombres, des chaînes de caractères, des valeurs booléennes et des ensembles de nœuds, XPath 2.0
        introduit la notion de séquence et plusieurs autres types
        de données pour noter les notes, la durée, les entiers,
        les nombres à virgule flottante, etc. XPath 2.0 supporte aussi
        les
  <a href="https://www.w3.org/TR/xpath-functions/#string.match" shape="rect">
   expressions régulières
  </a>
  avec les fonctions matches, replace, et tokenize. XPath 2.0 intègre maintenant
        la fonction « document » qui était une fonction XSLT.
 </p>
 <p>
  XPath 2.0 comprend maintenant un syntaxe if/then/else comme dans cet exemple :
        « if ( @sexe eq 'm' ) then 'Monsieur' else 'Madame' ». On peut aussi utiliser des boucles :
        « for $i in //etudiant return $i/note ». On peut vérifier si au moins un (some) ou
        tous (every) les éléments d'une séquence satisfont une condition: « every $i in //etudiant
        satisfies $i/note &gt; 0 » ou « some $i in //etudiant
        satisfies $i/note &lt; 100 ». En somme, XPath 2.0 permet d'effectuer plusieurs traitement qui n'étaient possible
        qu'avec des instructions XSLT auparavant.
 </p>
 <p>
  XPath 3.0 quant à lui renforce la notion de fonction en XPath. On peut définir et exécuter ses propres fonctions. Par exemple, on peut définir (en XPath 3.0) une fonction qui ajoute 10 à un nombre: « let $ajoute := function($n) {$n+10} ».
 </p>
 <p>
 </p>
</div>
<hr/>
