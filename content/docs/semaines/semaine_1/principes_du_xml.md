---
title: "Principes du XML"
weight: 60
---

# Principes du XML

## Quelques principes et notions importantes du XML

Rappelons qu'une **balise** est un segment de texte commençant par < et se terminant par >. Par exemple, <lavie> est une balise qui marque le début de l'élément *lavie*. Une balise commençant par </, comme </lavie>, est une balise de fin; dans cet exemple, elle termine l'élément *lavie*.

Le **nom XML** de la balise est le texte suivant le symbole < (ou </ pour une balise de fin) et pouvant contenir n'importe quelle lettre ou chiffre (a, b,... 0, 1, 2,...) ou les quatre symboles de ponctuation, soit la marque de soulignement ( _ ), le trait d'union ( - ), les deux-points (:) ou le point (.); un nom XML ne peut contenir d'autres caractères spéciaux, ni un espace". En outre, il ne peut pas commencer par un chiffre, un trait d'union ou un point. Par exemple, le nom XML de la balise <lavie> est « lavie », alors que la balise <7lavie> ne serait pas autorisée. On réserve les noms débutant par xml, Xml, xMl, xmL, XMl, xML,Xml et XML pour les spécifications XML. Ainsi, la balise <xmldanslavie> est à éviter.

Pour les balises de début, aussi dites d'ouverture, on peut ajouter un **attribut** au nom XML de la balise. Un attribut porte un nom XML qui doit respecter les mêmes règles que les noms XML des balises; il est suivi du symbole « = » et d'une valeur placée entre guillemets ou apostrophes. Par exemple, la balise <lavie age="5"> indique que l'élément *lavie* a un attribut (age="5") qui a comme nom XML « age » et comme valeur « 5 ». Une balise peut avoir plusieurs attributs, comme <lavie age="5" sexe="M">, mais ils doivent tous porter des noms XML différents : <lavie age="5" age="7"> n'est pas autorisée.

Par convention, on réserve l'attribut « xml:lang » à la spécification de la langue dans laquelle le texte est écrit. Cette spécification est optionnelle et assez rarement utilisée. Si on veut indiquer que le contenu d'un élément est en français, on fera comme dans cet exemple : « <explication xml:lang="fr">J'avais besoin d'une voiture.</explication> ». On peut ajouter au code de la langue, un code de région comme dans « fr-CA » ou « en-US ». Le code de la langue et le code de la région doivent être séparés par un tiret. Les codes de langue ou de région qui peuvent être utilisées sont disponibles à l'URL [http://www.iana.org/assignments/language-subtag-registry](http://www.iana.org/assignments/language-subtag-registry).

Un **élément** est l'ensemble du texte borné par deux balises ayant le même nom XML, comme <lavie> et </lavie>. On dit que l'élément <lavie></lavie> a pour nom XML « lavie ». L'élément hérite des attributs de sa balise de départ : l'élément <lavie age="5"></lavie> a l'attribut « age="5" ». Il est à noter que la casse est significative en XML : les balises <A> et <a> n'ont pas le même nom XML. Dans le cas particulier où l'élément est vide (sans contenu), on peut remplacer <lavie></lavie> par <lavie/> pour abréger. Un élément peut contenir d'autres éléments, comme dans <lavie><a></a></lavie>, ou du texte, ou du texte et des éléments comme

```xml
<lavie>fd<a>fsd</a>fd</lavie>.
```

Si un élément contient d'autres éléments, il doit aussi contenir, entre ses balises de début et de fin, les balises de début et de fin de chaque élément. Notez, de plus, que deux éléments ne peuvent se *chevaucher*, comme <b><a></b></a>; avant de passer à un autre élément, il faut terminer le premier avec sa balise de fin. L'exemple précédent est du XML mal formé!

Pour bien comprendre, illustrons notre propos par un exemple. Un document XML prend la forme suivante :

```xml
<racine>
 <element1>http://www.google.com</element1>
 <element2>Un moteur de recherche</element2>
 </racine>
```

