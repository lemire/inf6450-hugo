---
title: "Définition de type de document"
weight: 20
---

# Définition de type de document

## Document XML valide

Nous avons vu ce qu'était un document XML bien formé : un seul élément-racine, les éléments ne se chevauchent pas, les noms XML ne commencent pas par un chiffre, et ainsi de suite. De plus, un document XML bien formé peut contenir n'importe quel élément et dans n'importe quel ordre, et tous les éléments peuvent contenir des attributs, et peu importe ceux-ci.

En pratique, il est souvent suffisant pour les documents XML d'être bien formés, mais il arrive qu'on veuille imposer des contraintes supplémentaires aux éléments et attributs pouvant être utilisés. Par exemple, un élément « étudiant » pourrait posséder un numéro d'étudiant, mais pas l'inverse : un élément « numéro d'étudiant » ne pouvant contenir qu'un numéro et pas d'autres éléments. On peut aussi vouloir contraindre le contenu d'un document XML pour des raisons d'interopérabilité. Par exemple, si un groupe d'experts s'entendent sur un format XML pour un type de données, il est utile de pouvoir vérifier si un fichier XML donné correspond bien à ce sur quoi on s'est entendu. Un document XML qui est bien formé et qui respecte les contraintes définissant son type de document est dit valide (ou parfois valable).

En d'autres mots, un document XML qui est bien formé et qui, en plus, satisfait aux contraintes dictant quels éléments et attributs peuvent être utilisés, et dans quel ordre et avec quel contenu, est dit valide.

## Normes de définition de type de document

Il y a plusieurs façons de définir des types de documents XML. L'approche la plus répandue, la plus ancienne et la plus simple, est la norme de définition de type de document (DTD). Les deux autres possibilités émergentes les plus répandues sont XML Schema et Relax NG.

On fait généralement deux reproches à l'approche DTD : un document DTD n'est pas du XML et la norme n'est pas assez riche pour spécifier le contenu des documents XML avec finesse. En effet, L'approche DTD ne permet pas de déclarer qu'un contenu textuel doit être une date ou un nombre, et il n'y a pas de support pour les espaces de noms, sujet que nous traiterons plus loin dans ce module.

D'un autre côté, la norme DTD est très répandue et tous les logiciels qui supportent XML supportent maintenant cette norme, incluant Java, Google Chrome et Firefox. Les formats comme XHTML 2.0 sont toujours publiés avec une spécification DTD. Les autres possibilités, comme XML Schema, Relax NG, Schematron et Examplotron, sont moins bien supportées.

La norme XML Schema permet de définir avec une grande finesse des types de données comme une date ou un code de langue (« fr », « en »). Cette norme est très utile si on veut spécifier avec beaucoup de détail le format de nos documents XML. Comme vous pouvez le constater dans l'exemple suivant, la norme XML Schema permet non seulement de spécifier le nom des éléments et des attributs (« shipTo », « billTo », « comment », « items », « orderDate »), mais aussi leur type (« xsd:string », « xsd:decimal », « xsd:date »).

```xml
<xs:complexType name="PurchaseOrderType">
  <xs:sequence>
    <xs:element name="shipTo" type="USAddress"/>
    <xs:element name="billTo" type="USAddress"/>
    <xs:element ref="comment" minOccurs="0"/>
    <xs:element name="items"  type="Items"/>
  </xs:sequence>
  <xs:attribute name="orderDate" type="xs:date"/>
</xs:complexType>
```

La norme XML Schema est supportée en Java depuis la version 1.5. Il n'est pas nécessaire d'utiliser une librairie spécialisée. Elle est cependant sujette à des critiques sévères de la part des experts en XML tels que Tim Bray (co-inventeur du XML) qui écrivait en novembre 2006 sur son blogue :

Everybody who actually touches the technology has known the truth for years, and it's time to stop sweeping it under the rug. W3C XML Schemas (XSD) suck. They are hard to read, hard to write, hard to understand, have interoperability problems, and are unable to describe lots of things you want to do all the time in XML. Schemas based on Relax NG, also known as ISO Standard 19757, are easy to write, easy to read, are backed by a rigorous formalism for interoperability, and can describe immensely more different XML constructs.

