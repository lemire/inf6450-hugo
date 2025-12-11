---
title: "CSS"
weight: 40
---
# CSS

La norme CSS a d'abord été proposée par Håkon Lie du CERN en Suisse en 1994 (environ 4 ans après l'apparition de la première page web). Cette norme a été acceptée comme recommandation officielle du W3C deux ans plus tard, soit en 1996, et la seconde version (CSS 2.0) est devenue une recommandation du W3C l'année suivante, soit en 1997. Une troisième version (CSS 3) a été adoptée à compter de 2011. À l'origine, les instructions CSS étaient destinées uniquement à indiquer aux navigateurs comment présenter le HTML (couleurs, polices, etc.) ; on s'est vite rendu compte qu'on pouvait aussi l'appliquer au XML et on considère maintenant les CSS comme une technologie qui s'applique autant au HTML qu'au XML (et aussi, évidemment, au XHTML).

Nous avons vu que le XSLT permettait de transformer du XML en HTML pour l'affichage dans un navigateur. En général, le XSLT permet de transformer tout document XML en un autre format (HTML, XML ou autre).

Un fichier CSS est beaucoup plus limité dans la mesure où il ne transforme pas le document XML. Il permet seulement de spécifier comment le contenu du document XML sera affiché. Le fichier XSLT est un outil de transformation, alors que le fichier CSS est un outil de formatage. Un document CSS permet de rendre un document XML plus lisible. D'un autre côté, le fichier CSS permet de contrôler avec beaucoup de finesse la présentation du document XML, alors qu'il peut être difficile et fastidieux d'obtenir le même résultat en XSLT, sans utiliser les CSS. Les fichiers CSS tendent aussi à être plus simples que les fichiers XSLT ; il peut donc être plus facile de les modifier et de les garder à jour. Finalement, on peut utiliser à la fois des fichiers CSS et des fichiers XSLT, en combinant les avantages des deux (présentation et transformation).

## point de vue critique

CSS est un langage déclaratif relativement limité. Il n'est pas possible de définir des variables, des fonctions ou de faire de l'arithmétique en CSS. On peut, par contre, redéfinir à volonté des règles, ce qui peut rendre le comportement final difficile à comprendre pour un humain. Il n'est pas facile, en CSS, de détecter le navigateur utilisé alors que tous les navigateurs ne traitent pas les règles de la même façon.

### notions de base

Pour l'essentiel, le langage CSS prend la forme d'une succession d'affirmations de la forme *élément {propriété: valeur; autrepropriété: valeur;}*. Il s'agit d'une syntaxe très simple.

Supposons un document XML comme celui-ci :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<comptearecevoir>
  <facture>
    <personne>Jean Rochond</personne>
    <montant>10.10</montant>
    <raison>Achat d'ordinateur</raison>
  </facture>
  <facture>
    <personne>Madeleine Bédard</personne>
    <montant>20.10</montant>
    <raison>Achat d'un crayon</raison>
  </facture>
</comptearecevoir>
```

Certains navigateurs affichent le XML brut sans formatage, ce qui n'est pas très accessible. D'autres affichent le document sans les balises :

```
Jean Rochond
10.10
Achat d'ordinateur
Madeleine Bédard
20.10
Achat d'un crayon
```

Ce document XML est difficile à lire, même sans les balises, surtout si vous n'êtes pas un expert en XML. Sans le transformer, il est possible de l'afficher avec de la couleur ou de l'italique, comme ceci :

- Jean Rochond <span style="color:red">10.10</span>  
  <i>Achat d'ordinateur</i>
- Madeleine Bédard <span style="color:red">20.10</span>  
  <i>Achat d'un crayon</i>

Voilà qui est nettement plus lisible ! Nous pouvons obtenir ce résultat à l'aide du fichier CSS suivant :

```css
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
```

Pour vérifier que c'est bien le cas, il suffit de créer un fichier « chap12.css » avec le contenu CSS précédent et de modifier le fichier XML en y ajoutant une ligne pointant vers le fichier CSS (`<?xml-stylesheet type="text/css" href="chap12.css"?>`), comme ceci :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<?xml-stylesheet type="text/css" href="chap12.css"?>
<comptearecevoir>
  <facture>
    <personne>Jean Rochond</personne>
    <montant>10.10</montant>
    <raison>Achat d'ordinateur</raison>
  </facture>
  <facture>
    <personne>Madeleine Bédard</personne>
    <montant>20.10</montant>
    <raison>Achat d'un crayon</raison>
  </facture>
</comptearecevoir>
```

