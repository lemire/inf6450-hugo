---
title: "Les langages déclaratifs"
weight: 70
---
<h1>
 Les langages déclaratifs
</h1>
<p>
 Un langage comme Java est orienté objet et procédural. Ce n'est pas,
par contre, un langage déclaratif et on dit donc qu'il est impératif.
Les langages déclaratifs sont
des langages qui définissent le
 <b>
  problème au lieu d'en définir la solution
 </b>
 . On les reconnaît souvent parce qu'ils énoncent des règles au lieu
d'énoncer des procédures.
</p>
<p>
 Le langage Prolog est un exemple de langage déclaratif parce que le
programmeur ne fait que saisir des relations sans définir comment
l'ordinateur doit combiner ses relations:
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 pere(X,Y) :- parent(X,Y),homme(X).
        freresoeur(X,Y) :- parent(Z,X), parent(Z,Y).
</p>
<p>
 Le SQL est aussi déclaratif parce
qu'on spécifie à l'ordinateur quelles informations on veut sans pour autant
spécifier comment l'information doit être trouvée:
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 SELECT age FROM table WHERE age &gt; 25;
</p>
<p>
 Le XSLT et XQuery sont des exemples plus récents de langages déclaratifs.
On affirme souvent que les langages déclaratifs sont plus
 <b>
  lents
 </b>
 que les langages
impératifs parce que le logiciel doit lui-même trouver la meilleure stratégie
pour évaluer le programme sans recevoir beaucoup d'indices de la part de l'humain. Le contraire peut aussi être vrai: comme le logiciel peut optimiser
à sa guise l'exécution du programme étant donné l'absence de structure
imposée par l'humain, il est possible pour un langage déclaratif de
surpasser en vitesse un langage impératif.
En pratique, personne ne se plaint vraiment de la lenteur relative du XSLT, de SQL ou de Prolog. Cependant, pour le programmeur habitué
à la programmation impérative, la programmation déclarative peut être
source de confusion. Avec l'expérience, on se rend compte que, pour bien des problèmes, la programmation déclarative est préférable surtout lorsqu'on ne veut pas se soucier des détails techniques comme la façon dont le fichier XML est lu et comment il est stocké en mémoire.
</p>
<p>
 Le XSLT  peut aussi être considéré comme un langage fonctionnel (voir
 <a href="http://sourceforge.net/projects/fxsl/" shape="rect">
  FXSL
 </a>
 ou
 <a href="http://fxsl.sourceforge.net/articles/FuncProg/Functional%20Programming.html" shape="rect">
  The Functional Programming Language XSLT - A proof through examples
 </a>
 par Dimitre Navatchev) au même titre que APL, Lisp, Haskell, Maple, Mathematica, Ocaml ou Scheme. On peut dire la même chose du XPath 3.0.
</p>
<p>
</p>