En somme, XML Schema est trop difficile à utiliser et à comprendre. Tim Bray, ainsi que de nombreux autres experts, préconisent plutôt l'utilisation de Relax NG. Cette norme, comme XML Schema, possède plusieurs avantages sur la norme DTD : elle permet de spécifier des types de données (comme une date ou un nombre), supporte les espaces de noms, etc. De plus, la norme Relax NG est plus élégante techniquement et parfois plus simple que la norme XML Schema. Des formats importants comme l'Open Document Format, DocBook (format XML), TEI, XHTML et Atom sont définis par RelaxNG plutôt que par XML Schema. (Une définition XML Schema sera sans doute produite pour le format XHTML 2.0.) Relax NG dispose aussi d'une syntaxe « compacte », qui n'est pas en XML contrairement au format par défaut de Relax NG, et que nous allons utiliser dans nos exemples. Voici un exemple de Relax NG :

```xml
element addressBook {
  element card {
    element name { text }
    element email { text }
  }*
}
```

Cet exemple spécifie que le document XML doit avoir comme élément racine un élément « addressBook », contenant zéro ou plus éléments « card ». Un élément « card » doit obligatoirement contenir un élément « name » suivi d'un élément « email ».

Tout en étant plus élégante que la norme DTD, le format Relax NG est plus limitée que XML Schema puisqu'il ne permet que quatre types de contraintes sur le nombre d'occurences d'un élément (zeroOrMore comme dans notre exemple, optional, un nombre précis (comme une seule fois) et oneOrMore) alors que le XML Schema permet des contraintes beaucoup plus spécifiques. Cependant, la richesse de la norme XML Schema a un coût : il s'agit d'une norme beaucoup plus difficile à utiliser et à apprendre en pratique.

On peut passer automatiquement d'un document DTD à un document XML Schema ou Relax NG avec un outil comme NekoDTD.

En somme, la norme DTD n'est sans doute pas ce qui se fait de mieux, mais c'est de loin la norme la plus utilisée historiquement, et c'est celle que nous allons étudier en détail. Pour certaines applications, la norme DTD demeure supérieure aux alternatives mentionnées précédemment: la définition d'entités n'est pas possible en XML Schema ou Relax NG, par exemple. Si vous maîtrisez la norme DTD, vous n'aurez aucun mal à utiliser une autre norme comme Relax NG puisque les principes essentiels sont les mêmes.

## Documents valides utilisant la norme DTD

Un document valide commence par une déclaration XML, comme celle qui suit :

```xml
<?xml version="1.0" encoding="ISO-8859-1" standalone="no" ?>
```

Elle est suivie d'une déclaration de type de document sous la forme <!DOCTYPE ... SYSTEM ... > , où l'on remplace les premiers trois points par le nom XML de l'élément-racine que le document doit avoir, et les deuxièmes trois points par une URL vers le document DTD. L'URL peut être absolue, comme « http://www.google.com/mydtd.dtd », ou locale, comme « madtd.dtd » ou « ../dtd/madtd.dtd ». Dans le second cas, il faut que le fichier DTD soit sur le disque, à l'endroit indiqué par rapport au fichier XML. Ainsi, dans l'exemple « ../dtd/madtd.dtd », il faudrait que le fichier « madtd.dtd»  soit dans le répertoire « dtd », voisin du répertoire où se trouve le fichier XML. Ainsi, immédiatement après la déclaration XML, on pourrait avoir le texte suivant :

```xml
<!DOCTYPE baliseracine SYSTEM "http://www.mondomain.com/madtd.dtd">
```

où « baliseracine » est le nom de l'élément-racine du document, alors que le chemin « http://www.mondomain.com/madtd.dtd»  nous dit où trouver le document DTD.

