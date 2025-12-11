---
title: "XHTML"
weight: 20
---
<h1 class="">
 XHTML
</h1>
<div class="">
 <h2>
  Qu'est-ce que le XHTML?
 </h2>
 <p>
  Le HTML a été inventé par Tim Berners-Lee, alors qu'il travaillait pour le centre de recherche
CERN en Suisse. L'intention de Berners-Lee était de proposer un système révolutionnaire de
gestion de l'information qu'il appela
  <i>
   World Wide Web
  </i>
  . Comme pièce maîtresse de son architecture,
il avait besoin d'un format de documents qu'il appela HTML (
  <i>
   HyperText Markup Language
  </i>
  ).
La première page web, dont l'adresse était http://nxoc01.cern.ch/hypertext/WWW/TheProject.html, 
vit le jour en 1990.
 </p>
 <p>
  Le HTML est un langage à base de balises, un peu comme une application XML.
En fait, il existe une application XML appelée XHTML, qui est à la fois du HTML
et du XML. Le document que vous lisez en ce moment en est un exemple.
  <b>
   En effet, le document que vous lisez est à la fois du XML bien formé et valable, mais aussi du HTML.
  </b>
 </p>
 <p>
  Rappelons qu'une « application XML » est un ensemble de balises et d'attributs, 
c'est-à-dire un vocabulaire XML, avec des conventions d'usage dont certaines
peuvent être représentées par un document DTD.
 </p>
 <p>
  La très grande majorité des documents sur le web sont écrits en HTML et, de plus en plus,
en XHTML. Une des raisons principales de l'utilisation du XHTML, c'est que les outils qui
traitent le XML peuvent aussi traiter du XHTML puisque ce dernier est 
aussi du XML. Il est donc possible, dans une organisation, de combiner le contenu web (HTML) avec
le stockage des informations en XML. Comme nous le verrons plus tard dans le cours 
(module 3, section portant sur le XSLT),  on
peut même transformer automatiquement le XML en XHTML.
 </p>
 <p>
  Si on dit « HTML » tout court, ce n'est pas nécessairement du XML et
il se peut que les outils conçus pour le XML ne puissent être utilisés pour le traiter. 
Cependant, si on dit « XHTML », alors il s'agit à la fois de HTML et de 
XML et on peut utiliser les outils destinés au XML pour en traiter le contenu. 
Voici quelques différences entre le HTML et le XHTML :
 </p>
 <p>
  Les serveurs web distinguent le contenu en fournissant aux navigateurs différents codes MIME (Multipurpose Internet Mail Extensions), alors que le HTML a le code MIME « text/html », on utilise le code MIME « application/xml » ou « application/xhtml+xml » pour le XHTML. Avec le serveur web Apache, on obtient le résultat désiré en
ajoutant un fichier « .htaccess », dans le même répertoire que nos fichiers XHTML, contenant la ligne « AddType application/xml .xhtml ».
 </p>
 <ul>
  <li>
   En HTML traditionnel, on n'a pas à fermer les
éléments. Ainsi, le code suivant «
   <span style="color:#a65700; ">
    &lt;
   </span>
   <span style="color:#5f5035; ">
    p
   </span>
   <span style="color:#a65700; ">
    &gt;
   </span>
   <span style="color:#a65700; ">
    &lt;
   </span>
   <span style="color:#5f5035; ">
    i
   </span>
   <span style="color:#a65700; ">
    &gt;
   </span>
   texte
   <span style="color:#ffffff; background:#dd0000; font-weight:bold; font-style:italic; ">
    &lt;
   </span>
   <span style="color:#ffffff; background:#dd0000; font-weight:bold; font-style:italic; ">
    /
   </span>
   <span style="color:#ffffff; background:#dd0000; font-weight:bold; font-style:italic; ">
    p
   </span>
   <span style="color:#a65700; ">
    &gt;
   </span>
   » est 
acceptable en HTML, mais en XHTML, il faut écrire 
«
   <pre><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">p</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">i</span><span style="color:#a65700; ">&gt;</span>texte<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">i</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">p</span><span style="color:#a65700; ">&gt;</span> ».</pre>
  </li>
  <li>
   Les valeurs d'attributs en HTML n'ont pas à être entre des guillemets ou apostrophes. 
Ainsi, le code «
   <span style="color:#a65700; ">
    &lt;
   </span>
   <span style="color:#5f5035; ">
    table
   </span>
   <span style="color:#274796; ">
    border
   </span>
   <span style="color:#808030; ">
    =
   </span>
   <span style="color:#ffffff; background:#dd0000; font-weight:bold; font-style:italic; ">
    0
   </span>
   <span style="color:#ffffff; background:#dd0000; font-weight:bold; font-style:italic; ">
    &gt;
   </span>
   » est acceptable
en HTML, mais en XHTML, il faut écrire «
   <span style="color:#a65700; ">
    &lt;
   </span>
   <span style="color:#5f5035; ">
    table
   </span>
   <span style="color:#274796; ">
    border
   </span>
   <span style="color:#808030; ">
    =
   </span>
   <span style="color:#0000e6; ">
    "
   </span>
   <span style="color:#0000e6; ">
    0
   </span>
   <span style="color:#0000e6; ">
    "
   </span>
   <span style="color:#a65700; ">
    &gt;
   </span>
   ».
  </li>
  <li>
   En HTML, la casse des noms est sans importance. Ainsi, on peut remplacer
« &lt;p&gt; » par « &lt;P&gt; », alors que ce n'est pas permis en XHTML.
  </li>
 </ul>
 <p>
  Dans ce cours, nous nous intéresserons surtout au XHTML. Un document XHTML prend la forme suivante :
 </p>
 <pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#004a43; ">?&gt;</span>
<span style="color:#004a43; ">&lt;!</span><span style="color:#004a43; ">DOCTYPE</span> <span style="color:#004a43; ">html</span> <span style="color:#800000; font-weight:bold; ">PUBLIC</span> <span style="color:#0000e6; ">"-//W3C//DTD XHTML 1.0 Strict//EN"</span>
    <span style="color:#0000e6; ">"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"</span><span style="color:#004a43; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">html</span> <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/xhtml</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Titre de mon document<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
Voici mon document.
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">html</span><span style="color:#a65700; ">&gt;</span>
</pre>
 <p>
  On reconnaît d'abord la déclaration XML qui n'a rien de particulier : &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;. 
