---
title: "Format de document"
weight: 20
---

# Format de document

### Le SGML (*Standardized General Markup Language*)

En 1969, Charles Goldfarb, Edward Mosher et Raymond Lorie ont inventé le GML (*Generalized Markup Language*). Chercheurs chez IBM, ils voulaient faciliter l'échange d'informations entre les outils d'édition, de formatage et de recherche de documents. Le GML possédait déjà un concept de « type de documents » similaire aux documents DTD modernes. Chez IBM, le GML a été utilisé pour la production d'environ 90 % des documents électroniques.

En 1978, l'American National Standards Institute (ANSI) a travaillé sur un projet de langage de description de textes, basé sur le GML; le projet s'est terminé en 1985 par la normalisation du SGML. Le centre de recherche CERN a été l'une des premières institutions, outre IBM, à mettre au point des outils pour le SGML.

On dit souvent que le SGML est l'ancêtre du XML, dans la mesure où les créateurs du XML connaissaient le SGML et voulaient faire mieux. Le HTML est aussi fortement inspiré du SGML et existait au moment où le XML a été proposé. Il n'est donc pas surprenant que le XML et le HTML se ressemblent et puissent même se retrouver dans un seul format, le XHTML. La principale difficulté avec le SGML est sa complexité. On considère généralement que partout où le SGML était utilisé, il est maintenant préférable d'utiliser le XML. Comme les deux normes sont similaires, on migre souvent du SGML au XML. Quoiqu'il y ait de petits ennuis de conversion, le passage au XML permet de traiter les nouveaux documents avec les nombreux outils XML et de suivre la tendance.

Le SGML n'est pas très différent du XHTML. Par exemple, les paragraphes sont spécifiés avec des éléments « para » de la même façon qu'ils sont spécifiés avec des éléments « p » en XHTML.

### Le XML comme format de documents

Notons que le SGML, le HTML et le XML sont avant tout des formats de documents. On utilise maintenant le XML comme outil de programmation pour stocker et pour échanger des informations entre les logiciels; toutefois, l'objectif des créateurs du XML n'était que de créer un format de documents simple et pratique.

Pour les documents, un des avantages des nombreux formats basés sur le XML ou le SGML est qu'ils « décrivent l'information » au lieu de la présenter. Par la suite, il est facile de publier ou transformer un document XML en document PDF, HTML ou autre, selon les besoins. La séparation du contenu et de sa présentation est un facteur de productivité important parce qu'on simplifie la tâche de l'écriture, la ramenant au contenu seulement.

La séparation du contenu et de sa présentation existe, en partie, dans le XHTML. Par exemple, quand on ajoute un élément de paragraphe « p », on fait un choix qui s'appuie sur la logique du texte, non sur son apparence. Quant aux choix des polices, de l'espace entre les lignes, de l'espace entre les paragraphes ou des couleurs, ils ne sont généralement pas pris en compte par le XHTML. Mais tout n'est pas parfait; l'utilisation de balises pour appeler de l'italique, soit « i » en XHTML, ne nous assure pas une séparation complète entre la présentation et le contenu. Par exemple, il serait plus « logique » d'indiquer qu'un mot appartient à une langue étrangère et qu'il apparaisse dès lors en italique. Ainsi, au lieu d'écrire « La vie est &lt;i&gt;cool&lt;/i&gt;. », on aimerait écrire « La vie est &lt;anglais&gt;cool&lt;/anglais&gt;. » ou quelque chose de similaire. Le XHTML constitue donc un compromis entre une séparation complète du contenu et de sa présentation, et l'absence de séparation.

Comme nous le verrons dans le troisième module, la façon la plus naturelle de dicter la présentation d'un document XHTML est d'utiliser un ou plusieurs fichiers CSS. En plaçant les instructions de formatage dans des fichiers CSS, distincts des fichiers XHTML, on obtient une bonne séparation du contenu et de sa présentation. Cette approche a un grand avantage : si on doit changer l'apparence d'un site web, on peut se contenter d'éditer quelques fichiers CSS au lieu de modifier le contenu lui-même qui se trouve dans plusieurs fichiers XHTML. Par exemple, si on veut que le texte contenu dans les tableaux soit en caractères gras et que le texte des listes apparaisse en rouge, on utilisera les instructions CSS suivantes :

