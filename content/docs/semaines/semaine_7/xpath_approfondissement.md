---
title: "XPath : approfondissement"
weight: 30
---
# XPath : approfondissement

### Expression XPath avec « | »

Parfois, nous voulons sélectionner plusieurs noms d'éléments; nous pouvons obtenir ce résultat avec le symbole « | » (barre verticale) qui signifie « union ». Par exemple, le modèle qui suit s'applique à tous les éléments « facture » et « montant », et seulement à ces éléments est facture|montant.

### Expression XPath pour le nom d'un élément

Supposons que nous voulions afficher uniquement les noms des éléments (sans leur contenu). Nous pouvons obtenir ce résultat avec la fonction XPath « name » qui donne le nom de l'élément. La fonction name inclut le préfixe de l'espace de noms. Si on souhaite le nom de l'élément sans le préfixe, on peut utiliser la fonction « local-name ». La fonction « namespace-uri » donne l'URI de l'espace de noms de l'élément. Nous reviendrons sur ces expressions XPath dans le contexte du XSLT.

### Sélection conditionnelle

L'expression XPath « /listedeclients/client[nom='Sylvain'] » nous donnera les éléments pour lesquels le contenu du sous-élément « nom » est « Sylvain ». L'expression plus complète « /listedeclients/client[nom='Sylvain']/@telephone » pointera directement sur l'attribut « telephone ». D'un autre côté, l'expression XPath « /listedeclients/client[@telephone='533-3445']/nom », nous donnera l'élément « nom » contenant le nom du client ayant le numéro de téléphone indiqué.

L'absence du symbole « = » dans le crochets indique qu'il s'agit d'un test d'existence. Ainsi, « /listedeclients/client[nom] » donne les éléments « client » qui ont un sous-élément « nom ». De la même façon, « /listedeclients/client[@telephone] » donne les éléments « client » qui ont un attribut « telephone ».

Supposons maintenant que nous soyons devant un fichier XML comme celui-ci :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<listes>
<vendeur nom="Jean">
<client telephone="543-5454"><nom>Jacques</nom></client>
<client telephone="545-5455"><nom>Sylvain</nom></client>
<client telephone="443-4456"><nom>Claude</nom></client>
<client telephone="533-3445"><nom>Yvon</nom></client>
</vendeur>
<vendeur nom="Raymond">
<client telephone="432-2145"><nom>Arthur</nom></client>
<client telephone="545-5456"><nom>Sylvain</nom></client>
<client telephone="443-4556"><nom>Claudette</nom></client>
<client telephone="533-3445"><nom>Yvon</nom></client>
</vendeur>
</listes>
```

Il est maintenant plus fastidieux de trouver le numéro de téléphone d'un certain client, car il faut visiter tous les vendeurs. De plus, chaque vendeur peut avoir un numéro de téléphone (possiblement différent) pour chaque client. Comme nous allons le voir, XPath permet de gérer assez facilement ces situations.

Tout d'abord, l'expression « //client » donne une séquence de tous les éléments « client » dans le nœud courant. Avec l'expression XPath « //client[nom='Sylvain'] », nous pouvons obtenir la séquence de tous les éléments « client » ayant pour nom « Sylvain ».

Dans le même ordre d'idée, nous pouvons tester des conditions à l'aide d'expressions XPath contenant les symboles « < », « = », « != », « or », « and », « > », « >= », « <= ».

### Arithmétique en XPath

Nous pouvons aussi nous servir des expressions XPath pour faire du calcul simple. Par exemple, les trois expressions suivantes donneront 2, 2 et 2.5 respectivement :

```xml
<xsl:value-of select="1+1" />
<xsl:value-of select="2*1" />
<xsl:value-of select="5 div 2" />
```

Il arrive qu'on doive calculer une somme de nombres. Par exemple, supposons qu'une facture comporte une liste de montants.

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<?xml-stylesheet href="xslt.xml" 
type="application/xml"?>
<facture>
 <montant>10.10</montant>
 <montant>20.10</montant>
 <montant>40.10</montant>
</facture>
```

