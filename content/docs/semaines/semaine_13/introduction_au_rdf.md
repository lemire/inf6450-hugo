---
title: "Introduction au RDF"
weight: 30
---
<h1>
 Introduction au RDF
</h1>
<h2>
 Introduction
</h2>
<p>
 Le
 <i>
  Resource Description Framework
 </i>
 (RDF) est un langage pour les
    métadonnées sur le web,
    c'est-à-dire un langage pour énoncer ce que l'on sait sur quelque chose ou
    quelqu'un.
    Par exemple, le RDF est idéal pour indiquer qui est l'auteur d'un document
    ou quel est le titre du document.
    De plus, le langage RDF est prévu pour être à la fois simple (mais tout est
    relatif), suffisamment
    puissant pour « tout » décrire, et facilement utilisable par des
    logiciels.
    Dans le deuxième texte que nous proposons, nous verrons quelques
    applications intéressantes.
    Pour l'instant, nous ne présentons dans ce texte que les concepts de base.
</p>
<h2>
 Notions de base
</h2>
<p>
 Le RDF a été normalisé en 1999 (par une recommandation W3C) et est un effort
    commun de plusieurs experts.
    Le RDF se veut suffisamment riche pour représenter de façon formelle la
    connaissance
    tout en étant simple à utiliser. Une des prémisses du format RDF est que
 <i>
  tout peut être énoncé en utilisant des triplets :
        sujet, verbe et objet
 </i>
 . Notez que certains auteurs utiliseront le
    terme « prédicat » au lieu du
    terme « verbe ». Par exemple, pour décrire « Jean »,
    nous dirons que « Jean est un garçon »
    et nous décomposerons ainsi cette affirmation :
    (Jean)(est)(garçon)]]&gt;, ou l'afficherons dans un tableau :
</p>
<div class="tableau style1">
 <table border="1" class="tabNormal">
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
     Jean
    </td>
    <td>
     est
    </td>
    <td>
     garçon
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 Nous ne faisons pas de la grammaire, mais bien de la représentation : le
    verbe n'a
    pas à être un verbe de la langue française ou anglaise. L'important est que
    le verbe soit un lien, une relation, entre une première chose (sujet) et une
    seconde (objet).
    Par exemple, si nous voulons affirmer que le titre de la page web
    « http://lemire.me/ »
    est « Daniel Lemire's blog », nous pouvons le faire à l'aide du
    tableau suivant :
</p>
<div class="tableau style1">
 <table border="1" class="tabNormal">
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
     http://lemire.me/
    </td>
    <td>
     titre
    </td>
    <td>
     Daniel Lemire's blog
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 Ces exemples de représentation ne sont pas encore des exemples de données
    « RDF », car en RDF, le verbe doit être un « URI ». Le
    RDF, tout comme le XML, est fait pour être traité
    par des machines et les machines sont bêtes. Elles ne savent pas ce que
    signifie le mot
    « titre » dans le tableau précédent. Est-ce un titre à la Bourse,
    le
    titre d'une fonction (comme docteur) ou le titre d'une page? Pour régler ce
    problème, il faut utiliser des URI (
 <i>
  Uniform Resource Identifier
 </i>
 ),
    c'est-à-dire des adresses
    fictives qui identifient une ressource Internet.
