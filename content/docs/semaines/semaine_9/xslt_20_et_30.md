---
title: "XSLT 2.0 et 3.0"
weight: 100
---
<h1 class="">
 XSLT 2.0 et 3.0
</h1>
<p>
 Nous nous sommes concentrés sur la version 1.0 du XSLT car elle est la plus répandue et la mieux supportée.
</p>
<p>
 Une nouvelle version du XSLT est disponible, nommée XSLT 2.0. Elle ajoute
notamment la possibilité de générer plusieurs documents plutôt qu'un seul
avec l'instruction xslt:result-document. On peut aussi traiter
non seulement des fichiers XML, mais aussi d'autres types de fichiers
dont les fichiers CSV (comma-separated values) générés par les
chiffriers électroniques et bases de données. L'instruction « xsl:analyze-string » 
permet de prendre appui sur les nouvelles possibilités du traitement des chaînes
de caractères de XPath 2.0. L'instruction « xsl:function » permet quant à
elle de définir de nouvelles fonctions qui pourront être utilisées au sein des
expressions XPath. L'instruction « xsl:for-each-group » permet 
 de visiter les nœuds par groupes : on peut ainsi visiter
tous les éléments etudiant en les regroupant selon la valeur de leur attribut nom.
</p>
<p>
 Elliotte Rusty Harold a publié  une
 <a href="http://www.cafeconleche.org/slides/sd2002west/xslt2/XSLT_2.0_and_Beyond.html" shape="rect">
  page sur XSLT 2.0
 </a>
 qui présente quelques exemples.
</p>
<p>
 La version 3.0 du XSLT permet de traiter de grands volumes de données en évitant le chargement en mémoire de la totalité des documents. À cette fin, elle introduit des instructions comme xsl:iterate et xsl:stream.
</p>
