---
title: "CSS"
weight: 40
---
<h1>
 CSS
</h1>
<p>
 La norme CSS a d'abord été proposée par Håkon Lie du CERN en Suisse en 1994
    (environ 4 ans après l'apparition de la première page web). Cette norme a
    été acceptée
    comme recommandation officielle du W3C deux ans plus tard, soit en 1996, et
    la seconde version (CSS 2.0)
    est devenue une recommandation du W3C l'année suivante, soit en 1997. Une
    troisième version (CSS 3) a été adoptée à compter de 2011. À
    l'origine, les instructions CSS étaient destinées uniquement à indiquer aux
    navigateurs comment présenter
    le HTML (couleurs, polices, etc.); on s'est vite rendu compte qu'on pouvait
    aussi l'appliquer
    au XML et on considère maintenant les CSS comme une technologie qui
    s'applique
    autant au HTML qu'au XML (et aussi, évidemment, au XHTML).
</p>
<p>
 Nous avons vu que le XSLT permettait de transformer
    du XML en HTML pour l'affichage dans un navigateur. En général, le XSLT
    permet de transformer
    tout document XML en un autre format (HTML, XML ou autre).
</p>
<p>
 Un fichier CSS est beaucoup plus limité dans la mesure où il ne transforme
    pas le document XML.
    Il permet seulement de spécifier comment le contenu du document XML sera
    affiché.
    Le fichier XSLT est un outil de transformation, alors que le fichier CSS est
    un outil de formatage. Un document
    CSS permet de rendre un document XML plus lisible. D'un autre côté, le
    fichier CSS permet
    de contrôler avec beaucoup de finesse la présentation du document XML, alors
    qu'il peut être difficile et fastidieux d'obtenir
    le même résultat en XSLT, sans utiliser les CSS. Les fichiers CSS tendent
    aussi à être plus simples que les fichiers
    XSLT; il peut donc être plus facile de les modifier et de les garder à jour.
    Finalement, on
    peut utiliser à la fois des fichiers CSS et des fichiers XSLT, en combinant
    les avantages
    des deux (présentation et transformation).
</p>
<h2 class="recall">
 Point de vue critique
</h2>
<p>
 CSS est un langage déclaratif relativement limité.
    Il n'est pas possible de définir des variables, des fonctions ou de
    faire de l'arithmétique en CSS. On peut, par contre, redéfinir à volonté des
    règles, ce qui peut rendre le comportement final difficile à comprendre pour
    un humain. Il n'est pas facile, en CSS, de détecter le navigateur utilisé
    alors que tous les
    navigateurs ne traitent pas les règles de la même façon.
</p>
<h3 class="recall">
 Notions de base
</h3>
<p>
 Pour l'essentiel, le langage CSS prend la forme d'une succession
    d'affirmations de la
    forme
 <i>
  élément {propriété: valeur; autrepropriété: valeur;}
 </i>
 . Il s'agit
    d'une syntaxe très simple.
</p>
<p>
 Supposons un document XML comme celui-ci :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
    &lt;comptearecevoir&gt;
    &lt;facture&gt;
    &lt;personne&gt;Jean Rochond&lt;/personne&gt;
    &lt;montant&gt;10.10&lt;/montant&gt;
    &lt;raison&gt;Achat d'ordinateur&lt;/raison&gt;
    &lt;/facture&gt;
    &lt;facture&gt;
    &lt;personne&gt;Madeleine Bédard&lt;/personne&gt;
    &lt;montant&gt;20.10&lt;/montant&gt;
    &lt;raison&gt;Achat d'un crayon&lt;/raison&gt;
    &lt;/facture&gt;
    &lt;/comptearecevoir&gt;
</p>
<p>
 Certains navigateurs affichent
    le XML brut sans formatage, ce qui n'est pas
    très accessible. D'autres navigateurs
    affichent le document sans les balises :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 Jean Rochond
    10.10
    Achat d'ordinateur
    Madeleine Bédard
    20.10
    Achat d'un crayon
</p>
<p>
 Ce document XML est difficile à lire, même sans les balises, surtout si vous
    n'êtes pas un expert
    en XML. Sans le transformer, il est possible de l'afficher avec de la
    couleur ou de l'italique, comme
    ceci :
</p>
<ul>
 <li>
  Jean Rochond
  <span style="color:red">
   10.10
  </span>
  <p>
   <i>
    Achat d'ordinateur
   </i>
  </p>
 </li>
 <li>
  Madeleine Bédard
  <span style="color:red">
   20.10
  </span>
  <p>
   <i>
    Achat d'un crayon
   </i>
  </p>
 </li>
</ul>
<p>
 Voilà qui est nettement plus lisible! Nous pouvons obtenir ce résultat à
    l'aide du fichier CSS suivant :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 facture {
    display: block;
    margin-bottom: 30pt;
    }
    montant {
    color: red;
    }
    raison {
    display: block;
    font-style: italic;
    margin-left: 1cm;
    }
</p>
<p>
 Pour vérifier que c'est bien le cas, il suffit de créer un fichier
    « chap12.css »
    avec le contenu CSS précédent et de modifier le fichier XML en y ajouter une
    ligne
    pointant vers le fichier CSS (&lt;?xml-stylesheet type="text/css"
    href="chap12.css"?&gt;), comme ceci :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
    &lt;?xml-stylesheet type="text/css" href="chap12.css"?&gt;
    &lt;comptearecevoir&gt;
    &lt;facture&gt;
    &lt;personne&gt;Jean Rochond&lt;/personne&gt;
    &lt;montant&gt;10.10&lt;/montant&gt;
    &lt;raison&gt;Achat d'ordinateur&lt;/raison&gt;
    &lt;/facture&gt;
    &lt;facture&gt;
    &lt;personne&gt;Madeleine Bédard&lt;/personne&gt;
    &lt;montant&gt;20.10&lt;/montant&gt;
    &lt;raison&gt;Achat d'un crayon&lt;/raison&gt;
    &lt;/facture&gt;
    &lt;/comptearecevoir&gt;
