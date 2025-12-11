---
title: "Les boucles"
weight: 110
---
<h1 class="">
 Les boucles
</h1>
<h2 class="recall">
 Utiliser XSLT comme base de données et éléments
    « for-each »
</h2>
<p>
 L'exemple de la liste des clients avec leur numéro de téléphone nous permet
    de faire plus. Tout d'abord, l'expression « //client » donne une
    séquence de tous les éléments « client »
    dans le nœud courant.
    Avec l'expression XPath « //client[nom='Sylvain'] », nous pouvons
    obtenir la séquence de tous les
    éléments « client » ayant pour nom « Sylvain ». Dans ce
    cas précis, il y a plus d'un élément
    dans la réponse. Pour visiter l'ensemble des éléments dans la séquence,
    il suffit d'utiliser l'élément « xsl:for-each » comme ceci :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
    &lt;xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
    &lt;xsl:template match="/"&gt;
    &lt;html&gt;&lt;body&gt;Numéros de téléphone pour Sylvain:
    &lt;ul&gt;
    &lt;xsl:for-each select="//client[nom='Sylvain']/@telephone" &gt;
    &lt;li&gt;&lt;xsl:value-of select="." /&gt;&lt;/li&gt;
    &lt;/xsl:for-each&gt;
    &lt;/ul&gt;
    &lt;/body&gt;&lt;/html&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
<p>
 Le résultat de l'application de ce fichier XSLT au fichier XML contenant les
    numéros de téléphone sera :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;html&gt;&lt;body&gt;Numéros de téléphone pour Sylvain:
    &lt;ul&gt;
    &lt;li&gt;545-5455&lt;/li&gt;
    &lt;li&gt;545-5456&lt;/li&gt;
    &lt;/ul&gt;
    &lt;/body&gt;&lt;/html&gt;
</p>
<p>
 Dans une telle boucle, il peut être utile de savoir quel est le numéro du
    nœud
    courant. On obtient ce numéro avec la fonction XSLT « position() »
    qui a la valeur 1 quand
    il s'agit du premier nœud et la valeur « last() » quand il s'agit
    du dernier nœud.
    On peut aussi utiliser une instruction xsl:sort au sein d'un élément
    for-each.
</p>
<p>
 Supposons maintenant que nous voulions compter le nombre de fois qu'un client
    est dans la base de données.
    Un modèle XSLT comme celui qui suit semble une bonne piste :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;xsl:template match="client"&gt;
    &lt;li&gt;&lt;xsl:value-of select="count(//client[nom=./nom])"
    /&gt;&lt;/li&gt;
    &lt;/xsl:template&gt;
</p>
<p>
 Malheureusement, entre les crochets (partie conditionnelle de l'expression
    XPath), le symbole « . » ne
    représente plus l'élément « client » XSLT courant, mais bien
    chacun des éléments « client » du
    document tour à tour : la condition « nom=./nom » est ici
    toujours satisfaite.
    Heureusement, il existe une fonction XSLT, appelée
    « current() », qui représente toujours
    l'élément XSLT courant. Donc, si nous voulons parcourir tout le document et
    trouver combien de fois chaque client est dans la liste,
    nous pourrions utiliser le document XSLT suivant :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
    &lt;xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
    &lt;xsl:template match="listes"&gt;
    &lt;html&gt;&lt;body&gt;&lt;ul&gt;
    &lt;xsl:apply-templates select="*" /&gt;
    &lt;/ul&gt;&lt;/body&gt;&lt;/html&gt;
    &lt;/xsl:template&gt;
    &lt;xsl:template match="vendeur"&gt;
    &lt;li&gt;&lt;p&gt;Nom du vendeur: &lt;xsl:value-of select="@nom"
    /&gt;&lt;/p&gt;
    &lt;ul&gt;&lt;xsl:apply-templates select="*" /&gt;&lt;/ul&gt;&lt;/li&gt;
    &lt;/xsl:template&gt;
    &lt;xsl:template match="client"&gt;
    &lt;li&gt;&lt;xsl:value-of select="nom" /&gt;:
    &lt;xsl:value-of select="count(//client[nom=current()/nom])"
    /&gt;&lt;/li&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
<p>
 Le résultat de la transformation sera alors :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;html&gt;&lt;body&gt;&lt;ul&gt;
    &lt;li&gt;
    &lt;p&gt;Nom du vendeur: Jean&lt;/p&gt;
    &lt;ul&gt;
    &lt;li&gt;Jacques:
    1&lt;/li&gt;
    &lt;li&gt;Sylvain:
    2&lt;/li&gt;
    &lt;li&gt;Claude:
    1&lt;/li&gt;
    &lt;li&gt;Yvon:
    2&lt;/li&gt;
    &lt;/ul&gt;
    &lt;/li&gt;
    &lt;li&gt;
    &lt;p&gt;Nom du vendeur: Raymond&lt;/p&gt;
    &lt;ul&gt;
    &lt;li&gt;Arthur:
    1&lt;/li&gt;
    &lt;li&gt;Sylvain:
    2&lt;/li&gt;
    &lt;li&gt;Claudette:
    1&lt;/li&gt;
    &lt;li&gt;Yvon:
    2&lt;/li&gt;
    &lt;/ul&gt;
    &lt;/li&gt;
    &lt;/ul&gt;&lt;/body&gt;&lt;/html&gt;
</p>