```css
td {font-weight:bold;}
li {color:red;}
```

Le XML est aussi très utile pour aider à l'autodescription des informations. Par exemple, si dans un texte vous mettez tous les termes techniques en italique, il est possible que vous puissiez plus tard faire une recherche dans votre document pour tous les termes techniques. Toutefois, quelqu'un qui ne connaîtrait pas votre convention pourrait avoir beaucoup de mal à faire la même recherche. Par contre, si vous utilisez un élément particulier pour les termes techniques comme les balises &lt;technique&gt;&lt;/technique&gt;, il devient beaucoup plus facile à quelqu'un d'autre de s'y retrouver dans votre document. On pourrait objecter que l'ajout de nombreuses balises alourdira le texte qui occupera alors trop de place sur le disque; l'expérience montre que la pérennité des documents doit presque toujours être privilégiée par rapport à l'utilisation de l'espace disque.

En outre, le XML est un format ouvert : on peut utiliser une multitude d'outils différents pour manipuler les documents XML; nous ne sommes pas limités à des produits spécifiques à une compagnie ou institution donnée. Le XML a donc l'avantage sur plusieurs autres formats quant à sa pérennité.

### Le format DocBook

Développé à partir de 1991, le format DocBook est un format de documents souvent utilisé pour la documentation technique. Le format DocBook est une application SGML qui devient une application XML. Il existe de nombreux outils permettant de transformer un document DocBook en document HTML ou PDF.

Le format DocBook possède de nombreux avantages pour la rédaction de documents techniques parce qu'il assure une grande séparation entre le contenu et sa présentation : il ne permet que des balises ayant trait à la logique du texte; par exemple, il n'est pas possible de spécifier une police de caractères en DocBook. L'auteur peut alors concentrer son attention sur le contenu du document, sans perdre de temps avec le formatage, qui est une étape ultérieure. La séparation du contenu et de sa présentation permet aussi que plusieurs personnes puissent travailler sur un même projet de documentation tout en assurant une présentation uniforme, parce que DocBook ne comprend pas d'instructions de formatage.

Malheureusement, comme les autres formats hérités du SGML, plusieurs documents en format DocBook sont du SGML et non du XML; on ne peut donc pas utiliser les outils XML pour tous les documents DocBook. Par contre, la situation est en train de changer; il devient plus facile de déterminer si un document est bel et bien un document XML : la déclaration XML placée au début d'un document DocBook nous l'indique.

Le format DocBook est fréquemment utilisé dans les projets de logiciels libres et « open source », ainsi que par certaines grandes sociétés, comme IBM. En général, les avantages du format DocBook sont plus visibles dans un contexte de travail d'équipe.

La création d'un document DocBook simple n'est pas très difficile. Tout d'abord, bien qu'elle puisse varier selon les versions, la déclaration de type de document d'un document DocBook ressemble à ceci :

```
<!DOCTYPE book PUBLIC "-//OASIS//DTD DocBook XML V4.4CR2//EN"
"http://www.oasis-open.org/docbook/xml/4.4CR2/docbookx.dtd">
```

Dans ce cas, on voit que le document DTD se trouve à l'adresse :

```
http://www.oasis-open.org/docbook/xml/4.4CR2/docbookx.dtd
```

Il faut cependant noter qu'il s'agit d'un document DTD qui dépend d'autres documents DTD et que la lecture d'un tel type de document DTD n'est pas très facile.

L'élément-racine d'un document DocBook peut varier, mais les deux principales structures sont « book » (livre) et « article »; notez que l'on peut commencer par l'une ou l'autre :

```xml
<?xml version="1.0" encoding='ISO-8859-1' standalone="no"?>
<!DOCTYPE book PUBLIC "-//OASIS//DTD DocBook XML V4.4CR2//EN"
 "http://www.oasis-open.org/docbook/xml/4.4CR2/docbookx.dtd">
<book>
(...)
</book>
```

```xml
<?xml version="1.0" encoding='ISO-8859-1' standalone="no"?>
<!DOCTYPE article PUBLIC "-//OASIS//DTD DocBook XML V4.4CR2//EN"
 "http://www.oasis-open.org/docbook/xml/4.4CR2/docbookx.dtd">
<article>
(...)
</article>
```

