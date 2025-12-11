---
title: "Attribut mode"
weight: 80
---
<h1>
 Attribut mode
</h1>
<h2>
 Utilisation de l'attribut « mode »
</h2>
<p>
 Il arrive que nous voulions définir plus d'un modèle pour un élément donné.
    Nous pouvons ajouter des modèles en utilisant l'attribut « mode »
    qui s'applique aux
    éléments « xsl:apply-templates » et « xsl:template ». La
    règle est très simple :
    si votre élément « xsl:apply-templates » a une valeur d'attribut
    pour « mode », alors
    seuls les éléments « xsl:template » ayant la même valeur
    d'attribut pour « mode » s'appliquent.
    On utilise souvent l'attribut « mode » pour faire des tables des
    matières.
</p>
<p>
 Prenons, par exemple, la liste de cours suivants :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
    &lt;universite&gt;
    &lt;cours&gt;&lt;nom&gt;INF 102 Introduction avancée&lt;/nom&gt;
    &lt;description&gt;Un cours d'introduction à l'informatique pour futurs
    ingénieurs.&lt;/description&gt;&lt;/cours&gt;
    &lt;cours&gt;&lt;nom&gt;INF 101 Introduction&lt;/nom&gt;
    &lt;description&gt;Un cours d'introduction à l'informatique pour les
    étudiants en éducation.&lt;/description&gt;&lt;/cours&gt;
    &lt;cours&gt;&lt;nom&gt;INF 103 Java&lt;/nom&gt;
    &lt;description&gt;Un cours d'introduction au
    Java&lt;/description&gt;&lt;/cours&gt;
    &lt;/universite&gt;
</p>
<p>
 Nous pourrions vouloir que s'affiche d'abord seulement la liste des noms de
    cours et que cette dernière soit suivie d'une liste détaillée comprenant le
    nom et la description du cours :
</p>
<div style="border:solid 1px blue;padding-left:1em;">
 <p>
  La liste des cours en bref:
 </p>
 <ul>
  <li>
   INF 102 Introduction avancée
  </li>
  <li>
   INF 101 Introduction
  </li>
  <li>
   INF 103 Java
  </li>
 </ul>
 <p>
  La liste détaillée des cours:
 </p>
 <ul>
  <li>
   INF 102 Introduction avancée: Un cours d'introduction à
            l'informatique pour futurs
            ingénieurs.
  </li>
  <li>
   INF 101 Introduction: Un cours d'introduction à l'informatique pour
            les
            étudiants en éducation.
  </li>
  <li>
   INF 103 Java: Un cours d'introduction au Java
  </li>
 </ul>
</div>
<p>
 Nous pouvons obtenir ce résultat avec le document XSLT suivant qui utilise
    l'attribut « mode » :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
    &lt;xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
    &lt;xsl:template match="universite"&gt;
    &lt;html&gt;&lt;body&gt;
    &lt;p&gt;La liste des cours en bref:&lt;/p&gt;
    &lt;ul&gt;
    &lt;xsl:apply-templates select="cours" mode="initial" /&gt;
    &lt;/ul&gt;
    &lt;p&gt;La liste détaillée des cours:&lt;/p&gt;
    &lt;ul&gt;
    &lt;xsl:apply-templates select="cours" mode="complet" /&gt;
    &lt;/ul&gt;
    &lt;/body&gt;&lt;/html&gt;
    &lt;/xsl:template&gt;
    &lt;xsl:template match="cours" mode="initial"&gt;
    &lt;li&gt;&lt;xsl:value-of select="nom" /&gt;&lt;/li&gt;
    &lt;/xsl:template&gt;
    &lt;xsl:template match="cours" mode="complet"&gt;
    &lt;li&gt;&lt;xsl:value-of select="nom" /&gt; :
    &lt;xsl:value-of select="description" /&gt;&lt;/li&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