Comme pour tout document XML, on peut omettre la déclaration XML d'un document XHTML, 
mais si nous voulons écrire en français avec des lettres accentuées, il est nettement préférable 
d'avoir la déclaration XML de notre exemple.
 </p>
 <p>
  On reconnaît ensuite la déclaration de type de document :  &lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"&gt;. 
Observez qu'elle apparaît sur deux lignes, que c'est souvent le cas, mais que c'est un choix purement esthétique. 
La déclaration de type de document est un peu particulière : il s'agit d'une déclaration utilisant 
un identifiant public. On doit utiliser un tel identifiant 
quand on veut signifier qu'il s'agit d'une application XML commune; on évite ainsi 
que des milliers de personnes aillent chercher des documents DTD à l'adresse 
« http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd ». 
On s'attend qu'un logiciel qui dépend d'une application XML commune 
n'ait pas besoin d'aller chercher les documents DTD, chaque fois que le document XML est lu.
Un navigateur ne tient généralement pas compte de la DTD externe, on peut donc omettre
la déclaration DOCTYPE sans problème.
 </p>
 <p>
  Le reste du document est simplement un élément-racine « html » contenant deux éléments : 
un élément
  <i>
   head
  </i>
  et un élément
  <i>
   body
  </i>
  . L'élément
  <i>
   head
  </i>
  doit contenir 
un élément
  <i>
   title
  </i>
  , alors que l'élément
  <i>
   body
  </i>
  peut être vide, mais peut aussi posséder du 
contenu XML mixte (texte et diverses balises XHTML). L'espace de nom ayant l'URI « http://www.w3.org/1999/xhtml » 
est utilisé.
 </p>
 <p>
  Si vous copiez le texte qui précède dans un éditeur de texte comme
  <i>
   Bloc-notes
  </i>
  et que vous enregistrez le fichier 
sous un nom comme « test.xhtml », vous devriez être capable d'ouvrir le fichier dans votre 
navigateur et de voir le texte « Voici mon document. » s'afficher à l'écran. Les documents HTML sont tous des 
documents en format texte et l'extension du fichier est arbitraire : on utilise tout aussi bien
« .htm » que « .html », « .xhtml » ou même « .xml ». L'avantage de 
l'extension « .xhtml » est d'informer le navigateur qu'il s'agit d'un document XHTML, 
donc un document HTML et un document XML.
 </p>
 <h2>
  La structure du document XHTML :
  <i>
   head
  </i>
  et
  <i>
   body
  </i>
 </h2>
 <p>
  Comme nous le disions, l'élément-racine d'un document XHTML est nommé « html ». Cet élément contient
  <b>
   deux et exactement deux
  </b>
  sous-éléments :
  <i>
   head
  </i>
  et
  <i>
   body
  </i>
  . L'élément
  <i>
   head
  </i>
  n'est pas affiché directement dans le navigateur et contient des métadonnées, c'est-à-dire une description du contenu. 
Un élément
  <i>
   head
  </i>
  doit au minimum contenir un élément
  <i>
   title
  </i>
  qui donne le titre du 
document XHTML. Par la suite, l'élément
  <i>
   body
  </i>
  contient un ensemble de balises et 
du texte (contenu mixte) qui sera affiché directement dans le navigateur.
 </p>
 <h2>
  Les paragraphes en HTML
 </h2>
 <p>
  L'élément
  <i>
   body
  </i>
  contient des balises et du texte. Les retours de ligne sont traités
comme des espaces normaux. Ainsi, les deux documents suivants seront affichés
de la même manière par un navigateur.
 </p>
 <pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#004a43; ">?&gt;</span>
<span style="color:#004a43; ">&lt;!</span><span style="color:#004a43; ">DOCTYPE</span> <span style="color:#004a43; ">html</span> <span style="color:#800000; font-weight:bold; ">PUBLIC</span> <span style="color:#0000e6; ">"-//W3C//DTD XHTML 1.0 Strict//EN"</span>
    <span style="color:#0000e6; ">"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"</span><span style="color:#004a43; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">html</span> <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/xhtml</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Titre de mon document<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
Voici mon document.
Voici ma vie.
Voici mon chat.
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">html</span><span style="color:#a65700; ">&gt;</span>
</pre>
 <pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#004a43; ">?&gt;</span>
<span style="color:#004a43; ">&lt;!</span><span style="color:#004a43; ">DOCTYPE</span> <span style="color:#004a43; ">html</span> <span style="color:#800000; font-weight:bold; ">PUBLIC</span> <span style="color:#0000e6; ">"-//W3C//DTD XHTML 1.0 Strict//EN"</span>
    <span style="color:#0000e6; ">"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"</span><span style="color:#004a43; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">html</span> <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/xhtml</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Titre de mon document<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
Voici mon document.

Voici ma vie.

Voici mon chat.
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">html</span><span style="color:#a65700; ">&gt;</span>
</pre>
 <p>
  La question qui se pose alors est : Comment faire des paragraphes? En effet, dans les deux documents plus haut, le
texte s'affichera sur une seule ligne (vous pouvez le tester!). La solution consiste à utiliser l'élément « p » pour
« paragraphe ». Pour avoir trois paragraphes, on remplace le document HTML précédent par celui qui suit. Observez
que chaque balise « p » ouverte doit être fermée.
 </p>
 <pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#004a43; ">?&gt;</span>
<span style="color:#004a43; ">&lt;!</span><span style="color:#004a43; ">DOCTYPE</span> <span style="color:#004a43; ">html</span> <span style="color:#800000; font-weight:bold; ">PUBLIC</span> <span style="color:#0000e6; ">"-//W3C//DTD XHTML 1.0 Strict//EN"</span>
    <span style="color:#0000e6; ">"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"</span><span style="color:#004a43; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">html</span> <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/xhtml</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Titre de mon document<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">p</span><span style="color:#a65700; ">&gt;</span>Voici mon document.<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">p</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">p</span><span style="color:#a65700; ">&gt;</span>Voici ma vie.<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">p</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">p</span><span style="color:#a65700; ">&gt;</span>Voici mon chat.<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">p</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">html</span><span style="color:#a65700; ">&gt;</span>
</pre>
 <h2>
  Les listes en HTML
 </h2>
 <p>
  Supposons que l'on veuille faire une liste, comme ceci :
 </p>
 <ul>
  <li>
   Premier point : le chat est noir.
  </li>
  <li>
   Second point : le chat est blanc.
  </li>
  <li>
   Dernier point : le chat est marron.
  </li>
 </ul>
 <p>
  On peut obtenir ce résultat avec un élément « ul » pour
  <i>
   unordered list
  </i>
  (liste sans ordre),
