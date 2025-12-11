---
title: "Clés et aggrégation"
weight: 120
---

# Clés et aggrégation

## Obtenir l'aggrégation avec la fonction « generate-id »

Supposons qu'on veuille calculer le total des
   éléments « quantite », mais en faisant l'aggrégation
   pour chaque valeur de l'attribut « type » dans l'exemple suivant.

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
   <?xml-stylesheet href="produits.xsl" type="text/xsl" ?>
   <produits>
   <france>
   <quantite type="bain">53</quantite>
   <quantite type="chambre">12</quantite>
   </france>
   <canada>
   <quantite type="bain">14</quantite>
   <quantite type="chambre">12</quantite>
   </canada>
   </produits>
```

On pourrait tenter de résoudre ce problème avec une expression
   XPath de la forme « sum(//quantite[@type=current()/@type]) ».
   Malheureusement, on risque
   alors de calculer plusieurs fois la même somme. Par exemple, tentez
   d'appliquer
   la transformation suivante :
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
   <xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:template match="produits">
   <html>
   <body>
   <xsl:apply-templates select="*" />
   </body>
   </html>
   </xsl:template>
   <xsl:template match="quantite">
   <p>
   <xsl:value-of select="@type" />
   - <xsl:value-of select="sum(//quantite[@type=current()/@type])" />
   </p>
   </xsl:template>
   </xsl:stylesheet>
```

Vous obtiendrez alors le résultat suivant :

```xml
<html><body>
   <p>bain
   - 67</p>
   <p>chambre
   - 24</p>
   <p>bain
   - 67</p>
   <p>chambre
   - 24</p>
   </body></html>
```