</p>
<p>
 Un URI contient un protocole (http, mailto, ftp, etc.), un domaine comme
    « fichiers.com » et un chemin
    comme « /mesfichiers/index.html ». Dans ce cours, nous adoptons la
    norme RFC3986 et
    nous permettons que les URI comportent le symbole du dièse ( # ),
    comme « ftp://fichiers.com#maman » :
    tout ce qui apparaît après ce symbole forme le « fragment ».
    Notons
    que les accents ne peuvent pas être utilisés dans un URI selon la norme RFC3986; ainsi,
    « http://école.com » n'est pas un URI valable. Par contre, la plupart des navigateurs modernes utilisent la norme WHATWG URL qui supporte les caractères non-ASCII selon certaintes conditions.
    Un protocole particulier, « urn », est parfois utilisé dans
    les URI. Par exemple, pour
    identifier un livre par son code ISBN, nous pouvons utiliser l'URI
    « urn:ISBN:0-123-12345-1 ». La casse est significative dans un URI
    sauf pour le nom du protocole (HTTP ou http) et le nom du domaine (xerox.com
    ou XEROX.COM).
</p>
<p>
 Toutes les URL (
 <i>
  Uniform Resource Locator
 </i>
 ) utilisées sur le web,
    comme « http://www.google.com »,
    « mailto:bill@microsoft.com », « ftp://fichiers.com »,
    ainsi que d'autres adresses ayant la même syntaxe, mais qui ne pointent pas
    nécessairement
    vers une ressource Internet existante, sont des exemples d'URI. Ainsi, si
    l'on
    vous donne l'URI « http://www.mydomain.com/daniel », il n'est pas
    certain qu'une
    page web se trouve à cette adresse. Le seul but des URI est d'identifier des
    ressources.
    Le mot « ressource » a un sens très, très large : tout peut
    être considéré comme une ressource.
    Par exemple, pour identifier l'humoriste « Daniel Lemire », nous
    pouvons adopter l'URI
    « http://www.daniellemire.com/luimeme »; ce sera un bon choix si
    l'humoriste en
    question est propriétaire du nom de domaine (daniellemire.com) et compte le
    garder
    longtemps. Par ailleurs, on pourra utiliser l'URI
    « http://lemire.me/fr/ »
    pour identifier le professeur « Daniel Lemire » qui est
    responsable d'un
    cours portant sur le XML. Dans ce dernier exemple, l'URI est aussi un URL
    qui pointe
    vers la page personnelle du professeur. Nous voyons immédiatement l'avantage
    des URI : alors
    que l'ordinateur ne saura pas toujours faire la différence entre
    « Daniel Lemire » l'humoriste
    et « Daniel Lemire » le professeur, nous pourrons, en utilisant
    des URI, analyser automatiquement l'information,
    à la condition que tous utilisent le même URI pour représenter la même
    ressource.
    Pour distinguer les individus, nous pourrions utiliser leur numéro
    d'assurance sociale... Mais comme le concept de ressource
    est général, il faut aussi pouvoir distinguer les différentes significations
    que
    peuvent prendre le mot « titre », et ainsi de suite.
    La langue française (ou anglaise) permet à un mot d'avoir plusieurs sens,
    alors que
    chaque URI représente un concept et un concept seulement.
</p>
<p>
 L'URI n'a pas en soit un sens particulier. C'est un nom. Ainsi
    « http://google.com/2000/jacques/ » peut ne rien à voir avec l'an
    2000 ou une personne appelée Jacques... tout comme un homme appelé Pierre
    n'a pas à travailler sur des pierres ou qu'une personne appelée Meunier n'a
    pas à être meunier.
</p>
<p>
 Supposons maintenant que nous voulions décrire l'affirmation suivante en
    RDF :
    « Il y a une personne appelée Daniel Lemire dont l'adresse de courriel
    est lemire@gmail.com
    et qui est professeur. » Cette phrase peut être très difficile à
    analyser par un ordinateur. Commençons par la décomposer en affirmations
    simples : sujet/verbe/objet.
    D'abord, pour qu'il n'y ait pas de confusion, nous allons identifier
    l'individu s'appelant
    Daniel Lemire par l'URI « http://lemire.me/fr/ ».
</p>
<ul>
 <li>
  http://lemire.me/fr/ est une personne.
 </li>
 <li>
  http://lemire.me/fr/ s'appelle Daniel Lemire.
 </li>
 <li>
  http://lemire.me/fr/ peut être joint par courriel à lemire@gmail.com.
 </li>
 <li>
  http://lemire.me/fr/ a le titre de professeur.
 </li>
</ul>
<p>
 Rappelons ici que tous les verbes et tous les sujets doivent être
    identifiés par des URI. En ce qui nous concerne, il n'y a qu'un seul
    sujet identifié par « http://lemire.me/fr/ ». Il reste à
    trouver des URI pour les verbes et certains objets. Prenons d'abord
    la première affirmation : « http://lemire.me/fr/ est une
    personne ».
    Le verbe « être », dans cette phrase, associe la classe
    « personne » (au même sens que dans
    la programmation orientée objet) à la ressource
    « http://lemire.me/fr/ ».
    Nous pourrions inventer un URI ayant ce sens, mais il en existe déjà
    un : « http://www.w3.org/1999/02/22-rdf-syntax-ns#type ».
    Chaque fois que nous rencontrons cet URI, cela signifie qu'une ressource
    appartient à une certaine classe. Quant à
    l'objet « personne », il existe au moins un URI pour noter la
    classe « personne », soit
    « http://www.w3.org/2000/10/swap/pim/contact#Person ». Nous
    verrons que
    dans d'autres contextes, d'autres URI peuvent être utilisés avec un sens
    similaire.
</p>
<p>
 Finalement, l'affirmation « http://lemire.me/fr/ est une personne »
    peut s'écrire comme ceci :
</p>
<div class="tableau style1">
 <table border="1" class="tabNormal">
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
     http://lemire.me/ fr/
    </td>
    <td>
     http://www.w3.org/1999/ 02/22-rdf-syntax-ns#type
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#Person
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 Passons maintenant à la deuxième affirmation :
    « http://lemire.me/fr/
    s'appelle Daniel Lemire ». Le verbe « s'appelle » peut être
    identifié par
    l'URI « http://www.w3.org/2000/10/swap/pim/contact#fullName ».
    Encore une fois, nous aurions pu
    inventer notre propre URI, en autant que nous utilisons toujours le même
    avec la même signification.
    L'objet, « Daniel Lemire », n'a pas de signification particulière
    et n'est qu'une
    chaîne de caractères; nous ne sommes donc pas tenus d'utiliser un URI. Cela
    n'est vrai que pour les
    objets : les sujets et les verbes doivent toujours être représentés par
    des URI en RDF. Nous obtenons le tableau suivant :
</p>
<div class="tableau style1">
 <table border="1" class="tabNormal">
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
     http://lemire.me/ en/
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#fullName
    </td>
    <td>
     "Daniel Lemire"
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 Nous notons les chaînes de caractères avec les guillemets : alors que
    « http://www.unuri.org » est un URI,
    « "http://www.unuri.org" » est une chaîne de caractères.
</p>
<p>
 Dans l'affirmation « http://lemire.me/fr/ peut être joint par courriel à
    lemire@gmail.com »,
    nous pouvons remplacer le verbe par
    « http://www.w3.org/2000/10/swap/pim/contact#mailbox ». Quant à
    l'objet
    « lemire@gmail.com », c'est une adresse de courriel; afin qu'un
    ordinateur puisse comprendre qu'il s'agit d'une
    adresse de courriel et non d'une chaîne de caractères, nous utiliserons
    l'URL
    « mailto:lemire@gmail.com » pour le représenter. Nous avons donc
    le tableau suivant :
</p>
<div class="tableau style1">
 <table border="1" class="tabNormal">
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
     http://lemire.me/ en/
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#mailbox
    </td>
    <td>
     mailto:lemire@gmail.com
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 L'affirmation « http://lemire.me/fr/ a le titre de professeur » se
    traite
    de la même manière, de telle sorte que nous obtenons finalement le tableau
    suivant :
</p>
<div class="tableau style1">
 <table border="1" class="tabNormal">
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
     http://lemire.me/ en/
    </td>
    <td>
     http://www.w3.org/1999/ 02/22-rdf-syntax-ns#type
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#Person
    </td>
   </tr>
   <tr>
    <td>
     http://lemire.me/ en/
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#fullName
    </td>
    <td>
     "Daniel Lemire"
    </td>
   </tr>
   <tr>
    <td>
     http://lemire.me/ en/
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#mailbox
    </td>
    <td>
     mailto:lemire@gmail.com
    </td>
   </tr>
   <tr>
    <td>
     http://lemire.me/ en/
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#personalTitle
    </td>
    <td>
     "Professeur"
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 Précisons qu'en RDF, l'ordre des affirmations est sans importance. Ainsi,
    l'ordre des rangées dans le tableau est sans importance.
</p>
<p>
 Ce tableau est une description formelle de notre phrase d'origine « Il y
    a une personne appelée
    Daniel Lemire dont l'adresse de courriel est lemire@gmail.com et qui est
    professeur. »; cette description peut être
    traitée par un ordinateur.
</p>
<p>
 Comme nous le verrons plus loin, ce tableau RDF peut s'écrire en XML de la
    façon suivante :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">contact</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/2000/10/swap/pim/contact</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">contact</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Person</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">contact</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">fullName</span><span style="color:#a65700; ">&gt;</span>Daniel Lemire<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">contact</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">fullName</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">contact</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">mailbox</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">mailto:lemire@gmail.com</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">contact</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">personalTitle</span><span style="color:#a65700; ">&gt;</span>Professeur<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">contact</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">personalTitle</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">contact</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Person</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 On peut aussi représenter graphiquement le tableau RDF :
</p>
<svg font-size="0.65em" height="134pt" viewbox="0 0 513 134" width="513pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
 ../module5/dlprof.pdf
 <g class="graph" id="graph0">
  <!-- http://www.daniel-lemire.com/fr/ -->
  <g class="node" id="node1">
   http://www.daniel-lemire.com/fr/
   <ellipse cx="217" cy="23" rx="106" ry="18" style="fill:none;stroke:black;">
   </ellipse>
   <text text-anchor="middle" x="217" y="28">
    http://www.daniel-lemire.com/fr/
   </text>
  </g>
  <!-- Person -->
  <g class="node" id="node3">
   Person
   <ellipse cx="37" cy="111" rx="32" ry="18" style="fill:none;stroke:black;">
   </ellipse>
   <text text-anchor="middle" x="37" y="116">
    Person
   </text>
  </g>
  <!-- http://www.daniel-lemire.com/fr/-&gt;Person -->
  <g class="edge" id="edge2">
   http://www.daniel-lemire.com/fr/-&gt;P
                erson
   <path d="M182,40C149,56 102,79 70,95" style="fill:none;stroke:black;">
   </path>
   <polygon points="72,98 61,99 69,92 72,98" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="158" y="72">
    Type
   </text>
  </g>
  <!-- Daniel Lemire -->
  <g class="node" id="node5">
   Daniel Lemire
   <ellipse cx="141" cy="111" rx="54" ry="18" style="fill:none;stroke:black;">
   </ellipse>
   <text text-anchor="middle" x="141" y="116">
    Daniel Lemire
   </text>
  </g>
  <!-- http://www.daniel-lemire.com/fr/-&gt;Daniel Lemire -->
  <g class="edge" id="edge4">
   http://www.daniel-lemire.com/fr/-&gt;D
                aniel Lemire
   <path d="M201,41C190,54 175,72 163,86" style="fill:none;stroke:black;">
   </path>
   <polygon points="165,89 156,94 160,84 165,89" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="214" y="72">
    fullName
   </text>
  </g>
  <!-- lemire@gmail.com -->
  <g class="node" id="node7">
   lemire@gmail.com
   <ellipse cx="293" cy="111" rx="80" ry="18" style="fill:none;stroke:black;">
   </ellipse>
   <text text-anchor="middle" x="293" y="116">
    lemire@gmail.com
   </text>
  </g>
  <!-- http://www.daniel-lemire.com/fr/-&gt;lemire@gmail.com -->
  <g class="edge" id="edge6">
   http://www.daniel-lemire.com/fr/-&gt;d
                lemire@teluq.ca
   <path d="M233,41C244,54 259,71 271,85" style="fill:none;stroke:black;">
   </path>
   <polygon points="274,83 278,93 269,88 274,83" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="281" y="72">
    mailbox
   </text>
  </g>
  <!-- Professeur -->
  <g class="node" id="node9">
   Professeur
   <ellipse cx="433" cy="111" rx="42" ry="18" style="fill:none;stroke:black;">
   </ellipse>
   <text text-anchor="middle" x="433" y="116">
    Professeur
   </text>
  </g>
  <!-- http://www.daniel-lemire.com/fr/-&gt;Professeur -->
  <g class="edge" id="edge8">
   http://www.daniel-lemire.com/fr/-&gt;P
                rofesseur
   <path d="M259,40C274,46 292,53 308,59 336,70 368
    ,84 393,94" style="fill:none;stroke:black;">
   </path>
   <polygon points="395,91 403,98 392,98 395,91" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="378" y="72">
    personalTitle
   </text>
  </g>
 </g>
</svg>
<p>
 Nous pouvons également spécifier dans quelle langue une chaîne de caractères
    est écrite;
    par exemple, le mot « professeur » n'a de sens qu'en français.
    Pour ce faire, nous utiliserons un attribut « xml:lang » ayant
    pour valeur un code ISO à deux caractères pour
    représenter la langue : « fr » pour français,
    « en » pour anglais, et ainsi de suite.
    Notre exemple modifié se lit comme suit :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">contact</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/2000/10/swap/pim/contact</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">contact</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Person</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">contact</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">fullName</span><span style="color:#a65700; ">&gt;</span>Daniel Lemire<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">contact</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">fullName</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">contact</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">mailbox</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">mailto:lemire@gmail.com</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">contact</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">personalTitle</span> <span style="color:#666616; ">xml</span><span style="color:#800080; ">:</span><span style="color:#074726; ">lang</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">fr</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>Professeur<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">contact</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">personalTitle</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">contact</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Person</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Le choix de la langue ne constitue pas une nouvelle relation RDF, mais vient
    simplement annoter l'objet :
    dans un tableau sujet/verbe/objet, nous nous contenterons, par exemple, de
    remplacer « "Professeur" »
    par « "Professeur" (français) ».
</p>
<p>
 Nous pouvons résumer le RDF comme ceci :
</p>
<ul>
 <li>
  Le RDF peut être utilisé pour représenter tout objet, tant un site web
        qu'un individu.
 </li>
 <li>
  Le RDF peut être traité par une machine.
 </li>
 <li>
  Le RDF est composé de triplets : sujet/verbe/objet.
 </li>
 <li>
  Le sujet est toujours identifié par un URI; mais dans certains cas, on
        peut omettre l'URI et alors, un URI factice sera généré dynamiquement.
 </li>
 <li>
  Le verbe est toujours identifié par un URI, sans aucune exception.
 </li>
 <li>
  L'objet est soit un URI, soit une valeur explicite (une chaîne de
        caractères, par exemple).
 </li>
 <li>
  Le RDF peut être représenté en XML.
 </li>