contenant des éléments « li ». Observez que chaque balise « li » ouverte doit être fermée.
 </p>
 <pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#004a43; ">?&gt;</span>
<span style="color:#004a43; ">&lt;!</span><span style="color:#004a43; ">DOCTYPE</span> <span style="color:#004a43; ">html</span> <span style="color:#800000; font-weight:bold; ">PUBLIC</span> <span style="color:#0000e6; ">"-//W3C//DTD XHTML 1.0 Strict//EN"</span>
    <span style="color:#0000e6; ">"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"</span><span style="color:#004a43; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">html</span> <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/xhtml</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Titre de mon document<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">ul</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>Premier point: le chat est noir.<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>Second point: le chat est blanc.<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>Dernier point: le chat est marron.<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">ul</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">html</span><span style="color:#a65700; ">&gt;</span>
</pre>
 <p>
  Supposons maintenant que nous voulions une liste avec un compteur :
 </p>
 <ol>
  <li>
   Le chat est noir.
  </li>
  <li>
   Le chat est blanc.
  </li>
  <li>
   Le chat est marron.
  </li>
 </ol>
 <p>
  Il suffit alors de remplacer l'élément « ul » par l'élément « ol » 
pour
  <i>
   ordered list
  </i>
  (liste ordonnée) :
 </p>
 <pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#004a43; ">?&gt;</span>
<span style="color:#004a43; ">&lt;!</span><span style="color:#004a43; ">DOCTYPE</span> <span style="color:#004a43; ">html</span> <span style="color:#800000; font-weight:bold; ">PUBLIC</span> <span style="color:#0000e6; ">"-//W3C//DTD XHTML 1.0 Strict//EN"</span>
    <span style="color:#0000e6; ">"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"</span><span style="color:#004a43; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">html</span> <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/xhtml</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Titre de mon document<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">ol</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>Le chat est noir.<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>Le chat est blanc.<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>Le chat est marron.<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">ol</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">html</span><span style="color:#a65700; ">&gt;</span>
</pre>
 <h2>
  Les tableaux en HTML
 </h2>
 <p>
  Supposons maintenant que nous voulions produire un tableau. On peut l'obtenir à l'aide d'un élément
« table ». Cet élément contiendra plusieurs éléments « tr » (éléments correspondant à une ligne) qui eux-mêmes
contiennent des éléments « td » (éléments correspondant à une cellule). Ainsi, pour obtenir un tableau comme celui-ci :
 </p>
 <table border="0" class="tabblanc">
  <!-- border='0' est un convention pour le traitement XSLT -->
  <tbody>
   <tr>
    <td>
     Nom
    </td>
    <td>
     Valeur
    </td>
   </tr>
   <tr>
    <td>
     Mustang
    </td>
    <td>
     50 $
    </td>
   </tr>
   <tr>
    <td>
     Ferrari
    </td>
    <td>
     500 $
    </td>
   </tr>
  </tbody>
 </table>
 <p>
  On utilise le code suivant :
 </p>
 <pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#004a43; ">?&gt;</span>
<span style="color:#004a43; ">&lt;!</span><span style="color:#004a43; ">DOCTYPE</span> <span style="color:#004a43; ">html</span> <span style="color:#800000; font-weight:bold; ">PUBLIC</span> <span style="color:#0000e6; ">"-//W3C//DTD XHTML 1.0 Strict//EN"</span>
    <span style="color:#0000e6; ">"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"</span><span style="color:#004a43; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">html</span> <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/xhtml</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Titre de mon document<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">table</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>Nom<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>Valeur<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>Mustang<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>50 $<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>Ferrari<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>500 $<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">table</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">html</span><span style="color:#a65700; ">&gt;</span>
</pre>
 <p>
  Supposons maintenant que l'on veuille un tableau avec des lignes pour marquer et diviser les cellules. Il suffit alors
d'utiliser l'attribut « border ». Sa valeur numérique représente l'épaisseur en pixels de la bordure.
Ainsi, pour obtenir ce résultat :
 </p>
 <table border="1" class="tabblanc">
  <tbody>
   <tr>
    <td style="border-style: solid;">
     Nom
    </td>
    <td style="border-style: solid;">
     Valeur
    </td>
   </tr>
   <tr>
    <td style="border-style: solid;">
     Mustang
    </td>
    <td style="border-style: solid;">
     50 $
    </td>
   </tr>
   <tr>
    <td style="border-style: solid;">
     Ferrari
    </td>
    <td style="border-style: solid;">
     500 $
    </td>
   </tr>
  </tbody>
 </table>
 <p>
  On utilisera le code XHTML suivant :
 </p>
 <pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#004a43; ">?&gt;</span>
<span style="color:#004a43; ">&lt;!</span><span style="color:#004a43; ">DOCTYPE</span> <span style="color:#004a43; ">html</span> <span style="color:#800000; font-weight:bold; ">PUBLIC</span> <span style="color:#0000e6; ">"-//W3C//DTD XHTML 1.0 Strict//EN"</span>
    <span style="color:#0000e6; ">"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"</span><span style="color:#004a43; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">html</span> <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/xhtml</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Titre de mon document<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">table</span> <span style="color:#274796; ">border</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">1</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>Nom<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>Valeur<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>Mustang<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>50 $<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>Ferrari<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>500 $<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">table</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">html</span><span style="color:#a65700; ">&gt;</span>
</pre>
 <p>
  Tous les tableaux ne sont pas si simples. On peut faire en sorte
qu'une même cellule occupe deux colonnes
(&lt;td colspan="2"&gt;) ou deux rangées (&lt;td rowspan="2"&gt;). 
Aussi, souvent, on utilise l'élément « th » au lieu de l'élément « td » pour désigner
la première rangée d'un tableau lorsque celle-ci forme l'entête 
descriptive du tableau. Il est aussi possible d'utiliser 
un élément « caption » au sein d'un tableau pour
noter le titre du tableau :
 </p>
 <pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#004a43; ">?&gt;</span>
