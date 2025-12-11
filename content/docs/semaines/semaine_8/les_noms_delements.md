---
title: "Les noms d’éléments"
weight: 70
---
<h1>
 Les noms d’éléments
</h1>
<h2 class="recall">
 Capturer le nom d'un élément
</h2>
<p>
 Supposons que nous voulions afficher uniquement les noms des éléments (sans
    leur contenu). Nous pouvons
    obtenir ce résultat avec la fonction XPath « name » qui donne le
    nom de l'élément.
    La fonction name inclut le préfixe de l'espace de noms. Si on souhaite le
    nom de l'élément sans
    le préfixe, on peut utiliser la fonction « local-name ». La
    fonction
    « namespace-uri » donne l'URI de l'espace de noms de l'élément.
</p>
<p>
 Ainsi, le document XSLT suivant permet d'afficher tous les noms des
    éléments XML, sans le
    contenu textuel de ces éléments.
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
    &lt;xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
    &lt;xsl:template match="*"&gt;
    &lt;xsl:value-of select="name(.)" /&gt;
    &lt;xsl:apply-templates select="*" /&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
<p>
 Nous pourrions aussi vouloir afficher non seulement le nom de l'élément
    courant, mais aussi le
    nom de l'élément-parent, ce qu'on peut faire avec le document XSLT
    suivant :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
    &lt;xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
    &lt;xsl:template match="*"&gt;
    &lt;xsl:value-of select="name(..)" /&gt; / &lt;xsl:value-of select="name(.)"
    /&gt;
    &lt;xsl:apply-templates select="*" /&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
