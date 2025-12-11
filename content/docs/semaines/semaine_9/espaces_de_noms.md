---
title: "Espaces de noms"
weight: 50
---
<h1 class="">
 Espaces de noms
</h1>
<h2 class="recall">
 Espaces de noms
</h2>
<p>
 Les espaces de noms sont supportés et ne posent pas de problème. Il suffit
    de définir les préfixes, comme on le fait habituellement. Par exemple,
    considérons le code XML suivant :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml
    version="1.0" encoding="ISO-8859-1" ?&gt;
    &lt;?xml-stylesheet href="class2.xsl" type="text/xsl" ?&gt;
    &lt;université&gt;
    &lt;étudiant&gt;
    &lt;n:nom xmlns:n="http://www.mondomaine.com/"&gt;Réjean
    Tremblay&lt;/n:nom&gt;
    &lt;/étudiant&gt;
    &lt;/université&gt;
</p>
<p>
 Pour afficher le nom de l'étudiant, il suffira d'utiliser
    le document XSLT suivant :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
    &lt;xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:n="http://www.mondomaine.com/"&gt;
    &lt;xsl:template match="université" &gt;
    &lt;html&gt;&lt;body&gt;
    &lt;xsl:apply-templates select="étudiant/n:nom" /&gt;
    &lt;/body&gt;&lt;/html&gt;
    &lt;/xsl:template&gt;
    &lt;xsl:template match="n:nom" &gt;
    &lt;p&gt;&lt;xsl:value-of select="." /&gt;&lt;/p&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
<p>
 Observons que l'attribut « match="nom" » ne s'applique pas
    à l'élément « nom » dans l'espace de noms
    « http://www.mondomaine.com/ »,
    tel qu'il apparaît dans notre document XML : il est obligatoire
    d'utiliser un préfixe correspondant
    au bon espace de noms. Tout comme « match="*" » permet de
    sélectionner tous
    les éléments, « match="n:*" » permet de sélectionner tous les
    éléments qui sont
    dans un espace de noms donné.
</p>