</ul>
<h2>
 Le RDF en XML
</h2>
<p>
 <b>
  Avertissement.-
 </b>
 Tous les contenus RDF ne peuvent être représentés en
    XML
    selon la méthode que nous venons de présenter. La grande majorité du contenu
    RDF
    peut l'être, mais il y a des exceptions. Pour éviter les problèmes, nous
    supposerons ici que l'URI du verbe prend la forme
    « http://www.domaine.com/blabla/bla#vvv ». En d'autres termes,
    l'URI du verbe contient le symbole du dièse ( # )
    et le texte après ce symbole est un nom XML valable (pouvant être utilisé
    comme balise).
</p>
<p>
 Il existe plusieurs façons de représenter le RDF en XML, mais nous
    n'étudierons que
    l'approche préconisée par le W3C, qui est l'approche la plus courante. Par
    ailleurs, nous n'étudierons
    pas toute la syntaxe RDF/XML, mais seulement ce qui est nécessaire pour
    comprendre
    la majorité du RDF qui se trouve actuellement sur le web.
</p>
<p>
 En règle générale, les documents XML représentant du contenu RDF n'ont pas
    de DTD, mais utilisent
    les espaces de noms. Nous commençons habituellement un document par une
    déclaration XML qui
    sera soit « &lt;?xml version="1.0"?&gt; », soit « &lt;?xml
    version="1.0" encoding="ISO-8859-1"?&gt; »
    pour permettre l'utilisation des accents français. Ensuite,
    viendra toujours l'élément RDF comme élément-racine. Ainsi, un des documents
    XML les plus
    simples possibles représentant du contenu RDF est :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Observez l'utilisation de l'espace de noms identifié par l'URI
    « http://www.w3.org/1999/02/22-rdf-syntax-ns# ».
    Le fait de noter l'espace de noms par les trois lettres « rdf »
    est sans conséquence et nous pourrions aussi écrire :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">nimportequoidautre</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">nimportequoidautre</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">nimportequoidautre</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 L'important, c'est que l'élément-racine RDF soit dans l'espace de nom
    « http://www.w3.org/1999/02/22-rdf-syntax-ns# ».
    Supposons maintenant que nous voulions décrire l'affirmation RDF
    suivante :
