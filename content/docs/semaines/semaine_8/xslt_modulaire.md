---
title: "XSLT modulaire"
weight: 60
---
<h1>
 XSLT modulaire
</h1>
<h2>
 Modularité avec les éléments « xsl:apply-templates »
</h2>
<p>
 Notre fichier « xslt.xml » se complexifie et devient 
    plus difficile à comprendre. Tout est dans un seul modèle, le modèle
 <i>
  facture
 </i>
 . 
    Pour simuler un problème probable, imaginons que notre XML est plus complexe et prend la forme :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
     &lt;?xml-stylesheet href="xslt.xml" type="application/xml"?&gt;
     &lt;facture&gt;
      &lt;montant&gt;10.10&lt;/montant&gt;
     &lt;recipiendaire&gt;
      &lt;personne&gt;
      &lt;sexe&gt;M&lt;/sexe&gt;
      &lt;nom&gt;Rochond&lt;/nom&gt;
      &lt;prenom&gt;Jean&lt;/prenom&gt;
      &lt;/personne&gt;
     &lt;/recipiendaire&gt;
     &lt;commercant&gt;
      &lt;personne&gt;
      &lt;sexe&gt;F&lt;/sexe&gt;
      &lt;nom&gt;Ladouce&lt;/nom&gt;
      &lt;prenom&gt;Jeanne&lt;/prenom&gt;
      &lt;/personne&gt;
      &lt;/commercant&gt;
      &lt;raison&gt;Achat d'ordinateur&lt;/raison&gt;
      &lt;/facture&gt;
</p>
<p>
 Dans ce nouveau document XML, se trouvent deux éléments « personne ». Il serait bête, 
    dans le document XSLT, de répéter le travail chaque fois qu'on veut afficher un élément « personne ». 
    Regardons ce que cela pourrait donner en pratique :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
     &lt;xsl:stylesheet version="1.0" 
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
     &lt;xsl:template match="facture"&gt;
     &lt;html&gt;
     &lt;head&gt;
     &lt;title&gt;Facture de &lt;xsl:value-of select="personne" /&gt;&lt;/title&gt;
     &lt;/head&gt;
     &lt;body&gt;
      &lt;p&gt;Ceci est une facture pour 
      &lt;xsl:value-of select="recipiendaire/personne/prenom" /&gt;
      &lt;xsl:text&gt; &lt;/xsl:text&gt;
      &lt;xsl:value-of select="recipiendaire/personne/nom" /&gt; 
      de &lt;xsl:value-of select="montant" /&gt;$ pour:
      &lt;xsl:value-of select="raison" /&gt;.&lt;/p&gt;
      &lt;p&gt;Votre commerçant: 
      &lt;xsl:value-of select="commercant/personne/prenom" /&gt;
      &lt;xsl:text&gt; &lt;/xsl:text&gt;
      &lt;xsl:value-of select="commercant/personne/nom" /&gt; &lt;/p&gt;
     &lt;/body&gt;
     &lt;/html&gt;
     &lt;/xsl:template&gt;
     &lt;/xsl:stylesheet&gt;
</p>
<p>
 Observez comment on répète le texte suivant à deux reprises :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;xsl:value-of select="recipiendaire/personne/prenom" /&gt;
            &lt;xsl:text&gt; &lt;/xsl:text&gt;
     &lt;xsl:value-of select="recipiendaire/personne/nom" /&gt;
</p>
<p>
 Voici une autre solution, plus élégante, qui donne le même résultat :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
     &lt;xsl:stylesheet version="1.0" 
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
    
     &lt;!-- d'abord un modèle pour les éléments facture --&gt;
     &lt;xsl:template match="facture"&gt;
     &lt;html&gt;
     &lt;head&gt;
     &lt;title&gt;Facture de &lt;xsl:value-of select="recipiendaire/personne" /&gt;&lt;/title&gt;
     &lt;/head&gt;
     &lt;body&gt;
      &lt;p&gt;Ceci est une facture pour 
      &lt;xsl:apply-templates select="recipiendaire" /&gt; 
      de &lt;xsl:value-of select="montant" /&gt;$ pour: 
      &lt;xsl:value-of select="raison" /&gt;.&lt;/p&gt;
      &lt;p&gt;Votre commerçant: &lt;xsl:apply-templates select="commercant" /&gt; &lt;/p&gt;
     &lt;/body&gt;
     &lt;/html&gt;
     &lt;/xsl:template&gt;
    
     &lt;!-- le modèle pour les éléments facture 
     utilise un modèle pour les éléments personne --&gt;
     &lt;xsl:template match="personne"&gt;
            &lt;xsl:value-of select="prenom" /&gt;
            &lt;xsl:text&gt; &lt;/xsl:text&gt;
            &lt;xsl:value-of select="nom" /&gt;
     &lt;/xsl:template&gt;
     &lt;/xsl:stylesheet&gt;