</p>
<p>
 Si le fichier XML est dans le même répertoire que le fichier CSS, votre
    navigateur
    devrait vous présenter le document XML avec le montant en rouge et le
    commentaire (raison) en italique,
    comme nous l'avons présenté plus haut.
</p>
<p>
 Notez que dans le laboratoire de cette semaine, vous pourrez expérimenter
    avec CSS au sein de votre navigateur sans devoir créer de fichiers.
</p>
<p>
 Examinons maintenant les différentes instructions du fichier CSS.
</p>
<ul>
 <li>
  L'instruction « display: block; » déclare que l'élément
        devrait
        former son propre paragraphe. L'instruction « display: none; »
        rend l'élément invisible.
 </li>
 <li>
  Les instructions « margin-bottom: 30pt; » et
        « margin-left: 1cm; » définissent des marges
        en bas et à gauche de 30 points et de 1 cm respectivement.
 </li>
 <li>
  L'instruction « color: red; » affirme que le contenu de
        l'élément devrait être écrit en rouge,
        alors que « font-style: italic; » nous dit que le texte de
        l'élément devrait être en italique. On pourrait
        aussi contrôler la couleur de fond avec un instruction comme
        « background-color:red ».
 </li>
</ul>
<p>
 Dans l'éventualité où nous voulons choisir une couleur très précise, et non
    les
    couleurs courantes comme « red », « green »,
    « blue », « yellow », « white »,
    « black », etc.,
    nous pouvons la spécifier selon sa composition avec les couleurs de base
    (« red »,
    « green , « blue ») avec une instruction
    comme « background-color:rgb(200,200,200); », où chaque valeur
    numérique est entre 0 et 255 inclusivement.
</p>
<h3 class="recall">
 Les unités de mesure
</h3>
<p>
 En CSS, on peut spécifier la taille d'un objet avec plusieurs unités de
    mesure, par exemple cm pour centimètre ou px pour pixel. Ainsi donc
    l'instruction « width:1px » spécifie une largeur de 1 pixel. On peut aussi
    utiliser des unités relatives comme « em », « rem » ou « % ». Une mesure de
    « 50 % » indique que l'objet devrait occuper la moitié de l'espace
    disponible. Une mesure de « 1em » correspond à la taille de la police de
    caractère dans l'élément courant alors que « 1rem » correspond à la taille
    de la police de caractère dans l'élément-racine du document. On peut aussi
    combiner les unités... par exemple, pour spécifier une dimension
    correspondant à tout l'espace disponible moins 80 pixels, on peut utiliser
    la valeur «calc(100% - 80px)». Pour bien comprendre, l'idéal est de faire
    des expériences.
</p>
<h3 class="recall">
 Contenu en ligne ou en bloc ?
</h3>
<p>
 Par défault, les éléments s'affichent en ligne, un à la suite de l'autre. On
    peut contrôler comment s'affiche un élément avec la propriété
    « display » qui peut prendre plusieurs valeurs dont
    celles-ci :
</p>
<ul>
 <li>
  « display: none »: l'élément ne doit pas s'afficher. Par
        exemple, l'instruction « img{display: none;} » fait en sorte
        que les images ne s'affichent plus en HTML. Il est fréquent qu'avec du
        JavaScript, on cache et affiche tour à tour des éléments pour donner
        l'impression que la page est dynamique.
 </li>
 <li>
  « display: inline »: l'élément s'affiche à la suite du
        précédent comme s'il s'agissait d'un caractère.
 </li>
 <li>
  « display: block »: l'élément s'affiche dans un bloc distinct,
        comme un nouveau paragraphe, par exemple.
 </li>
 <li>
  « display: list-item »: l'élément s'affiche comme un élément
        d'une liste.
 </li>
 <li>
  « display: flex » ou « display: inline-flex »: les
        éléments contenus s'affichent selon un modèle flexible (voir
        https://css-tricks.com/snippets/css/a-guide-to-flexbox/).
 </li>
</ul>
<p>
 Voici un exemple :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 p { display: block }
    strong { display: inline }
    li { display: list-item }
    img { display: none }
</p>
<p>
 On peut aussi définir la propriété « float » d'un élément qui lui
    permet de sortir du flot normal des éléments et de se placer à gauche ou à
    droite. Par exemple, une image en XHTML s'affiche normalement comme un bloc.
    On peut forcer l'image à s'intégrer au paragraphe suivant avec l'instruction
    « float: right » ou « float: left ». On peut aussi
    utiliser la propriété « float » pour créer plusieurs colonnes
    de texte comme dans un journal. Je vous invite à faire différentes
    expériences pour mieux comprendre l'utilisation de cette instruction.
</p>
<h3 class="recall">
 Centrer un élément
</h3>
<p>
 Bien qu'on puisse changer la justification du texte avec une instruction
    comme « text-align: center », centrer un élément requiert plutôt
    une manipulation des marges avec la valeur spéciale « auto »,
    comme dans cet exemple :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 p { width: 5cm;
    margin-left: auto;
    margin-right: auto;}
</p>
<p>
 Il aurait été sans doute préférable d'avoir une instruction dédiée pour
    centrer les éléments comme il s'agit d'une opération courante.
</p>
<h3 class="recall">
 Les commentaires
</h3>
<p>
 Tout comme en Java, on peut ajouter des commentaires à un fichier CSS qui
    sont systématiquement ignorés par la machine. Un bloc de commentaire
    débute par « /* » et se termine par « */ ».
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 /* mon fichier css */
    montant {
    color: red; /* la couleur rouge */
    }
</p>
<h3 class="recall">
 Sélectionner le premier caractère ou la première ligne
</h3>
<p>
 On peut sélectionner la première ligne d'un élément s'affichant en mode
    « block » et le premier caractère de tout élément avec
    les sélecteurs « :first-line » et :« :first-letter »
    respectivement. Voici
    un exemple :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 p:first-line {text-transform: uppercase}
    p:first-letter {font-size: 200%;float: left;}
</p>
<h3 class="recall">
 Ajouter du contenu avant et après un élément
</h3>
<p>
 Avec CSS, on peut demander qu'une certaine chaîne de caractères apparaisse
    avant ou après un élément. Par exemple, si on veut ajouter automatiquement
    des guillemets avant et après un élément, on peut procéder comme ceci :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 blockquote:before {content:"«";}
    blockquote:after {content:"»";}