</p>
<div class="tableau style1">
 <table border="1" class="tabNormal">
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
     http://lemire.me/fr/
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#mailbox
    </td>
    <td>
     mailto:lemire@gmail.com
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 La première étape consiste à décomposer l'URI du verbe en deux parties :
    l'URI jusqu'au symbole « # » inclusivement, soit
    « http://www.w3.org/2000/10/swap/pim/contact# »,
    et le reste du texte, soit « mailbox ». La première partie devient
    un espace de noms, et la deuxième, appelée fragment,
    deviendra un nom d'élément. On utilise ensuite habituellement une balise
    « Description »
    dans l'espace de noms
    « http://www.w3.org/1999/02/22-rdf-syntax-ns# »
    avec le nom d'attribut « about » comme ceci :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/2000/10/swap/pim/contact</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">mailbox</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">mailto:lemire@gmail.com</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Dans cet exemple, le sujet est la valeur d'attribut de « about »,
    soit « http://lemire.me/fr/ »,
    le verbe est le nom de l'élément contenu dans l'élément
    « rdf:Description », ici « mailbox », auquel on ajoute
    en préfixe l'espace de noms auquel il appartient, soit
    « http://www.w3.org/2000/10/swap/pim/contact# ».
    L'URI de l'objet est la valeur de l'attribut « rdf:resource »,
    soit « mailto:lemire@gmail.com ».
