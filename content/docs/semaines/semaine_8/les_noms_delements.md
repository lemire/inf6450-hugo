---
title: "Les noms d’éléments"
weight: 70
---

# Les noms d’éléments

## Capturer le nom d'un élément

Dans cette section, nous apprenons à capturer et afficher les noms des éléments XML en utilisant les fonctions XPath name, local-name et namespace-uri.

Supposons que nous voulions afficher uniquement les noms des éléments (sans
   leur contenu). Nous pouvons
   obtenir ce résultat avec la fonction XPath « name » qui donne le
   nom de l'élément.
   La fonction name inclut le préfixe de l'espace de noms. Si on souhaite le
   nom de l'élément sans
   le préfixe, on peut utiliser la fonction « local-name ». La
   fonction
   « namespace-uri » donne l'URI de l'espace de noms de l'élément.

Ainsi, le document XSLT suivant permet d'afficher tous les noms des
   éléments XML, sans le
   contenu textuel de ces éléments.

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
   <xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:template match="*">
    <xsl:value-of select="name(.)" />
    <xsl:apply-templates select="*" />
   </xsl:template>
   </xsl:stylesheet>
```

Nous pourrions aussi vouloir afficher non seulement le nom de l'élément
   courant, mais aussi le
   nom de l'élément-parent, ce qu'on peut faire avec le document XSLT
   suivant :
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
   <xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:template match="*">
   <xsl:value-of select="name(..)" /> / <xsl:value-of select="name(.)"
   />
   <xsl:apply-templates select="*" />
   </xsl:template>
   </xsl:stylesheet>
```