</p>
<p>
 Nous ne sommes pas limités au texte cependant. Il est possible, par exemple,
    d'ajouter automatiquement une image avant chaque élément comme ceci :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 p:before {content:url("monimage.png";}
</p>
<h3 class="recall">
 Qu'est-ce qu'un pseudo-élément?
</h3>
<p>
 Les instructions first-line, first-letter, before et after que nous venons de
    présenter
    sont les principaux exemples de pseudo-éléments.
</p>
<h3 class="recall">
 Sélecteurs d'interaction
</h3>
<p>
 Certains sélecteurs n'agissent qu'en réponse aux comportements de
    l'utilisateur. Par exemple, le sélecteur « p:hover » sélectionne
    les éléments « p » qui sont survolés par le curseur de la souris.
    Il existe plusieurs sélecteurs d'interaction dont « :link » (lien
    non visité), « :visited » (lien visité), « active »
    (l'utilisateur utilise un élément), « :focus » (l'élément est
    sélectionné par l'utilisateur). On peut aussi combiner les sélecteurs comme
    dans cet exemple : « a:hover:focus ».
    On appelle aussi ces sélecteurs de pseudo-classes.
</p>
<h3 class="recall">
 Règles par défaut
</h3>
<p>
 Dans le cas du HTML ou du XHTML, les navigateurs utilisent une liste de
    règles par
    défaut. Ces règles vont varier d'un navigateur à l'autre, mais voici un
    exemple de règles
    utilisées par des navigateurs :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 html, div {
    display: block;
    }
    body {
    display: block;
    margin: 8px;
    }
    p, dl, multicol {
    display: block;
    margin: 1em 0;
    }
    blockquote {
    display: block;
    margin: 1em 40px;
    }
    h1 {
    display: block;
    font-size: 2em;
    font-weight: bold;
    margin: .67em 0;
    }
    h2 {
    display: block;
    font-size: 1.5em;
    font-weight: bold;
    margin: .83em 0;
    }
    pre {
    display: block;
    white-space: pre;
    margin: 1em 0;
    }
    b, strong {
    font-weight: bolder;
    }
    i, cite, em, var, dfn {
    font-style: italic;
    }
    u, ins {
    text-decoration: underline;
    }
    s, strike, del {
    text-decoration: line-through;
    }
    big {
    font-size: larger;
    }
    small {
    font-size: smaller;
    }
    sub {
    vertical-align: sub;
    font-size: smaller;
    line-height: normal;
    }
    sup {
    vertical-align: super;
    font-size: smaller;
    line-height: normal;
    }
    ul, menu, dir {
    display: block;
    list-style-type: disc;
    margin: 1em 0;
    }
    ol {
    display: block;
    list-style-type: decimal;
    margin: 1em 0;
    }
    li {
    display: list-item;
    }
    area, base, basefont, head, meta, script, style, title,
    noembed, param {
    display: none;
    }
</p>
<h3 class="recall">
 L'astérisque
</h3>
<p>
 L'astérisque nous permet d'appliquer une règle à tous les éléments, comme
    dans cet exemple :
    « * {color:red;} ».
</p>
<h3 class="recall">
 Sélection sur la base des attributs
</h3>
<p>
 Avec les CSS, en utilisant les crochets, nous pouvons sélectionner tous les
    éléments ayant un attribut donné.
    Par exemple, l'instruction « *[monattribut] { color:red;} » mettra
    en rouge tous les éléments
    ayant un attribut portant le nom « monattribut ». Nous pouvons
    aussi, bien sûr, limiter la sélection à des
    éléments portant un nom donné comme dans cet exemple :
    « maman[monattribut] { color:red;} »
    où les éléments « maman » ayant un attribut
    « monattribut » seront en rouge.
    Finalement, nous pouvons de plus limiter la sélection à des attributs ayant
    une certaine valeur,
    comme dans « maman[monattribut="papa"] { color:red;} ».
</p>
<p>
 Il arrive fréquemment qu'une valeur d'attribut contiennent plusieurs
    mots, comme dans « &lt;amerique pays="États-Unis Canada" /&gt; ».
    Pour sélectionner tous les élément dont un attribut
    contiennent un mot particulier, on remplace « = » par
    « ~= » comme dans l'instruction « *[pays~="Canada"] {
    color:red;} » qui mettra en rouge tout élément dont l'attribut
    « pays » contient le mot « Canada ». Les mots
    doivent être séparés par des espaces. Dans l'éventualité où les mots
    sont séparés par des tirets, comme dans « &lt;amerique
    pays="Mexique-Canada" /&gt; », on peut obtenir le même résultat
    avec « |= » comme dans « *[pays|="Canada"] {
    color:red;} ».
</p>
<h3 class="recall">
 Les espaces de noms
</h3>
<p>
 Les espaces de noms ne sont pas supportés en CSS 1 ou CSS 2.
    Ainsi « monelement { color:red;} » met en rouge le
    contenu de tous les éléments monelement, peu importe leur espace de noms.
    Il est incorrect d'utiliser la syntaxe
    « xhtml:monelement { color:red;} ».
</p>
<h3 class="recall">
 Sélection de la langue
</h3>
<p>
 On a vu qu'il est possible en XML de spécifier la langue dans laquelle est
    écrit un texte avec l'attribut « xml:lang. ». On pourrait penser
    que pour mettre le texte déclaré comme étant en anglais en rouge,
    il suffirait de l'instruction « *[lang="fr"] { color:red;} », mais
    que se passera-t-il si on a utilisé un code
    de région avec la langue comme « fr-CA »? Une solution
    plus élégante consiste alors à utiliser la sélection sur la langue
    avec une instruction comme « :lang(en) { color:red;} ».
</p>
<h3 class="recall">
 Sélection de plusieurs éléments
</h3>
<p>
 Supposons maintenant que nous voulions afficher en rouge tous les éléments
    « facture » et « maison ».
    Nous pouvons le faire avec deux instructions :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 facture { color:red;}
    maison { color:red;}