La fonction XPath « sum » nous permet de calculer la somme des montants sans effort comme dans cet exemple :

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" 
 xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="facture">
<html>
<body>
<xsl:value-of select="sum(montant)" />
</body>
</html>
</xsl:template>
</xsl:stylesheet>
```

Comme en Java, on a aussi les fonctions « floor », « ceiling », « mod » et « round ». On peut aussi utiliser les paranthèses dans toutes expressions XPath : « (5 + 2) div 2 ».

La fonction « count » compte le nombre de valeurs. On obtient la moyenne en divisant la somme par le compte (sum(x)/count(x)). Et ainsi de suite.

### Manipulations des chaînes de caractères en XPath

Outre les fonctions arithmétiques, on peut aussi manipuler les chaînes de caractères en XPath. La fonction la plus simple est « string-length ». Elle calcule la longueur d'une chaîne. Une autre fonction simple est « normalize-space » qui élimine tous les espaces au début et à la fin d'une chaîne en plus de remplacer les espaces répétés par un espace simple. La fonction « translate » permet de remplacer des caractères. Par exemple, pour remplacer les é par des e et les à par des a, on pourrait utiliser l'instruction suivante « translate("à la vérité","éà","ea") » qui renvoie « a la verite ».

On peut extraire des sous-chaînes de caractères de diverses manières : la fonction « substring » permet d'extraire une sous-chaîne lorsqu'on en connaît sa position et sa longueur, la fonction « substring-after » permet d'aller chercher un suffixe, la fonction « substring-before » permet d'aller chercher un préfixe. Par exemple, « substring("la vie est belle",3,7) » renvoie « vie est », « substring-after("la vie est belle","est") » renvoie « belle » alors que « substring-before("la vie est belle","est") » renvoie « la vie »

On peut aussi additionner deux chaînes de caractères pour en faire une seule avec la fonction « concat ». L'expression « concat("a","b") » a comme valeur "ab".

On peut tester une chaîne pour la présence d'une sous-chaîne avec la fonction XPath « contains ». L'expression « contains("abc","bc") » est vraie parce que "bc" est une sous-chaîne de "abc", alors que l'expression « contains("abc","bz") » est fausse.

### Tester le contenu des chaînes de caractères

Nous avons vu comment comparer le nom ou le contenu d'un élément avec une chaîne de caractères donnée, mais il arrive qu'on veuille faire des comparaisons plus fine. Heureusement, il existe des fonctions XPath permettant d'analyser le contenu des chaînes. Par exemple, « starts-with(@toto,"a") » renvoie la valeur vraie si et seulement si la valeur de l'attribut « toto » débute avec la lettre « a ». L'expression « ends-with(@toto,"a") » est vraie si et seulement si la valeur de l'attribut « toto » se termine avec la lettre « a ». De la même façon, « contains(@toto,"abc") » renvoie la valeur vraie si et seulement si la valeur de l'attribut « toto » contient la chaîne « abc » (comme dans « j'ai un abc »).

### Accès aux éléments d'un ensemble d'éléments

Avec XPath, nous pouvons traiter du XML un peu comme nous traitons un tableau en Java ou en C/C++. Par exemple, supposons que nous ayons une liste de clients avec leur numéro de téléphone, comme ceci :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<listedeclients>
<client telephone="543-5454"><nom>Jacques</nom></client>
<client telephone="545-5455"><nom>Sylvain</nom></client>
<client telephone="443-4456"><nom>Claude</nom></client>
<client telephone="533-3445"><nom>Yvon</nom></client>
</listedeclients>
```

Notez que l'expression XPath « /listedeclients/client » est en fait une séquence (ensemble ordonné) d'éléments. Ainsi, « /listedeclients/client[2] » représente le deuxième (et non le troisième!) élément « client », celui dont le nom est « Sylvain ».

