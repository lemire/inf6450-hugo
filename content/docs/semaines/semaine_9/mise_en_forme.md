---
title: "Mise en forme"
weight: 40
---

# Mise en forme
## Format et mise en forme

Cette section explique comment contrôler le format de sortie des transformations XSLT.

Par défaut, le document créé par une transformation XSLT est en XML, sauf si
    le nœud-racine est nommé HTML et qu'il est précédé uniquement d'espaces et
    de retours de charriot, auquel cas le document créé est un document HTML.
    L'instruction xsl:output permet de spécifier explicitement le format du
    document
    nouvellement créé comme étant en XML, en HTML ou même au format texte (sans
    balise). On peut aussi spécifier l'encodage des caractères ainsi que
    l'indentation
    des éléments. Voici des exemples :

```xml
<xsl:output method="text" />
   <xsl:output method="html" />
   <xsl:output method="xml" version="1.0" indent="yes"
   encoding="ISO-8859-1"/>
```

Le résultat d'une transformation XSLT peut ensuite être redirigé vers un
    fichier sur disque en utilisant un autre langage, comme JavaScript ou Java.
    Avec XSLT 1.0, il n'est pas possible de créer directement un fichier
    avec XSLT.