</p>
<p>
 En pratique cependant, il est préférable d'utiliser la virgule pour grouper
    les éléments, comme ceci :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 facture, maison { color:red;}
</p>
<p>
 Les deux instructions et cette dernière forme sont exactement équivalentes.
</p>
<h3 class="recall">
 Sélection sur la base de la relation entre les éléments
</h3>
<p>
 Supposons maintenant que nous ne voulions pas afficher tous les éléments
    « personne » en rouge,
    mais seulement les éléments « personne » contenus dans un élément
    « facture ».
    Nous obtiendrons ce résultat en plaçant les deux noms d'élément côte-à-côte
    (séparé par un espace). Ainsi, l'instruction
    « facture personne { color:red;} » affichera en rouge tous les
    éléments « personne »
    contenus dans un élément « facture », comme dans l'exemple qui
    suit :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
    &lt;?xml-stylesheet type="text/css" href="chap12.css"?&gt;
    &lt;comptearecevoir&gt;
    &lt;facture&gt;
    &lt;personne&gt;Jean Rochond&lt;/personne&gt;
    &lt;/facture&gt;
    &lt;/comptearecevoir&gt;
</p>
<p>
 ou dans ce deuxième exemple...
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
    &lt;?xml-stylesheet type="text/css" href="chap12.css"?&gt;
    &lt;comptearecevoir&gt;
    &lt;facture&gt;
    &lt;client&gt;&lt;personne&gt;Jean Rochond&lt;/personne&gt;&lt;/client&gt;
    &lt;/facture&gt;
    &lt;/comptearecevoir&gt;
</p>
<p>
 Nous pourrions vouloir que seuls les éléments immédiatement contenus
    dans l'élément « facture », comme dans le premier exemple, soient
    en rouge,
    et non pas ceux qui sont contenus dans des éléments eux-mêmes dans un
    élément « facture » (deuxième exemple).
    Nous pouvons obtenir ce résultat avec l'instruction « facture &gt;
    personne { color:red;} ».
</p>
<p>
 En somme, la règle « a b { color:red;} » s'applique à l'élément
    « b »,
    si l'élément « b » est contenu dans un élément « a »
    comme dans
    « &lt;a&gt;&lt;b&gt;&lt;/b&gt;&lt;/a&gt; » ou
    « &lt;a&gt;&lt;c&gt;&lt;b&gt;&lt;/b&gt;&lt;/c&gt;&lt;/a&gt; ».
</p>
<p>
 Par contre, la règle « a &gt; b { color:red;} » s'applique à
    l'élément « b »,
    si et seulement si l'élément « b » est immédiatement contenu dans
    un élément « a »,
    comme dans « &lt;a&gt;&lt;b&gt;&lt;/b&gt;&lt;/a&gt; ». Elle ne
    s'applique toutefois pas si « b »
    est contenu dans un élément lui-même contenu dans « a », comme
    dans
    « &lt;a&gt;&lt;c&gt;&lt;b&gt;&lt;/b&gt;&lt;/c&gt;&lt;/a&gt; ».
</p>
<p>
 Supposons maintenant, dans l'exemple suivant, que nous voulions indenter le
    premier
    paragraphe (élément « p ») suivant le titre (élément
    « titre ») :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
    &lt;titre&gt;Mon histoire&lt;/titre&gt;
    &lt;p&gt;C'est triste.&lt;/p&gt;
    &lt;p&gt;Oui, c'est triste.&lt;/p&gt;
</p>
<p>
 Ce résultat s'obtient avec l'instruction « titre + p { text-indent:
    0cm;} ».
    La syntaxe « a + b { ... } » s'applique à l'élément
    « b »
    quand les éléments « a » et « b » sont contenus dans le
    même élément, et que « b » est
    immédiatement après « a ». Notez que la règle « a + b { ...
    } » s'applique
    à « b », mais ne s'applique pas à « a ».
</p>
<p>
 Supposons que nous désirions indenter le premier
    paragraphe (élément « p ») dans l'élément
    « section » :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
    &lt;section titre="Mon histoire" &gt;
    &lt;p&gt;C'est triste.&lt;/p&gt;
    &lt;p&gt;Oui, c'est triste.&lt;/p&gt;
    &lt;/titre&gt;
</p>
<p>
 On peut obtenir ce résultat avec le sélecteur « section &gt;
    p:first-child { ... } » où « :first-child » signifie que
    seuls les éléments « p » étant le premier élément au sein d'un
    autre élément sont sélectionnés. En fait, dans cet exemple particulier, on
    obtiendrait aussi le résultat voulu avec le sélecteur « p:first-child {
    ... } ».
</p>
<p>
 Par ailleurs, nous pouvons combiner les espaces, les « + », les
    virgules et les « &gt; »
    dans un même sélecteur. Par exemple, « a + b, c { ... } »
    s'applique aux éléments « c »
    et aux éléments « b » qui suivent immédiatement un élément
    « a ».
</p>
<h3 class="recall">
 Sélection d'élément par valeur ID
</h3>
<p>
 Si vous avez des éléments ayant des attributs ayant une valeur de type
    « ID »,
    on sait alors que leur valeur est un nom XML et qu'elle ne doit être
    utilisée qu'une seule
    fois. C'est le cas des attributs de la forme « id="xxx" » que l'on
    peut utiliser
    avec pratiquement tous les éléments XHTML. On peut sélectionner un élément
    basé sur la
    valeur d'un tel attribut en utilisant le symbole « # » :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 #xxx {
    color: red;
    }
</p>
<p>
 Dans ce cas, le contenu d'un élément comme une balise XHTML « &lt;p
    id='xxx'&gt;test&lt;/p&gt; » s'affichera
    en rouge. On peut combiner les sélecteurs « # » avec les autres
    règles que nous avons traitées , par exemple,
    le code suivant ne mettra en rouge que les éléments « i » contenus
    dans un élément ayant un attribut
    de type « ID » avec pour valeur « xxx » :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 #xxx i{
    color: red;
    }
</p>
<h3 class="recall">
 Mais que se passe-t-il en cas de conflit?
