---
title: "Attribut mode"
weight: 80
---

# Attribut mode

## Utilisation de l'attribut « mode »

Dans cette section, nous explorons l'utilisation de l'attribut mode en XSLT, qui permet de définir plusieurs modèles pour le même élément et de les appliquer sélectivement pour créer des vues différentes du document XML.

Il arrive que nous voulions définir plus d'un modèle pour un élément donné.
   Nous pouvons ajouter des modèles en utilisant l'attribut « mode »
   qui s'applique aux
   éléments « xsl:apply-templates » et « xsl:template ». La
   règle est très simple :
   si votre élément « xsl:apply-templates » a une valeur d'attribut
   pour « mode », alors
   seuls les éléments « xsl:template » ayant la même valeur
   d'attribut pour « mode » s'appliquent.
   On utilise souvent l'attribut « mode » pour faire des tables des
   matières.

Prenons, par exemple, la liste de cours suivants :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
   <universite>
   <cours><nom>INF 102 Introduction avancée</nom>
   <description>Un cours d'introduction à l'informatique pour futurs
   ingénieurs.</description></cours>
   <cours><nom>INF 101 Introduction</nom>
   <description>Un cours d'introduction à l'informatique pour les
   étudiants en éducation.</description></cours>
   <cours><nom>INF 103 Java</nom>
   <description>Un cours d'introduction au
   Java</description></cours>
   </universite>
```

Nous pourrions vouloir que s'affiche d'abord seulement la liste des noms de
   cours et que cette dernière soit suivie d'une liste détaillée comprenant le
   nom et la description du cours :

<div style="padding:5em; color:blue;">

La liste des cours en bref:

- INF 102 Introduction avancée
- INF 101 Introduction
- INF 103 Java

La liste détaillée des cours:

- INF 102 Introduction avancée: Un cours d'introduction à
           l'informatique pour futurs
           ingénieurs.
- INF 101 Introduction: Un cours d'introduction à l'informatique pour
           les
           étudiants en éducation.
- INF 103 Java: Un cours d'introduction au Java

</div>



Nous pouvons obtenir ce résultat avec le document XSLT suivant qui utilise
   l'attribut « mode » :
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
   <xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:template match="universite">
   <html><body>
   <p>La liste des cours en bref:</p>
   <ul>
   <xsl:apply-templates select="cours" mode="initial" />
   </ul>
   <p>La liste détaillée des cours:</p>
   <ul>
   <xsl:apply-templates select="cours" mode="complet" />
   </ul>
   </body></html>
   </xsl:template>
   <xsl:template match="cours" mode="initial">
   <li><xsl:value-of select="nom" /></li>
   </xsl:template>
   <xsl:template match="cours" mode="complet">
   <li><xsl:value-of select="nom" /> :
   <xsl:value-of select="description" /></li>
   </xsl:template>
   </xsl:stylesheet>
```