<span style="color:#004a43; ">&lt;!</span><span style="color:#004a43; ">DOCTYPE</span> <span style="color:#004a43; ">html</span> <span style="color:#800000; font-weight:bold; ">PUBLIC</span> <span style="color:#0000e6; ">"-//W3C//DTD XHTML 1.0 Strict//EN"</span>
    <span style="color:#0000e6; ">"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"</span><span style="color:#004a43; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">html</span> <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/xhtml</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Titre de mon document<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">table</span> <span style="color:#274796; ">border</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">1</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">caption</span><span style="color:#a65700; ">&gt;</span>Valeur de différents véhicule<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">caption</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">th</span><span style="color:#a65700; ">&gt;</span>Nom<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">th</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">th</span><span style="color:#a65700; ">&gt;</span>Valeur<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">th</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>Mustang<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>50 $<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>Ferrari<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>500 $<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">td</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">tr</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">table</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">html</span><span style="color:#a65700; ">&gt;</span>
</pre>
 <h2>
  Les caractères italiques et gras
 </h2>
 <p>
  On peut très facilement utiliser des effets de polices de caractères en HTML. Pour obtenir des caractères en italique, 
par exemple
  <i>
   maman
  </i>
  , il suffit d'utiliser un élément « i » comme ceci : &lt;i&gt;maman&lt;/i&gt;. 
Pour des caractères en gras, comme
  <b>
   maman
  </b>
  , il suffit d'utiliser un élément « b » comme ceci : 
&lt;b&gt;maman&lt;/b&gt;. On peut également combiner les deux, comme
  <b>
   <i>
    maman
   </i>
  </b>
  , en écrivant &lt;i&gt;&lt;b&gt;maman&lt;/b&gt;&lt;/i&gt; 
ou bien &lt;b&gt;&lt;i&gt;maman&lt;/i&gt;&lt;/b&gt;. Il est cependant préférable d'utiliser
« em » (emphase) au lieu de « i » et « strong » (fort) au lieu de « b » : le navigateur choisira alors de 
rendre le texte dans un élément  « em » avec un italique ou une autre technique appropriée, et de rendre le texte dans un élément « strong » en caractères gras ou une autre technique appropriée. On évite ainsi de confondre la présentation (italique ou gras) et la sémantique (emphase ou point fort). Dans le cas où un terme est défini, vous devriez utiliser un élément « dfn » (définition) comme dans cet exemple: « La &lt;dfn&gt;mort&lt;/dfn&gt; est la fin de la vie ». La plupart des navigateurs afficheront alors le mot « mort » en caratères italiques.
 </p>
 <h2>
  Les listes de définitions
 </h2>
 <p>
  Supposons que nous voulions une liste de définitions comme celle qui suit :
 </p>
 <dl>
  <dt>
   Voiture
  </dt>
  <dd>
   Véhicule sur roues.
  </dd>
  <dt>
   Chat
  </dt>
  <dd>
   Bête sauvage qui se nourrit de lait.
  </dd>
  <dt>
   Éléphant
  </dt>
  <dd>
   Bête sauvage de couleur rose.
  </dd>
 </dl>
 <p>
  On obtient ce résultat en XHTML avec un élément « dl » pour
  <i>
   definition list
  </i>
  contenant 
une série d'éléments « dt » et « dd » en paire, où l'élément « dt » fournit le terme à définir 
et l'élément « dd » sa définition.
 </p>
 <pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#004a43; ">?&gt;</span>
<span style="color:#004a43; ">&lt;!</span><span style="color:#004a43; ">DOCTYPE</span> <span style="color:#004a43; ">html</span> <span style="color:#800000; font-weight:bold; ">PUBLIC</span> <span style="color:#0000e6; ">"-//W3C//DTD XHTML 1.0 Strict//EN"</span>
    <span style="color:#0000e6; ">"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"</span><span style="color:#004a43; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">html</span> <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/xhtml</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Titre de mon document<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">dl</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">dt</span><span style="color:#a65700; ">&gt;</span>Voiture<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">dt</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">dd</span><span style="color:#a65700; ">&gt;</span>Véhicule sur roues. <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">dd</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">dt</span><span style="color:#a65700; ">&gt;</span>Chat<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">dt</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">dd</span><span style="color:#a65700; ">&gt;</span>Bête sauvage qui se nourrit de lait. <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">dd</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">dt</span><span style="color:#a65700; ">&gt;</span>Éléphant<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">dt</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">dd</span><span style="color:#a65700; ">&gt;</span>Bête sauvage de couleur rose. <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">dd</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">dl</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">html</span><span style="color:#a65700; ">&gt;</span>
</pre>
 <h2>
  Les lignes horizontales
 </h2>
 <p>
  Pour obtenir une ligne horizontale, on utilise l'élément « hr » qui doit être vide. On 
doit donc écrire &lt;hr&gt;&lt;/hr&gt; ou plus simplement &lt;hr /&gt;. Voici une ligne horizontale :
 </p>
 <hr/>
 <h2>
  Les images
 </h2>
 <p>
  Au moment d'écrire ces lignes, on trouve un logo de l'UQAM à l'URL
 </p>
 <pre>https://upload.wikimedia.org/wikipedia/commons/2/24/Université_du_Québec_à_Montréal_Logo.svg.</pre>
 <p>
  Pour insérer une image dans un document HTML, il suffit d'utiliser une balise « img » 
avec comme attribut « src » pour source, soit l'URL. Par 
exemple, le code
 </p>
 <pre>&lt;img src="https://upload.wikimedia.org/wikipedia/commons/2/24/Université_du_Québec_à_Montréal_Logo.svg"&gt;</pre>
 <p>
  ou
 </p>
 <pre>&lt;img src="https://upload.wikimedia.org/wikipedia/commons/2/24/Université_du_Québec_à_Montréal_Logo.svg" /&gt;</pre>
 <p>
  permettra d'insérer le logo de l'UQAM 
dans un document. Il est préférable de prévoir que l'image
pourrait ne pas être trouvée ou affichée en ajoutant un attribut « alt » qui contient 
du texte décrivant le contenu de l'image; si l'image n'est pas disponible, le texte contenu 
dans l'attribut « alt » s'affichera.
  <!-- est-ce que le contenu de alt s'affiche à la place de 
l'image si elle n'est pas disponible ? -->
  Le résultat final prend la forme
