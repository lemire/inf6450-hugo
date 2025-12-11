---
title: "Clés et aggrégation"
weight: 120
---
<h1 class="">
 Clés et aggrégation
</h1>
<h2 class="recall">
 Obtenir l'aggrégation avec la fonction
    « generate-id »
</h2>
<p>
 Supposons qu'on veuille calculer le total des
    éléments « quantite », mais en faisant l'aggrégation
    pour chaque valeur de l'attribut « type » dans l'exemple suivant.
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
    &lt;?xml-stylesheet href="produits.xsl" type="text/xsl" ?&gt;
    &lt;produits&gt;
    &lt;france&gt;
    &lt;quantite type="bain"&gt;53&lt;/quantite&gt;
    &lt;quantite type="chambre"&gt;12&lt;/quantite&gt;
    &lt;/france&gt;
    &lt;canada&gt;
    &lt;quantite type="bain"&gt;14&lt;/quantite&gt;
    &lt;quantite type="chambre"&gt;12&lt;/quantite&gt;
    &lt;/canada&gt;
    &lt;/produits&gt;
</p>
<p>
 On pourrait tenter de résoudre ce problème avec une expression
    XPath de la forme « sum(//quantite[@type=current()/@type]) ».
    Malheureusement, on risque
    alors de calculer plusieurs fois la même somme. Par exemple, tentez
    d'appliquer
    la transformation suivante :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
    &lt;xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
    &lt;xsl:template match="produits"&gt;
    &lt;html&gt;
    &lt;body&gt;
    &lt;xsl:apply-templates select="*" /&gt;
    &lt;/body&gt;
    &lt;/html&gt;
    &lt;/xsl:template&gt;
    &lt;xsl:template match="quantite"&gt;
    &lt;p&gt;
    &lt;xsl:value-of select="@type" /&gt;
    - &lt;xsl:value-of select="sum(//quantite[@type=current()/@type])" /&gt;
    &lt;/p&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
<p>
 Vous obtiendrez alors le résultat suivant :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;html&gt;&lt;body&gt;
    &lt;p&gt;bain
    - 67&lt;/p&gt;
    &lt;p&gt;chambre
    - 24&lt;/p&gt;
    &lt;p&gt;bain
    - 67&lt;/p&gt;
    &lt;p&gt;chambre
    - 24&lt;/p&gt;
    &lt;/body&gt;&lt;/html&gt;
</p>
<p>
 Pour calculer la somme qu'une seule fois pour chaque valeur de l'attribut
    type,
    on pourrait ne faire le calcul que la première fois qu'on rencontre une
    valeur
    d'attribut donnée. L'expression XPath « //quantite[@type=x] »
    représente
    l'ensemble des éléments quantite ayant un attribut de valeur x.
    L'expression « //quantite[@type=x][1] » nous donne le premier
    élément de ce type
    rencontré.
    On pourrait penser que l'expression XPath
    « //quantite[@type=x][1]=current() » permet
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
    « //quantite[@type=current()/@type]) » donne la séquence de tous
    les éléments quantite ayant un attribut type de même valeur que l'élément
    courant,
    alors que
    « (//quantite[@type=current()/@type])[1] »
    sélectionne le premier de cette liste.
    On peut vérifier si l'élément « quantite » est le premier
    du document ayant un certain type avec la fonction « generate-id »
    et l'expression « generate-id((//quantite[@type=current()/@type])[1])
    = generate-id(.) ».
    On peut aussi vérifier que c'est le dernier
    avec l'expression
    « generate-id((//quantite[@type=current()/@type])[last()])
    = generate-id(.) ». En utilisant cette astuce, on peut obtenir
    l'aggrégation
    souhaitée avec le programme XSLT suivant où l'on fait la somme seulement
    pour le premier élément rencontré ayant un certain type :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
    &lt;xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
    &lt;xsl:template match="produits"&gt;
    &lt;html&gt;
    &lt;body&gt;
    &lt;xsl:apply-templates select="*" /&gt;
    &lt;/body&gt;
    &lt;/html&gt;
    &lt;/xsl:template&gt;
    &lt;xsl:template match="quantite"&gt;
    &lt;xsl:if
    test="generate-id((//quantite[@type=current()/@type])[1])
    = generate-id(.)" &gt;
    &lt;p&gt;
    &lt;xsl:value-of select="@type" /&gt;
    - &lt;xsl:value-of select="sum(//quantite[@type=current()/@type])" /&gt;
    &lt;/p&gt;
    &lt;/xsl:if&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
<p>
 On peut appliquer cette technique à notre exemple de la section précédente
    avec
    les vendeurs et les clients. La transformation suivante permet de ne
    calculer la fréquence
    de chaque client qu'une seule fois.
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
    &lt;xsl:apply-templates select="*" /&gt;
    &lt;/xsl:template&gt;
    &lt;xsl:template match="client"&gt;
    &lt;xsl:if
    test="generate-id(.)=generate-id(//client[nom=current()/nom][1])"&gt;
    &lt;li&gt;&lt;xsl:value-of select="nom" /&gt;:
    &lt;xsl:value-of select="count(//client[nom=current()/nom])"
    /&gt;&lt;/li&gt;
    &lt;/xsl:if&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
<p>
 Le résultat de cette transformation donne une liste désordonnée de
    clients :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;html&gt;&lt;body&gt;&lt;ul&gt;
    &lt;li&gt;Jacques:
    1&lt;/li&gt;
    &lt;li&gt;Sylvain:
    2&lt;/li&gt;
    &lt;li&gt;Claude:
    1&lt;/li&gt;
    &lt;li&gt;Yvon:
    2&lt;/li&gt;
    &lt;li&gt;Arthur:
    1&lt;/li&gt;
    &lt;li&gt;Claudette:
    1&lt;/li&gt;
    &lt;/ul&gt;&lt;/body&gt;&lt;/html&gt;
</p>
<p>
 On peut trier le nom des clients en utilisant un
    élément xsl:sort :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
    &lt;xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
    &lt;xsl:template match="listes"&gt;
    &lt;html&gt;&lt;body&gt;&lt;ul&gt;
    &lt;xsl:for-each select="//client" &gt;
    &lt;xsl:sort select="nom" order="ascending" data-type="text" /&gt;
    &lt;xsl:if
    test="generate-id(.)=generate-id(//client[nom=current()/nom][1])"&gt;
    &lt;li&gt;&lt;xsl:value-of select="nom" /&gt;:
    &lt;xsl:value-of select="count(//client[nom=current()/nom])"
    /&gt;&lt;/li&gt;
    &lt;/xsl:if&gt;
    &lt;/xsl:for-each&gt;
    &lt;/ul&gt;&lt;/body&gt;&lt;/html&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
<h3 class="recall">
 Un peu plus de performance avec la fonction XSLT
    « key »
</h3>
<p>
 Le problème avec l'utilisation d'expressions XPath telles que
    //client[nom=current()/nom] est qu'elles peuvent s'avérer coûteuses en temps
    de calcul si on les utilisent à répétition. Afin d'accélérer les choses
    et simplifier un peu nos programmes, on peut créer un
 <a href="http://fr.wikipedia.org/wiki/Table_associative" shape="rect">
  tableau associatif
 </a>
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
    &lt;xsl:key name="montableau" match="client" use="nom"/&gt; va créer un
    tableau associatif
    s'appelant montableau et qui associe à chaque valeur client/nom l'élément
    nom correspondant.
    La fonction key quant à elle prend deux paramètres incluant le nom du
    tableau et la valeur
    de la clef. À titre d'exemple, la transformation suivante permet de calculer
    la fréquence
    de chaque client comme à la question précédente, mais en utilisant un
    tableau associatif :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
    &lt;xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
    &lt;xsl:key name="montableau" match="client" use="nom"/&gt;
    &lt;xsl:template match="listes"&gt;
    &lt;html&gt;&lt;body&gt;&lt;ul&gt;
    &lt;xsl:for-each select="//client" &gt;
    &lt;xsl:sort select="nom" order="ascending" data-type="text" /&gt;
    &lt;xsl:if test="generate-id(.)=generate-id(key('montableau',nom)[1])"&gt;
    &lt;li&gt;&lt;xsl:value-of select="nom" /&gt;:
    &lt;xsl:value-of select="count(//client[nom=current()/nom])"
    /&gt;&lt;/li&gt;
    &lt;/xsl:if&gt;
    &lt;/xsl:for-each&gt;
    &lt;/ul&gt;&lt;/body&gt;&lt;/html&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
