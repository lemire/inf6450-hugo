---
title: "Introduction au XSLT"
weight: 20
---
<h1>
 Introduction au XSLT
</h1>
<h2>
 Qu'est-ce que le XSLT
</h2>
<p>
 La première version du langage XSLT (
 <i>
  Extensible Stylesheet Language Transformation
 </i>
 )
    a été publiée en 1997 et elle est devenue une recommandation W3C en 1999.
    Elle fait partie du XSL (
 <i>
  Extensible Stylesheet Language
 </i>
 ) qui comprend une seconde composante,
    les XSL-FO (
 <i>
  Extensible Stylesheet Language Formatting Objects
 </i>
 ).
    La technologie XSL tire son origine du besoin d'un langage simple, mais suffisamment puissant
    pour pouvoir contrôler finement l'affichage du XML. On utilise beaucoup le XSLT sur le web et au sein
    des systèmes d'information, alors que le XSL-FO est davantage utile pour les applications
    de mise en page spécialisées. Dans ce cours, nous nous soucierons seulement du XSLT, dont l'utilité
    dépasse de loin les problèmes de présentation.
</p>
<p>
 L'objectif poursuivi par le XSLT est de transformer les documents XML en d'autres documents.
    Par exemple, supposons que vous ayez le document suivant :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#004a43; ">?&gt;</span>
        <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">facture</span><span style="color:#a65700; ">&gt;</span>
            <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">montant</span><span style="color:#a65700; ">&gt;</span>10.10<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">montant</span><span style="color:#a65700; ">&gt;</span>
            <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">personne</span><span style="color:#a65700; ">&gt;</span>Jean Rochond<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">personne</span><span style="color:#a65700; ">&gt;</span>
            <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">raison</span><span style="color:#a65700; ">&gt;</span>Achat d'ordinateur<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">raison</span><span style="color:#a65700; ">&gt;</span>
         <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">facture</span><span style="color:#a65700; ">&gt;</span>
    </pre>
<p>
 et que vous vouliez transformer ce type de document XML en document HTML qui aurait la forme suivante :
</p>
<pre><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">html</span><span style="color:#a65700; ">&gt;</span>
      <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
      <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Facture de Jean Rochond<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
      <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">head</span><span style="color:#a65700; ">&gt;</span>
      <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">p</span><span style="color:#a65700; ">&gt;</span>Ceci est une facture pour Jean Rochond de 10.10$
      pour: Achat d'ordinateur.<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">p</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">body</span><span style="color:#a65700; ">&gt;</span>
      <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">html</span><span style="color:#a65700; ">&gt;</span>
    </pre>
<p>
 Si votre entreprise utilise du XML et que vous désirez envoyer des factures
    par courriel, vous pourriez envoyer le document HTML au lieu du document XML. De cette
    manière, le client pourrait consulter sa facture sans avoir à comprendre le XML.
</p>
<p>
 On pourrait bien sûr écrire un programme en Java qui effectuerait cette opération, mais
    la conception d'un programme Java prend du temps et on cherche parfois une solution
    plus économique, plus rapide. Avec l'exemple que nous venons de voir,
    on pourrait automatiser la transformation de XML en HTML en moins d'une quinzaine de minutes.
    Pour obtenir le résultat désiré, il faut utiliser un petit fichier XSLT. À la fin de cette semaine, vous devriez être capable de faire ce travail.
</p>
<h3 class="recall">
 Les documents XSLT
</h3>
<p>
 Le document XSLT contient des règles qu'un « processeur XSLT » applique aux documents XML
    pour les transformer. Heureusement, si vous utilisez un navigateur récent, vous avez déjà un
    processeur XSLT moderne à même votre navigateur. Lors de l'ouverture d'un document XML,
    votre navigateur tente automatiquement de trouver et d'exécuter un document XSLT
    pour transformer le document XML.
</p>
<p>
 Un processeur XSLT va parcourir les noeuds de votre document en
    commençant par l'élément-racine et, à chaque fois, il va tenter d'appliquer une règle. Certaines règles peuvent lui dire de continuer l'application des règles au sein des noeuds contenus dans un élément (avec l'instruction apply-template) alors que d'autres peuvent simplement extraire une information particulière.
</p>
<p>
 Commençons par créer le fichier XSLT suivant qu'on enregistrera
    sur le disque comme étant « xslt.xml » :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
     <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">stylesheet</span> <span style="color:#274796; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">1.0</span><span style="color:#0000e6; ">"</span> 
     <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">xsl</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/XSL/Transform</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
     <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">stylesheet</span><span style="color:#a65700; ">&gt;</span>
    </pre>