</p>
<p>
 Quelques éléments « xsl:value-of » ont été remplacés par des 
    éléments « xsl:apply-templates ». Un élément « xsl:apply-templates » prend le contenu 
    et, au lieu d'insérer le contenu textuel comme le fait « xsl:value-of » à l'endroit prévu, il insère plutôt le résultat 
    obtenu par l'application de modèles (éléments « xsl:template »).
    Ainsi, dans l'exemple que nous venons de voir, 
    chaque fois que le processeur XSLT rencontre 
    l'instruction « &lt;xsl:apply-templates select="recipiendaire" /&gt; », il 
    prend l'élément « recipiendaire » et essaie d'appliquer ses modèles. Comme il n'a pas de modèle pour
    les éléments « recipiendaire », il explore le contenu de l'élément et y trouve immédiatement un
    élément « personne ». Puisqu'il dispose d'un modèle pour ce type d'élément, il va l'appliquer.
    Par ailleurs, comme les éléments « recipiendaire » et « commercant » 
    ne contiennent qu'un élément « personne »,
    c'est donc le modèle défini pour les éléments « personne » qui s'appliquera
    dans les deux cas.
</p>
<p>
 Normalement, les éléments  « xsl:apply-templates » sont utilisés 
    au sein des éléments « xsl:template ». On peut aussi les
    utiliser au sein d'autres éléments que nous discuterons prochainement,
    « xsl:param » et « xsl:variable ».
</p>
<p>
 Notre fichier « xslt.xml » est maintenant plus modulaire, 
    parce qu'il contient deux modèles (éléments « xsl:template »).
</p>
<p>
 <b>
  En résumé, il est souvent préférable d'utiliser un élément « xsl:apply-templates » 
    qu'un élément « xsl:value-of » quand la complexité du modèle augmente; ceci permet d'assurer 
    la modularité et de garder la simplicité du document XSLT.
 </b>
</p>
<p>
 Par défaut, l'instruction apply-templates traite les nœuds dans l'ordre où ils
    se présentent dans le document original. On peut forcer le XSLT à trier les éléments
    avant de le traiter avec l'instruction xsl:sort. Dans notre exemple, on peut 
    remplacer l'élément &lt;xsl:apply-templates select="recipiendaire" /&gt; par cet élément
    si on veut que les individus soient triés par leur nom de famille.
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;xsl:apply-templates select="étudiant" &gt;
    &lt;xsl:sort select="personne/nom" order="ascending" data-type="text" /&gt;
    &lt;/xsl:apply-templates&gt;
</p>
<p>
 Si on souhaite un tri sur la valeur numérique d'une expression, on
    remplacera data-type="text" par data-type="number".
</p>
<p>
 On peut aussi importer un autre fichier XSLT avec l'instruction xsl:import. Celle-ci
    doit apparaître au tout début du fichier XSLT comme premier sous-élément de l'élément 
    xsl:stylesheet comme dans cet exemple :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
     &lt;xsl:stylesheet version="1.0" 
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
    &lt;xsl:import href="mesregles.xsl"/&gt;
     &lt;xsl:template match="facture"&gt;
     &lt;html&gt;
     &lt;head&gt;
     &lt;title&gt;Facture de &lt;xsl:value-of select="personne" /&gt;&lt;/title&gt;
     &lt;/head&gt;
     &lt;/xsl:template&gt;
     &lt;/xsl:stylesheet&gt;
</p>
<p>
 En cas de conflit entre les règles de fichier XSLT principal et 
    celles du fichier importé, les règles du fichier XSLT principal l'emporte.
</p>
