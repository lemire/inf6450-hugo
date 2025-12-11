---
title: "Glossaire"
weight: 170
---

# Glossaire

**Appel d’entité**

Un appel d’entité est une suite de caractères qui commence par une esperluette (`&`) et se termine par un point-virgule (`;`). Les entités courantes :

| Entité | Résultat |
|---|---:|
| `&amp;lt;` | `<` |
| `&amp;amp;` | `&` |
| `&amp;gt;` | `>` |
| `&amp;quot;` | `"` |
| `&amp;apos;` | `’` |


**Attribut**

Un attribut est un nom XML qui suit les mêmes règles que les noms d’éléments. Il est immédiatement suivi d’un signe `=` et d’une valeur entre guillemets. Exemple : `<lavie age="5">` a l’attribut `age="5"`. Une balise peut avoir plusieurs attributs, mais leurs noms doivent être distincts.

**Balise**

Une balise commence par `<` et se termine par `>`. Il existe : balises ouvrantes (`<tag>`), fermantes (`</tag>`) et vides (`<tag/>`). Les déclarations `<!DOCTYPE>`, les instructions `<?xml?>`, les commentaires `<!-- -->` et les sections `<![CDATA[ ]]>` ne sont pas des balises d’élément.

**Bien formé**

Un document XML est bien formé s’il respecte la grammaire XML (p. ex. éléments correctement imbriqués, attributs bien formés). Tout parseur XML générique peut lire un document bien formé.

**Commentaire**

Commence par `<!--` et se termine par `-->`. On ne peut pas avoir deux tirets consécutifs `--` à l’intérieur d’un commentaire.

**CSS** — Cascading Style Sheets.

**Déclaration de type de document (DOCTYPE)**

Une déclaration DOCTYPE a la forme `<!DOCTYPE racine SYSTEM "URL">`. Elle indique le nom de l’élément racine attendu et (optionnellement) l’emplacement du DTD.

---

## Définitions et mots-clés utiles

- **CDATA** : type d’attribut indiquant que la valeur est du texte.
- **#PCDATA** : contenu textuel (parsed character data).
- **REQUIRED** : attribut obligatoire.
- **IMPLIED** : attribut optionnel.
- **FIXED** : attribut avec valeur fixe.
- **<!ATTLIST nomElement nomAttribut ...>** : déclaration d’attributs pour un élément.
- **<!ENTITY nomEntite "valeur">** : définit une entité nommée.
- **<!ENTITY % nomEntite "valeur">** : définit une entité paramètre (locale à la DTD).

> Remarque : j’ai retiré les sauts de ligne HTML et nettoyé la mise en forme pour faciliter la lecture et l’édition. Si vous voulez que je convertisse le reste du contenu en sections séparées (ex. listes alphabétiques, index), je peux automatiser cela.
 
## Formats de données populaires

### YAML