Pour calculer la somme qu'une seule fois pour chaque valeur de l'attribut
   type,
   on pourrait ne faire le calcul que la première fois qu'on rencontre une
   valeur
   d'attribut donnée. L'expression XPath « //quantite[@type=x] »
   représente
   l'ensemble des éléments quantite ayant un attribut de valeur x.
   L'expression « //quantite[@type=x][1] » nous donne le premier
   élément de ce type
   rencontré.
   On pourrait penser que l'expression XPath
   « //quantite[@type=x][1]=current() » permet
   de déterminer si le nœud courant est le premier. Malheureusement,
   cette expression XPath vérifie plutôt si les deux éléments ont le même
   contenu.
   Comme nous avons deux éléments quantite ayant le même contenu dans notre
   exemple,
   cette solution ne suffit pas.
   La fonction generate-id quant à elle associe un identifiant unique à chaque
   nœud d'un
   document XML et permet donc de distinguer les éléments entre eux même
   lorsqu'ils ont le même contenu.
   L'expression
   « //quantite[@type=current()/@type]) » donne la séquence de tous
   les éléments quantite ayant un attribut type de même valeur que l'élément
   courant,
   alors que
   « (//quantite[@type=current()/@type])[1] »
   sélectionne le premier de cette liste.
   On peut vérifier si l'élément « quantite » est le premier
   du document ayant un certain type avec la fonction « generate-id »
   et l'expression « generate-id((//quantite[@type=current()/@type])[1])
   = generate-id(.) ».
   On peut aussi vérifier que c'est le dernier
   avec l'expression
   « generate-id((//quantite[@type=current()/@type])[last()])
   = generate-id(.) ». En utilisant cette astuce, on peut obtenir
   l'aggrégation
   souhaitée avec le programme XSLT suivant où l'on fait la somme seulement
   pour le premier élément rencontré ayant un certain type :
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
   <xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:template match="produits">
   <html>
   <body>
   <xsl:apply-templates select="*" />
   </body>
   </html>
   </xsl:template>
   <xsl:template match="quantite">
   <xsl:if
   test="generate-id((//quantite[@type=current()/@type])[1])
   = generate-id(.)" >
   <p>
   <xsl:value-of select="@type" />
   - <xsl:value-of select="sum(//quantite[@type=current()/@type])" />
   </p>
   </xsl:if>
   </xsl:template>
   </xsl:stylesheet>
```

On peut appliquer cette technique à notre exemple de la section précédente
   avec
   les vendeurs et les clients. La transformation suivante permet de ne
   calculer la fréquence
   de chaque client qu'une seule fois.
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
   <xsl:apply-templates select="*" />
   </xsl:template>
   <xsl:template match="client">
   <xsl:if
   test="generate-id(.)=generate-id(//client[nom=current()/nom][1])">
   <li><xsl:value-of select="nom" />:
   <xsl:value-of select="count(//client[nom=current()/nom])"
   /></li>
   </xsl:if>
   </xsl:template>
   </xsl:stylesheet>
```

Le résultat de cette transformation donne une liste désordonnée de
   clients :
```xml
<html><body><ul>
   <li>Jacques:
   1</li>
   <li>Sylvain:
   2</li>
   <li>Claude:
   1</li>
   <li>Yvon:
   2</li>
   <li>Arthur:
   1</li>
   <li>Claudette:
   1</li>
   </ul></body></html>
```

On peut trier le nom des clients en utilisant un
   élément xsl:sort :
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
   <xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:template match="listes">
   <html><body><ul>
   <xsl:for-each select="//client" >
   <xsl:sort select="nom" order="ascending" data-type="text" />
   <xsl:if
   test="generate-id(.)=generate-id(//client[nom=current()/nom][1])">
   <li><xsl:value-of select="nom" />:
   <xsl:value-of select="count(//client[nom=current()/nom])"
   /></li>
   </xsl:if>
   </xsl:for-each>
   </ul></body></html>
   </xsl:template>
   </xsl:stylesheet>
```

### Un peu plus de performance avec la fonction XSLT « key »

Cette section explore l'utilisation de la fonction XSLT « key » pour améliorer les performances lors de l'aggrégation de données.

Le problème avec l'utilisation d'expressions XPath telles que
   //client[nom=current()/nom] est qu'elles peuvent s'avérer coûteuses en temps
   de calcul si on les utilisent à répétition. Afin d'accélérer les choses
   et simplifier un peu nos programmes, on peut créer un
[tableau associatif](http://fr.wikipedia.org/wiki/Table_associative)
avec l'élément xsl:key et sa
   fonction correspondante key. Un tableau
   associatif est simplement une structure de donnée qui associe à chaque clef
   ou au plusieurs
   valeurs. Puisque ce tableau est construit une seule fois lorsque le
   processeur rencontre
   l'élément xsl:key, le processeur XSLT n'a pas à visiter les nœuds du
   document plusieurs fois.
   L'élément xsl:key comprend trois attributs incluant le nom du tableau
   associative (name),
   les clefs à inclure (use) et les nœuds à traiter (match). L'instruction
   `<xsl:key name="montableau" match="client" use="nom"/>` va créer un
   tableau associatif
   s'appelant montableau et qui associe à chaque valeur client/nom l'élément
   nom correspondant.
   La fonction key quant à elle prend deux paramètres incluant le nom du
   tableau et la valeur
   de la clef. À titre d'exemple, la transformation suivante permet de calculer
   la fréquence
   de chaque client comme à la question précédente, mais en utilisant un
   tableau associatif :
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
   <xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:key name="montableau" match="client" use="nom"/>
   <xsl:template match="listes">
   <html><body><ul>
   <xsl:for-each select="//client" >
   <xsl:sort select="nom" order="ascending" data-type="text" />
   <xsl:if test="generate-id(.)=generate-id(key('montableau',nom)[1])">
   <li><xsl:value-of select="nom" />:
   <xsl:value-of select="count(//client[nom=current()/nom])"
   /></li>
   </xsl:if>
   </xsl:for-each>
   </ul></body></html>
   </xsl:template>
   </xsl:stylesheet>
```
