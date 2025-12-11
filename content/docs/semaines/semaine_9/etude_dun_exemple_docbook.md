---
title: "Étude d’un exemple (DocBook)"
weight: 70
---

# Étude d’un exemple (DocBook)

## L'étude d'un exemple: docbook.xslt

On peut utiliser [un document XSLT pour transformer des documents DocBook simple en HTML](http://www.google.com).

Nous allons passer en revue brièvement les éléments « xsl:template » qu'il contient.

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" indent="yes"
    encoding="ISO-8859-1" />
    <xsl:template match="book"> <html>
    <head><xsl:apply-templates select="bookinfo"/></head>
    <body><h1><xsl:value-of select="bookinfo/title"
    /></h1>
    <p style="text-indent:1em;">
    <xsl:value-of select="bookinfo/author/firstname" />
    <xsl:text> </xsl:text>
    <xsl:value-of select="bookinfo/author/surname" />
    &#169; <xsl:value-of select="bookinfo/copyright/year" />
    </p><h2>Table des matières</h2>
    <ul><xsl:apply-templates select="chapter"
    mode="tdm"/></ul>
    <xsl:apply-templates select="chapter"/>
    </body></html>
    </xsl:template>
    <xsl:template match="bookinfo">
    <title><xsl:value-of select="title" />
    par <xsl:value-of select="author/firstname" /><xsl:text>
    </xsl:text><xsl:value-of select="author/surname" />
    </title>
    </xsl:template>
    <xsl:template match="chapter" mode="tdm">
    <li><a href="#{generate-id(.)}">
    <xsl:number format="digit" lang="fr" count="chapter"/>.
    <xsl:value-of select="title" /></a></li>
    <ul><xsl:apply-templates select="section"
    mode="tdm"/></ul>
    </xsl:template>
    <xsl:template match="section" mode="tdm">
    <li><a href="#{generate-id(.)}">
    <xsl:number format="digit" lang="fr" count="chapter"/>.
    <xsl:number format="digit" lang="fr" count="section"/>
    <xsl:text> </xsl:text>
    <xsl:value-of select="title" /></a></li>
    </xsl:template>
    <xsl:template match="chapter">
    <h2><a name="{generate-id(.)}" >Chapitre
    <xsl:number format="digit" lang="fr"
    count="chapter"/>.<xsl:text> </xsl:text>
    <xsl:value-of select="title" /></a></h2>
    <div style="margin-left:1em">
    <xsl:apply-templates select="section"/> </div>
    </xsl:template>
    <xsl:template match="section">
    <h3><a name="{generate-id(.)}">
    <xsl:number format="digit" lang="fr" count="chapter"/>.
    <xsl:number format="digit" lang="fr" count="section"/>
    <xsl:text> </xsl:text>
    <xsl:value-of select="title" /></a></h3>
    <div style="margin-left:1em">
    <xsl:apply-templates/>
    </div>
    </xsl:template>
    <xsl:template match="itemizedlist">
    <ul style="margin-left:1em"><xsl:apply-templates /></ul>
    </xsl:template>
    <xsl:template match="orderedlist">
    <ol style="margin-left:1em"><xsl:apply-templates /></ol>
    </xsl:template>
    <xsl:template match="listitem">
    <li style="text-indent:0.5em"><xsl:apply-templates /></li>
    </xsl:template>
    <xsl:template match="programlisting">
    <pre style="color:blue;background-color:rgb(200,200,200);
        margin-left:1em"><code>
    <xsl:apply-templates />
    </code></pre>
    </xsl:template>
    <xsl:template match="para">
    <xsl:choose>
    <xsl:when test="name(..) =
        'listitem'"><xsl:apply-templates /></xsl:when>
    <xsl:otherwise><p><xsl:apply-templates /></p>
    </xsl:otherwise>
    </xsl:choose>
    </xsl:template>
    <xsl:template match="title" />
    </xsl:stylesheet>
```

Le premier élément « xsl:template » sert à capturer l'élément « book ». Comme il s'agit de l'élément-racine, on en profite pour produire les éléments « html », « head » et « body ». Le contenu de l'élément « head » sera rempli par l'élément « xsl:template » traitant l'élément DocBook « bookinfo ». On affiche immédiatement le prénom et le nom de l'auteur à l'aide des expressions XPath « bookinfo/author/firstname » et « bookinfo/author/surname ». Notez l'utilisation de l'élément <xsl:text> </xsl:text> pour produire un espace entre le nom et le prénom. En effet, sans cet élément, il n'y aurait pas d'espace puisque les espaces et retours de charriot sont ignorés dans les fichiers XSLT. Le reste du document est produit avec les deux éléments « xsl:template » traitant les éléments « chapter » : on utilise le l'attribut mode « tdm » pour produire la table des matières, et le reste du document est produit avec le traitement des éléments « chapter » par défaut (sans attribut mode).

```xml
<xsl:template match="book"> <html>
    <head><xsl:apply-templates select="bookinfo"/></head>
    <body><h1><xsl:value-of select="bookinfo/title"
    /></h1>
    <p style="text-indent:1em;">
    <xsl:value-of select="bookinfo/author/firstname" />
    <xsl:text> </xsl:text>
    <xsl:value-of select="bookinfo/author/surname" />
    &#169; <xsl:value-of select="bookinfo/copyright/year" />
    </p><h2>Table des matières</h2>
    <ul><xsl:apply-templates select="chapter"
    mode="tdm"/></ul>
    <xsl:apply-templates select="chapter"/>
    </body></html>
    </xsl:template>
```

L'élément « xsl:template » traitant l'élément DocBook « bookinfo » est simple : l'expression XPath « title » permet de trouver le titre du document puisqu'un élément « title » doit être présent dans tout élément DocBook « bookinfo ». Comme on l'a fait précédemment, on trouve le prénom et le nom de l'auteur, mais cette fois-ci, avec les expressions XPath « author/firstname » et « author/surname » puisque nous sommes maintenant au sein d'un élément « bookinfo ».

```xml
<xsl:template match="bookinfo">
    <title><xsl:value-of select="title" />
    par <xsl:value-of select="author/firstname" /><xsl:text>
    </xsl:text><xsl:value-of select="author/surname" />
    </title>
    </xsl:template>
```

Les élément « xsl:template » avec attribut mode génèrent la table des matières. Les éléments « xsl:number » permettent de numéroter automatiquement les chapitres et sections. Afin de générer des hyperliens permettant de naviguer dans le document à partir de la table des matières, on utilise des fragments générés à partir de la fonction XSLT « generate-id ». Lorsque nous générons le contenu du document lui-même, on utilise à nouveau la fonction XSLT « generate-id » pour placer des ancres dans le document au bon endroit. L'avantage de la fonction XSLT « generate-id » est qu'elle permet de générer facilement un identifiant unique pour chaque paragraphe.

```xml
<xsl:template match="chapter" mode="tdm">
    <li><a href="#{generate-id(.)}">
    <xsl:number format="digit" lang="fr" count="chapter"/>.
    <xsl:value-of select="title" /></a></li>
    <ul><xsl:apply-templates select="section"
    mode="tdm"/></ul>
    </xsl:template>
    <xsl:template match="section" mode="tdm">
    <li><a href="#{generate-id(.)}">
    <xsl:number format="digit" lang="fr" count="chapter"/>.
    <xsl:number format="digit" lang="fr" count="section"/>
    <xsl:text> </xsl:text>
    <xsl:value-of select="title" /></a></li>
    </xsl:template>
```

Les élément « xsl:template » sans attribut mode génèrent le document lui-même. La principale différence avec la génération de la table des matières est la présence de l'élément <xsl:apply-templates/> qui traite le contenu des éléments « section ».

```xml
<xsl:template match="chapter">
    <h2><a name="{generate-id(.)}" >Chapitre
    <xsl:number format="digit" lang="fr"
    count="chapter"/>.<xsl:text> </xsl:text>
    <xsl:value-of select="title" /></a></h2>
    <div style="margin-left:1em">
    <xsl:apply-templates select="section"/> </div>
    </xsl:template>
    <xsl:template match="section">
    <h3><a name="{generate-id(.)}">
    <xsl:number format="digit" lang="fr" count="chapter"/>.
    <xsl:number format="digit" lang="fr" count="section"/>
    <xsl:text> </xsl:text>
    <xsl:value-of select="title" /></a></h3>
    <div style="margin-left:1em">
    <xsl:apply-templates/>
    </div>
    </xsl:template>
```

Le traitement des éléments DocBook « itemizedlist », « orderedlist » et « listitem » est simple : il suffit de les convertir en éléments HTML « ul », « ol » et « li » respectivement.

```xml
<xsl:template match="itemizedlist">
    <ul style="margin-left:1em"><xsl:apply-templates /></ul>
    </xsl:template>
    <xsl:template match="orderedlist">
    <ol style="margin-left:1em"><xsl:apply-templates /></ol>
    </xsl:template>
    <xsl:template match="listitem">
    <li style="text-indent:0.5em"><xsl:apply-templates /></li>
    </xsl:template>
```

Les éléments DocBook « programlisting » sont convertis en éléments HTML « pre » ( *préformaté* ).

```xml
<xsl:template match="programlisting">
    <pre
    style="color:blue;background-color:rgb(200,200,200); margin-left:1em">
    <code>
    <xsl:apply-templates />
    </code></pre>
    </xsl:template>
```

Les éléments DocBook « para » sont convertis en éléments HTML « p » sauf lorsqu'ils sont au sein d'un élément DocBook « listitem ».

```xml
<xsl:template match="para">
    <xsl:choose>
    <xsl:when test="name(..) = 'listitem'">
    <xsl:apply-templates /></xsl:when>
    <xsl:otherwise><p><xsl:apply-templates /></p>
    </xsl:otherwise>
    </xsl:choose>
    </xsl:template>
    </xsl:stylesheet>
```

Les éléments DocBook « title » ne doivent pas être traités directement lorsqu'on les rencontre.

```xml
<xsl:template match="title" />
```