</h3>
<p>
 Plusieurs instructions peuvent s'appliquer en même temps: un texte peut être
    en rouge
    et souligné. Il peut arriver cependant que deux instructions CSS se
    contredisent. Par exemple, un texte
    ne peut être à la fois en rouge et en bleu. Dans ce cas,
    la sélection la plus spécifique l'emporte. Ainsi, dans l'exemple qui suit...
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 * {
    color: black;
    }
    montant {
    color: red;
    }
    montant &gt; montant {
    color: yellow;
    }
</p>
<p>
 les éléments « montant » seront en rouge, sauf s'ils sont
    immédiatement
    contenus dans un autre élément « montant », auquel cas ils seront
    en jaune.
</p>
<p>
 Par ailleurs, si deux sélections de même spécificité sont rencontrées, c'est
    la dernière qui l'emporte.
    Ainsi, dans l'exemple qui suit...
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 montant {
    color: red;
    }
    montant {
    color: black;
    }
</p>
<p>
 les éléments « montant » seront en noir.
</p>
<p>
 On peut cependant forcer le navigateur à considérer une règle qui apparaît
    avant une autre
    comme ayant tout de même priorité (à spécificité égale). Il suffit
    d'utiliser la mention !important...
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 montant {
    color: red !important;
    }
    montant {
    color: black;
    }
</p>
<p>
 les éléments « montant » seront en rouge.
    Notez que la mention !important permet souvent d'ignorer la spécificité de
    la règle: les
    règles avec cette mention l'emportent toujours sur les autres. (Si une autre
    règle avec la mention !important a une plus grande spécificité, elle aura
    bien sûr priorité.)
</p>
<p>
 Les règles par défaut utilisées par votre navigateur dans le cas du HTML ou
    du XHTML
    sont lues en premier. De cette manières, toutes les règles qui vous stipulez
    dans
    vos propres fichiers CSS et à même le XML ou HTML ont priorité pour une même
    spécificité. On peut considérer que
    les règles
    avec la mention !important sont lues en dernier dans la mesure où elles
    l'emportent toujours sur les autres.
</p>
<p>
 Calculer la
 <a href="http://www.w3.org/TR/CSS21/cascade.html#specificity" shape="rect">
  spécificité des règles
 </a>
 n'est pas une mince affaire,
    mais c'est pourtant nécessaire dans certains cas difficiles. La spécificité
    se mesure avec
    une valeur à 4 chiffres (a,b,c,d). Lorsqu'on compare deux spécificités
    (a1,b1,c1,d1) et (a2,b2,c2,d2), on
    utilise l'ordre lexicographique pour déterminer lequel est supérieur. Ainsi,
    si a1 est plus grand que a2,
    alors (a1,b1,c1,d1) a une plus grande spécificité que (a2,b2,c2,d2), si a1
    est égal à a2, alors on
    compare b1 et b2, et ainsi de suite.
</p>
<ul>
 <li>
  La première valeur (a) vaut 1 si et seulement si la règle apparaît dans
        le fichier XML, HTML ou XHTML dans un
        attribut style. Par exemple, si on a un élément paragraphe en HTML de
        cette forme &lt;p style="color:red" &gt;, alors la règle color:red aura
        une très grande spécificité.
 </li>
 <li>
  La seconde valeur (b) est le nombre de sélections sur la valeur ID
        utilisée par la règle. Ainsi, la règle
        #x {color:red} pourra avoir une spécificité de 0,1,0,0. En pratique, la
        sélection par valeur ID l'emporte souvent
        sur les autres règles.
 </li>
 <li>
  La troisième valeur (c) est le nombre de valeurs d'attributs utilisées
        par la règle (excluant l'attribut ID). Ainsi, la règle
        *[monattribut] { color:red;} pourrait avoir comme spécificité 0,0,1,0.
        Les pseudo-classes comptent comme des attributs.
 </li>
 <li>
  La quatrième valeur (c) est le nombre d'éléments utilisés par la règle.
        Ainsi, la règle
        p[monattribut] { color:red;} pourrait avoir comme spécificité 0,0,1,1.
 </li>
</ul>
<p>
 Pour mieux comprendre, prenons un exemple concret...
</p>
<pre xml:space="preserve">z[x] &gt; a[i] {color: blue;}
    z z[x] a {text-decoration: underline;}
    z &gt; z a , z z z + a { color: red ;}
</pre>
<p>
 Il est plus facile de comptabiliser la spécificité si on écrit les règles
    individuellement (sans la virgule).
    Voyez si vous êtes capable de voir pourquoi les différentes règles ont les
    spécificités annoncées
    dans les commentaires...
</p>
<pre xml:space="preserve">/* spécificité: 0,0,2,2 */
    z[x] &gt; a[i] {color: blue;}
    /* spécificité: 0,0,0,3 */
    z &gt; z a { color: red ; }
    /* spécificité: 0,0,0,4 */
    z z z + a { color: red; }
    /* spécificité: 0,0,1,3 */
    z z[x] a {text-decoration: underline;}
</pre>
<p>
 Prenons maintenant un fichier XML auquel on applique les instructions
    CSS précédente. L'élément a dans le fichier suivant est sélectionné par
    les 4 règles du fichier CSS. Comment sera affiché le texte dans
    votre navigateur?
</p>
<pre xml:space="preserve">&lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
    &lt;?xml-stylesheet type="text/css" href="test.css"?&gt;
    &lt;z&gt;&lt;z x="x"&gt;
    &lt;z /&gt;
    &lt;a i="x"&gt;mon texte&lt;/a&gt;
    &lt;/z&gt;
    &lt;/z&gt;
</pre>
<p>
 Le texte apparaîtra en bleu et sera souligné. Si on ajoute une instruction
    avec la mention !important comme « * {color: black !important;} »
    alors
    on peut faire en sorte que le texte soit noir.
</p>
<h3 class="recall">
 Le modèle de boîte CSS
</h3>
<p>
 En CSS, on peut spécifier la hauteur et la largeur d'un objet à l'aide
    des instructions « width » et « height ». Par exemple,
    pour indiquer qu'un paragraphe devrait n'avoir qu'une largeur de
    20 pixels,
    on utilise un sélecteur comme celui-ci :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 p{
    width: 20px;
    }
</p>
<p>
 Le CSS supporte plusieurs unités de mesure outre les pixels dont les pouces
    (in), les centimètres (cm), pourcentage (%), etc.
</p>
<p>
 On peut ensuite définir une marge (
 <i>
  margin
 </i>
 en anglais) autour de tout
    objet. La marge est une région où rien ne peut apparaître, incluant un autre
    objet. Mais la marge ne fait pas partie de l'objet lui-même. Ainsi, si un
    objet fait 10 pixels de hauteur et de largeur, et que vous définissez
    une marge de 10 pixels tout autour de l'objet, un espace d'une
    superficie de 900 pixels sera occupée sur l'écran. Voici un exemple de
    marge :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 p{
    margin-top:10px;
    margin-bottom:10px;
    margin-right:10px;
    margin-left:10px;
    }
</p>
<p>
 Outre la marge, on peut aussi définir une région d'espacement (
 <i>
  padding
 </i>
 en anglais). Contrairement à la marge, la région d'espacement fait partie de
    l'objet dans la mesure où, si vous
    définissez une couleur de fond pour l'objet, la région d'espacement sera
    colorée, car elle fait partie de l'objet. Tout comme la marge, rien n'occupe
    cette région et elle n'est pas comptabilisée dans la hauteur et la largeur
    de l'objet.
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 p{
    padding-top:10px;
    padding-bottom:10px;
    padding-right:10px;
    padding-left:10px;
    }
