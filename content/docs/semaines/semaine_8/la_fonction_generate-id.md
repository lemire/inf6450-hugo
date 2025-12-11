---
title: "La fonction generate-id"
weight: 90
---

# La fonction generate-id

## Fonction « generate-id »

Dans cette section, nous découvrons la fonction generate-id en XSLT, qui permet de générer des identifiants uniques pour les éléments XML, utiles pour créer des références ou des ancres dans les documents transformés.

La fonction XSLT « generate-id » génère un « nom » unique
   pour chaque élément d'un document XML.
   Ce nom sera toujours le même pour un même élément, même si nous le
   rencontrons à plusieurs reprises.
   Si nous reprenons la liste des cours de l'exemple précédent sur
   l'utilisation de l'attribut « mode »,
   nous pourrions générer un identifiant unique pour chaque cours et l'afficher
   comme dans l'exemple de document XSLT qui suit :

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
   <xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:template match="universite">
   <html><body>
   <p>La liste des cours en bref :</p>
   <ul>
   <xsl:apply-templates select="cours" mode="initial" />
   </ul>
   <p>La liste détaillée des cours :</p>
   <ul>
   <xsl:apply-templates select="cours" mode="complet" />
   </ul>
   </body></html>
   </xsl:template>
   <xsl:template match="cours" mode="initial">
   <li><xsl:value-of select="nom" />
   (identifiant: <xsl:value-of select="generate-id(.)" />)</li>
   </xsl:template>
   <xsl:template match="cours" mode="complet">
   <li><xsl:value-of select="nom" /> :
   <xsl:value-of select="description" />
   (identifiant: <xsl:value-of select="generate-id(.)" />)</li>
   </xsl:template>
   </xsl:stylesheet>
```

Nous pourrions alors obtenir un résultat comme celui-ci :

<div style="padding:2em; color:blue">

La liste des cours en bref:

- INF 102 Introduction avancée (identifiant: id2243749)
- INF 101 Introduction (identifiant: id2243760)
- INF 103 Java (identifiant: id2243686)

La liste détaillée des cours:

- INF 102 Introduction avancée: Un cours d'introduction à
           l'informatique pour futurs
           ingénieurs. (identifiant: id2243749)
- INF 101 Introduction: Un cours d'introduction à l'informatique pour
           les
           étudiants en éducation. (identifiant: id2243760)
- INF 103 Java: Un cours d'introduction au Java (identifiant:
           id2243686)

</div>

Les valeurs exactes que prennent les identifiants sont sans importance, mais
   il importe que
   ce soit toujours la même valeur pour un même élément. Par exemple, le cours
   sur Java obtient toujours
   l'identifiant « id2243686 » dans notre exemple.