`YAML` (YAML Ain't Markup Language) est un format de sérialisation de données lisible par l'humain, souvent utilisé pour les fichiers de configuration. Il s'appuie sur l'indentation pour représenter la structure.

Exemple :

```yaml
person:
   name: "Alice"
   age: 30
   tags:
      - xml
      - yaml
```

YAML est pratique pour écrire des structures arborescentes sans beaucoup de ponctuation. Attention à l'indentation (espaces, pas de tabulations) et au typage implicite (ex. `on`, `yes`, `no`, `true`, `false` peuvent être interprétés).

### JSON

`JSON` (JavaScript Object Notation) est un format léger d'échange de données, très répandu pour les API et la configuration. Il est strict sur la syntaxe (guillemets, virgules, crochets).

Exemple :

```json
{
   "person": {
      "name": "Alice",
      "age": 30,
      "tags": ["xml", "json"]
   }
}
```

JSON est facile à parser et largement supporté par les langages. Quand on convertit entre XML, JSON et YAML, il faut décider comment représenter les attributs, les éléments vides et l'ordre des nœuds.

 <strong>
   Déclaration XML :
 </strong>
 La déclaration XML
 <br class="autobr"/>
 ressemble à s’y méprendre à une instruction de traitement et
 <br class="autobr"/>
 prend la forme &lt; ?xml ... ?&gt;. Le contenu d’une
    déclaration
 <br class="autobr"/>
 XML comporte généralement au maximum trois
 <em>
  attributs
 </em>
 :
 <br class="autobr"/>
 version="...", encoding="..." et standalone="...". La version du
 <br class="autobr"/>
 XML la plus utilisée est la 1.0 ; bien que la version 1.1 existe,
 <br class="autobr"/>
 elle est fort peu utilisée. On utilisera souvent une déclaration
 <br class="autobr"/>
 XML avec « encoding="ISO-8859-1" » pour pouvoir utiliser les
 <br class="autobr"/>
 accents dans le document ; par défaut, on ne peut pas utiliser les
 <br class="autobr"/>
 accents dans un document XML, sans des outils supportant les normes
 <br class="autobr"/>
 UTF-8/UTF-16. L’attribut « standalone » prend les
 <br class="autobr"/>
 valeurs
 <i>
  yes
 </i>
 ou
 <i>
  no
 </i>
 , selon que l’on veut que la DTD externe soit
    lue
 <br class="autobr"/>
 ou pas. La déclaration XML
 <br class="autobr"/>
 doit obligatoirement être au tout début du document ou être
 <br class="autobr"/>
 carrément absente : même un espace avant n’est pas permis.
</p>
<p>
 <strong>
  DocBook :
 </strong>
 C’est un format de
 <br class="autobr"/>
 document souvent utilisé pour la documentation
 <br class="autobr"/>
 technique.
</p>
<p>
 <strong>
  DOM (
  <i>
   Document Object Model
  </i>
  ) :
 </strong>
 Le terme
    « DOM »
 <br class="autobr"/>
 a deux significations : un ensemble d’API utilisant un modèle en arbre
    ou un
 <br class="autobr"/>
 certain modèle en arbre.
</p>
<p>
 <strong>
  DTD (
  <i>
   Définition de Type Document
  </i>
  ) :
 </strong>
 <br class="autobr"/>
 Une DTD permet de définir un type de document XML en spécifiant
 <br class="autobr"/>
 des contraintes sur les éléments, les attributs et leur contenu.
 <br class="autobr"/>
 Un document XML qui satisfait ces contraintes et qui est bien formé est dit
    valable.
</p>
<p>
 <strong>
  Élément :
 </strong>
 Un élément est l’ensemble du texte borné par
    deux
 <br class="autobr"/>
 balises ayant le même nom XML, comme &lt;lavie&gt; et &lt;/lavie&gt;.
 <br class="autobr"/>
 On dit que l’élément &lt;lavie&gt;&lt;/lavie&gt; a le nom
 <br class="autobr"/>
 XML « lavie ». L’élément hérite des attributs de sa balise de
 <br class="autobr"/>
 départ : l’élément &lt;lavie age="5"&gt;&lt;/lavie&gt; possède
 <br class="autobr"/>
 l’attribut « age="5" ». Il est à noter que la casse est
    significative
 <br class="autobr"/>
 en XML : les balises &lt; A &gt; et &lt; a &gt; n’ont pas le même nom
    XML.
 <br class="autobr"/>
 Lorsque l’élément est vide, c’est-à-dire sans contenu, on
 <br class="autobr"/>
 peut remplacer &lt;lavie&gt;&lt;/lavie&gt; par &lt;lavie /&gt;,
 <br class="autobr"/>
 pour être plus bref. Par ailleurs, un élément peut contenir d’autres
 <br class="autobr"/>
 éléments, comme dans
 <br class="autobr"/>
 &lt;lavie&gt;&lt;a&gt;&lt;/a&gt;&lt;/lavie&gt;, ou du texte ou
 <br class="autobr"/>
 du texte et des éléments, comme
 <br class="autobr"/>
 &lt;lavie&gt;fd&lt;a&gt;fsd&lt;/a&gt;fd&lt;/lavie&gt;. Si un
 <br class="autobr"/>
 élément contient l’élément de début ou de fin d’un élément, alors
 <br class="autobr"/>
 il doit aussi contenir l’autre. Ainsi, un élément peut être
 <br class="autobr"/>
 contenu par un autre ou non, mais deux éléments ne peuvent se
 <br class="autobr"/>
 <em>
  chevaucher
 </em>
 , comme &lt;b&gt;&lt;a&gt;&lt;/b&gt;&lt;/a&gt;,
 <br class="autobr"/>
 qui est du XML mal formé.
</p>
<p>
 <strong>
  Élément-racine :
 </strong>
 Tout document XML bien formé doit
    avoir un
 <br class="autobr"/>
 élément-racine, et un seul. Tous les autres
 <br class="autobr"/>
 éléments doivent être contenus dans cet
 <br class="autobr"/>
 élément-racine.
</p>
<p>
 <strong>
  Espace de noms :
 </strong>
 Les espaces de noms
 <br class="autobr"/>
 permettent d’utiliser plusieurs vocabulaires XML en même
 <br class="autobr"/>
 temps.
</p>
<p>
 <strong>
  Extensible :
 </strong>
 Voir
 <strong>
  <i>
   Métalangage
  </i>
  .
 </strong>
</p>
<p>
 <strong>
  Graphe :
 </strong>
 Un graphe est un ensemble de nœuds liés par
    des
 <br class="autobr"/>
 relations d’un nœud à un autre.
</p>
<p>
 <strong>
  Graphe dirigé :
 </strong>
 Un graphe est dirigé
 <br class="autobr"/>
 si les relations sont à sens unique.
</p>
<p>
 <strong>
  Graphe annoté :
 </strong>
 Un graphe est annoté
 <br class="autobr"/>
 si les relations entre deux nœuds peuvent être de
 <br class="autobr"/>
 différentes natures.
</p>
<p>
 <strong>
  HTML (
  <i>
   HyperText Markup
   <br class="autobr"/>
   Language
  </i>
  ) :
 </strong>
 Le HTML est un
 <br class="autobr"/>
 langage à base de balises. La majorité des documents
 <br class="autobr"/>
 sur le web sont écrits en HTML.
</p>
<p>
 <strong>
  Instruction de traitement :
 </strong>
 <br class="autobr"/>
 L’instruction de traitement ne fait rien en
 <br class="autobr"/>
 soit, mais peut indiquer aux programmes comment obtenir un
 <br class="autobr"/>
 certain résultat. Une instruction de traitement débute par
    « &lt; ? »
 <br class="autobr"/>
 et se termine par « ?&gt; » ; immédiatement après le
    « &lt; ? », un nom XML
 <br class="autobr"/>
 valable doit apparaître et tous les noms XML valables sont
 <br class="autobr"/>
 autorisés à l’exception de xml, Xml, XMl, XML, XmL, xMl, xML et
 <br class="autobr"/>
 xmL. Ainsi n’importe quel autre texte peut être utilisé, mais il faut
 <br class="autobr"/>
 faire des appels d’entités pour « &lt; » et « &amp; »,
    comme pour n’importe
 <br class="autobr"/>
 quel contenu textuel XML.
</p>
<p>
 <strong>
  Métalangage :
 </strong>
 Le XML est un « métalangage »
    permettant d’échanger
 <br class="autobr"/>
 de l’information, principalement sur le web. On dit que c’est un
 <br class="autobr"/>
 « métalangage » parce qu’il permet de créer de
 <br class="autobr"/>
 nouveaux
 <em>
  langages
 </em>
 pour l’échange d’informations, mais
 <br class="autobr"/>
 qu’il ne constitue pas un langage en soi. On dit donc que le
 <br class="autobr"/>
 XML est « extensible » (peut être étendu) et que c’est un
 <br class="autobr"/>
 métalangage : les deux affirmations ont le même sens et notent la
 <br class="autobr"/>
 capacité du XML à s’adapter à des besoins différents.
</p>
<p>
 <strong>
  Nom XML :
 </strong>
 Le nom XML d’une balise
 <br class="autobr"/>
 est le texte suivant le symbole « &lt; » ou « &lt;/ »
    pour une balise de
 <br class="autobr"/>
 fin ; il peut contenir n’importe quelle lettre (a, b,...) ou
 <br class="autobr"/>
 chiffre (0,1,2,...) et les signes de ponctuation suivants : la barre de
    soulignement ( _ ),
 <br class="autobr"/>
 le trait d’union ( - ) et le point ( . ) ; il ne peut contenir ni les
    autres signes de ponctuation
 <br class="autobr"/>
 ni un espace. En outre, un nom XML ne peut pas commencer par un nombre, un
    trait d’union
 <br class="autobr"/>
 ou un point. Par exemple, le nom XML de la balise
 <br class="autobr"/>
 &lt;lavie&gt; est « lavie », alors que la balise &lt;7lavie&gt;
    ne
 <br class="autobr"/>
 serait pas autorisée.
</p>
<p>
 <strong>
  RDF (
  <em>
   Resource Description
   <br class="autobr"/>
   Framework
  </em>
  ) :
 </strong>
 Le RDF est un langage pour les
    métadonnées sur le web,
 <br class="autobr"/>
 c’est-à-dire un langage pour énoncer ce que l’on sait
 <br class="autobr"/>
 sur quelque chose ou quelqu’un.
</p>
<p>
 <strong>
  SGML :
 </strong>
 <i>
  Standard Generalized Markup Language
 </i>
 .
</p>
<p>
 <strong>
  Syntaxe :
 </strong>
 La syntaxe XML est la
 <br class="autobr"/>
 manière d’écrire les informations dans un document
 <br class="autobr"/>
 XML. Les notions importantes de la
 <br class="autobr"/>
 syntaxe de base du XML sont la
 <i>
  balise
 </i>
 , l’
 <i>
  élément
 </i>
 ,
 <br class="autobr"/>
 l’
 <i>
  élément-racine
 </i>
 et l’
 <i>
  attribut
 </i>
 .
</p>
<p>
 <strong>
  URI :
 </strong>
 C’est une adresse Internet
 <br class="autobr"/>
 fictive. L’URI agit un peu comme le
 <br class="autobr"/>
 numéro d’assurance sociale des vocabulaires XML.
</p>
<p>
 <strong>
  Valable :
 </strong>
 : Un document est valable s’il répond à
    certains critères
 <br class="autobr"/>
 de base de l’application XML. Un document XML qui est bien formé, qui en
    plus
 <br class="autobr"/>
 satisfait aux contraintes dictant quels éléments et attributs
 <br class="autobr"/>
 peuvent être utilisés, et dans quel ordre et avec quel contenu,
 <br class="autobr"/>
 est dit valable.
</p>
<p>
 <strong>
  Vocabulaire XML :
 </strong>
 <br class="autobr"/>
 Un « vocabulaire XML » est un ensemble de noms de balises et
 <br class="autobr"/>
 d’attributs ayant une signification donnée. Un vocabulaire XML
 <br class="autobr"/>
 peut être associé à un document DTD.
</p>
<p>
 <strong>
  XHTML :
 </strong>
 Le XHTML est un format
 <br class="autobr"/>
 hybride : il tient à la fois du HTML et du XML.
</p>
<p>
 <strong>
  XML :
 </strong>
 <i>
  eXtensible MarkupLanguage
 </i>
 .
</p>
<p>
 <strong>
  XSL :
 </strong>
 <i>
  eXtensible Stylesheet
  <br class="autobr"/>
  Language
 </i>
 .
</p>
<p>
 <strong>
  XSLT :
 </strong>
 <i>
  XSL
  <br class="autobr"/>
  Transformations
 </i>
 .
</p>
<p>
 <strong>
  XSL-FO :
 </strong>
 <i>
  eXtensible Stylesheet Language
  <br class="autobr"/>
  Formatting Objects
 </i>
 .
</p>
