---
title: "Les valeurs d’attribut"
weight: 50
---
# Les valeurs d’attribut

## Spécifier les valeurs d'attributs

Nous savons maintenant comment aller chercher la valeur d'un attribut en utilisant une expression XPath contenant le symbole « @ ». Cependant, qu'en est-il de la spécification des valeurs d'attributs? Supposons le document suivant :

```xml
<facture>
   <montant>10.10</montant>
   </facture>
```

Nous voulons le simplifier pour n'avoir que :

```xml
<facture montant="10.10" />
```

Nous pouvons obtenir ce résultat en utilisant les accolades, pour indiquer une valeur XPath comme valeur d'attribut, de la façon suivante :

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
   <xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:template match="facture">
   <facture montant="{montant}" />
   </xsl:template>
   </xsl:stylesheet>
```
