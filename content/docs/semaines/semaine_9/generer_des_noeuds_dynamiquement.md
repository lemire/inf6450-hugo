---
title: "Générer des noeuds dynamiquement"
weight: 20
---
<h1 class="">
 Générer des noeuds dynamiquement
</h1>
<h2 class="recall">
 Générer un commentaire
</h2>
<p>
 Il arrive qu'on veuille produire un commentaire dans la sortie XML. Rien
    de plus simple ! Il suffit d'utiliser l'instruction xsl:comment comme
    dans cet
    exemple :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
    &lt;xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
    &lt;xsl:comment&gt;Ceci est un commentaire.&lt;/xsl:comment&gt;
    &lt;/xsl:stylesheet&gt;
</p>
<p>
 Le résultat devrait ressembler à ceci :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
    &lt;!--Ceci est un commentaire.--&gt;
</p>
<h3 class="recall">
 Créer des éléments dynamiquement avec
    « xsl:element »
</h3>
<p>
 Il est parfois utile de créer dynamiquement un élément avec
    « xsl:element » et de créer des attributs avec
    « xsl:attribute ».
    Dans l'exemple suivant, on va créer un élément dont le nom nous est fourni
    par un paramètre.
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
    &lt;xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
    &lt;xsl:param name="ele" select="p" /&gt;
    &lt;xsl:template match="/"&gt;
    &lt;xsl:element name="{$ele}" namespace="http://mondom.com/" &gt;
    &lt;xsl:attribute name="couleur" namespace="http://mondom.com/"&gt;
    bleu
    &lt;/xsl:attribute&gt;
    &lt;/xsl:element&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
<h3 class="recall">
 Copier des nœuds avec « xsl:copy » et
    « xsl:copy-of »
</h3>
<p>
 Il est parfois nécessaire de dire au XSLT qu'on souhaite tout simplement
    recopier
    le nœud courant dans le document sortant. L'élément « xsl:copy »
    copie
    l'élément (seul, sans ses attributs mais avec son espace de noms) alors que
    l'élément
    « xsl:copy-of » permet de copier un élément ainsi que
    tous les nœuds qu'il contient. XSLT ne transforme pas les
    nœuds ainsi copiés, ils sont insérés dans le résultat directement.
    Par exemple, ce document XSLT va créer une copie
    intégrale du document:
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    version="1.0"&gt;
    &lt;xsl:output method="xml" version="1.0" indent="yes"
    encoding="ISO-8859-1"/&gt;
    &lt;xsl:template match="/"&gt;
    &lt;xsl:copy-of select="." /&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
<p>
 Dans le cas où l'on sélectionne plus d'un élément, notamment avec une
    expression du type nom|prenom,
    tous les éléments sont copiés l'un après l'autre. Ce comportement diffère de
    l'instruction value-of
    qui n'extrait le contenu textuel que du premier élément rencontré.
</p>
<p>
 Par contre, si on ne souhaite qu'un document XML qui contient le même
    élément-racine,
    mais sans le contenu de l'élément racine, on utilisera plutôt un élément
    « xsl:copy », comme ceci :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    version="1.0"&gt;
    &lt;xsl:output method="xml" version="1.0" indent="yes"
    encoding="ISO-8859-1"/&gt;
    &lt;xsl:template match="/*"&gt;
    &lt;xsl:copy/&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
<p>
 Naturellement, on peut même définir le contenu de l'élément copié à l'aide
    d'un modèle :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    version="1.0"&gt;
    &lt;xsl:output method="xml" version="1.0" indent="yes"
    encoding="ISO-8859-1"/&gt;
    &lt;xsl:template match="/*"&gt;
    &lt;xsl:copy &gt;
    &lt;a&gt;x&lt;/a&gt;
    &lt;/xsl:copy&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
<p>
 Si on souhaite ne copier qu'une partie du contenu de l'élément ainsi
    reproduit, par exemple
    ses attributs, on peut utiliser copy-of :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    version="1.0"&gt;
    &lt;xsl:output method="xml" version="1.0" indent="yes"
    encoding="ISO-8859-1"/&gt;
    &lt;xsl:template match="/*"&gt;
    &lt;xsl:copy &gt;
    &lt;xsl:copy-of select="@*"/&gt;
    &lt;a&gt;x&lt;/a&gt;
    &lt;/xsl:copy&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