&lt;img src="https://upload.wikimedia.org/wikipedia/commons/2/24/Université_du_Québec_à_Montréal_Logo.svg" alt="logo de l'UQAM" /&gt;
ce qui donne :
 </p>
 <img alt="logo de l'UQAM" src="https://upload.wikimedia.org/wikipedia/commons/2/24/Université_du_Québec_à_Montréal_Logo.svg"/>
 <h2>
  Les hyperliens
 </h2>
 <p>
  Pour inclure un hyperlien, comme dans l'exemple de la
  <a href="http://www.uqam.ca/">
   page de l'UQAM
  </a>
  [lien vers http://www.uqam.ca/], il suffit d'utiliser 
la syntaxe « &lt;a href="http://www.uqam.ca/"&gt;page de l'UQAM ».
 </p>
 <p>
  On peut également ajouter des marqueurs dans une page web en utilisant 
la syntaxe « &lt;a name="point1"&gt;Premier point de mon document&lt;/a&gt; ».
Contrairement à la syntaxe « &lt;a href="..."&gt; », l'attribut « name » 
n'ajoute pas un hyperlien, mais un marqueur généralement invisible dans la page. 
Par exemple, si la page contient plusieurs sections, on peut ajouter un marqueur au début de chaque section. 
On pourra alors faire des liens non seulement vers le document, mais aussi vers la section marquée dans le document. 
Ainsi, l'hyperlien « &lt;a href="pageweb.html#point1"&gt;aller vers le premier point du document pageweb.html&lt;/a&gt; » 
mènera l'utilisateur dans le document « pageweb.html », précisément au marqueur du « point 1 », 
s'il existe, évidemment.
 </p>
 <h2>
  Les abbréviations
 </h2>
 <p>
  On utilise parfois des abbréviations dans une page web tel que « etc. » ou « no ». On peut indiquer au navigateur qu'il
s'agit d'une abbréviation avec un élément abbr comme ceci : « &lt;abbr&gt;no&lt;/abbr&gt; ». Il est parfois utile d'utiliser
l'attribut « title » pour décrire l'abbréviation en question
comme dans ceci : « &lt;abbr title="numéro"&gt;no&lt;/abbr&gt; ». De la même façon, on peut noter les acronymes avec un élément « acronym » comme 
ceci : « &lt;acronym title="Organisation du traité de l'Atlantique Nord"&gt;OTAN&lt;/acronym&gt; ».
 </p>
 <h2>
  Les adresses
 </h2>
 <p>
  Il est fréquent qu'une page web contienne un adresse. Le XHTML nous permet
d'indiquer au navigateur qu'il s'agit bien d'une adresse avec l'élément « address », comme ceci :
« &lt;address&gt;
Daniel Lemire&lt;br /&gt;
100, rue Sherbrooke
&lt;/address&gt; ». Ici, l'élément « br » sert à noter un retour de charriot.
 </p>
 <h2>
  Les indices et exposants
 </h2>
 <p>
  Dans un texte, il arrive qu'on veuille utiliser des exposants
et des indices. Les éléments « sup » et « sub » servent à cette fonction.
Par exemple, « premier » peut s'écrit « 1
  <sup>
   er
  </sup>
  ». Il n'est malheureusement pas possible de noter automatiquement des notes en bas de page en HTML ou XHTML.
 </p>
 <h2>
  Le code et les exemples
 </h2>
 <p>
  Il y a plusieurs éléments permettant de traiter de la programmation informatique ou des mathématiques. Le code informatique peut s'écrire dans un élément « code ».
Le texte saisi à l'écran par un utilisateur peut s'écrire dans un élément « kbd ».
Les exemples de sortie à l'écran peuvent s'écrire dans un élément « samp » (pour sample) et les variables peuvent s'écrire dans un élément « var ». Voici un exemple : «
  <span style="color:#a65700; ">
   &lt;
  </span>
  <span style="color:#5f5035; ">
   p
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  La valeur de la variable
  <span style="color:#a65700; ">
   &lt;
  </span>
  <span style="color:#5f5035; ">
   var
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  i
  <span style="color:#a65700; ">
   &lt;/
  </span>
  <span style="color:#5f5035; ">
   var
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  est obtenue avec ce code:
  <span style="color:#a65700; ">
   &lt;/
  </span>
  <span style="color:#5f5035; ">
   p
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  <span style="color:#a65700; ">
   &lt;
  </span>
  <span style="color:#5f5035; ">
   code
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  int i = 1; i+=1
  <span style="color:#a65700; ">
   &lt;/
  </span>
  <span style="color:#5f5035; ">
   code
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  <span style="color:#a65700; ">
   &lt;
  </span>
  <span style="color:#5f5035; ">
   p
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  On s'attend à ce que l'utilisateur tape
  <span style="color:#a65700; ">
   &lt;
  </span>
  <span style="color:#5f5035; ">
   kbd
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  Yes
  <span style="color:#a65700; ">
   &lt;/
  </span>
  <span style="color:#5f5035; ">
   kbd
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  pour oui. Voici un exemple de résultat:
  <span style="color:#a65700; ">
   &lt;
  </span>
  <span style="color:#5f5035; ">
   samp
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  Error!
  <span style="color:#a65700; ">
   &lt;/
  </span>
  <span style="color:#5f5035; ">
   samp
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  .
  <span style="color:#a65700; ">
   &lt;/
  </span>
  <span style="color:#5f5035; ">
   p
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  ».
 </p>
 <h2>
  Les citations
 </h2>
 <p>
  Pour citer quelqu'un, on peut utiliser un élément  « q » lorsqu'il s'agit d'un courte citation au sein d'un paragraphe ou élément  « blockquote » lorsque la citation doit former un court paragraphe. Plusieurs navigateur mettent automatiquement le contenu de l'élément  « q » entre guillemets et le contenu de l'élément  « blockquote » en retrait. Voici un exemple : «
  <span style="color:#a65700; ">
   &lt;
  </span>
  <span style="color:#5f5035; ">
   p
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  Jean a dit:
  <span style="color:#a65700; ">
   &lt;
  </span>
  <span style="color:#5f5035; ">
   q
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  mon cher!
  <span style="color:#a65700; ">
   &lt;/
  </span>
  <span style="color:#5f5035; ">
   q
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  . Par la suite, je lui ai lu ce texte fatidique.
  <span style="color:#a65700; ">
   &lt;/
  </span>
  <span style="color:#5f5035; ">
   p
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  <span style="color:#a65700; ">
   &lt;
  </span>
  <span style="color:#5f5035; ">
   blockquote
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  <span style="color:#a65700; ">
   &lt;
  </span>
  <span style="color:#5f5035; ">
   p
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  Oh! Comme la mer a merée! Oh! Comme j'ai jéjé!
  <span style="color:#a65700; ">
   &lt;/
  </span>
  <span style="color:#5f5035; ">
   p
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  <span style="color:#a65700; ">
   &lt;/
  </span>
  <span style="color:#5f5035; ">
   blockquote
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  ».
 </p>
 <h2>
  Les révisions
 </h2>
 <p>
  Les éléments del et ins permettent de noter un retrait et un ajout, respectivement, comme dans cet exemple:
 </p>
 <pre>J'ai <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">del</span><span style="color:#a65700; ">&gt;</span>marié<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">del</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">ins</span><span style="color:#a65700; ">&gt;</span>épousé<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">ins</span><span style="color:#a65700; ">&gt;</span> ta mère
</pre>
 Le navigateur se
chargera d'afficher les retraits et les ajouts de manière compréhensible.
 <p>
 </p>
 <h2>
  La langue
 </h2>
 <p>
  Le XHTML respecte la spécification XML voulant qu'on indique
la langue dans laquelle est écrite un texte avec l'attribute « xml:lang ». Cet attribut est optionnel, mais peut 
s'avérer pratique. Dans le cas où un texte 
en langue étrangère est présent dans un paragraphe, on peut utiliser
l'élément « span » pour en indiquer la langue.
Voici un exemple :
«
  <span style="color:#a65700; ">
   &lt;
  </span>
  <span style="color:#5f5035; ">
   p
  </span>
  <span style="color:#666616; ">
   xml
  </span>
  <span style="color:#800080; ">
   :
  </span>
  <span style="color:#074726; ">
   lang
  </span>
  <span style="color:#808030; ">
   =
  </span>
  <span style="color:#0000e6; ">
   "
  </span>
  <span style="color:#0000e6; ">
   fr-CA
  </span>
  <span style="color:#0000e6; ">
   "
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  Jean aime les
  <span style="color:#a65700; ">
   &lt;
  </span>
  <span style="color:#5f5035; ">
   span
  </span>
  <span style="color:#666616; ">
   xml
  </span>
  <span style="color:#800080; ">
   :
  </span>
  <span style="color:#074726; ">
   lang
  </span>
  <span style="color:#808030; ">
   =
  </span>
  <span style="color:#0000e6; ">
   "
  </span>
  <span style="color:#0000e6; ">
   en-US
  </span>
  <span style="color:#0000e6; ">
   "
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  computers
  <span style="color:#a65700; ">
   &lt;/
  </span>
  <span style="color:#5f5035; ">
   span
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  <span style="color:#a65700; ">
   &lt;/
  </span>
  <span style="color:#5f5035; ">
   p
  </span>
  <span style="color:#a65700; ">
   &gt;
  </span>
  ». L'élément « span » 
ne sert  qu'à nous permettre de sélectionner un texte
au sein d'un autre élément.
 </p>
 <h2>
  Les commentaires
 </h2>
 <p>
  Ajouter des commentaires en XHTML est facile. Les commentaires
du XML s'appliquent: il suffit de débuter le commentaire par &lt;!-- et
de le terminer par --&gt;. Il n'est pas permis d'inclure au sein d'un
commentaire deux tirets (--) ni de terminer un commentaire par un tiret.
 </p>
 <h2>
  Séparation du contenu et de la présentation
 </h2>
 <p>
  Avec le XHTML, on peut contrôler en partie l'apparence du texte, en utilisant
des italiques ou en plaçant des bordures dans nos tableaux. Ce contrôle est cependant limité : 
on ne peut pas ajuster l'indentation des paragraphes et on ne peut que difficilement ajuster les marges de la page. 
Nous verrons au module 3, dans la section sur le CSS, qu'il existe une façon élégante d'y arriver.
 </p>
 <h2>
  Convertir du HTML mal formé
 </h2>
 <p>
  Dans une organisation, il est fréquent d'avoir à composer avec des sites web
qui ne respectent pas les normes les plus élémentaires. Réécrire le HTML en XHTML
peut sembler une tâche très ardue. Heureusement, il existe des outils gratuits
pour corriger du HTML mal formé et générer automatiquement un XHTML valable, comme
par exemple HTMLTidy (
  <a href="http://tidy.sourceforge.net/">
   http://tidy.sourceforge.net/
  </a>
  ).
Le W3C rend aussi disponible un outil de vérification en ligne des sites web pour
s'assurer de leur conformité avec les normes (
  <a href="http://validator.w3.org/">
   http://validator.w3.org/
  </a>
  ).