</p>
<p>
 Pour nous assurer de bien comprendre, voyons un autre exemple, quoique plus
    abstrait. Supposons que nous
    ayons le contenu RDF suivant :
</p>
<div class="tableau style1">
 <table border="1" class="tabNormal">
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
     http://domaine.com/page/
    </td>
    <td>
     http://domaine.com#unverbe
    </td>
    <td>
     http://www.objet.com/
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 Nous pourrions utiliser la représentation XML suivante :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">domaine.com</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://domaine.com/page/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">unverbe</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.objet.com/</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Que devons-nous faire si l'objet n'est pas un URI, mais une chaîne de
    caractères?
    Dans ce cas, nous omettrons l'attribut « rdf:resource » et nous
    placerons notre valeur
    dans l'élément. Ainsi, pour représenter le contenu RDF suivant :
</p>
<div class="tableau style1">
 <table border="1" class="tabNormal">
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
     http://lemire.me/fr/
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#personalTitle
    </td>
    <td>
     "Professeur"
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 nous pourrons utiliser le code XML qui suit :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/2000/10/swap/pim/contact</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">personalTitle</span><span style="color:#a65700; ">&gt;</span>Professeur<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">personalTitle</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Encore une fois, les conventions relatives aux espaces de noms s'appliquent
    et nous pourrions
    remplacer le XML de l'exemple précédent par celui-ci :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">espacedenom</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/2000/10/swap/pim/contact</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">personalTitle</span><span style="color:#a65700; ">&gt;</span>Professeur<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">personalTitle</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Donc, pour représenter l'ensemble des données RDF suivantes :
</p>
<div class="tableau style1">
 <table border="1" class="tabNormal">
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
     http://lemire.me/fr/
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#fullName
    </td>
    <td>
     "Daniel Lemire"
    </td>
   </tr>
   <tr>
    <td>
     http://lemire.me/fr/
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#mailbox
    </td>
    <td>
     mailto:lemire@gmail.com
    </td>
   </tr>
   <tr>
    <td>
     http://lemire.me/fr/
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#personalTitle
    </td>
    <td>
     "Professeur"
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 nous utiliserons plusieurs éléments, les uns à la suite des autres, comme
    ceci :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">espacedenom</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/2000/10/swap/pim/contact</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">fullName</span><span style="color:#a65700; ">&gt;</span>Daniel Lemire<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">fullName</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">mailbox</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">mailto:lemire@gmail.com</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">personalTitle</span><span style="color:#a65700; ">&gt;</span>Professeur<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">personalTitle</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 En pratique toutefois, nous ne répétons pas l'élément
    « Description » avec la même valeur
    d'attribut « about »; nous préférons la syntaxe qui suit :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">espacedenom</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/2000/10/swap/pim/contact</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">fullName</span><span style="color:#a65700; ">&gt;</span>Daniel Lemire<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">fullName</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">mailbox</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">mailto:lemire@gmail.com</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">personalTitle</span><span style="color:#a65700; ">&gt;</span>Professeur<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">personalTitle</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Et comme l'ordre est sans importance en RDF, nous pourrions aussi avoir le
    XML suivant :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">espacedenom</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/2000/10/swap/pim/contact</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">personalTitle</span><span style="color:#a65700; ">&gt;</span>Professeur<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">personalTitle</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">fullName</span><span style="color:#a65700; ">&gt;</span>Daniel Lemire<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">fullName</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">espacedenom</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">mailbox</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">mailto:lemire@gmail.com</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<h2>
 Les classes en RDF
</h2>
<p>
 Jusqu'à présent, nous n'avons pas représenté en XML l'affirmation
    suivante :
</p>
<div class="tableau style1">
 <table border="1" class="tabNormal">
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
     http://lemire.me/fr/
    </td>
    <td>
     http://www.w3.org/1999/ 02/22-rdf-syntax-ns#type
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#Person
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 Évidemment, nous pouvons tout simplement écrire ceci :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/2000/10/swap/pim/contact</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">type</span>
    <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.w3.org/2000/10/swap/pim/contact#Person</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Mais, avouons-le, c'est assez peu lisible.
    Dans « http://www.w3.org/2000/10/swap/pim/contact#Person »,
    « Person » est un fragment.
    Dans les cas où l'URI contient un fragment, nous représentons l'affirmation
    de la façon suivante :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/2000/10/swap/pim/contact</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">Person</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">Person</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Nous remplaçons « rdf:Description » par le nom de la classe, soit
    « Person », avec le préfixe
    « http://www.w3.org/2000/10/swap/pim/contact# ».
    En pratique, cette dernière approche est presque toujours utilisée et son
    avantage devient évident
    quand on combine toutes les affirmations RDF de la première section :