Dans ce document, il y a **trois éléments**. Tout d'abord, il y a **l'élément-racine** qui comprend tout ce qui est entre les balises <racine> et </racine>. La première balise marque le début de l'élément-racine. Tout document XML bien formé doit avoir un élément-racine et un seul élément-racine. Tous les autres éléments doivent être contenus dans cet élément-racine. Dans notre exemple, cet élément a deux sous-éléments :

```xml
<element1>http://www.google.com</element1>
```

et

```xml
<element2>Un moteur de recherche</element2>
```

On peut ajouter un attribut à un des éléments de la façon suivante :

```xml
<racine date="aujourd'hui">
 <element1>http://www.google.com</element1>
 <element2>Un moteur de recherche</element2>
 </racine>
```

Le texte *date="aujourd'hui"* est un attribut de l'élément-racine avec pour nom « date » et comme valeur d'attribut « aujourd'hui ».

Tout le texte qui ne se trouve pas dans une balise, mais qui se trouve dans l'élément-racine se décompose en nœuds de texte. Par exemple, le document suivant contient un élément contenant un nœud de texte.

```xml
<racine>mon texte</racine>
```

## Points importants dans la syntaxe de base

Un document XML ne doit avoir qu'un et un seul élément appelé « élément-racine », qui doit contenir tous les autres éléments.

Il faut correctement ouvrir et fermer les éléments en séquence, ainsi <a><b></a></b> n'a aucun sens en XML, il faut plutôt écrire <a><b></b></a> ou alors <a></a><b></b>.

Les éléments peuvent eux aussi avoir des attributs, par exemple <a att="test"></a>, mais il faut obligatoirement mettre la valeur de l'attribut entre guillemets (") ou apostrophes (').

## Dans l'ordre ou dans le désordre

Dans un document XML, l'ordre dans lequel les éléments sont présentés importe. Par exemple, les deux documents XML suivants ne sont pas équivalents.

```xml
<racine>
 <element1>http://www.google.com</element1>
 <element2>Un moteur de recherche</element2>
 </racine>
```

```xml
<racine>
 <element2>Un moteur de recherche</element2>
 <element1>http://www.google.com</element1>
 </racine>
```

Par contre, l'ordre dans lequel les attributs sont présentés est sans importance. Les deux documents XML suivants sont donc équivalents.

```xml
<racine attr1="test" attr2="retest"></racine>
```

```xml
<racine attr2="retest" attr1="test"></racine>
```

## Appels d'entités

Un élément peut contenir du texte, mais ne peut contenir le symbole <, comme dans l'exemple <a><</a>, parce que cela mène à de la confusion. On ne peut non plus y trouver le symbole & ou la séquence « ]]&gt; ». Que faire alors s'il faut utiliser le caractère < dans un texte mathématique, par exemple? Il faut utiliser un **appel d'entité**. Un appel d'entité est un bout de texte qui commence par une esperluette ( &) et se termine par un point-virgule ( ; ). Nous verrons plus tard que nous pouvons définir nos propres appels d'entités; les appels d'entités suivants font partie de la définition du XML :

| appel d'entité | résultat |
|---------------|----------|
| &lt; | < |
| &amp; | & |
| &gt; | > |
| &quot; | " |
| &apos; | ' |

Ainsi, si le nom de votre compagnie est John&Smith, vous ne devrez pas utiliser un élément comme ceci <nom>John&Smith</nom>; il vous faudra plutôt utiliser

```xml
<nom>John&amp;Smith</nom>.
```

Le texte « ]]&gt; » s'écrit « ]]&gt; ».

On utilise aussi les appels d'entités pour noter les valeurs des attributs. Supposons que la valeur d'un attribut est une apostrophe suivi d'un guillemet ('"). Les deux choix possibles <nom att="'""&gt; et <nom att=''"'&gt; ne sont pas valables. Dans ce cas, il faudra écrire <nom att="'&quot;"&gt;, <nom att='&apos;"'&gt;, <nom att="&apos;&quot;"&gt; ou <nom att='&apos;&quot;'&gt;.

Prenez le temps de mémoriser ces appels d'entités et retenez bien dans quel cas on peut être obligé de les utiliser.