Rappelons que l'attribut « encoding » nous donne le jeu des caractères. On choisit souvent « ISO-8859-1 », mais par défaut, XML utilise un jeu de caractères Unicode (UTF-8). Si le contenu est en français (avec les accents), il est essentiel que le fichier soit enregistré avec le jeu de caractères déclaré sinon on pourra constater des messages d'erreurs ou des accents manquants. L'attribut « standalone » permet au logiciel de décider, s'il est nécessaire, d'aller chercher la DTD externe avant de lire le fichier XML, même si, très souvent, un logiciel tel Mozilla Firefox ignore la consigne et ne va pas chercher la DTD externe. En gros, s'il y a une DTD externe, on utilisera l'attribut « standalone="no" », autrement on utilise « standalone="yes" ».

## La syntaxe des documents DTD

Les documents DTD contiennent des instructions de la forme <!ELEMENT ... >. Bien que celle-ci ait l'apparence d'une balise XML, ce n'est pas du XML. Dans une instruction, on met d'abord un nom XML qui correspond à un nom d'élément : par exemple, l'instruction « <!ELEMENT montant ... > » définira ce qui peut être contenu dans un élément de nom « montant ». Tout ce qui suit le nom de l'élément dicte ce que l'élément peut contenir. Le plus souvent, on place la description du contenu entre parenthèses (« <!ELEMENT montant (quelque chose) > »), sauf pour les cas particuliers (« ANY » et « EMPTY ») définis plus loin. De façon courante, on définit le contenu d'un élément par une liste de noms XML, correspondant à des noms d'élément et séparés par des virgules. Par exemple, l'instruction « <!ELEMENT montant (devise,valeur) > » nous informe qu'un élément « montant » doit contenir un élément « devise » suivi d'un élément « valeur ». Notons que l'ordre des éléments importe et que les instructions « <!ELEMENT montant (devise,valeur) > » et « <!ELEMENT montant (valeur,devise) > » ne sont pas équivalentes.

Bien qu'on ne puisse exprimer toutes les possibilités, la syntaxe DTD permet tout de même de spécifier un grand nombre de règles. Par exemple, le symbole « ? » permet de spécifier qu'un élément peut être présent ou non (élément optionnel). Ainsi, l'instruction « <!ELEMENT montant (devise?,valeur) > » signifie que l'élément « montant » peut contenir un élément « devise » (ou non) et doit contenir un élément « valeur ». Si jamais l'élément « devise » apparaît, il doit apparaître avant l'élément « valeur ». Si jamais on veut qu'un élément soit optionnel et que, s'il apparaît, il puisse apparaître plus d'une fois, on utilise le symbole « * ». Ainsi, l'instruction « <!ELEMENT montant (devise*,valeur) > » signifie qu'on peut avoir zéro, un ou plusieurs éléments « devise », puis un élément « valeur ». De la même façon, le symbole « + » est utilisé pour spécifier qu'un élément doit être présent, mais peut apparaître plus d'une fois.

