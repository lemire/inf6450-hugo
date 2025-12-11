---
title: "Les tests"
weight: 100
---
<h1 class="">
 Les tests
</h1>
<h2 class="recall">
 Utilisation des tests
</h2>
<p>
 Nous pouvons tester des conditions à l'aide d'expressions XPath contenant
    les symboles « &lt; », « = », « != »,
    « or », « and », « &gt; »,
    « &gt;= », « &lt;= ».
    Nous utilisons les tests en XSLT avec les éléments « xsl:choose »
    et « xsl:if ».
    Par exemple, faire quelque chose de particulier, si le nom de l'élément
    courant est « montant ».
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;xsl:template match="*"&gt;
    &lt;xsl:if test="name(.) = 'montant'"&gt;
    Il s'agit d'un élément nommé «montant».
    &lt;/xsl:if&gt;
    &lt;/xsl:template&gt;
</p>
<p>
 La syntaxe de l'élément « xsl:if » est très simple; si la valeur de
    l'expression XPath
    contenue dans l'attribut « test » est vraie, le contenu de
    l'élément « xsl:if » s'applique,
    sinon, on l'omet. Notez qu'il n'y a pas d'élément « xsl:else »
</p>
<p>
 Nous pouvons aussi traiter plusieurs tests dans un seul élément
    « xsl:choose » comme ceci :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;xsl:template match="*"&gt;
    &lt;xsl:choose&gt;
    &lt;xsl:when test="name(.)='montant'"&gt;
    Il y a une balise "montant"
    &lt;/xsl:when&gt;
    &lt;xsl:when test="name(.)='facture'"&gt;
    J'ai trouvé une "facture"
    &lt;/xsl:when&gt;
    &lt;xsl:otherwise&gt;
    Je ne connais pas cet élément
    &lt;/xsl:otherwise&gt;
    &lt;/xsl:choose&gt;
    &lt;/xsl:template&gt;
</p>
<p>
 On peut aussi combiner plusieurs tests avec les opérateurs logiques
    and, or et not comme le montre le prochain exemple.
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;xsl:template match="*"&gt;
    &lt;xsl:choose&gt;
    &lt;xsl:when test="name(.)='montant' or name(.)='facture'"&gt;
    Il y a une balise "montant" ou une
    balise "facture"
    &lt;/xsl:when&gt;
    &lt;xsl:when test="not(name(.)='argent')"&gt;
    Ce n'est ni montant, ni facture, ni argent.
    &lt;/xsl:when&gt;
    &lt;xsl:otherwise&gt;
    Je ne connais pas cet élément.
    &lt;/xsl:otherwise&gt;
    &lt;/xsl:choose&gt;
    &lt;/xsl:template&gt;
</p>
<p>
 On peut aussi tester la langue d'un élément avec la fonction
    XPath « lang ». L'expression « count(//p[lang('en')]) »
    compte le nombre d'élément « p » ayant été déclaré comme contenant
    du
    texte en langue anglaise.
</p>
<p>
 Observez qu'un élément « xsl:choose » contient plusieurs éléments
    « xsl:when »
    qui sont testés tour à tour, jusqu'à ce qu'une condition soit vraie;
    l'élément « xsl:otherwise »
    est présent pour l'éventualité où tous les tests échouent.
    Tous les tests sont réalisés en séquence et
    dès qu'une condition est vraie, les tests s'arrêtent et le contenu
    de l'élément « xsl:when » est évalué.
</p>
<p>
 En XSLT, il ne faut pas abuser des tests; il est préférable
    d'utiliser des éléments « xsl:template » qui sont plus modulaires.
</p>
