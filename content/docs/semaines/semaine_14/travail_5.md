---
title: "Travail 5"
weight: 40
---
<h1>
 Travail 5
</h1>
<h2>
 Consignes
</h2>
<p>
 Lorsque vous aurez terminé le travail, transmettez à votre personne tutrice,
    un seul document (Word 97/2000/XP,
 <a href="https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=office">
  ODF
 </a>
 ,
    PDF, RTF ou en format texte) comprenant,
    pour chaque exercice, le tableau, le code ou le contenu de votre document
    XSLT.
 <strong>
  Ne transmettez pas vos solutions en plusieurs fichiers. Ne
        transmettez pas
        une archive
        compressée (zip ou autre).
 </strong>
 Il s'agit d'un travail personnel et vous ne devez pas partager vos
    solutions.
</p>
<p>
 Vous devez transmettre votre travail en utilisant l'outil de dépôt de
    l'Université.
</p>
<p>
 Cette activité notée compte pour 10% de la note globale.
</p>
<p>
 Dans un tableau de triplets, les objets qui ne sont pas des URI, doivent être
    placés entre guillements (" ").
</p>
<h2>
 Exercice 1
</h2>
<p>
 Représentez, dans un tableau de triplets (sujet, verbe, objet), le document
    RDF/XML suivant :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">md</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.mondomaine.com</span><span style="color:#40015a; ">/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">https://www.uqam.ca/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">md</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">titre</span><span style="color:#a65700; ">&gt;</span>Site de l'UQAM<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">md</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">titre</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">md</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">autre</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">https://www.uqam.ca/index.html</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<h2>
 Exercice 2
</h2>
<p>
 Écrivez un programme Java qui utilise l'API DOM pour extraire tous les titres
    des items d'un document RSS 1.0. Vous pouvez supposer que le fichier
    réside sur votre disque. Ne joignez pas un fichier à l'extension java.
</p>
<h2>
 Exercice 3
</h2>
<p>
 Représentez, dans un tableau de triplets (sujet, verbe, objet), l'exemple en
    RDF qui suit et qui provient
    de la norme
 <a href="https://en.wikipedia.org/wiki/Publishing_Requirements_for_Industry_Standard_Metadata">
  PRISM
 </a>
 .
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">UTF-8</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">pcv</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">prismstandard.org</span><span style="color:#40015a; ">/namespaces/pcv/1.0/</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">dc</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">purl.org</span><span style="color:#40015a; ">/dc/elements/1.1/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">https://wanderlust.com/2000/08/Corfu.jpg</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">identifier</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">https://wanderlust.com/content/2357845</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">creator</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">pcv</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Descriptor</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">https://wanderlust.com/emp3845</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">pcv</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">label</span><span style="color:#a65700; ">&gt;</span>John Peterson <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">pcv</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">label</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">pcv</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Descriptor</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">creator</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">coverage</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">pcv</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Descriptor</span>
    <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">https://prismstandard.org/vocabs/ISO-3166/GR</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">pcv</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">label</span> <span style="color:#666616; ">xml</span><span style="color:#800080; ">:</span><span style="color:#074726; ">lang</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">en</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>Greece<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">pcv</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">label</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">pcv</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">label</span> <span style="color:#666616; ">xml</span><span style="color:#800080; ">:</span><span style="color:#074726; ">lang</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">fr</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>Grece<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">pcv</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">label</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">pcv</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Descriptor</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">coverage</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<h2>
 Exercice 4
</h2>
<p>
 Ecrivez un document XML/RDF correspondant au tableau suivant :
</p>
<div class="tableau style1">
 <table border="1" class="tablebleu">
  <tbody>
   <tr>
    <td>
     Sujet
    </td>
    <td>
     Verbe
    </td>
    <td>
     Objet
    </td>
   </tr>
   <tr>
    <td>
     https://www.uqam.ca
    </td>
    <td>
     https://www.uquebec.ca/nom
    </td>
    <td>
     "UQÀM"
    </td>
   </tr>
  </tbody>
 </table>
</div>
<h2>
 Exercice 5
</h2>
<p>
 La licence identifiée par l'URI
    « https://www.mondomaine.ca/licence »
    permet la reproduction, la distribution et la modification des œuvres.
    Décrivez cette licence en utilisant
 <i>
  Creative Commons
 </i>
 et le format
    RDF/XML.
</p>
<h2>
 Exercice 6
</h2>
<p>
 Le site
 <a href="https://www.flickr.com/">
  flickr
 </a>
 permet de chercher des
    photographies publiées avec une licence Creative Commons. Visitez
    la page
 <a href="https://www.flickr.com/photos/guppiecat/1351724368/in/set-72157601927001088/">
  https://www.flickr.com/photos/guppiecat/1351724368/in/set-72157601927001088/
 </a>
 et trouvez la licence Creative Commons. Écrivez-la en XML.
</p>
<h2>
 Exercice 7
</h2>
<p>
 L'
 <a href="https://r-libre.teluq.ca/">
  archive institutionelle de la TÉLUQ
 </a>
 donne accès aux articles scientifiques de ses professeurs. Choisissez un
    article (à votre guise) et consultez le code source HTML de la page web
    correspondante. Vous y trouverez des étiquettes Dublin Core. Écrivez le tout
    en XML.
</p>