Il arrive parfois qu'il soit trop lourd d'utiliser des appels d'entités, et on peut alors utiliser un segment « CDATA ». Un tel segment débute par « <![CDATA[ » et se termine par « ]]&gt; ». Tout le texte au sein du segment est rendu verbatim. Ainsi, le texte « <![CDATA[<monelement />]]&gt; » est équivalent à « <monelement /> ».

## Les commentaires

Dans un document XML, on peut ajouter un commentaire qui est normalement destiné à être lu par un humain. Par exemple, dans un fichier de configuration XML, les commentaires pourraient être utilisés pour expliquer la signification des différents éléments pour qu'un humain puisse faire des modifications au besoin.

Un commentaire commence par <!-- et se termine par --> et ne doit pas contenir deux tirets de suite (--) entre ces deux bornes, il ne doit pas se terminer par un tiret, mais peut contenir n'importe quel autre texte. Un commentaire peut apparaître avant ou après l'élément-racine, dans un élément, entre deux éléments, etc. Cependant, un commentaire ne peut pas apparaître au sein d'une balise, comme <a <!--ceci est la balise a-->&gt;. C'est du XML mal formé!

## Les instructions de traitement

En pratique, il serait parfois utile d'appeler des fonctions externes (ou programmes) à partir du XML. Par exemple, vous pourriez avoir un programme « cout » qui donne le prix d'un produit à partir de son numéro de série : pourquoi ne pas appeler ce programme directement du XML?

**Le XML ne permet pas de le faire : le XML n'est qu'un métalangage pour produire des documents.**

Par contre, en XML, on peut utiliser des instructions de traitement. L'instruction de traitement ne fait rien en soi, mais peut indiquer à vos programmes comment trouver un certain résultat. L'exemple suivant décrit un produit portant le numéro de série 423890 et dont le prix pourrait être déterminé par une application appelée « cout ».

```xml
<?cout 423890?>
```

La syntaxe d'une telle instruction de traitement est simple. L'instruction débute par <? et se termine par ?&gt;; immédiatement après <?, un nom XML valable doit apparaître (tous les noms XML valables sont autorisés à l'exception de xml, Xml, XMl, XML, XmL, xMl, xML et xmL). Rappelons que, comme pour n'importe quel contenu textuel XML, il faut faire des appels d'entités pour < et &amp;. Une instruction de traitement n'est pas une balise ou un élément.

Notez que le langage informatique *PHP* utilise les instructions de traitement avec comme nom « php ». Voyons l'exemple suivant :

```xml
<?php echo "Hello World"; ?>
```

Tout comme les commentaires, on peut mettre les instructions de traitement partout dans un document XML, sauf à l'intérieur d'une balise.

## Jeux de caractères

Historiquement, on a longtemps représenté les caractères en utilisant des octets (8 bits). Aux États-Unis, on utilisait la norme ASCII qui utilisait les sept premiers bits de chaque octet. Avec le temps, les normes ISO se sont imposées. En français, on utilise souvent le jeu de caractères « ISO-8859-1 ». Historiquement, l'outil Bloc-note de Microsoft utilise par défaut un jeu de caractères qui est très similaire à ISO-8859-1 (qu'ils nomment parfois ANSI) sur les PC vendus en Amérique du Nord. Malheureusement, n'utiliser que 8 bits pour représenter les caractères signifie qu'il est impossible de tenir compte des langues asiatiques, par exemple, et qu'on ne peut mélanger un texte français avec de l'arabe. Pour cette raison, en 1991, la norme Unicode fut proposée.