Maintenant, si nous voulons obtenir le numéro de téléphone du deuxième client de la liste, il faut d'abord ajouter le symbole « / » (barre oblique) pour indiquer qu'on cherche un sous-nœud de l'élément en question, suivi de « @telephone » pour désigner l'attribut « telephone ». L'expression XPath "/listedeclients/client[2]/@telephone" nous donnerait le numéro de téléphone désiré.

Notez que l'expression « /listedeclients/client[0] » n'est pas valable, car la numérotation des éléments d'une séquence débute à 1 en XPath, contrairement à Java et à C/C++.

Notez aussi qu'on aurait pu obtenir le même résultat avec l'expression XPath « (/listedeclients/client/@telephone)[2] », car « /listedeclients/client/@telephone » est aussi une séquence (mais une séquence d'attributs). Nous devons toutefois ajouter une parenthèse pour marquer la priorité des opérations. En effet, la syntaxe « a/b[2] » signifie : deuxième nœud de type « b » dans les nœuds de type « b ». Comme il ne peut y avoir qu'un seul attribut d'un type donné dans un élément, la syntaxe « a/@b[2] » donnera toujours un ensemble vide. D'un autre côté, la syntaxe « (a/b)[2] » signifie : deuxième nœud de type « b » dans la séquence des nœuds de type « b » contenus dans les nœuds de type « a ». De la même manière, « //b[2] » donne la liste de tous les éléments b « b » dans le document apparaissant deuxième dans la liste des éléments contenus dans un autre élément, alors que « (//b)[2] » est le deuxième élément « b » rencontré dans tout le document.

Vous croyez avoir bien compris ? Quelle est la différence entre « (b)[2] » et « b[2] » ? Quelle est la différence entre « (b[2])/a » et « b[2]/a » ?

### Union, intersection et différence en XPath

Nous avons vu que le symbole « | » nous permet d'obtenir l'union de deux expressions XPath. Prenons l'exemple de ce document :

```xml
<x>
<a s="1" t="0" />
<b s="1" t="1" />
<c s="0" t="1" />
<d s="0" t="0" />
</x>
```

L'expression « //\*[@s="1"] » représente les éléments a et b, l'expression « //\*[@t="1"] » représente les éléments b et c, alors que l'expression « //\*[@s="1"]|//\*[@t="1"] » représente les éléments a,b,c (une union de « //\*[@s="1"] » et « //\*[@t="1"] »).

Supposons maintenant que nous désirions obtenir les éléments qui satisfont « @s="1" » et « @t="1" » : on veut calculer l'intersection entre « //\*[@s="1"] » et « //\*[@t="1"] ». On pourrait, bien sûr, obtenir ce résultat avec « //\*[@s="1" and @t="1"] », mais il existe une autre façon de le faire qui est d'application plus générale. Supposons que les résultats des expressions « //\*[@s="1"] » et « //\*[@t="1"] » sont déjà stockés dans les variables a1 et a2 respectivement. Alors l'expression « $a1[count(.|$a2)=count($a2)] » sélectionne l'élément b (ou « //\*[@s="1" and @t="1"] »). Ce motif particulier calcule l'intersection entre le contenu des variables a1 et a2. Pour le comprendre, il suffit de réaliser que la condition « count(.|$a2)=count($a2) » n'est vraie que pour les nœuds appartenant déjà à l'ensemble a2.

Supposons maintenant que l'on souhaite trouver les éléments qui satisfont « @s="1" » mais pas « @t="1" », c'est-à-dire l'élément a. En fait, on souhaite calculer la différence entre deux ensembles («&nbsp;//\*[@s="1"] » et « //\*[@t="1"] »). On pourrait obtenir ce résultat avec l'expression « //\*[@s="1" and not(@t="1")] », mais encore une fois, il existe un motif plus général: « $a1[count(.|$a2)!=count($a2)] » ou « //\*[@s="1"][count(.|//\*[@t="1"])!=count(//\*[@t="1"])] ». Pour comprendre cette expression, il suffit de réaliser que si et seulement si un nœud x n'appartient pas à a2, alors l'expression «&nbsp;count(x|$a2)!=count($a2) » sera vraie.

---