Si le fichier XML est dans le même répertoire que le fichier CSS, votre navigateur devrait vous présenter le document XML avec le montant en rouge et le commentaire (raison) en italique, comme nous l'avons présenté plus haut.

Notez que dans le laboratoire de cette semaine, vous pourrez expérimenter avec CSS au sein de votre navigateur sans devoir créer de fichiers.

Examinons maintenant les différentes instructions du fichier CSS.

L'instruction « `display: block;` » déclare que l'élément devrait former son propre paragraphe. L'instruction « `display: none;` » rend l'élément invisible.

Les instructions « `margin-bottom: 30pt`; » et « `margin-left: 1cm;` » définissent des marges en bas et à gauche de 30 points et de 1 cm respectivement.

L'instruction « `color: red;` » affirme que le contenu de l'élément devrait être écrit en rouge, alors que « `font-style: italic;` » nous dit que le texte de l'élément devrait être en italique. On pourrait aussi contrôler la couleur de fond avec une instruction comme « `background-color:red` ».

Dans l'éventualité où nous voulons choisir une couleur très précise, et non les couleurs courantes comme « red », « green », « blue », « yellow », « white », « black », etc., nous pouvons la spécifier selon sa composition avec les couleurs de base (« red », « green », « blue ») avec une instruction comme « `background-color:rgb(200,200,200);` », où chaque valeur numérique est entre 0 et 255 inclusivement.

### les unités de mesure

En CSS, on peut spécifier la taille d'un objet avec plusieurs unités de mesure, par exemple cm pour centimètre ou px pour pixel. Ainsi donc l'instruction « `width:1px` » spécifie une largeur de 1 pixel. On peut aussi utiliser des unités relatives comme « em », « rem » ou « % ». Une mesure de « 50 % » indique que l'objet devrait occuper la moitié de l'espace disponible. Une mesure de « 1em » correspond à la taille de la police de caractère dans l'élément courant alors que « 1rem » correspond à la taille de la police de caractère dans l'élément-racine du document. On peut aussi combiner les unités... par exemple, pour spécifier une dimension correspondant à tout l'espace disponible moins 80 pixels, on peut utiliser la valeur « `calc(100% - 80px)` ». Pour bien comprendre, l'idéal est de faire des expériences.

### contenu en ligne ou en bloc ?

Par défaut, les éléments s'affichent en ligne, un à la suite de l'autre. On peut contrôler comment s'affiche un élément avec la propriété « display » qui peut prendre plusieurs valeurs dont celles-ci :

- « `display: none` » : l'élément ne doit pas s'afficher. Par exemple, l'instruction « img{display: none;} » fait en sorte que les images ne s'affichent plus en HTML. Il est fréquent qu'avec du JavaScript, on cache et affiche tour à tour des éléments pour donner l'impression que la page est dynamique.
- « `display: inline` » : l'élément s'affiche à la suite du précédent comme s'il s'agissait d'un caractère.
- « `display: block` » : l'élément s'affiche dans un bloc distinct, comme un nouveau paragraphe, par exemple.
- « `display: list-item` » : l'élément s'affiche comme un élément d'une liste.
- « `display: flex` » ou « `display: inline-flex` » : les éléments contenus s'affichent selon un modèle flexible (voir https://css-tricks.com/snippets/css/a-guide-to-flexbox/).

Voici un exemple :

```css
p      { display: block }
strong { display: inline }
li     { display: list-item }
img    { display: none }
```

On peut aussi définir la propriété « float » d'un élément qui lui permet de sortir du flot normal des éléments et de se placer à gauche ou à droite. Par exemple, une image en XHTML s'affiche normalement comme un bloc. On peut forcer l'image à s'intégrer au paragraphe suivant avec l'instruction « float: right » ou « float: left ». On peut aussi utiliser la propriété « float » pour créer plusieurs colonnes de texte comme dans un journal. Je vous invite à faire différentes expériences pour mieux comprendre l'utilisation de cette instruction.

### centrer un élément

Bien qu'on puisse changer la justification du texte avec une instruction comme « text-align: center », centrer un élément requiert plutôt une manipulation des marges avec la valeur spéciale « auto », comme dans cet exemple :

```css
p {
  width: 5cm;
  margin-left: auto;
  margin-right: auto;
}
```

Il aurait été sans doute préférable d'avoir une instruction dédiée pour centrer les éléments comme il s'agit d'une opération courante.

### les commentaires

Tout comme en Java, on peut ajouter des commentaires à un fichier CSS qui sont systématiquement ignorés par la machine. Un bloc de commentaire débute par « /* » et se termine par « */ ».

