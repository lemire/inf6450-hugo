---
title: "Générer des noeuds dynamiquement"
weight: 20
---

# Générer des noeuds dynamiquement
## Générer un commentaire

Cette section explique comment générer des commentaires dans la sortie XML à l'aide de XSLT.

Il arrive qu'on veuille produire un commentaire dans la sortie XML. Rien
    de plus simple ! Il suffit d'utiliser l'instruction xsl:comment comme
    dans cet
    exemple :

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
   <xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:comment>Ceci est un commentaire.</xsl:comment>
   </xsl:stylesheet>
```

Le résultat devrait ressembler à ceci :

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
   <!--Ceci est un commentaire.-->
```
### Créer des éléments dynamiquement avec « xsl:element »

Cette section montre comment créer des éléments XML dynamiquement en utilisant xsl:element et xsl:attribute.

Il est parfois utile de créer dynamiquement un élément avec
    « xsl:element » et de créer des attributs avec
    « xsl:attribute ».
    Dans l'exemple suivant, on va créer un élément dont le nom nous est fourni
    par un paramètre.

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
   <xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:param name="ele" select="p" />
   <xsl:template match="/">
   <xsl:element name="{$ele}" namespace="http://mondom.com/" >
   <xsl:attribute name="couleur" namespace="http://mondom.com/">
   bleu
   </xsl:attribute>
   </xsl:element>
   </xsl:template>
   </xsl:stylesheet>
```
### Copier des nœuds avec « xsl:copy » et « xsl:copy-of »

Cette section explique comment copier des nœuds XML en utilisant xsl:copy et xsl:copy-of.

Il est parfois nécessaire de dire au XSLT qu'on souhaite tout simplement
    recopier
    le nœud courant dans le document sortant. L'élément « xsl:copy »
    copie
    l'élément (seul, sans ses attributs mais avec son espace de noms) alors que
    l'élément
    « xsl:copy-of » permet de copier un élément ainsi que
    tous les nœuds qu'il contient. XSLT ne transforme pas les
    nœuds ainsi copiés, ils sont insérés dans le résultat directement.
    Par exemple, ce document XSLT va créer une copie
    intégrale du document:

```xml
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
   version="1.0">
   <xsl:output method="xml" version="1.0" indent="yes"
   encoding="ISO-8859-1"/>
   <xsl:template match="/">
   <xsl:copy-of select="." />
   </xsl:template>
   </xsl:stylesheet>
```

Dans le cas où l'on sélectionne plus d'un élément, notamment avec une
    expression du type nom|prenom,
    tous les éléments sont copiés l'un après l'autre. Ce comportement diffère de
    l'instruction value-of
    qui n'extrait le contenu textuel que du premier élément rencontré.

Par contre, si on ne souhaite qu'un document XML qui contient le même
    élément-racine,
    mais sans le contenu de l'élément racine, on utilisera plutôt un élément
    « xsl:copy », comme ceci :

```xml
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
   version="1.0">
   <xsl:output method="xml" version="1.0" indent="yes"
   encoding="ISO-8859-1"/>
   <xsl:template match="/*">
   <xsl:copy/>
   </xsl:template>
   </xsl:stylesheet>
```

Naturellement, on peut même définir le contenu de l'élément copié à l'aide
    d'un modèle :

```xml
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
   version="1.0">
   <xsl:output method="xml" version="1.0" indent="yes"
   encoding="ISO-8859-1"/>
   <xsl:template match="/*">
   <xsl:copy >
   <a>x</a>
   </xsl:copy>
   </xsl:template>
   </xsl:stylesheet>
```

Si on souhaite ne copier qu'une partie du contenu de l'élément ainsi
    reproduit, par exemple
    ses attributs, on peut utiliser copy-of :

```xml
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
   version="1.0">
   <xsl:output method="xml" version="1.0" indent="yes"
   encoding="ISO-8859-1"/>
   <xsl:template match="/*">
   <xsl:copy >
   <xsl:copy-of select="@*"/>
   <a>x</a>
   </xsl:copy>
   </xsl:template>
   </xsl:stylesheet>
```