Vous pourrez facilement constater que plusieurs pages à l'UQAM ne sont pas du HTML valable,
y compris certaines pages web de ce cours !
 </p>
 <h2>
  Spécification Relax NG
 </h2>
 <p>
  Il existe des définitions de type de document
officielle pour le XHML, mais elles sont longues et 
peu lisible. Sean B. Palmer a écrit une spécification
Relax NG pour un sous-ensemble du XHTML que je
reproduis ici avec permission.
Je vous invite à vérifier que vous pouvez
en comprendre l'essentiel.
 </p>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<grammar xmlns="http://relaxng.org/ns/structure/1.0"
         datatypeLibrary="http://www.w3.org/2001/XMLSchema-datatypes"
         ns="http://www.w3.org/1999/xhtml">

  <start>
    <ref name="html"/>
  </start>

  <!-- Common attribute groups -->
  <define name="Core.attrs">
    <optional><attribute name="id"><data type="ID"/></attribute></optional>
    <optional><attribute name="class"><text/></attribute></optional>
    <optional><attribute name="style"><text/></attribute></optional>
    <optional><attribute name="title"><text/></attribute></optional>
  </define>

  <define name="I18n.attrs">
    <optional><attribute name="xml:lang"><text/></attribute></optional>
    <optional><attribute name="dir"><choice><value>ltr</value><value>rtl</value></choice></attribute></optional>
  </define>

  <define name="Main.attrs">
    <ref name="Core.attrs"/>
    <ref name="I18n.attrs"/>
    <optional><attribute name="onclick"><text/></attribute></optional>
  </define>

  <!-- Content models -->
  <define name="BlockMinusForm">
    <zeroOrMore>
      <choice>
        <ref name="address"/>
        <ref name="blockquote"/>
        <ref name="del"/>
        <ref name="div.elem"/>
        <ref name="dl"/>
        <ref name="h1"/>
        <ref name="h2"/>
        <ref name="h3"/>
        <ref name="hr"/>
        <ref name="ins"/>
        <ref name="ol"/>
        <ref name="p"/>
        <ref name="pre"/>
        <ref name="script"/>
        <ref name="table"/>
        <ref name="ul"/>
      </choice>
    </zeroOrMore>
  </define>

  <define name="Block">
    <zeroOrMore>
      <choice>
        <ref name="BlockMinusForm"/>
        <ref name="form"/>
      </choice>
    </zeroOrMore>
  </define>

  <define name="InlineMinusMedia">
    <zeroOrMore>
      <choice>
        <ref name="a"/>
        <ref name="abbr"/>
        <ref name="br"/>
        <ref name="cite"/>
        <ref name="code"/>
        <ref name="del"/>
        <ref name="em"/>
        <ref name="input"/>
        <ref name="ins"/>
        <ref name="label"/>
        <ref name="script"/>
        <ref name="span"/>
        <ref name="strong"/>
        <ref name="sub"/>
        <ref name="sup"/>
        <ref name="textarea"/>
        <text/>
      </choice>
    </zeroOrMore>
  </define>

  <define name="Inline">
    <zeroOrMore>
      <choice>
        <ref name="InlineMinusMedia"/>
        <ref name="img"/>
        <ref name="object"/>
      </choice>
    </zeroOrMore>
  </define>

  <define name="Flow">
    <zeroOrMore>
      <choice>
        <ref name="Block"/>
        <ref name="Inline"/>
      </choice>
    </zeroOrMore>
  </define>

  <!-- Elements -->
  <define name="html">
    <element name="html">
      <ref name="I18n.attrs"/>
      <ref name="head"/>
      <ref name="body"/>
    </element>
  </define>

  <define name="head">
    <element name="head">
      <ref name="I18n.attrs"/>
      <optional><attribute name="profile"><text/></attribute></optional>
      <ref name="title"/>
      <optional><ref name="base"/></optional>
      <interleave>
        <zeroOrMore><ref name="script"/></zeroOrMore>
        <zeroOrMore><ref name="style"/></zeroOrMore>
        <zeroOrMore><ref name="meta"/></zeroOrMore>
        <zeroOrMore><ref name="link"/></zeroOrMore>
      </interleave>
    </element>
  </define>

  <define name="title">
    <element name="title">
      <ref name="I18n.attrs"/>
      <text/>
    </element>
  </define>

  <define name="base">
    <element name="base">
      <attribute name="href"><text/></attribute>
      <empty/>
    </element>
  </define>

  <define name="meta">
    <element name="meta">
      <ref name="I18n.attrs"/>
      <optional><attribute name="content"><text/></attribute></optional>
      <optional><attribute name="name"><text/></attribute></optional>
      <empty/>
    </element>
  </define>

  <define name="link">
    <element name="link">
      <ref name="Main.attrs"/>
      <optional><attribute name="href"><text/></attribute></optional>
      <optional><attribute name="rel"><text/></attribute></optional>
      <optional><attribute name="type"><text/></attribute></optional>
      <empty/>
    </element>
  </define>

  <define name="style">
    <element name="style">
      <ref name="I18n.attrs"/>
      <attribute name="type"><text/></attribute>
      <optional><attribute name="title"><text/></attribute></optional>
      <text/>
    </element>
  </define>

  <define name="script">
    <element name="script">
      <attribute name="type"><text/></attribute>
      <optional><attribute name="src"><text/></attribute></optional>
      <text/>
    </element>
  </define>

  <define name="body">
    <element name="body">
      <ref name="Main.attrs"/>
      <optional><attribute name="onload"><text/></attribute></optional>
      <ref name="Block"/>
    </element>
  </define>

  <define name="div.elem">
    <element name="div">
      <ref name="Main.attrs"/>
      <ref name="Flow"/>
    </element>
  </define>

  <define name="p">
    <element name="p">
      <ref name="Main.attrs"/>
      <ref name="Inline"/>
    </element>
  </define>

  <define name="h1">
    <element name="h1">
      <ref name="Main.attrs"/>
      <ref name="Inline"/>
    </element>
  </define>

  <define name="h2">
    <element name="h2">
      <ref name="Main.attrs"/>
      <ref name="Inline"/>
    </element>
  </define>

  <define name="h3">
    <element name="h3">
      <ref name="Main.attrs"/>
      <ref name="Inline"/>
    </element>
  </define>

  <define name="ul">
    <element name="ul">
      <ref name="Main.attrs"/>
      <oneOrMore><ref name="li"/></oneOrMore>
    </element>
  </define>

  <define name="ol">
    <element name="ol">
      <ref name="Main.attrs"/>
      <oneOrMore><ref name="li"/></oneOrMore>
    </element>
  </define>

  <define name="li">
    <element name="li">
      <ref name="Main.attrs"/>
      <ref name="Flow"/>
    </element>
  </define>

  <define name="dl">
    <element name="dl">
      <ref name="Main.attrs"/>
      <oneOrMore>
        <group>
          <ref name="dt"/>
          <oneOrMore><ref name="dd"/></oneOrMore>
        </group>
      </oneOrMore>
    </element>
  </define>

  <define name="dt">
    <element name="dt">
      <ref name="Main.attrs"/>
      <ref name="Inline"/>
    </element>
  </define>

  <define name="dd">
    <element name="dd">
      <ref name="Main.attrs"/>
      <ref name="Flow"/>
    </element>
  </define>

  <define name="address">
    <element name="address">
      <ref name="Main.attrs"/>
      <ref name="Inline"/>
    </element>
  </define>

  <define name="hr">
    <element name="hr">
      <ref name="Main.attrs"/>
      <empty/>
    </element>
  </define>

  <define name="pre">
    <element name="pre">
      <ref name="Main.attrs"/>
      <ref name="InlineMinusMedia"/>
    </element>
  </define>

  <define name="blockquote">
    <element name="blockquote">
      <ref name="Main.attrs"/>
      <optional><attribute name="cite"><text/></attribute></optional>
      <ref name="Block"/>
    </element>
  </define>

  <define name="ins">
    <element name="ins">
      <ref name="Main.attrs"/>
      <optional><attribute name="cite"><text/></attribute></optional>
      <ref name="Flow"/>
    </element>
  </define>

  <define name="del">
    <element name="del">
      <ref name="Main.attrs"/>
      <optional><attribute name="cite"><text/></attribute></optional>
      <ref name="Flow"/>
    </element>
  </define>

  <define name="a">
    <element name="a">
      <ref name="Main.attrs"/>
      <optional><attribute name="href"><text/></attribute></optional>
      <optional><attribute name="rel"><text/></attribute></optional>
      <interleave>
        <zeroOrMore><text/></zeroOrMore>
        <zeroOrMore><ref name="img"/></zeroOrMore>
        <zeroOrMore><ref name="span"/></zeroOrMore>
      </interleave>
    </element>
  </define>

  <define name="span">
    <element name="span">
      <ref name="Main.attrs"/>
      <ref name="Inline"/>
    </element>
  </define>

  <define name="br">
    <element name="br">
      <ref name="Core.attrs"/>
      <empty/>
    </element>
  </define>

  <define name="em">
    <element name="em">
      <ref name="Main.attrs"/>
      <ref name="Inline"/>
    </element>
  </define>

  <define name="strong">
    <element name="strong">
      <ref name="Main.attrs"/>
      <ref name="Inline"/>
    </element>
  </define>

  <define name="code">
    <element name="code">
      <ref name="Main.attrs"/>
      <ref name="Inline"/>
    </element>
  </define>

  <define name="cite">
    <element name="cite">
      <ref name="Main.attrs"/>
      <ref name="Inline"/>
    </element>
  </define>

  <define name="abbr">
    <element name="abbr">
      <ref name="Main.attrs"/>
      <ref name="Inline"/>
    </element>
  </define>

  <define name="sub">
    <element name="sub">
      <ref name="Main.attrs"/>
      <ref name="Inline"/>
    </element>
  </define>

  <define name="sup">
    <element name="sup">
      <ref name="Main.attrs"/>
      <ref name="Inline"/>
    </element>
  </define>

  <define name="object">
    <element name="object">
      <ref name="Main.attrs"/>
      <optional><attribute name="data"><text/></attribute></optional>
      <optional><attribute name="type"><text/></attribute></optional>
      <ref name="Flow"/>
    </element>
  </define>

  <define name="img">
    <element name="img">
      <ref name="Main.attrs"/>
      <attribute name="alt"><text/></attribute>
      <attribute name="src"><text/></attribute>
      <optional><attribute name="height"><text/></attribute></optional>
      <optional><attribute name="width"><text/></attribute></optional>
      <empty/>
    </element>
  </define>

  <define name="form">
    <element name="form">
      <ref name="Main.attrs"/>
      <attribute name="action"><text/></attribute>
      <optional><attribute name="method"><text/></attribute></optional>
      <ref name="BlockMinusForm"/>
    </element>
  </define>

  <define name="label">
    <element name="label">
      <ref name="Main.attrs"/>
      <ref name="Inline"/>
    </element>
  </define>

  <define name="input">
    <element name="input">
      <ref name="Main.attrs"/>
      <attribute name="type">
        <choice>
          <value>text</value>
          <value>submit</value>
          <value>hidden</value>
        </choice>
      </attribute>
      <optional><attribute name="name"><text/></attribute></optional>
      <optional><attribute name="size"><text/></attribute></optional>
      <optional><attribute name="value"><text/></attribute></optional>
      <empty/>
    </element>
  </define>

  <define name="textarea">
    <element name="textarea">
      <ref name="Main.attrs"/>
      <attribute name="cols"><text/></attribute>
      <attribute name="rows"><text/></attribute>
      <optional><attribute name="name"><text/></attribute></optional>
      <text/>
    </element>
  </define>

  <define name="table">
    <element name="table">
      <ref name="Main.attrs"/>
      <optional><ref name="caption"/></optional>
      <oneOrMore><ref name="tr"/></oneOrMore>
    </element>
  </define>

  <define name="caption">
    <element name="caption">
      <ref name="Main.attrs"/>
      <ref name="Inline"/>
    </element>
  </define>

  <define name="tr">
    <element name="tr">
      <ref name="Main.attrs"/>
      <oneOrMore>
        <choice>
          <ref name="th"/>
          <ref name="td"/>
        </choice>
      </oneOrMore>
    </element>
  </define>

  <define name="th">
    <element name="th">
      <ref name="Main.attrs"/>
      <ref name="Flow"/>
    </element>
  </define>

  <define name="td">
    <element name="td">
      <ref name="Main.attrs"/>
      <ref name="Flow"/>
    </element>
  </define>