Ensuite, on doit ajouter un élément « bookinfo » ou « articleinfo », selon que le document est un livre ou un article. Le plus souvent, les éléments en question contiennent un élément « title » contenant le titre, ainsi qu'un élément « author » qui contiendra les éléments « firstname » (prénom) et « surname » (nom de famille). On peut aussi ajouter un élément « copyright » (droit d'auteur) qui contiendra un élément « year » (année) et un élément « holder » (titulaire). Voici quelques structures courantes de documents DocBook :

```xml
<?xml version="1.0" encoding='ISO-8859-1' standalone="no"?>
<!DOCTYPE book PUBLIC "-//OASIS//DTD DocBook XML V4.4CR2//EN"
 "http://www.oasis-open.org/docbook/xml/4.4CR2/docbookx.dtd">
<book>
<bookinfo>
 <title>Notre documentation</title>
 <author>
  <firstname>Alexis</firstname>
  <surname>Letrotteur</surname>
 </author>
 <copyright><year>2004</year><holder>Bell Canada</holder></copyright>
</bookinfo>
(...)
</book>
```

```xml
<?xml version="1.0" encoding='ISO-8859-1' standalone="no"?>
<!DOCTYPE article PUBLIC "-//OASIS//DTD DocBook XML V4.4CR2//EN"
 "http://www.oasis-open.org/docbook/xml/4.4CR2/docbookx.dtd">
<article>
<articleinfo>
 <title>Le sens de la vie</title>
 <author>
  <firstname>Gilles</firstname>
  <surname>Proulx</surname>
 </author>
 <copyright><year>2004</year>
 <holder>Gouvernement du Canada</holder>
 </copyright>
</articleinfo>
(...)
</article>
```

L'élément de base d'un document DocBook est l'élément « para » qui note la présence d'un paragraphe. Dans le cas d'un livre, on va le plus souvent faire suivre l'élément « bookinfo » d'éléments « chapter » (chapitre), qui eux-mêmes peuvent contenir des éléments « section », comme dans l'exemple qui suit :

```xml
<?xml version="1.0" encoding='ISO-8859-1' standalone="no"?>
<!DOCTYPE book PUBLIC "-//OASIS//DTD DocBook XML V4.4CR2//EN"
 "http://www.oasis-open.org/docbook/xml/4.4CR2/docbookx.dtd">
<book>
<bookinfo>
 <title>Notre documentation</title>
 <author>
  <firstname>Alexis</firstname>
  <surname>Letrotteur</surname>
 </author>
 <copyright><year>2004</year><holder>Bell Canada</holder></copyright>
</bookinfo>
<chapter>
 <title>Premier chapitre</title>
 <section>
 <title>Première section du premier chapitre</title>
 <para>Mettre ici le premier paragraphe de la première section.</para>
 </section>
</chapter>
</book>
```

Observe que tous les éléments « chapter », ainsi que tous les éléments « section » débutent par un élément « title » : c'est souvent suffisant. Il n'est pas permis de commencer un élément « section » ou « chapter » directement par un élément « para ». Par contre, on pourrait omettre d'avoir des sections dans nos chapitres, comme dans l'exemple qui suit :

```xml
<?xml version="1.0" encoding='ISO-8859-1' standalone="no"?>
<!DOCTYPE book PUBLIC "-//OASIS//DTD DocBook XML V4.4CR2//EN"
 "http://www.oasis-open.org/docbook/xml/4.4CR2/docbookx.dtd">
<book>
<bookinfo>
 <title>Notre documentation</title>
 <author>
  <firstname>Alexis</firstname>
  <surname>Letrotteur</surname>
 </author>
 <copyright><year>2004</year><holder>Bell Canada</holder></copyright>
</bookinfo>
<chapter>
 <title>Premier chapitre</title>
 <para>Mettre ici le premier paragraphe du premier chapitre.</para>
</chapter>
</book>
```

Dans le cas d'un simple article, nous n'utiliserons pas les éléments « chapitre » et il suffit, le plus souvent, d'utiliser des éléments « section », comme dans l'exemple qui suit :