Au lieu d'utiliser la virgule, on peut utiliser le symbole « | » pour spécifier qu'un élément ou un autre peut apparaître. Ainsi, l'instruction « <!ELEMENT montant (devise|valeur) > » signifie que l'élément « montant » peut contenir soit l'élément « devise », soit l'élément « valeur » (l'un ou l'autre, mais pas les deux ou aucun des deux). Finalement, on peut combiner le tout; par exemple, l'instruction « <!ELEMENT montant (devise+|valeur*) > » signifie que l'élément « montant » peut contenir au moins un élément « devise » (et rien d'autre) ou alors, aucun, 1 ou plusieurs éléments « valeur ».

Si jamais on veut qu'un élément puisse contenir du texte, on utilise le terme technique « #PCDATA » dans l'instruction DTD. Par exemple, l'instruction « <!ELEMENT montant (#PCDATA) > » signifie que l'élément « montant » contient du texte et seulement du texte (pas d'éléments). Supposons maintenant qu'on veut permettre du contenu mixte, comme dans l'exemple qui suit :

```xml
<mixte> du texte et <important>un élément</important> </mixte>
```

On pourrait penser que l'instruction « <!ELEMENT mixte (#PCDATA|important) > » permettra du texte ou des éléments « important », et c'est vrai; mais elle permet l'un (juste du texte) ou l'autre (juste un élément « important »), mais pas un mélange des deux. Pour pouvoir obtenir le résultat désiré, soit un mélange d'éléments « important » et de texte, il faut permettre la répétition du choix, comme dans l'instruction « <!ELEMENT mixte (#PCDATA|important)* > ». Il s'agit de la seule façon de spécifier qu'on permet un mélange de texte et d'éléments (contenu mixte).

Voyons un autre exemple de contenu mixte. Considérons l'instruction « <!ELEMENT montant (#PCDATA|devise)* > ». Ce qu'elle signifie exactement, c'est que les éléments « montant » peuvent contenir un mélange de texte et des éléments « devise », comme l'exemple qui suit :

```xml
<montant>10 $ et <devise>dollars</devise></montant>
```

On peut aussi utiliser « ANY » pour spécifier qu'un élément peut contenir n'importe quoi (n'importe quelle séquence d'éléments déclarés dans la DTD et du texte) ou « EMPTY » pour spécifier qu'un élément doit être vide (sans même un seul espace). C'est le seul cas où l'on n'utilise pas de parenthèses lors de la définition du contenu, comme dans ces exemples : <!ELEMENT question ANY> et <!ELEMENT question EMPTY>.

Un document DTD prendra donc la forme d'un fichier en format texte contenant une suite d'instructions comme :

```xml
<!ELEMENT lettre (#PCDATA|personne)* >
<!ELEMENT personne (age,nom) >
<!ELEMENT age (#PCDATA) >
<!ELEMENT nom (#PCDATA) >
```

Notez qu'on écrit rarement de nouvelles DTD : dans un domaine particulier, il existera souvent des DTD déjà utilisées; sinon, on fera l'effort de les créer, mais qu'une seule fois. L'important demeure toutefois de pouvoir lire et comprendre les DTD.

## Exemple supplémentaire

Pour s'assurer de bien comprendre, voyons un autre exemple :

```xml
<!ELEMENT lettre (#PCDATA|personne)* >
<!ELEMENT personne (age,nom) >
```

Cette DTD nous spécifie que l'élément « lettre » contient du mélange de texte et d'éléments « personne » (contenu mixte), alors que l'élément « personne » doit contenir un élément « age », suivi d'un élément « nom ».

Par exemple, ce document XML serait valide :

```xml
<lettre> Bonjour <personne><age>30</age><nom>Jean</nom></personne> </lettre>
```

Assurez-vous de bien comprendre pourquoi ce document est valide avant de continuer.

## Les attributs

Par défaut, aucun élément n'est autorisé à avoir un attribut. Pour permettre d'ajouter un attribut à un élément, il faut une instruction de la forme <!ATTLIST recipiendaire age ...> qui spécifie que l'élément recipiendaire peut avoir un attribut « age ». On permet généralement aux valeurs d'attribut de contenir n'importe quel texte, ce qu'on représente par « CDATA ». Hormis le contenu, il existe deux types d'attributs : les attributs obligatoires (« #REQUIRED ») et les attributs optionnels (« #IMPLIED »). Par exemple, l'instruction «  <!ATTLIST recipiendaire age CDATA #IMPLIED> » signifie qu'on peut (ou pas) accorder à un élément « recipiendaire » un attribut nommé « age » pouvant contenir n'importe quel texte. Si l'on désire que l'attribut soit obligatoire, on utilise une instruction comme « <!ATTLIST recipiendaire age CDATA #REQUIRED> ».

Si l'on veut permettre à un élément d'avoir plusieurs attributs, on peut le faire en utilisant plusieurs instructions comme dans « <!ATTLIST recipiendaire age CDATA #REQUIRED> <!ATTLIST recipiendaire nom CDATA #REQUIRED> »; on peut aussi combiner les instructions dans une seule : « <!ATTLIST recipiendaire age CDATA #REQUIRED nom CDATA #REQUIRED> ». Cependant, il n'est pas possible de spécifier l'ordre dans lequel les attributs doivent apparaître, les instructions « <!ATTLIST recipiendaire age CDATA #REQUIRED nom CDATA #REQUIRED> » et « <!ATTLIST recipiendaire nom CDATA #REQUIRED age CDATA #REQUIRED> » sont équivalentes.

L'attribut « xml:lang » utilisé pour définir la langue d'un texte, peut être déclaré comme ceci : « <!ATTLIST monelement xml:lang CDATA #IMPLIED> ». L'attribut xml:space peut être déclaré comme ceci : « <!ATTLIST monelement xml:space (default|preserve) #IMPLIED> ».

On peut également spécifier qu'un élément donné a toujours un attribut donné (indiqué ou non dans le XML) comme ceci : «<!ATTLIST recipiendaire age CDATA #FIXED "40 ans">». Dans ce dernier exemple, tous les éléments « recipiendaire » ont l'attribut « age="40 ans" », même si on omet de l'indiquer dans la balise de départ de l'élément « recipiendaire ».

Plus simplement, on peut spécifier une valeur par défaut qui ne prendra effet que si l'on n'a pas explicitement indiqué l'attribut. Par exemple, l'instruction « <!ATTLIST recipiendaire age CDATA "40 ans">  » signifie que l'élément « recipiendaire » aura l'attribut « age="40 ans" », à moins qu'on ne spécifie autre chose dans le XML.

Il peut être utile de donner une liste de valeurs que pourra prendre un attribut. Par exemple, une pièce de monnaie est soit sur « face », soit sur « pile » : il n'y a que deux choix. Si la liste de choix est composée de textes sans espace ou ponctuation, sauf la barre du soulignement ( _  ), le trait d'union ( - ) et le point ( . ), alors on peut faire une énumération comme dans l'exemple suivant : « <!ATTLIST piece position (face|pile) #REQUIRED>». On peut aussi spécifier une valeur par défaut, si l'on suppose, jusqu'à preuve du contraire, que la pièce est dans la position « face », comme ceci «  <!ATTLIST piece position (face|pile) "face"> »

On peut également spécifier qu'un attribut servira à identifier un élément de façon unique. Pour ce faire, on utilise une instruction comme «  <!ATTLIST recipiendaire code ID> ». Il n'est pas possible, pour deux attributs de type ID, d'avoir la même valeur dans un même document XML. En somme, si l'on donne une valeur « ID », elle devrait correspondre de façon unique à un élément et un seul. Un attribut de type « ID » doit avoir comme valeur un « nom XML », c'est-à-dire un texte sans espace ou ponctuation, sauf la barre du soulignement ( _  ), le trait d'union ( - ) et le point ( . ), et qui ne commence pas par un chiffre, un trait d'union ou un point.

On peut faire référence aux attributs de type « ID » avec des attributs de type « IDREF ». La valeur d'un attribut « IDREF » doit non seulement être un nom XML, mais doit aussi avoir un attribut de type « ID » qui possède cette même valeur quelque part dans le document XML. Par exemple, si on a l'instruction «  <!ATTLIST recipiendaire code ID> », on pourra ensuite faire référence à l'élément ayant une valeur d'attribut « code » particulière, avec une instruction comme «  <!ATTLIST mauvaispayeur code IDREF> ».

Dans ce contexte, le document XML qui suit n'est pas valide :

```xml
<recipiendaire code="123">...</recipiendaire>
<mauvaispayeur code="456">...</mauvaispayeur>
```

Par contre, l'exemple qui suit est valide :

```xml
<recipiendaire code="123">...</recipiendaire>
<mauvaispayeur code="123">...</mauvaispayeur>
```

Il existe d'autres types d'attributs, mais ils sont peu utilisés.

## Les entités

Vous vous rappelez sans doute que le XML définit quelques entités par défaut, « &lt; », par exemple. On peut toutefois définir ses propres entités avec une instruction DTD comme celle-ci :

```xml
<!ENTITY monentite "Introduction à XML">
```

La signification de ce dernier exemple, c'est que partout où « &monentite; » apparaît dans un document, il sera remplacé par le texte « Introduction à XML ». Ce remplacement s'applique aussi aux valeurs par défaut des attributs de la DTD.

On peut mettre des éléments et des attributs dans une entité comme dans cet exemple :

```xml
<!ENTITY monentite "<paragraphe>texte</paragraphe>">
```

Il n'est cependant pas permis de ne mettre qu'une partie d'un élément comme ceci :

```xml
<!ENTITY monentite "<paragraphe>">
```

Une entité peut faire appel à une autre entité :

```xml
<!ENTITY monentite1 "&monentite2;">
<!ENTITY monentite2 "texte">
```

Une entité ne peut cependant pas faire appel à elle même de manière récursive, directement ou indirectement. Cet exemple n'est donc pas valide :

```xml
<!ENTITY monentite "&monentite;">
```

## DTD interne et externe

Normalement, on fait référence à un document DTD à l'aide d'une URL, c'est ce qu'on appelle la DTD externe. Mais il est possible d'ajouter ses propres instructions DTD directement dans le document XML, en ajoutant une DTD interne qui est lue avant la DTD externe.

Prenons l'exemple suivant, soit un document XML qui débute par :

```xml
<?xml version="1.0" ?>
<!DOCTYPE question SYSTEM "question.dtd" [
  <!ELEMENT question #PCDATA>
]>
```

Dans ce cas, tout ce passe comme si on ajoutait la ligne « <!ELEMENT question #PCDATA> » à la DTD externe. Normalement, il ne devrait jamais y avoir de conflit entre les deux DTD (interne et externe); on ne peut pas redéfinir un élément, mais on peut y définir des éléments! Par contre, les entités peuvent être redéfinies et la définition trouvée dans le DTD interne l'emporte.

On peut même omettre complètement la DTD externe comme dans l'exemple suivant :

```xml
<?xml version="1.0" ?>
<!DOCTYPE question [
  <!ELEMENT question #PCDATA>
]>
```

## Les entités paramètres

On peut aussi définir des entités particulières qui ne s'appliquent que dans le contexte de la DTD, et non pas dans le document XML. Pour ces entités, au lieu d'utiliser l'esperluette ( & ), on utilise plutôt le symbole du pourcentage ( % ). Ainsi, l'instruction suivante :

```xml
<!ENTITY % monentite "#PCDATA|age*">
```

signifie que partout, dans la DTD externe, où se trouve le texte « %monentite; », il sera remplacé par « #PCDATA|age* »; on appelle ces entités des « entités paramètres ». On peut définir une entité paramètre dans la DTD interne, mais on ne peut pas l'y utiliser; elle doit être utilisée dans la DTD externe. Si l'entité paramètre « %monentite; » est définie, à la fois dans la DTD interne et dans la DTD externe, la DTD interne a préséance. En somme, les entités paramètres ne s'appliquent que dans la DTD externe; elles ne s'appliquent ni dans le document XML, ni dans le DTD interne, soit la partie de la DTD définie dans le document XML.

## Commentaires dans les fichiers DTD

Pour rendre un fichier DTD plus compréhensible, on peut ajouter des commentaires. La syntaxe est la même que pour les fichiers XML comme le montre l'exemple suivant.

```xml
<!-- ceci est un commentaire -->
```

Les commentaires dans les fichiers Relax NG non-textuel sont obtenus en débutant une ligne par le symbole « # » comme dans cet exemple.

```xml
# ceci est un commentaire
```

## Une comparaison entre Relax NG et DTD

Une fois qu'on connaît bien le format DTD, il est facile d'apprendre Relax NG. Prenons d'abord un de nos exemples de fichier DTD.

```xml
<!ELEMENT lettre (#PCDATA|personne)* >
<!ELEMENT personne (age,nom) >
```

Une étude attentive vous permettra de constater que ce fichier est très similaire au fichier Relax NG suivant, qui lui est essentiellement équivalent.

```xml
element lettre { (text | element personne { element age { text }, element nom { text } })* }
```

Pour bien comprendre, prenons un autre exemple, plus complexe cette fois-ci. Voici un autre fichier DTD discuté précédemment.

```xml
<!ELEMENT question (questionText,answer+) >
<!ELEMENT questionText (#PCDATA) >
<!ELEMENT answer (#PCDATA) >
```

Voici l'équivalent en Relax NG. Si vous l'étudiez avec soin, vous verrez qu'encore une fois, le format Relax NG est très similaire au format DTD.

```xml
element question { element questionText { text }, element answer { text }+ }
```

Prenons maintenant un exemple de fichier DTD contenant un attribut.

```xml
<!ELEMENT personne (nom,age) >
<!ATTLIST personne code CDATA #REQUIRED>
```

L'équivalent Relax NG est, encore une fois, assez compréhensible comme vous pourrez le constater, l'instruction ATTLIST étant remplacée par l'instruction « attribute ».

```xml
element personne { attribute code { text }, element nom { text }, element age { text } }
```

Lorsqu'on utilise l'instruction attribute, la présence de l'attribut est requise à moins d'ajouter le point d'interrogation (« ? ») à la suite de l'instruction.

Le format Relax NG permet aussi de définir des motifs qui peuvent être réutilisés. Prenons ce fichier DTD simple.

```xml
<!ELEMENT problemset (choice+) >
<!ELEMENT choice (#PCDATA) >
```

L'équivalent en Relax NG donne ceci.

```xml
choiceele = element choice { text }
element problemset { choiceele+ }
```

Le format Relax NG a cependant plusieurs avantages. Par exemple, l'esperluette (&) permet de spécifier que des éléments puissent être inclus dans n'importe quel ordre. Il n'y a pas d'équivalent en DTD. Considérons l'exemple suivant.

```
element card { element name { text } & element email { text } }
```

On peut alors permettre le XML suivant. Il n'est pas possible de spécifier le contenu de l'élément card avec une instruction DTD similaire.

```xml
<card><email>jean@exemple.com</email><name>Jean</name></card>
```

Supposons maintenant qu'un élément puisse avoir soit l'attribut nas, soit à la fois les attributs nas1 et nas2. Alors qu'il n'est pas possible de représenter cette condition en DTD, c'est une chose facile en Relax NG.

```
element personne { attribute nas { text } | (attribute nas1 { text } & attribute nas2 { text }) }
```

## Une approche plus modulaire

En pratique, les fichiers DTD et Relax NG peuvent devenir complexes. On souhaite donc souvent les diviser en plusieurs fichiers plus petits. Par exemple, pour une spécification portant des ventes et achats de biens, on pourra avoir un fichier portant sur la description des biens, un fichier portant sur la description des acheteurs, et ainsi de suite. Une approche modulaire, avec de petits fichiers, a aussi l'avantage qu'on peut réutiliser les fichiers dans plus d'une spécification.

À titre d'exemple, reprenons le fichier DTD portant sur la définition de l'élément « problemset ». Au lieu de définir tout d'un seul coup, on peut commencer par un fichier DTD qui ne définit que l'élément « choice » :

```xml
<!ELEMENT choice (#PCDATA)>
```

Pour les fins de notre exemple, supposons que ce dernier fichier porte le nom de « choice.dtd » et se trouve à l'adresse « http://www.mondomaine.com/choice.dtd ». On pourra alors en importer le contenu dans un autre fichier externe avec une « entité paramètre externe ». À la différence d'une entité paramètre usuelle, une entité paramètre externe pointe vers un autre document que le logiciel devra traiter. On définit l'entité paramètre externe avec l'instruction « SYSTEM » suivie d'une adresse web comme dans cet exemple :

```xml
<!ENTITY % monentite SYSTEM "http://www.mondomaine.com/choice.dtd">
```

Pour inclure le contenu du fichier externe (« choice.dtd » dans notre exemple), il suffit tout simplement de faire appel à l'entité comme ceci :

```xml
%monentite;
```

Dans ce cas, tout se déroule comme si le contenu du fichier « choice.dtd » était inséré à l'endroit où se trouve l'appel (« %monentite; »). On peut définir l'élément « problemset » à l'aide du fichier DTD suivant :

```xml
<!ELEMENT problemset (choice+)>
```

On peut obtenir le même résultat avec Relax NG, un peu plus simplement avec l'utilisation de l'instruction « include ». Créons d'abord un fichier « choice.rnc » avec le contenu suivant :

```xml
choiceele = element choice { text }
```

On peut alors réutiliser le motif « choiceele » dans n'importe quel autre fichier Relax NG comme le montre cet exemple :

```xml
include "choice.rnc"
element problemset { choiceele+ }
```

En bref, il est facile de diviser des spécifications Relax NG ou DTD en plusieurs fichiers plus petits, plus faciles à éditer, et qui peuvent être plus facilement réutilisés.

## Définir l'élément-racine

Avec une DTD, il n'est pas possible de définir l'élément-racine. Celui-ci est déclaré par l'instruction DOCTYPE qui se trouve dans le document XML. Avec Relax NG, on peut non seulement spécifier l'élément-racine avec le mot-clef start, mais on peut aussi permettre une certaine flexibilité. Par exemple, l'instruction « start = problemset | choice » placée dans un fichier Relax NG, nous indique qu'on peut utilisé l'élément problemset ou l'élément choice comme élément-racine.

## Définir le type de contenu en Relax NG

Dans tous nos exemples de Relax NG, nous n'avons prévu que du contenu textuel (text) ou des éléments vides (empty). Relax NG permet de spécifier le contenu d'un élément ou d'un attribut d'une manière très fine. Il emprunte ici la spécification mise au point par XML Schema. En particulier, on peut spécifier un contenu textuel à l'aide d'une expression régulière. Voici quelques exemples.

| Type | Explication | Exemple |
|------|-------------|---------|
| xsd:date | Une date formattée avec la convention YYYY-MM-DD | 2001-01-01 ou 1999-12-30 |
| xsd:dateTime | Un moment spécifique à la seconde près | 2000-12-31T03:32:00 |
| xsd:string {pattern = "[^:]+" } | Une chaîne de caractères contenant au moins un caractère, à l'exclusion du symbole : | maison |
| xsd:string { pattern = ".+/.+" } | Deux chaînes de caractères séparée par un caractère / | 01/01 |
| xsd:string { pattern = ".+@.+"} | Deux chaînes de caractères séparée par un caractère @ | lala@to.com |
| "text" \| "html" | text ou html | text |
| xsd:string { minLength="7" maxLength="25" } | Une chaîne caractères faisant entre 7 et 25 caractères | monmotdepasse |
| xsd:decimal { minExclusive="0.0" maxInclusive="10.0" } | Un nombre entre 0 et 10 | 5 |
| xsd:decimal { fractionDigits="3" } | Un nombre n'ayant pas plus de 3 chiffres après la virgule (le point) | 5.001 |

On déclare ensuite le contenu d'un élément ou d'un attribut comme ceci : element madate {xsd:date}.

## Est-ce qu'il existe un outil pour passer d'un format à l'autre (DTD, Relax NG, XML Schema)?

Oui, le programme Java Trang permet de passer facilement d'un format à l'autre.

## Est-ce qu'un document DTD est un document XML?

Absolument pas. Par contre, une DTD est un document textuel. Les fichiers XML Schema sont par contre toujours en XML, alors que les fichiers Relax NG sont parfois en XML, parfois en simple format textuel comme dans nos exemples.

## Pourquoi est-ce qu'il n'est pas suffisant d'utiliser des documents bien formés? À quoi sert la validation?

Les documents XML sont faits pour être échangés et assurer la pérennité des informations. Si plusieurs individus ou plusieurs institutions s'entendent sur une DTD commune, il sera beaucoup plus facile d'échanger de l'information.

## Est-ce vraiment nécessaire d'avoir des documents valides? Est-ce que je dois vraiment toujours travailler avec des fichiers DTD, XML Schema ou Relax NG?

En pratique, la validation n'est pas essentielle et une application logicielle ne devrait pas exiger des documents valides. Si vous concevez une application, la règle implicite est que toute balise ou attribut non prévue devrait être ignorée. Un navigateur qui sait lire et afficher du XML devrait pouvoir lire tout XML bien formé, même s'il n'est pas valide. Si vous inventez une nouvelle balise XHTML, le navigateur devrait tout simplement ne pas en tenir compte. Les concepteurs du XML n'ont pas inscrit la nécessité d'être valide à même la définition du XML et c'est un choix qui n'a jamais été remis en question par l'organisme de normalisation W3C.

Il arrive, par exemple, qu'il soit inutilement complexe d'exiger que les documents soient valides. Si on se contraint à des documents valides, on peut même en arriver à des solutions qui sont techniquement inférieures.