</p>
<div class="tableau style1">
 <table border="1" class="tabNormal">
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
     http://lemire.me/ en/
    </td>
    <td>
     http://www.w3.org/1999/ 02/22-rdf-syntax-ns#type
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#Person
    </td>
   </tr>
   <tr>
    <td>
     http://lemire.me/ en/
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#fullName
    </td>
    <td>
     "Daniel Lemire"
    </td>
   </tr>
   <tr>
    <td>
     http://lemire.me/ en/
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#mailbox
    </td>
    <td>
     mailto:lemire@gmail.com
    </td>
   </tr>
   <tr>
    <td>
     http://lemire.me/ en/
    </td>
    <td>
     http://www.w3.org/2000/ 10/swap/pim/contact#personalTitle
    </td>
    <td>
     "Professeur"
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 Nous savons maintenant que nous pouvons représenter toutes ses informations
    par le XML suivant :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/2000/10/swap/pim/contact</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">Person</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">fullName</span><span style="color:#a65700; ">&gt;</span>Daniel Lemire<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">fullName</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">mailbox</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">mailto:lemire@gmail.com</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">personalTitle</span><span style="color:#a65700; ">&gt;</span>Professeur<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">personalTitle</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">Person</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 C'est comme ça que nous pouvons écrire « Il y a une personne appelée
    Daniel Lemire dont
    l'adresse de courriel est lemire@gmail.com et qui est professeur. » en
    RDF/XML.
</p>
<h2>
 Et s'il n'y a pas de symbole « # » dans l'URI?
</h2>
<p>
 Dans les exemples précédents, nous supposions que l'URI (du verbe) contenait
    un symbole « # »,
    ce qui nous permettait de la décomposer en deux parties (nom et préfixe).
    Mais quoi faire si l'URI
    prend plutôt la forme « http://www.ondelette.com/employeur »? Dans
    un tel cas,
    nous pouvons choisir de retenir « http://www.ondelette.com/ »
    comme préfixe et « employeur » comme nom.
    Nous pourrons donc représenter les données RDF suivantes :
</p>
<div class="tableau style1">
 <table border="1" class="tabNormal">
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
     http://lemire.me/fr/
    </td>
    <td>
     http://www.ondelette.com/employeur
    </td>
    <td>
     http://www.uquebec.ca/
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 par le XML suivant :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.ondelette.com</span><span style="color:#40015a; ">/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">employeur</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.uquebec.ca/</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<h2>
 Des objets qui sont eux-mêmes des sujets
</h2>
<p>
 Supposons que nous voulons dire que la pièce de théatre Othello a comme
    auteur William Shakespeare. En fait, nous voulons faire quatre
    affirmations :
    « Othello est une pièce de théatre », « Shakespeare est une
    personne »,
    « Shakespeare est l'auteur d'Othello » et « Shakespeare a
    pour nom "William Shakespeare" ».
    Nous pourrions choisir de représenter en RDF
    ces quatre affirmations selon le tableau qui suit :
</p>
<div class="tableau style1">
 <table border="1" class="tabNormal">
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
     http://www.othello.org/
    </td>
    <td>
     http://www.w3.org/1999/ 02/22-rdf-syntax-ns#type
    </td>
    <td>
     http://unuri.org/PieceDeTheatre
    </td>
   </tr>
   <tr>
    <td>
     http://www.othello.org/
    </td>
    <td>
     http://unuri.org/auteur
    </td>
    <td>
     http://www.shakespeare.org
    </td>
   </tr>
   <tr>
    <td>
     http://www.shakespeare.org
    </td>
    <td>
     http://www.w3.org/1999/ 02/22-rdf-syntax-ns#type
    </td>
    <td>
     http://unuri.org/Personne
    </td>
   </tr>
   <tr>
    <td>
     http://www.shakespeare.org
    </td>
    <td>
     http://unuri.org/nom
    </td>
    <td>
     "William Shakespeare"
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 Nous pouvons utiliser la représentation XML suivante :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">unuri.org</span><span style="color:#40015a; ">/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">PieceDeTheatre</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.othello.org/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">auteur</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.shakespeare.org</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">PieceDeTheatre</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">Personne</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.shakespeare.org</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>William Shakespeare<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">Personne</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 La représentation graphique du tableau RDF est :
</p>
<svg font-size="0.65em" height="222pt" viewbox="0 0 373 222" width="373pt" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
 ../module5/othello.pdf
 <g class="graph" id="graph0">
  <!-- http://www.othello.org/ -->
  <g class="node" id="node1">
   http://www.othello.org/
   <ellipse cx="117" cy="23" rx="79" ry="18" style="fill:none;stroke:black;">
   </ellipse>
   <text text-anchor="middle" x="117" y="28">
    http://www.othello.org/
   </text>
  </g>
  <!-- PieceDeTheatre -->
  <g class="node" id="node3">
   PieceDeTheatre
   <ellipse cx="63" cy="111" rx="58" ry="18" style="fill:none;stroke:black;">
   </ellipse>
   <text text-anchor="middle" x="63" y="116">
    PieceDeTheatre
   </text>
  </g>
  <!-- http://www.othello.org/-&gt;PieceDeTheatre -->
  <g class="edge" id="edge2">
   http://www.othello.org/-&gt;PieceDeTheatre
   <path d="M106,41C99,53 88,70 79,84" style="fill:none;stroke:black;">
   </path>
   <polygon points="82,86 74,93 76,83 82,86" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="109" y="72">
    type
   </text>
  </g>
  <!-- http://www.shakespeare.org -->
  <g class="node" id="node5">
   http://www.shakespeare.org
   <ellipse cx="230" cy="111" rx="91" ry="18" style="fill:none;stroke:black;">
   </ellipse>
   <text text-anchor="middle" x="230" y="116">
    http://www.shakespeare.org
   </text>
  </g>
  <!-- http://www.othello.org/-&gt;http://www.shakespeare.org -->
  <g class="edge" id="edge4">
   http://www.othello.org/-&gt;http://www.shakespeare.org
   <path d="M139,40C156,54 180,72 199,87" style="fill:none;stroke:black;">
   </path>
   <polygon points="201,84 207,93 197,90 201,84" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="196" y="72">
    auteur
   </text>
  </g>
  <!-- Personne -->
  <g class="node" id="node7">
   Personne
   <ellipse cx="165" cy="199" rx="39" ry="18" style="fill:none;stroke:black;">
   </ellipse>
   <text text-anchor="middle" x="165" y="204">
    Personne
   </text>
  </g>
  <!-- http://www.shakespeare.org-&gt;Personne -->
  <g class="edge" id="edge6">
   http://www.shakespeare.org-&gt;Personne
   <path d="M217,129C207,142 194,160 184,174" style="fill:none;stroke:black;">
   </path>
   <polygon points="187,176 178,182 181,172 187,176" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="215" y="160">
    type
   </text>
  </g>
  <!-- William Shakespeare -->
  <g class="node" id="node9">
   William Shakespeare
   <ellipse cx="295" cy="199" rx="73" ry="18" style="fill:none;stroke:black;">
   </ellipse>
   <text text-anchor="middle" x="295" y="204">
    William
                Shakespeare
   </text>
  </g>
  <!-- http://www.shakespeare.org-&gt;William Shakespeare -->
  <g class="edge" id="edge8">
   http://www.shakespeare.org-&gt;William Shakespeare
   <path d="M243,129C253,141 266,159 276,173" style="fill:none;stroke:black;">
   </path>
   <polygon points="279,171 282,181 273,175 279,171" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="277" y="160">
    nom
   </text>
  </g>
 </g>