```xml
<?xml version="1.0" encoding='ISO-8859-1' standalone="no"?>
<!DOCTYPE article PUBLIC "-//OASIS//DTD DocBook XML V4.4CR2//EN"
 "http://www.oasis-open.org/docbook/xml/4.4CR2/docbookx.dtd">
<article>
<articleinfo>
 <title>Notre documentation</title>
 <author>
  <firstname>Alexis</firstname>
  <surname>Letrotteur</surname>
  </author>
 <copyright><year>2004</year><holder>Bell Canada</holder></copyright>
</articleinfo>
<section>
 <title>Première section de l'article</title>
 <para>Mettre ici le premier paragraphe de la première section.</para>
</section>
<section>
 <title>Deuxième section de l'article</title>
 <para>Mettre ici le premier paragraphe de la seconde section.</para>
</section>
</article>
```

On pourrait aussi utiliser les éléments « sect1 », « sect2 », « sect3 » et ainsi de suite, pour obtenir les notions de *section*, *sous-section*, *sous-sous-section* et ainsi de suite.

Comme le format DocBook est destiné à la documentation technique, il existe plusieurs balises pour décrire le code informatique. L'élément le plus simple est l'élément « programlisting ». Ainsi, pour ajouter un petit programme Java dans un document DocBook, on utilisera l'élément suivant :

```java
<programlisting>
public static void main(String[] arg) {
System.out.println("Allo!");
}
</programlisting>
```

On peut également placer un élément « programlisting » dans les éléments « section », « chapter », « para », etc.

Tout comme en HTML, on peut créer des listes avec les éléments « itemizedlist » (liste non ordonnée, équivalent de « ul » en HTML) et « orderedlist » (liste ordonnée, équivalent de « ol » en HTML). Une liste est constituée d'éléments « listitem » qui ne peuvent contenir directement du texte : on met généralement des éléments « para » dans les éléments « listitem ». Par contre, les éléments « listitem » ne peuvent apparaître hors des éléments « itemizedlist » et « orderedlist ». En outre, on place les listes dans les éléments « chapter », « section », etc. Voici quelques exemples :

```xml
<itemizedlist>
 <listitem> 
 <para>un triangle</para>
 </listitem>
 <listitem>
 <para>un losange</para>
 </listitem>
</itemizedlist>
```

```xml
<orderedlist>
 <listitem> 
 <para>Premier élément (numéro 1)</para>
 </listitem>
 <listitem>
 <para>Second élément (numéro 2)</para>
 </listitem>
</orderedlist>
```

Le format DocBook est supporté par certains traitement de textes comme [OpenOffice](http://fr.openoffice.org/) qui est disponible gratuitement.

### L'ODF (*Open Document Format*)

Historiquement, les formats de bureautiques ont été propriétaires, que ce soit le format WordPerfect ou le format Microsoft Word. Pour une institution, cela pose le problème de la pérennité des documents : qu'est-ce qui se produit si la compagnie qui propose un format décide de ne plus supporter un ancien format, parce qu'elle fait faillite ou change sa stratégie commerciale ? Qu'est-ce qui se produit si elle décide d'augmenter le coût de ses produits ? L'*Open Document Format* (ODF) est une norme XML [adoptée en mai 2005](http://www.oasis-open.org/committees/tc_home.php?wg_abbrev=office) par OASIS et est devenu une norme ISO (ISO 26300.2006) le 30 novembre 2006. Le format ODF est un format XML que tout le monde peut utiliser librement. Nous allons voir différentes techniques dans ce cours qui permettent de manipuler des documents XML et elles s'appliquent au format ODF.

Le format ODF n'est pas très différent des nouveaux formats [Open XML](https://en.wikipedia.org/wiki/Office_Open_XML) utilisés par Microsoft Office, mais au lieu de n'être soutenu que par une seule compagnie, ODF provient d'une entente entre plusieurs grandes sociétés : Adobe Systems, IBM, Intel, Novell et Sun Microsystems. Dans les deux cas (ODF et Open XML), les fichiers XML sont mis dans une archive compressée et nous avons accès à la sémantique des balises XML. Le logiciel [OpenOffice](http://fr.openoffice.org/) utilise le format ODF et a les avantages d'être gratuit et disponible pour une variété de systèmes (Apple, Linux, Microsoft, etc.). Il est aussi possible de créer des documents ODF à partir de Microsoft Office 2007 à l'aide d'une composante logicielle supplémentaire ([Open XML Translator](http://sourceforge.net/projects/odf-converter)).