```css
/* mon fichier css */
montant {
  color: red; /* la couleur rouge */
}
```

### sélectionner le premier caractère ou la première ligne

On peut sélectionner la première ligne d'un élément s'affichant en mode « block » et le premier caractère de tout élément avec les sélecteurs « :first-line » et « :first-letter » respectivement. Voici un exemple :

```css
p:first-line  {text-transform: uppercase}
p:first-letter {font-size: 200%; float: left;}
```

### ajouter du contenu avant et après un élément

Avec CSS, on peut demander qu'une certaine chaîne de caractères apparaisse avant ou après un élément. Par exemple, si on veut ajouter automatiquement des guillemets avant et après un élément, on peut procéder comme ceci :

```css
blockquote:before {content:"«";}
blockquote:after  {content:"»";}
```

Nous ne sommes pas limités au texte cependant. Il est possible, par exemple, d'ajouter automatiquement une image avant chaque élément comme ceci :

```css
p:before {content:url("monimage.png");}
```

### qu'est-ce qu'un pseudo-élément ?

Les instructions first-line, first-letter, before et after que nous venons de présenter sont les principaux exemples de pseudo-éléments.

### sélecteurs d'interaction

Certains sélecteurs n'agissent qu'en réponse aux comportements de l'utilisateur. Par exemple, le sélecteur « p:hover » sélectionne les éléments « p » qui sont survolés par le curseur de la souris. Il existe plusieurs sélecteurs d'interaction dont « :link » (lien non visité), « :visited » (lien visité), « :active » (l'utilisateur utilise un élément), « :focus » (l'élément est sélectionné par l'utilisateur). On peut aussi combiner les sélecteurs comme dans cet exemple : « a:hover:focus ». On appelle aussi ces sélecteurs de pseudo-classes.

### règles par défaut

Dans le cas du HTML ou du XHTML, les navigateurs utilisent une liste de règles par défaut. Ces règles vont varier d'un navigateur à l'autre, mais voici un exemple de règles utilisées par des navigateurs :

```css
html, div { display: block; }
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
b, strong { font-weight: bolder; }
i, cite, em, var, dfn { font-style: italic; }
u, ins { text-decoration: underline; }
s, strike, del { text-decoration: line-through; }
big  { font-size: larger; }
small { font-size: smaller; }
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
li { display: list-item; }
area, base, basefont, head, meta, script, style, title,
noembed, param { display: none; }
```

### l'astérisque

L'astérisque nous permet d'appliquer une règle à tous les éléments, comme dans cet exemple : « * {color:red;} ».

### sélection sur la base des attributs

Avec les CSS, en utilisant les crochets, nous pouvons sélectionner tous les éléments ayant un attribut donné. Par exemple, l'instruction « `*[monattribut] { color:red;}` » mettra en rouge tous les éléments ayant un attribut portant le nom « monattribut ». Nous pouvons aussi limiter la sélection à des éléments portant un nom donné comme dans « `maman[monattribut] { color:red;}` » où les éléments « maman » ayant un attribut « monattribut » seront en rouge. Finalement, nous pouvons de plus limiter la sélection à des attributs ayant une certaine valeur, comme dans « `maman[monattribut="papa"] { color:red;}` ».

Il arrive fréquemment qu'une valeur d'attribut contienne plusieurs mots, comme dans « `<amerique pays="États-Unis Canada" />` ». Pour sélectionner tous les éléments dont un attribut contient un mot particulier, on remplace « = » par « ~= » comme dans l'instruction « `*[pays~="Canada"] { color:red;}` » qui mettra en rouge tout élément dont l'attribut « pays » contient le mot « Canada ». Les mots doivent être séparés par des espaces. Dans l'éventualité où les mots sont séparés par des tirets, comme dans « `<amerique pays="Mexique-Canada" />` », on peut obtenir le même résultat avec « |= » comme dans « `*[pays|="Canada"] { color:red;}` ».

### les espaces de noms

Les espaces de noms ne sont pas supportés en CSS 1 ou CSS 2. Ainsi « `monelement { color:red;}` » met en rouge le contenu de tous les éléments monelement, peu importe leur espace de noms. Il est incorrect d'utiliser la syntaxe « `xhtml:monelement { color:red;}` ».

### sélection de la langue

On a vu qu'il est possible en XML de spécifier la langue dans laquelle est écrit un texte avec l'attribut «  `xml:lang` ». On pourrait penser que pour mettre le texte déclaré comme étant en anglais en rouge, il suffirait de l'instruction « `*[lang="fr"] { color:red;}` », mais que se passera-t-il si on a utilisé un code de région avec la langue comme « fr-CA » ? Une solution plus élégante consiste alors à utiliser la sélection sur la langue avec une instruction comme « `:lang(en) { color:red;}` ».

### sélection de plusieurs éléments

Supposons maintenant que nous voulions afficher en rouge tous les éléments « facture » et « maison ». Nous pouvons le faire avec deux instructions :

```css
facture { color:red;}
maison  { color:red;}
```

En pratique cependant, il est préférable d'utiliser la virgule pour grouper les éléments, comme ceci :

```css
facture, maison { color:red;}
```

Les deux formes sont exactement équivalentes.

### sélection sur la base de la relation entre les éléments

Supposons maintenant que nous ne voulions pas afficher tous les éléments « personne » en rouge, mais seulement les éléments « personne » contenus dans un élément « facture ». Nous obtiendrons ce résultat en plaçant les deux noms d'élément côte-à-côte (séparés par un espace). Ainsi, l'instruction « facture personne { color:red;} » affichera en rouge tous les éléments « personne » contenus dans un élément « facture », comme dans l'exemple qui suit ou dans ce deuxième exemple.

Nous pourrions vouloir que seuls les éléments immédiatement contenus dans l'élément « facture », comme dans le premier exemple, soient en rouge, et non pas ceux qui sont contenus dans des éléments eux-mêmes dans un élément « facture » (deuxième exemple). Nous pouvons obtenir ce résultat avec l'instruction « facture > personne { color:red;} ».

En somme, la règle « `a b { color:red;}` » s'applique à l'élément « b », si l'élément « b » est contenu dans un élément « a » comme dans « `<a><b></b></a>` » ou « `<a><c><b></b></c></a>` ».

Par contre, la règle « `a > b { color:red;}` » s'applique à l'élément « b », si et seulement si l'élément « b » est immédiatement contenu dans un élément « a », comme dans « `<a><b></b></a>` ». Elle ne s'applique pas si « b » est contenu dans un élément lui-même contenu dans « a », comme dans « `<a><c><b></b></c></a>` ».

Supposons maintenant, dans l'exemple suivant, que nous voulions indenter le premier paragraphe (élément « p ») suivant le titre (élément « titre ») :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<titre>Mon histoire</titre>
<p>C'est triste.</p>
<p>Oui, c'est triste.</p>
```

Ce résultat s'obtient avec l'instruction « titre + p { text-indent: 0cm;} ». La syntaxe « a + b { ... } » s'applique à l'élément « b » quand les éléments « a » et « b » sont contenus dans le même élément, et que « b » est immédiatement après « a ». Notez que la règle « a + b { ... } » s'applique à « b », mais ne s'applique pas à « a ».

Supposons que nous désirions indenter le premier paragraphe (élément « p ») dans l'élément « section » :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<section titre="Mon histoire" >
  <p>C'est triste.</p>
  <p>Oui, c'est triste.</p>
</section>
```

On peut obtenir ce résultat avec le sélecteur « section > p:first-child { ... } » où « :first-child » signifie que seuls les éléments « p » étant le premier élément au sein d'un autre élément sont sélectionnés. En fait, dans cet exemple particulier, on obtiendrait aussi le résultat voulu avec le sélecteur « p:first-child { ... } ».

Par ailleurs, nous pouvons combiner les espaces, les « + », les virgules et les « > » dans un même sélecteur. Par exemple, « a + b, c { ... } » s'applique aux éléments « c » et aux éléments « b » qui suivent immédiatement un élément « a ».

### sélection d'élément par valeur ID

Si vous avez des éléments ayant des attributs de type « ID », on sait alors que leur valeur est un nom XML et qu'elle ne doit être utilisée qu'une seule fois. C'est le cas des attributs de la forme « id="xxx" » que l'on peut utiliser avec pratiquement tous les éléments XHTML. On peut sélectionner un élément basé sur la valeur d'un tel attribut en utilisant le symbole « # » :

```css
#xxx {
  color: red;
}
```

Dans ce cas, le contenu d'un élément comme une balise XHTML « `<p id='xxx'>test</p>` » s'affichera en rouge. On peut combiner les sélecteurs « # » avec les autres règles que nous avons traitées ; par exemple, le code suivant ne mettra en rouge que les éléments « i » contenus dans un élément ayant un attribut de type « ID » avec pour valeur « xxx » :

```css
#xxx i{
  color: red;
}
```