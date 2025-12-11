---
title: "La fonction generate-id"
weight: 90
---
<h1 class="">
 La fonction generate-id
</h1>
<h2 class="recall">
 Fonction « generate-id »
</h2>
<p>
 La fonction XSLT « generate-id » génère un « nom » unique
    pour chaque élément d'un document XML.
    Ce nom sera toujours le même pour un même élément, même si nous le
    rencontrons à plusieurs reprises.
    Si nous reprenons la liste des cours de l'exemple précédent sur
    l'utilisation de l'attribut « mode »,
    nous pourrions générer un identifiant unique pour chaque cours et l'afficher
    comme dans l'exemple de document XSLT qui suit :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
    &lt;xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
    &lt;xsl:template match="universite"&gt;
    &lt;html&gt;&lt;body&gt;
    &lt;p&gt;La liste des cours en bref :&lt;/p&gt;
    &lt;ul&gt;
    &lt;xsl:apply-templates select="cours" mode="initial" /&gt;
    &lt;/ul&gt;
    &lt;p&gt;La liste détaillée des cours :&lt;/p&gt;
    &lt;ul&gt;
    &lt;xsl:apply-templates select="cours" mode="complet" /&gt;
    &lt;/ul&gt;
    &lt;/body&gt;&lt;/html&gt;
    &lt;/xsl:template&gt;
    &lt;xsl:template match="cours" mode="initial"&gt;
    &lt;li&gt;&lt;xsl:value-of select="nom" /&gt;
    (identifiant: &lt;xsl:value-of select="generate-id(.)" /&gt;)&lt;/li&gt;
    &lt;/xsl:template&gt;
    &lt;xsl:template match="cours" mode="complet"&gt;
    &lt;li&gt;&lt;xsl:value-of select="nom" /&gt; :
    &lt;xsl:value-of select="description" /&gt;
    (identifiant: &lt;xsl:value-of select="generate-id(.)" /&gt;)&lt;/li&gt;
    &lt;/xsl:template&gt;
    &lt;/xsl:stylesheet&gt;
</p>
<p>
 Nous pourrions alors obtenir un résultat comme celui-ci :
</p>
<div style="border:solid 1px blue;padding-left:1em;">
 <p>
  La liste des cours en bref:
 </p>
 <ul>
  <li>
   INF 102 Introduction avancée (identifiant: id2243749)
  </li>
  <li>
   INF 101 Introduction (identifiant: id2243760)
  </li>
  <li>
   INF 103 Java (identifiant: id2243686)
  </li>
 </ul>
 <p>
  La liste détaillée des cours:
 </p>
 <ul>
  <li>
   INF 102 Introduction avancée: Un cours d'introduction à
            l'informatique pour futurs
            ingénieurs. (identifiant: id2243749)
  </li>
  <li>
   INF 101 Introduction: Un cours d'introduction à l'informatique pour
            les
            étudiants en éducation. (identifiant: id2243760)
  </li>
  <li>
   INF 103 Java: Un cours d'introduction au Java (identifiant:
            id2243686)
  </li>
 </ul>
</div>
<p>
 Les valeurs exactes que prennent les identifiants sont sans importance, mais
    il importe que
    ce soit toujours la même valeur pour un même élément. Par exemple, le cours
    sur Java obtient toujours
    l'identifiant « id2243686 » dans notre exemple.
</p>
