---
title: "Examen préparatoire"
weight: 20
---
# Examen préparatoire

Afin de bien vous préparer à l’examen final de ce cours, voici un examen préparatoire.

# Examen factice

## Question 1

Écrire un programme en Java utilisant l'API DOM modifiant un fichier XML de manière à ce que le préfixe « foo » soit ajouté aux noms de tous les éléments. Le fichier

```xml
<element><a></a></element>
```

deviendra donc

```xml
<fooelement><fooa></fooa></fooelement>.
```

Vous pouvez supposer que le document ne contient que des éléments, sans attributs, sans espaces de noms.

## Question 2

Même question, mais cette fois-ci, utilisez XSLT pour faire la transformation (indice: pensez à xsl:element).

## Question 3

Dessinez l'arbre DOM de ce fichier XML :

```xml
<a xmlns="http://www.w3.org/1999/xhtml"><b type="x" /></a>
```

Pour chaque élément et attribut, donner son nom et son espace de noms. (Indice: attention à l'espace de noms de l'attribut.)

## Question 4

Donnez une DTD équivalente à ce fichier Relax NG :

```xml
element p { (element c {text}, element d{text}*)? }
```

## Question 5

Écrivez en RDF/XML les triplets suivants :

sujet : http://www.com.com/jeanne

prédicat : http://www.w3.org/1999/02/22-rdf-syntax-ns#type

objet : http://www.com.com/maman

sujet : http://www.com.com/maman

prédicat : http://action.com/etre

objet : http://www.com.com/femme

sujet : http://www.com.com/enfant

prédicat : http://action.com/avoir

objet : http://www.com.com/maman

## Question 6

Définissez et expliquez les différences entre XPath, XLink, XQuery et XSLT.

## Question 7

Que signifie cette expression XPath :

//table[@border="0" and @cellspacing="0"] | //table[@border="1" and @cellspacing="1"]

## Question 8

Que va retourner cette expression XPath :

//table[@border]

## Question 9

Que va retourner cette expression XPath :

//table[@border]/@cellspacing

## Question 10

Que va retourner cette expression XPath :

//table[@border]/*/*[@style]

## Question 11

Que va retourner cette expression XPath :

//table[@border]/*/*[not(@style)]

## Question 12

Écrivez un programme Java qui applique l'expression XPath de la question précédente à un fichier chargé à partir du disque.

## Question 13

Expliquez ce que fera ce fichier XSLT :

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
xmlns:dc="http://purl.org/dc/elements/1.1/"
>
<xsl:template match="/">
- <xsl:for-each select="@type" >
<li>
<xsl:value-of select="." />
</li><xsl:text>
</xsl:text>
</xsl:for-each>
</xsl:template>
</xsl:stylesheet>
```

## Question 14

Écrivez une expression XPath qui compte le nombre d'éléments ayant été déclarés comme contenant du texte en langue française.

## Question 15

Nommez au moins 3 modèles de programmation XML utilisés en Java.

## Question 16

Définissez AJAX et expliquez pourquoi il s'agit d'une technique importante en développement web. Quel est le lien entre AJAX et DOM ?

## Question 17

Selon ce fichier CSS, de quelle couleur sera un élément p ?

```css
* {color: black;} p {color: olive;} body p {color: blue;} body > p {color: red;} body > p {color: green;} * {color: yellow;}
```

## Question 18

Selon le modèle de boîte CSS du W3C, quelle est la hauteur (height) minimale d'un objet ayant les propriétés CSS « padding: 10px; » et « margin: 12px; » ?

## Question 19

Donner un exemple de document XML contenant des attributs ID et des attributs IDREF.

## Question 20

Selon ce fragment de DTD, qu'est-ce qu'il est permis de mettre dans un élément p ? Comment nomme-t-on le concept utilisé ici ?

```xml
<!ENTITY % fontstyle "big | small"> <!ENTITY % phrase "em | cite"> <!ENTITY % in "%fontstyle; | %phrase;"> <!ENTITY % In "(#PCDATA | %in;)*"> <!ELEMENT p %In;>
```

## Question 21

Expliquez les expressions XPath suivantes et décrivez le résultat selon la théorie des ensembles (union, intersection et complément) :

```xml
//*[@s="1"]//*[@t="1"] //*[@s="1"]/[count(//*[@t="1"])=count(//*[@t="1"])] //*[@s="1"]/[count(//*[@t="1"])=count(//*[@t="1"])]
```

## Question 22

Comment passe-t-on des paramètres à une feuille de style XSLT à partir d'un document XML ?

## Question 23

Quelles sont les principales différences entre JSON et XML en termes de structure et d'utilisation ?

## Question 24

Écrivez un exemple de code JavaScript qui parse une chaîne JSON et accède à une propriété imbriquée.

## Question 25

Qu'est-ce qu'un schéma JSON et pourquoi est-il utile ?

## Question 26

Expliquez la syntaxe de base de YAML et donnez un exemple simple.

## Question 27

Comment YAML se compare-t-il à XML pour la configuration d'applications ?

## Question 28

Écrivez un exemple de document YAML qui représente une liste d'objets avec des propriétés imbriquées.

## Vous avez aimé le cours ?

Si vous avez aimé le cours, voici quelques façons de le montrer :

- Parlez du cours autour de vous et partagez vos commentaires positifs en ligne.
- Visitez la [page du professeur](https://www.teluq.ca/siteweb/univ/dlemire.html) pour découvrir les autres cours qu’il a conçus.
- Si vous avez un compte GitHub, [suivez le professeur](https://github.com/lemire) en cliquant sur le bouton « follow ».
- Si vous lisez l’anglais, [abonnez-vous au blog du professeur](https://lemire.me/blog/).
- Suivez le professeur sur [X](https://x.com/lemire).
- Découvrez les [livres écrits par le professeur](https://www.amazon.ca/stores/Daniel-Lemire/author/B0CR7YMZT2).

## Un problème ou une suggestion ?

Vous pouvez à tout moment soumettre un commentaire anonyme concernant le cours via [ce formulaire dédié](https://docs.google.com/forms/d/1emnei-XQua_DaLPXxMby-SCI9UMbQgSiilKOCRNhUZQ/viewform). Cela nous permet de réagir rapidement en cas de problème. Vous pouvez également en discuter directement avec la personne qui vous encadre.

Nous accordons une grande importance à vos retours et travaillons continuellement à l’amélioration du cours.