</svg>
<p>
 Nous pouvons cependant le faire plus brièvement. Considérons d'abord le
    modèle suivant :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">unuri.org</span><span style="color:#40015a; ">/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">PieceDeTheatre</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.othello.org/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">auteur</span><span style="color:#a65700; ">&gt;</span>
    (...)
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">auteur</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">PieceDeTheatre</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Nous avons vu que si nous mettons un nœud de texte là où les points
    « (...) » apparaissent,
    nous associerons « http://www.othello.org/ » avec un objet texte
    par le
    verbe « http://unuri.org/auteur ». Cependant, si nous mettons
    plutôt un
    élément muni d'un attribut « rdf:about », ce sera l'URI contenu
    dans l'attribut qui deviendra l'objet; nous
    gagnons alors la possibilité d'utiliser ce même objet comme sujet à son
    tour, comme dans cet exemple :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">unuri.org</span><span style="color:#40015a; ">/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">PieceDeTheatre</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.othello.org/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#696969; ">&lt;!--</span><span style="color:#696969; ">
        le verbe est </span><span style="color:#5555dd; ">http://unuri.org/auteur</span><span style="color:#696969; "> </span><span style="color:#696969; ">--&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">auteur</span><span style="color:#a65700; ">&gt;</span> <span style="color:#696969; ">&lt;!--</span><span style="color:#696969; ">
        début de l'objet </span><span style="color:#696969; ">--&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">Personne</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.shakespeare.org</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#696969; ">&lt;!--</span><span style="color:#696969; ">
        l'objet devient un sujet à son tour </span><span style="color:#696969; ">--&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>William Shakespeare<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">Personne</span><span style="color:#a65700; ">&gt;</span><span style="color:#696969; ">&lt;!--</span><span style="color:#696969; "> fin
        de l'objet </span><span style="color:#696969; ">--&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">auteur</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">PieceDeTheatre</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Ce nouveau document RDF est équivalent aux trois affirmations RDF du début,
    mais il est un peu plus court.
</p>
<p>
 Nous pourrions pousser l'expérience plus loin - ce qui peut devenir
    absurde - comme dans l'exemple qui suit :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">unuri.org</span><span style="color:#40015a; ">/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">PieceDeTheatre</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.othello.org/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">auteur</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.shakespeare.org</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">PieceDeTheatre</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">Personne</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.shakespeare.org</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">Texte</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.texte.org/william</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">contenu</span><span style="color:#a65700; ">&gt;</span>
    William Shakespeare
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">contenu</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">Texte</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">Personne</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Ce document est maintenant équivalent au tableau suivant :
</p>
<div class="tableau style1">
 <table border="1" class="tabNormal">
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
     http://www.othello.org/
    </td>
    <td>
     http://www.w3.org/1999/ 02/22-rdf-syntax-ns#type
    </td>
    <td>
     http://unuri.org/PieceDeTheatre
    </td>
   </tr>
   <tr>
    <td>
     http://www.othello.org/
    </td>
    <td>
     http://unuri.org/auteur
    </td>
    <td>
     http://www.shakespeare.org
    </td>
   </tr>
   <tr>
    <td>
     http://www.shakespeare.org
    </td>
    <td>
     http://www.w3.org/1999/ 02/22-rdf-syntax-ns#type
    </td>
    <td>
     http://unuri.org/Personne
    </td>
   </tr>
   <tr>
    <td>
     http://www.texte.org/william
    </td>
    <td>
     http://www.w3.org/1999/ 02/22-rdf-syntax-ns#type
    </td>
    <td>
     http://unuri.org/Texte
    </td>
   </tr>
   <tr>
    <td>
     http://www.texte.org/william
    </td>
    <td>
     http://unuri.org/contenu
    </td>
    <td>
     "William Shakespeare"
    </td>
   </tr>
   <tr>
    <td>
     http://www.shakespeare.org
    </td>
    <td>
     http://unuri.org/nom
    </td>
    <td>
     http://www.texte.org/william
    </td>
   </tr>
  </tbody>
 </table>
