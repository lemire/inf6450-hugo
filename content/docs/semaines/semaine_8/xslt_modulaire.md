---
title: "XSLT modulaire"
weight: 60
---

# XSLT modulaire
## Modularité avec les éléments « xsl:apply-templates »

Cette section explique comment utiliser l'élément xsl:apply-templates pour rendre les feuilles de style XSLT plus modulaires et réutilisables, en évitant la répétition de code.

Notre fichier « xslt.xml » se complexifie et devient plus difficile à comprendre. Tout est dans un seul modèle, le modèle *facture*. Pour simuler un problème probable, imaginons que notre XML est plus complexe et prend la forme :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
    <?xml-stylesheet href="xslt.xml" type="application/xml"?>
    <facture>
     <montant>10.10</montant>
    <recipiendaire>
        <personne>
            <sexe>M</sexe>
            <nom>Rochond</nom>
            <prenom>Jean</prenom>
        </personne>
    </recipiendaire>
    <commercant>
        <personne>
            <sexe>F</sexe>
            <nom>Ladouce</nom>
            <prenom>Jeanne</prenom>
        </personne>
     </commercant>
     <raison>Achat d'ordinateur</raison>
     </facture>
```

Dans ce nouveau document XML, se trouvent deux éléments « personne ». Il serait bête, dans le document XSLT, de répéter le travail chaque fois qu'on veut afficher un élément « personne ». Regardons ce que cela pourrait donner en pratique :
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
    <xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="facture">
    <html>
    <head>
    <title>Facture de <xsl:value-of select="personne" /></title>
    </head>
    <body>
     <p>Ceci est une facture pour 
     <xsl:value-of select="recipiendaire/personne/prenom" />
     <xsl:text> </xsl:text>
     <xsl:value-of select="recipiendaire/personne/nom" /> 
     de <xsl:value-of select="montant" />$ pour:
     <xsl:value-of select="raison" />.</p>
     <p>Votre commerçant: 
     <xsl:value-of select="commercant/personne/prenom" />
     <xsl:text> </xsl:text>
     <xsl:value-of select="commercant/personne/nom" /> </p>
    </body>
    </html>
    </xsl:template>
    </xsl:stylesheet>
```

Observez comment on répète le texte suivant à deux reprises :

```xml
<xsl:value-of select="recipiendaire/personne/prenom" />
           <xsl:text> </xsl:text>
    <xsl:value-of select="recipiendaire/personne/nom" />
```

Voici une autre solution, plus élégante, qui donne le même résultat :

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
    <xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <!-- d'abord un modèle pour les éléments facture -->
    <xsl:template match="facture">
    <html>
    <head>
    <title>Facture de <xsl:value-of select="recipiendaire/personne" /></title>
    </head>
    <body>
     <p>Ceci est une facture pour 
     <xsl:apply-templates select="recipiendaire" /> 
     de <xsl:value-of select="montant" />$ pour: 
     <xsl:value-of select="raison" />.</p>
     <p>Votre commerçant: <xsl:apply-templates select="commercant" /> </p>
    </body>
    </html>
    </xsl:template>
    <!-- le modèle pour les éléments facture 
    utilise un modèle pour les éléments personne -->
    <xsl:template match="personne">
           <xsl:value-of select="prenom" />
           <xsl:text> </xsl:text>
           <xsl:value-of select="nom" />
    </xsl:template>
    </xsl:stylesheet>
```

Quelques éléments « xsl:value-of » ont été remplacés par des éléments « xsl:apply-templates ». Un élément « xsl:apply-templates » prend le contenu et, au lieu d'insérer le contenu textuel comme le fait « xsl:value-of » à l'endroit prévu, il insère plutôt le résultat obtenu par l'application de modèles (éléments « xsl:template »). Ainsi, dans l'exemple que nous venons de voir, chaque fois que le processeur XSLT rencontre l'instruction « <xsl:apply-templates select="recipiendaire" /> », il prend l'élément « recipiendaire » et essaie d'appliquer ses modèles. Comme il n'a pas de modèle pour les éléments « recipiendaire », il explore le contenu de l'élément et y trouve immédiatement un élément « personne ». Puisqu'il dispose d'un modèle pour ce type d'élément, il va l'appliquer. Par ailleurs, comme les éléments « recipiendaire » et « commercant » ne contiennent qu'un élément « personne », c'est donc le modèle défini pour les éléments « personne » qui s'appliquera dans les deux cas.

Normalement, les éléments « xsl:apply-templates » sont utilisés au sein des éléments « xsl:template ». On peut aussi les utiliser au sein d'autres éléments que nous discuterons prochainement, « xsl:param » et « xsl:variable ».

Notre fichier « xslt.xml » est maintenant plus modulaire, parce qu'il contient deux modèles (éléments « xsl:template »).

**En résumé, il est souvent préférable d'utiliser un élément « xsl:apply-templates » qu'un élément « xsl:value-of » quand la complexité du modèle augmente; ceci permet d'assurer la modularité et de garder la simplicité du document XSLT.**

Par défaut, l'instruction apply-templates traite les nœuds dans l'ordre où ils se présentent dans le document original. On peut forcer le XSLT à trier les éléments avant de le traiter avec l'instruction xsl:sort. Dans notre exemple, on peut remplacer l'élément <xsl:apply-templates select="recipiendaire" /> par cet élément si on veut que les individus soient triés par leur nom de famille.
```xml
<xsl:apply-templates select="étudiant" >
   <xsl:sort select="personne/nom" order="ascending" data-type="text" />
   </xsl:apply-templates>
```

Si on souhaite un tri sur la valeur numérique d'une expression, on remplacera data-type="text" par data-type="number".

On peut aussi importer un autre fichier XSLT avec l'instruction xsl:import. Celle-ci doit apparaître au tout début du fichier XSLT comme premier sous-élément de l'élément xsl:stylesheet comme dans cet exemple :

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
    <xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:import href="mesregles.xsl"/>
    <xsl:template match="facture">
    <html>
    <head>
    <title>Facture de <xsl:value-of select="personne" /></title>
    </head>
    </xsl:template>
    </xsl:stylesheet>
```

En cas de conflit entre les règles de fichier XSLT principal et celles du fichier importé, les règles du fichier XSLT principal l'emporte.