La norme [Unicode](http://unicode.org) est de plus en plus utilisée et elle est popularisée en partie par son utilisation dans le XML. En effet, par défaut, un document XML utilise Unicode (spécifiquement UTF-8 ou UTF-16) et ce sont les seuls jeux de caractères qu'un processeur XML est requis de connaître. L'avantage principal d'Unicode est sa richesse : la version 5.0 du format Unicode permet de représenter 99 000 caractères différents incluant les caractères Klingon de Star Trek. En comparaison, le jeu de caractères ISO-8859-1 permet de représenter moins de 255 caractères (8 bits).

UTF-8 et UTF-16 sont les deux encodages Unicode les plus utilisés en XML. UTF-8 est un encodage à longueur variable qui représente les caractères ASCII (les 128 premiers) sur un seul octet, exactement comme l'ancien ASCII, ce qui le rend totalement rétrocompatible avec les innombrables fichiers et outils qui supposent cet encodage ; les caractères accentués latins occupent deux octets, et les caractères plus rares (asiatiques, émojis, etc.) jusqu'à quatre octets. Cette économie fait d'UTF-8 l'encodage par défaut sur le web, dans les bases de données modernes et dans la majorité des fichiers XML actuels. UTF-16, quant à lui, utilise des unités de deux octets (16 bits) pour chaque caractère de base ; les caractères du plan multilangue supplémentaire nécessitent alors une paire de substituts (surrogate pairs) et occupent donc quatre octets. Il est plus compact que UTF-8 pour les textes majoritairement asiatiques, mais consomme davantage d'espace pour les textes latins et pose des problèmes de compatibilité avec les outils qui s'attendent à un octet = un caractère. En XML, un parseur doit obligatoirement comprendre les deux, mais UTF-8 reste très largement dominant grâce à sa compatibilité et à sa robustesse.

Les caractères de la langue anglaise (ASCII) sont toujours stockés de la même façon, qu'on utilise UTF-8 ou ISO-8859-1, en utilisant 7 bits. C'est donc dire que les programmeurs anglophones travaillant pour des utilisateurs anglophones peuvent, jusqu'à un certain point, ignorer les questions d'encodage des caractères.

La plupart des logiciels récents supportent la norme Unicode. D'ailleurs, depuis le tout début, une chaîne de caractères en Java est représentée en utilisant la norme Unicode. Par contre, il restera toujours des logiciels utilisant d'autres jeux de caractères.

## La déclaration XML

La déclaration XML ressemble à s'y méprendre à une instruction de traitement et prend la forme <?xml ... ?&gt;. Une déclaration XML n'est pas une balise ou un élément. Le contenu d'une déclaration XML comporte généralement au maximum trois *attributs* : version="...", encoding="..." et standalone="...". La version 1.0 du XML est la plus utilisée; bien que la version 1.1 existe, elle est fort peu utilisée. Selon l'un des inventeurs du XML, Tim Bray, il est peu probable qu'il y ait une version 2.0 du XML .

> Je ne pense pas qu'il y aura de XML 2.0. Les obstacles politiques seraient effrayants - tout le monde voudra sa part du gâteau -, et la base installée de logiciels qui reconnaissent XML comprend aujourd'hui à peu près tous les ordinateurs liés à Internet, donc une transition me semblerait trop onéreuse. ([Interview de Tim Bray](http://developpeur.journaldunet.com/itws/070129-itw-sun-bray.shtml), JDN Développeurs, 29 janvier 2007)

Sur un disque ou dans un réseau, un document XML n'est rien donc qu'une chaîne d'octets. Pour interpréter cette chaîne comme du texte, il faut spécifier l'encodage des caractères. Par défaut, le XML suppose que nous avons un encodage des caractères de type Unicode. On utilise souvent une déclaration XML avec « encoding="ISO-8859-1" » pour pouvoir utiliser les accents dans le document en conjonction des outils logiciels n'ayant pas été mis à jour au vingt-et-unième siècle. Seuls les caractères de la langue anglaise (ASCII) ne changent pas entre ISO-8859-1 et unicode. L'utilisation des accents en français sans la déclaration « encoding="ISO-8859-1" » peut alors entraîner des problèmes si le document a été enregistré avec l'encodage ISO-8859-1.

Un même document XML peut être enregistré sous plusieurs jeux de caractères. Cependant, il faut que la déclaration correspondent au format utilisé lors de l'enregistrement du fichier, sinon les caractères accentués (par exemple) seront pervertis.

L'attribut « standalone » prend la valeur *yes* ou *no*, selon que l'on veut que la DTD externe soit lue ou non. Nous traiterons des DTD, plus tard.

Il est important de prendre en compte l'encodage des caractères. Le document XML suivant, si on l'enregistre en ISO-8859-1, ne serait pas bien formé, car il utilise des accents :

```xml
<étudiant>
 Jean
 </étudiant>
```

Par contre, le document XML qui suit est bien formé lorsqu'on l'enregistre en ISO-8859-1 :

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
 <étudiant>
 Jean
 </étudiant>
```

La déclaration XML doit **obligatoirement être au tout début du document** ou être carrément absente : même un espace n'est pas permis.

## Les espaces

En XML, les espaces entre les balises comptent, qu'il s'agisse d'un retour de charriot, d'une [tabulation](http://fr.wikipedia.org/wiki/Tabulation) ou d'un simple espace. Ainsi, le document suivant se décompose en 7 parties ou nœuds : un élément-racine nommé html qui contient d'abord un nœud de texte (le retour de charriot) suivi d'un élément produit contenant le nœud de texte «1», suivi d'un autre nœud de texte (le retour de charriot), suivi d'un élément serie (vide), suivi d'un quatrième nœud de texte (le retour de charriot).

```xml
<html>
<produit>1</produit>
<serie />
</html>
```

Par contre ce document ne contient que 4 nœuds (3 éléments et 1 nœud de texte) :

```xml
<html><produit>1</produit><serie /></html>
```

En effet, comme il n'y a pas d'espace ou de retour de charriot entre les balises, il n'y a qu'un seul nœud de texte. Si on omet les attributs, les nœuds débutent et se terminent généralement avec les balises.

On peut indiquer que les espaces entre les éléments sont significatifs avec l'attribut xml:space qui peut prendre la valeur default ou la valeur preserve. Dans cet exemple, on souhaite indiquer que les espaces sont significatifs :

```xml
<html xml:space="preserve">
<produit>1</produit>
<serie />
</html>
```

## Les fins de ligne

Les fichiers de texte sont souvent organisés en lignes. Selon le système d'exploitation, il y a plusieurs façon de représenter une fin de ligne. Les systèmes d'exploitation Microsoft utilisent deux caractères (« retour de charriot » et « nouvelle ligne ») à la fin de chaque ligne. Les autres système utilisent généralement un seul caractère (« nouvelle ligne »). Les processeurs XML sont requis de normaliser la situation et de remplacer les deux caractères utilisés par les systèmes Microsoft par un seul caractère lors de la lecture du fichier. Ainsi, peu importe comment l'on note les fins de ligne, un processeur XML ne vera qu'un caractère « nouvelle ligne ».

## Les hyperliens

Il arrive fréquemment qu'on utilise des hyperliens dans les documents XML. On distingue deux types d'hyperliens : les hyperliens contenant une adresse absolue (telle que http://domaine.ca/pong.png) et les hyperliens contenant des adresses relatives (pong.png). On reconnaît les adresses relatives parce qu'elles ne débutent pas par un protocole tel que http ou ftp. Pour compléter les adresses relatives et les transformer en adresses absolues, on utilise fréquemment l'adresse du document. Ainsi, si le document suivant se trouve à l'adresse http://domaine.ca/fichier.xml, alors un logiciel pourra charger une image située à l'adresse http://domaine.ca/pong.png :

```xml
<racine>
adresse relative:
<image lien="pong.png" />
</racine>
```

Le XML permet de spécifier un attribut xml:base qui sert à interpréter les adresses relatives remplaçant l'adresse du document. Le document suivant pointe vers une image à l'adresse http://domaine.ca/image/pong.png :

```xml
<racine xml:base="http://domaine.ca/">
<p xml:base="image/">
<image lien="pong.png" />
</p>
</racine>
```

## Documents bien formés

Un document XML qui respecte ces règles de base est dit « bien formé ». Pour éviter la confusion, il ne faut pas utiliser des synonymes comme « correct ».

La terminologie utilisée peut sembler très aride. Cependant, la rigueur qu'exige le XML est aussi garante de la cohérence. Comme tous les termes sont bien définis, il est plus facile de s'entendre entre experts. Comme le XML est surtout utilisé pour la communication entre les logiciels, la rigueur évitera plus tard les bogues et les incompréhensions.

Pouvoir reconnaître un document XML bien formé ou comprendre pourquoi un document n'est pas bien formé, permet de s'assurer qu'un logiciel pourra traiter les informations, et qu'on saura quoi faire en cas de problème.