</div>
<h2>
 Les contenants en RDF
</h2>
<p>
 Il arrive fréquemment, en pratique, que l'on doive donner comme valeur à un
    objet, non pas une
    chaîne de caractères, mais plutôt un ensemble de chaînes de caractères. Par
    exemple, nous pouvons
    vouloir affirmer que « les étudiants du cours 101 sont Jean
    Roberge, Alexandre Coma et Julie LeChat ».
    Comment le faire? Supposons que l'URI du cours est
    « http://www.teluq.ca/101 » et que le verbe
    correspondant à « être inscrit à un cours » est identifié par
    l'URI « http://www.education.com#inscription ».
    Nous pouvons alors essayer ceci :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.education.com</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.teluq.ca/101</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">inscription</span><span style="color:#a65700; ">&gt;</span>Jean Roberge<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">inscription</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">inscription</span><span style="color:#a65700; ">&gt;</span>Alexandre Coma<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">inscription</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">inscription</span><span style="color:#a65700; ">&gt;</span>Julie LeChat<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">inscription</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Cela équivaut à remplacer l'affirmation « les étudiants du cours 101
    sont Jean Roberge,
    Alexandre Coma et Julie LeChat » par les trois affirmations « le
    cours 101 a comme étudiant Jean Roberge »,
    « le cours 101 a comme étudiant Alexandre Coma »,
    « le cours 101 a comme étudiant Julie LeChat ». Il n'est pas
    certain qu'une telle décomposition de l'affirmation préserve toujours
    le sens original. Par exemple, nous pourrions vouloir donner la liste
    complète de tous les étudiants dans le cours.
    RDF nous permet de regrouper tous les étudiants dans un seul élément
    « Bag » (sac, en anglais) comme ceci :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.education.com</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.teluq.ca/101</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">inscription</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Bag</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>Jean Roberge<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>Alexandre Coma<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>Julie LeChat<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Bag</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">inscription</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Les éléments dans un « Bag » ne sont pas ordonnés. Nous pourrons
    remplacer le XML précédent
    par celui-ci, sans problème :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.education.com</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.teluq.ca/101</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">inscription</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Bag</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>Julie LeChat<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>Jean Roberge<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>Alexandre Coma<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Bag</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">inscription</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Si l'ordre importe, alors nous utiliserons un élément « Seq » (pour
    séquence), comme dans
    l'exemple suivant qui énonce les jours de la semaine, dans l'ordre :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.jourdelasemaine.com</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.jourdelasemaine.com/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">journees</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Seq</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>dimanche<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>lundi<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>mardi<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>mercredi<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>jeudi<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>vendredi<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>samedi<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Seq</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">journees</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Finalement, nous pourrions ne pas connaître exactement la valeur de l'objet,
    mais savoir
    que la valeur appartient à un ensemble fini de possibilités. Par exemple, si
    nous jouons
    à un jeu de détective et qu'il n'y a que trois coupables possibles (le
    majordome, la princesse
    et le seigneur), nous écrirons :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.jeududetective.com</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span>
    <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.jeududetective.com/partie/2004/10/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">suspects</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Alt</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>majordome<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>princesse<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>seigneur<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Alt</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">suspects</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<h2>
 RDFa
</h2>
<p>
 Il peut sembler un peu lourd de créer des fichiers XML distincts pour stocker
    le RDF.
    Heureusement, il existe donc plusieurs approches pour inscrire le RDF à même
    des fichiers XHTML.
    La spécification
 <a href="http://en.wikipedia.org/wiki/RDFa">
  RDFa
 </a>
 permet
    d'inscrire du RDF directement au sein d'un
    document XHTML avec les attributs about et property. Voici un exemple
    d'annotation RDFa ajoutée
    à un élément XHTML :
</p>
<pre><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">ul</span> <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">dc</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">purl.org</span><span style="color:#40015a; ">/dc/elements/1.1/</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.example.com/books/wikinomics</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">li</span> <span style="color:#274796; ">property</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">dc:title</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>Wikinomics<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">li</span> <span style="color:#274796; ">property</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">dc:author</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>Don Tapscott<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">li</span> <span style="color:#274796; ">property</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">dc:date</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>2006-10-01<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">li</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">ul</span><span style="color:#a65700; ">&gt;</span>
</pre>
<h2>
 Conclusion
</h2>
<p>
 Nous avons vu que le modèle RDF sert à décrire pratiquement n'importe quoi en
    associant des URI à tous les objets et relations. Les données RDF peuvent
    généralement
    être représentées en XML selon l'approche que nous avons décrite, ce qui
    permet de combiner les avantages
    du XML (format entièrement normalisé et non propriétaire, outils très
    disponibles, etc.),
    tout en gardant les avantages du RDF (contenu pouvant être traité par des
    machines,
    relative simplicité).
</p>