</p>
<p>
 On peut définir une bordure (
 <i>
  border
 </i>
 en anglais) afin de tracer
    un ligne tout autour de l'objet. La bordure se place entre la région
    d'espacement et la marge. La bordure peut prendre différente épaisseurs
    (telles que
 <i>
  thin
 </i>
 ,
 <i>
  medium
 </i>
 , et
 <i>
  thick
 </i>
 ) et aussi une
    couleur.
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 p{
    border-color: black;
    border-width: medium;
    }
</p>
<p>
 Voici un diagramme qui résume les différentes définitions :
</p>
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
<p>
 (Comme il se doit, ce diagramme est XML par l'entremise du SVG.)
</p>
<h3 class="recall">
 Quand le contenu excède le contenant
</h3>
<p>
 Il arrive qu'une image ou qu'un texte excède la taille de
    l'élément dans lequel il a été placé. Par défaut, ce texte
    ou cet image s'affichera au-delà du cadre de sa boîte
    (« overflow:visible »). L'instruction
    « overflow:hidden » permet de faire disparaître
    la partie d'un texte ou d'une image qui excède la boîte, alors
    que l'instruction « overflow:scroll » va faire
    apparaître des barres de défilement pour permettre à l'utilisateur
    d'avoir accès à tout le contenu sans pour autant avoir un
    dépassement..
</p>
<h3 class="recall">
 Encodage des caractères
</h3>
<p>
 Il peut être utile de spécifier l'encodage des caractères utilisé pour créer
    le document CSS. Il suffit d'inclure une instruction « @charset »
    au tout début du document. Voici deux exemples :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 @charset "UTF-8";
    @charset "ISO-8859-1";
</p>
<h3 class="recall">
 Différentes règles pour différents média
</h3>
<p>
 Il arrive qu'on veuille qu'une page s'affiche différemment selon qu'on
    utilise un écran, qu'on l'imprime sur papier ou qu'on utilise un
    téléphone cellulaire. L'instruction « @media » permet de
    préciser quel médium est concerné par la règle CSS. Plusieurs média sont
    reconnus dont « handheld » (appareil portable comme un téléphone
    cellulaire), « screen » (à l'écran), « tv » (sur un
    téléviseur), « print » (sur papier), etc. Lorsque l'instruction
    « @media » n'est pas précisée, la règle s'applique tout le temps.
    Voici un exemple :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 @media print, handheld {
    img { display: none }
    h1 {color: black }
    }
    @media screen, tv {
    h1 {color: blue }
    }
</p>
<h3 class="recall">
 Inclure d'autres fichiers CSS
</h3>
<p>
 Il arrive parfois qu'on veuille adopter une approche modulaire et
    créer plusieurs petits fichiers CSS. L'instruction
    « @import » apparaissant avant le début des règles, mais après une
    éventuelle instruction « @charset » permet d'inclure un ou
    plusieurs
    fichiers CSS. On peut aussi spécifier le type de médium concerné.
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 @import "mineure.css";
    @import "print-mineure.css" print;
</p>
<h3 class="recall">
 Indentation de la première ligne d'un paragraphe
</h3>
<p>
 On peut indenter la première ligne d'un paragraphe avec
    l'instruction « text-indent ». Par exemple, pour indenter la
    première ligne de tous les paragraphes par 1 cm, on peut utiliser
    l'instruction « text-indent: 1cm ».
</p>
<h3 class="recall">
 Modifier la casse du texte
</h3>
<p>
 L'instruction « text-transform » permet de modifier la casse du
    texte
    ce qui est particulièrement utile avec les titres. Par exemple,
    « text-transform: capitalize » modifie le texte de manière à ce
    que le premier caractère de chaque mot soit en majuscule. Les instructions
    « text-transform: uppercase » et « text-transform:
    lowercase » permettent de passer à une casse uniforme (majuscule ou
    minuscule).
</p>
<h3 class="recall">
 Autres variantes des polices
</h3>
<p>
 Il est possible de modifier de diverses façons les polices :
    « font-style:italic », « font-style:oblique »
    « font-family: sans-serif », « font-family: serif »,
    « font-weight: bold », « font-weight: bolder »,
    « font-weight: lighter ». On peut modifier la taille des
    caractères : « font-size: large », « font-size:
    small ». On peut
    ajouter des lignes sous, sur ou au dessus le texte, ou faire clignoter le
    texte : « text-decoration: underline »,
    « text-decoration: overline »,
    « text-decoration: line-through »,
    « text-decoration: blink ».
    Vous pouvez aussi spécifier
    l'apparence que prendra le curseur
    avec l'attribut « cursor » qui prend la
    valeur « text » par défaut, et la valeur
    « pointer » pour les hyperliens.
</p>
<h3 class="recall">
 Ajouter des compteurs
</h3>
<p>
 On peut définir des compteurs pour, par exemple, numéroter des chapitres
    ou paragraphes. Ce premier exemple numérote les paragraphes (éléments
    « p ») contenus entre
    chaque élément « h1 » avec des nombres romains :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 p {counter-increment: par-num}
    h1 {counter-reset: par-num}
    p:before {content: counter(par-num, upper-roman) ". "}
</p>
<p>
 Ce second exemple numérote les éléments « h1 » avec des
    nombres arabes :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 h1 {counter-increment: h1-num}
    h1:before {content: counter(h1-num, decimal) ". "}
</p>
<p>
 Ce troisième exemple « numérote » les éléments « h1 » et
    « h2 » avec des
    lettres (a,b,c,...) :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 h1 {counter-reset: h2counter; counter-increment: h1counter}
    h2 {counter-increment: h1counter}
    h1:before {content: counter(h1counter, lower-latin) ". "}
    h2:before {
    content: counter(h1counter, lower-latin) "."
    counter(h2counter, lower-latin) ". " }
</p>
<h3 class="recall">
 Traitement des retours de chariot
</h3>
<p>
 Par défaut, le contenu textuel d'un élément est affiché sans tenir compte des
    retours de chariot présents dans le fichier XML, mais en insérant plutôt des
    retours de chariot au besoin. Avec l'instruction « white-space :
    pre », on force le maintient des retours de chariot là où ils sont, ce
    qui est très utile pour présenter du code informatique. L'instruction
    « white-space : nowrap » élimine toute utilisation des retours de
    chariot, alors que l'instruction« white-space : normal »
    correspond au comportement pas défaut.
</p>
<h3 class="recall">
 Des nouveautés en CSS 3
</h3>
<p>
 La nouvelles version du CSS, CSS 3, apporte de nombreuses améliorations. En
    particulier, elle ajoute plusieurs sélecteurs. Voici un tableau qui résume
    certains des sélecteurs les plus utilisés ainsi que le niveau CSS
    correspondant.
</p>
<div class="tableau style1">
 <table class="selectorsReview">
  <!--<thead>
     <tr>
       <th class="pattern">Sélecteur</th>
       <th class="meaning">Signification</th>
       <th class="origin">Version CSS</th></tr>
     </thead>
     <tbody>-->
  <tbody>
   <tr>
    <td class="pattern" colspan="1" rowspan="1">
     Sélecteur
    </td>
    <td class="meaning" colspan="1" rowspan="1">
     Signification
    </td>
    <td class="origin" colspan="1" rowspan="1">
     Niveau CSS
    </td>
   </tr>
   <tr>
    <td class="pattern" colspan="1" rowspan="1">
     *
    </td>
    <td class="meaning" colspan="1" rowspan="1">
     tout élément
    </td>
    <td class="origin" colspan="1" rowspan="1">
     2
    </td>
   </tr>
   <tr>
    <td class="pattern" colspan="1" rowspan="1">
     E
    </td>
    <td class="meaning" colspan="1" rowspan="1">
     un élément de nom E
    </td>
    <td class="origin" colspan="1" rowspan="1">
     1
    </td>
   </tr>
   <tr>
    <td class="pattern" colspan="1" rowspan="1">
     E[foo]
    </td>
    <td class="meaning" colspan="1" rowspan="1">
     un élément E ayant
                    un
                    attribut foo
    </td>
    <td class="origin" colspan="1" rowspan="1">
     2
    </td>
   </tr>
   <tr>
    <td class="pattern" colspan="1" rowspan="1">
     E[foo="bar"]
    </td>
    <td class="meaning" colspan="1" rowspan="1">
     un élément E ayant
                    un
                    attribut foo dont la valeur est « bar »
    </td>
    <td class="origin" colspan="1" rowspan="1">
     2
    </td>
   </tr>
   <tr>
    <td class="pattern" colspan="1" rowspan="1">
     E[foo~="bar"]
    </td>
    <td class="meaning" colspan="1" rowspan="1">
     un élément E ayant
                    un
                    attribut foo dont la valeur contient le mot
                    « bar »
                    séparé par des espaces
    </td>
    <td class="origin" colspan="1" rowspan="1">
     2
    </td>
   </tr>
   <tr>
    <td class="pattern" colspan="1" rowspan="1">
     E[foo^="bar"]
    </td>
    <td class="meaning" colspan="1" rowspan="1">
     un élément E ayant
                    un
                    attribut foo débute par le texte « bar »
    </td>
    <td class="origin" colspan="1" rowspan="1">
     3
    </td>
   </tr>
   <tr>
    <td class="pattern" colspan="1" rowspan="1">
     E[foo$="bar"]
    </td>
    <td class="meaning" colspan="1" rowspan="1">
     un élément E ayant
                    un
                    attribut foo se termine par le texte « bar »
    </td>
    <td class="origin" colspan="1" rowspan="1">
     3
    </td>
   </tr>
   <tr>
    <td class="pattern" colspan="1" rowspan="1">
     E[foo*="bar"]
    </td>
    <td class="meaning" colspan="1" rowspan="1">
     un élément E ayant
                    un
                    attribut foo dont la valeur contient le texte
                    « bar »
    </td>
    <td class="origin" colspan="1" rowspan="1">
     3
    </td>
   </tr>
   <tr>
    <td class="pattern" colspan="1" rowspan="1">
     E[foo|="bar"]
    </td>
    <td class="meaning" colspan="1" rowspan="1">
     un élément E ayant
                    un
                    attribut foo dont la valeur contient le mot
                    « bar »
                    séparé par des tirets
    </td>
    <td class="origin" colspan="1" rowspan="1">
     2
    </td>
   </tr>
   <tr>
    <td class="pattern" colspan="1" rowspan="1">
     E F
    </td>
    <td class="meaning" colspan="1" rowspan="1">
     un élément F contenu
                    dans un élément E
    </td>
    <td class="origin" colspan="1" rowspan="1">
     1
    </td>
   </tr>
   <tr>
    <td class="pattern" colspan="1" rowspan="1">
     E &gt; F
    </td>
    <td class="meaning" colspan="1" rowspan="1">
     un élément F contenu
                    directement dans un élément E
    </td>
    <td class="origin" colspan="1" rowspan="1">
     2
    </td>
   </tr>
   <tr>
    <td class="pattern" colspan="1" rowspan="1">
     E + F
    </td>
    <td class="meaning" colspan="1" rowspan="1">
     un élément F précédé
                    immédiatement par un élément-voisin E
    </td>
    <td class="origin" colspan="1" rowspan="1">
     2
    </td>
   </tr>
   <tr>
    <td class="pattern" colspan="1" rowspan="1">
     E ~ F
    </td>
    <td class="meaning" colspan="1" rowspan="1">
     un élément F précédé
                    par
                    un élément-voisin E
    </td>
    <td class="origin" colspan="1" rowspan="1">
     3
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 Avec CSS 3, il devient donc possible, par exemple, de sélectionner tous les
    hyperliens ayant une adresse (attribut « href ») débutant par
    « http » avec le
    sélecteur « a[href^="http"] », ce qui pourrait être utilisé pour
    indiquer
    visuellement les liens externes.
</p>
<p>
 CSS 3 ajoute aussi la possibilité d'entourer du texte comme dans cet exemple:
</p>
<pre style="white-space: pre-wrap"><span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">span</span><span style="color:#274796; "> </span><span style="color:#074726; ">style</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#274796; ">
    </span><span style="color:#bb7977; font-weight:bold; ">border</span><span style="color:#808030; ">:</span><span style="color:#274796; ">
    </span><span style="color:#008c00; ">2</span><span style="color:#006600; ">px</span><span style="color:#274796; ">
    </span><span style="color:#074726; ">solid</span><span style="color:#274796; "> </span><span style="color:#797997; ">blue</span><span style="color:#800080; ">;</span><span style="color:#274796; ">
        border-radius </span><span style="color:#808030; ">:</span><span style="color:#274796; "> </span><span style="color:#008c00; ">25</span><span style="color:#006600; ">px</span><span style="color:#800080; ">;</span><span style="color:#bb7977; font-weight:bold; ">padding</span><span style="color:#808030; ">:</span><span style="color:#008c00; ">2</span><span style="color:#006600; ">px</span><span style="color:#800080; ">;</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>Entoure-moi!<span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">span</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 <span style=" border: 2px solid blue; border-radius : 25px;padding:2px;">
  Entoure-moi!
 </span>
</p>
<p>
 Par le passé, il était nécessaire de créer une image pour obtenir un tel
    effet. Ilest beaucoup plus efficace d'utiliser une simple instruction CSS.
</p>
<p>
 On peut aussi transformer géométriquement le texte. Par exemple, on peut le
    tourner de 180 degré ou faire un effet miroir comme dans cet exemple:
</p>
<pre style="white-space:pre-wrap"><span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">p</span><span style="color:#274796; "> </span><span style="color:#074726; ">style</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#274796; ">transform</span><span style="color:#808030; ">:</span><span style="color:#274796; ">
        rotate(</span><span style="color:#008c00; ">180</span><span style="color:#006600; ">deg</span><span style="color:#274796; ">)</span><span style="color:#800080; ">;</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>On peut maintenant retourner le
    texte<span style="color:#008c00; ">.</span> N'est-ce pas superbement
    mignon?<span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">p</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">p</span><span style="color:#274796; "> </span><span style="color:#074726; ">style</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#274796; ">transform</span><span style="color:#808030; ">:</span><span style="color:#274796; ">
        scale(</span><span style="color:#808030; ">-</span><span style="color:#008c00; ">1</span><span style="color:#808030; ">,</span><span style="color:#274796; ">
    </span><span style="color:#008c00; ">1</span><span style="color:#274796; ">)</span><span style="color:#800080; ">;</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>On peut aussi faire un effet
    miroir<span style="color:#008c00; ">.</span><span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">p</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p style="transform: rotate(180deg);">
 On peut maintenant retourner le texte.
    N'est-ce pas superbement mignon?
</p>
<p style="transform: scale(-1, 1);">
 On peut aussi faire un effet miroir.
</p>
<p>
 Le CSS est maintenant très riche et nous nous contentons d'illustrer quelques
    possibilités..
</p>
<h3 class="recall">
 Optimisation des fichiers CSS
</h3>
<p>
 Il y a plusieurs façons d'écrire un même ensemble d'instructions.
    Par exemple, ce fichier CSS est trop long et difficile à comprendre :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 montant {
    color: red;
    font-weight: bold;
    background:white;
    font-style: normal;
    text-align: center;
    }
    nom {
    color: white;
    background:white;
    font-style: normal;
    text-align: left;
    }
    texte {
    color: black;
    text-align: center;
    font-style: normal;
    background:white;
    text-align: left;
    }
</p>
<p>
 On peut le réécrire dans un format plus concis et plus clair :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
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
    montant, nom, texte {
    background: white;
    font-style: normal;
    }
</p>
<p>
 Il existe de nombreux outils pour optimiser les fichiers CSS dont
 <a href="http://csstidy.sourceforge.net/" shape="rect">
  CSSTidy
 </a>
 qui est
 <a href="http://cdburnerxp.se/cssparse/css_optimiser.php" shape="rect">
  disponible en ligne
 </a>
 .
</p>
<h3 class="recall">
 En terminant
</h3>
<p>
 La syntaxe CSS est beaucoup plus riche que ce que nous venons de voir. Pour
    plus d'information, nous vous invitons
    à lire le document de référence
 <a href="http://developer.mozilla.org/en/docs/CSS" shape="rect">
  http://developer.mozilla.org/en/docs/CSS
 </a>.
</p>
.
<h3 class="recall">
 Livres de référence
</h3>
<ul>
 <li>
  David Sawyer McFarland,
  <a href="https://www.amazon.ca/CSS-Missing-David-Sawyer-McFarland/dp/1491918055/ref=dp_ob_image_bk" shape="rect">
   CSS: The Missing Manual
  </a>
  , O'Reilly Media, 2015, 718
        pages.
 </li>
</ul>
