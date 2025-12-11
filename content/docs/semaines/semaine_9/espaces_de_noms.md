---
title: "Espaces de noms"
weight: 50
---

# Espaces de noms
## Espaces de noms

Cette section explique comment travailler avec les espaces de noms XML en XSLT.

Les espaces de noms sont supportés et ne posent pas de problème. Il suffit
    de définir les préfixes, comme on le fait habituellement. Par exemple,
    considérons le code XML suivant :

```xml
<?xml
   version="1.0" encoding="ISO-8859-1" ?>
   <?xml-stylesheet href="class2.xsl" type="text/xsl" ?>
   <université>
   <étudiant>
   <n:nom xmlns:n="http://www.mondomaine.com/">Réjean
   Tremblay</n:nom>
   </étudiant>
   </université>
```

Pour afficher le nom de l'étudiant, il suffira d'utiliser
    le document XSLT suivant :

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
   <xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
   xmlns:n="http://www.mondomaine.com/">
   <xsl:template match="université" >
   <html><body>
   <xsl:apply-templates select="étudiant/n:nom" />
   </body></html>
   </xsl:template>
   <xsl:template match="n:nom" >
   <p><xsl:value-of select="." /></p>
   </xsl:template>
   </xsl:stylesheet>
```

Observons que l'attribut « match="nom" » ne s'applique pas
    à l'élément « nom » dans l'espace de noms
    « http://www.mondomaine.com/ »,
    tel qu'il apparaît dans notre document XML : il est obligatoire
    d'utiliser un préfixe correspondant
    au bon espace de noms. Tout comme « match="*" » permet de
    sélectionner tous
    les éléments, « match="n:*" » permet de sélectionner tous les
    éléments qui sont
    dans un espace de noms donné.