<p>
 Ce document ne contient aucune « règle » et constitue le document XSLT de base.
    Nous vous suggérons de faire l'exercice de création de ce document avec
 <i>
  Bloc-notes
 </i>
 , par exemple.
</p>
<p>
 Un document XSLT est un document XML bien formé, utilisant
    l'espace de noms « http://www.w3.org/1999/XSL/Transform » et ayant
    pour élément-racine
 <i>
  stylesheet
 </i>
 (ou
 <i>
  transform
 </i>
 ), lequel a lui-même un attribut « version ».
    On ne discute ici que de la première version de XSLT (1.0);
    on utilise donc 1.0 comme valeur d'attribut pour version.
</p>
<p>
 Prenons maintenant le fichier XML que nous avions auparavant; modifions-le un peu
    en le faisant pointer vers le fichier XSLT nouvellement créé :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span><span style="color:#004a43; ">?&gt;</span>
      <span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml-stylesheet</span><span style="color:#004a43; "> </span><span style="color:#074726; ">href</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#40015a; ">xslt.xml</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; "> </span>
    <span style="color:#004a43; ">  </span><span style="color:#074726; ">type</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">application/xml</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
      <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">facture</span><span style="color:#a65700; ">&gt;</span>
       <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">montant</span><span style="color:#a65700; ">&gt;</span>10.10<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">montant</span><span style="color:#a65700; ">&gt;</span>
      <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">personne</span><span style="color:#a65700; ">&gt;</span>Jean Rochond<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">personne</span><span style="color:#a65700; ">&gt;</span>
      <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">raison</span><span style="color:#a65700; ">&gt;</span>Achat d'ordinateur<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">raison</span><span style="color:#a65700; ">&gt;</span>
      <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">facture</span><span style="color:#a65700; ">&gt;</span>
    </pre>
<p>
 On ajoute donc la ligne : « &lt;?xml-stylesheet href="xslt.xml" type="application/xml"?&gt; ».
    Cette ligne indique au navigateur, ou à un autre logiciel, que le document XML peut être transformé
    par le fichier XSLT nommé « xslt.xml ». Le chemin peut être relatif ou absolu : on pourrait
    donc aussi avoir une ligne comme :
</p>
<pre xml:space="preserve">«&lt;?xml-stylesheet href="http://www.mondomaine.com/xslt.xml"
     type="application/xml"?&gt;»</pre>
<p>
 si l'URL « http://www.mondomaine.com/xslt.xml » pointe vers un fichier XSLT.
</p>
<p>
 Dans un navigateur, on peut enregistrer ce nouveau document XML dans le même répertoire
    que le fichier « xslt.xml », disons avec le nom « test.xml »,
    puis d'ouvrir le fichier « test.xml » dans votre navigateur; il est malheureusement nécessaire de déposer les fichiers sur un serveur web pour que cela fonctionne, les développeurs craignant les failles de sécurité associées aux fichiers locaux. Heureusement, vous n'avez pas à faire ce travail: nous fournissons un
  outil en ligne
 qui vous permet de saisir vos fichiers XSLT and XML dans votre navigateur sans devoir créer de fichiers. Nous vous présenterons cet outil dans le prochain article. Ceux qui souhaitent travailler avec des fichiers directement peuvent utiliser un serveur web.
</p>
<p>
 Une fois le fichier XML chargé et la transformation XSLT appliquée, normalement,
    on ne devrait rien voir à l'écran (une page vide), car le document XSLT utilisé est vide de
    toute instruction et le résultat ne sera donc pas du HTML.
    Le résultat peut cependant varier selon le navigateur utilisé, car votre navigateur pourrait afficher le texte,
    même s'il ne s'agit pas de HTML : dans ce cas, vous ne verriez que le texte contenu dans le document XML,
    les balises en moins. Nous expliquerons bientôt pourquoi cela est le cas.
</p>
<h2 class="recall">
 Application de bureau Java (optionelle)
</h2>
<p>
 Nous avons préparé une application conviviale en Java qui vous permet d'appliquer une transformation XSLT à un document XML.
 <a href="https://github.com/lemire/javaxslt">
  Nous vous invitons à la mettre à l'essai en suivant nos consignes
 </a>
 .
</p>