</grammar>
```



 <h2>
  Conclusion
 </h2>
 <p>
  Le XHTML est un vocabulaire XML.  
Vous pouvez en consulter la DTD en ligne, à l'adresse http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd; 
il ne s'agit pas d'une DTD facile à lire, mais elle est néanmoins disponible. 
Notez qu'il existe de très bons livres de référence pour approfondir le XHTML, mais
pour ce cours, il suffit de connaître les quelques balises présentées dans ce document.
 </p>
 <p>
  Un des avantages importants du XHTML sur des pages web traditionnelles (souvent mal formées)
est qu'on peut facilement traiter des pages XHTML avec des outils destinés au XML.  En somme, on peut plus facilement extraire et traiter l'information d'une page XHTML
que l'on peut le faire d'une page HTML mal formée.
 </p>
 <h2>
  Livres de référence
 </h2>
 <ul>
  <li>
   Jennifer Robbins,
   <a href="http://www.amazon.ca/HTML-XHTML-Pocket-Reference-Robbins/dp/0596527276/sr=1-6/qid=1159624221/ref=sr_1_6/702-1271204-2832035?ie=UTF8&amp;s=books">
    HTML and XHTML Pocket Reference
   </a>
   , O'Reilly Media, 2006, 97 pages.
  </li>
  <li>
   Jean Engels,
   <a href="http://www.amazon.ca/Xhtml-css-exercices-Jean-Engels/dp/2212116373/sr=1-1/qid=1159624092/ref=sr_1_1/702-1271204-2832035?ie=UTF8&amp;s=books-en-francais">
    XHTML et css : cours et exercices
   </a>
   , Eyrolles, 2006.
  </li>
 </ul>
 <h2>
  Activité d'autoévaluation
 </h2>
 <p>
  Afin de vous assurez d'avoir bien compris les notions présentées dans cette leçon, vous devez créer un document XHTML valable, utilisant les différents éléments que nous avons étudiés. Afin que votre navigateur reconnaisse le document comme étant du XHTML, vous devriez utiliser l'extension « xhtml ». Si vous déposez le fichier sur un serveur web Apache, il peut être nécessaire de créer aussi un fichier « .htaccess » et de le déposer dans
le même répertoire que votre fichier XHTML afin que le serveur puisse reconnaître
les fichiers XHTML. Votre fichier « .htaccess » pourrait avoir le contenu suivant :
 </p>
 <pre>DirectoryIndex index.xhtml index.html index.php index.pl index.cgi
AddType application/xml .xhtml
</pre>
</div>
<hr/>
