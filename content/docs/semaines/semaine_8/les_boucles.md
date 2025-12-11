---
title: "Les boucles"
weight: 110
---

# Les boucles

## Utiliser XSLT comme base de données et éléments « for-each »

Dans cette section, nous explorons l'utilisation de XSLT pour traiter des séquences d'éléments avec l'élément xsl:for-each, permettant de boucler sur des nœuds sélectionnés par XPath et d'effectuer des opérations répétitives.

L'exemple de la liste des clients avec leur numéro de téléphone nous permet
   de faire plus. Tout d'abord, l'expression « //client » donne une
   séquence de tous les éléments « client »
   dans le nœud courant.
   Avec l'expression XPath « //client[nom='Sylvain'] », nous pouvons
   obtenir la séquence de tous les
   éléments « client » ayant pour nom « Sylvain ». Dans ce
   cas précis, il y a plus d'un élément
   dans la réponse. Pour visiter l'ensemble des éléments dans la séquence,
   il suffit d'utiliser l'élément « xsl:for-each » comme ceci :

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
   <xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:template match="/">
   <html><body>Numéros de téléphone pour Sylvain:
   <ul>
   <xsl:for-each select="//client[nom='Sylvain']/@telephone" >
   <li><xsl:value-of select="." /></li>
   </xsl:for-each>
   </ul>
   </body></html>
   </xsl:template>
   </xsl:stylesheet>
```

Le résultat de l'application de ce fichier XSLT au fichier XML contenant les
   numéros de téléphone sera :

```xml
<html><body>Numéros de téléphone pour Sylvain:
   <ul>
   <li>545-5455</li>
   <li>545-5456</li>
   </ul>
   </body></html>
```
Dans une telle boucle, il peut être utile de savoir quel est le numéro du
   nœud
   courant. On obtient ce numéro avec la fonction XSLT « position() »
   qui a la valeur 1 quand
   il s'agit du premier nœud et la valeur « last() » quand il s'agit
   du dernier nœud.
   On peut aussi utiliser une instruction xsl:sort au sein d'un élément
   for-each.

Supposons maintenant que nous voulions compter le nombre de fois qu'un client
   est dans la base de données.
   Un modèle XSLT comme celui qui suit semble une bonne piste :

```xml
<xsl:template match="client">
   <li><xsl:value-of select="count(//client[nom=./nom])"
   /></li>
   </xsl:template>
```

Malheureusement, entre les crochets (partie conditionnelle de l'expression
   XPath), le symbole « . » ne
   représente plus l'élément « client » XSLT courant, mais bien
   chacun des éléments « client » du
   document tour à tour : la condition « nom=./nom » est ici
   toujours satisfaite.
   Heureusement, il existe une fonction XSLT, appelée
   « current() », qui représente toujours
   l'élément XSLT courant. Donc, si nous voulons parcourir tout le document et
   trouver combien de fois chaque client est dans la liste,
   nous pourrions utiliser le document XSLT suivant :
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
   <xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:template match="listes">
   <html><body><ul>
   <xsl:apply-templates select="*" />
   </ul></body></html>
   </xsl:template>
   <xsl:template match="vendeur">
   <li><p>Nom du vendeur: <xsl:value-of select="@nom"
   /></p>
   <ul><xsl:apply-templates select="*" /></ul></li>
   </xsl:template>
   <xsl:template match="client">
   <li><xsl:value-of select="nom" />:
   <xsl:value-of select="count(//client[nom=current()/nom])"
   /></li>
   </xsl:template>
   </xsl:stylesheet>
```

Le résultat de la transformation sera alors :

```xml
<html><body><ul>
   <li>
   <p>Nom du vendeur: Jean</p>
   <ul>
   <li>Jacques:
   1</li>
   <li>Sylvain:
   2</li>
   <li>Claude:
   1</li>
   <li>Yvon:
   2</li>
   </ul>
   </li>
   <li>
   <p>Nom du vendeur: Raymond</p>
   <ul>
   <li>Arthur:
   1</li>
   <li>Sylvain:
   2</li>
   <li>Claudette:
   1</li>
   <li>Yvon:
   2</li>
   </ul>
   </li>
   </ul></body></html>
```
