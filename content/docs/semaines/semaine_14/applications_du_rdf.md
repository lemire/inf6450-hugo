---
title: "Applications du RDF"
weight: 20
---
<h1>
 Applications du RDF
</h1>
<p>
 Le RDF se retrouve un peu partout sur le web, parfois de façon
    « invisible »,
    c'est-à-dire qu'il est souvent utilisé dans les échanges automatiques entre
    les logiciels. En outre, il est
    utilisé au sein des portails, par exemple. Voyons maintenant
    quatre applications RDF bien établies :
</p>
<dl>
 <dt>
  Dublin Core
 </dt>
 <dd>
  Il s'agit sans doute de l'utilisation la plus connue et
        la plus répandue du RDF. La norme
  <i>
   Dublin Core
  </i>
  est assez simple et
        vise à
        décrire les travaux rendus disponibles sur le web (auteur, titre, date,
        etc.). Elle est notamment utilisée au sein des livres électroniques
        (comme les EPUB). Cette norme s'inspire de la bibliothéconomie.
 </dd>
 <dt>
  Creative Commons
 </dt>
 <dd>
  Il s'agit d'une façon de décrire les
        droits accordés sur le contenu placé sur le web.
        Par exemple, vous voulez savoir si vous pouvez recopier telle ou telle
        page web; si l'auteur a utilisé
        la norme
  <i>
   Creative Commons
  </i>
  , alors vous devriez pouvoir savoir ce
        qui est permis par l'auteur.
 </dd>
 <dt>
  FOAF
 </dt>
 <dd>
  La norme
  <i>
   FOAF
  </i>
  (« Friend Of A Friend » - « ami d'un
        ami ») permet
        de décrire un individu et les gens qu'il connaît. Cette norme sert
        à traiter les réseaux sociaux.
 </dd>
 <dt>
  RSS/RDF
 </dt>
 <dd>
  La norme
  <i>
   RSS
  </i>
  est utilisée par les blogues et sites de nouvelles.
        Le site mozilla.org a plusieurs articles sur le sujet (
  <a href="http://developer.mozilla.org/en/docs/RSS">
   http://developer.mozilla.org/en/docs/RSS
  </a>
  ).
        En gros,
        un document RSS/RDF contient une version XML des dernières nouvelles.
        Par la suite,
        plusieurs de ces fichiers XML peuvent être combinés pour créer un
        portail de nouvelles ou
        utilisés avec un outil-client de type « RSS aggregator » pour
        obtenir
        automatiquement les dernières nouvelles.
 </dd>
</dl>
<h2>
 Un exemple :
 <i>
  Dublin Core
 </i>
</h2>
<p>
 La norme
 <i>
  Dublin Core
 </i>
 définit plusieurs « verbes » (au sein
    du RDF);
    on peut en consulter la liste à l'adresse
 <a href="http://dublincore.org/documents/dcmi-terms/">
  http://dublincore.org/documents/dcmi-terms/
 </a>
 (en anglais).
    Cette norme a été publiée pour la première fois
    en juillet 1999.
</p>
<p>
 Le préfixe de la norme
 <i>
  Dublin Core
 </i>
 est
    « http://purl.org/dc/elements/1.1/ », du moins pour les
    éléments de base présentés ici. Voici les URI complets et leur
    signification :
</p>
<dl>
 <dt>
  http://purl.org/dc/elements/1.1/creator
 </dt>
 <dd>
  Personne ou organisme qui est l'auteur du travail.
 </dd>
 <dt>
  http://purl.org/dc/elements/1.1/contributor
 </dt>
 <dd>
  Personne ou organisme qui a contribué à un travail, mais sans en être
        l'auteur.
 </dd>
 <dt>
  http://purl.org/dc/elements/1.1/coverage
 </dt>
 <dd>
  Lieu et période correspondant au travail.
 </dd>
 <dt>
  http://purl.org/dc/elements/1.1/date
 </dt>
 <dd>
  Date associée au travail, généralement sous la forme AAAA-MM-JJ. Il peut
        s'agir de
        la date de publication, de création ou de la dernière révision.
 </dd>
 <dt>
  http://purl.org/dc/elements/1.1/description
 </dt>
 <dd>
  Brève description du travail.
 </dd>
 <dt>
  http://purl.org/dc/elements/1.1/format
 </dt>
 <dd>
  Format sous lequel est publié le travail. Si le travail est publié en
        HTML, alors on utilisera souvent « text/html » pour décrire le
        format.
 </dd>
 <dt>
  http://purl.org/dc/elements/1.1/identifier
 </dt>
 <dd>
  Code ou URI qui correspond de façon unique au travail.
        Si un travail est publié à une adresse web, on peut utiliser
        cette adresse comme URI; si c'est un livre avec un ISBN, on peut
        utiliser un URI de la forme « urn:ISBN:0-123-12345-1 ».
 </dd>
 <dt>
  http://purl.org/dc/elements/1.1/language
 </dt>
 <dd>
  Code ISO-639/ISO-3166 décrivant le travail. Si le travail est publié en
        français,
        on peut utiliser « fr-CA »; sinon, en anglais, ce serait
        « en-CA » (CA signifie Canada).
 </dd>
 <dt>
  http://purl.org/dc/elements/1.1/publisher
 </dt>
 <dd>
  Organisme responsable de la publication du travail.
 </dd>
 <dt>
  http://purl.org/dc/elements/1.1/relation
 </dt>
 <dd>
  Ressource liée au travail. Par exemple, pour un travail fait en classe,
        on peut établir un lien avec l'exposé du travail.
 </dd>
 <dt>
  http://purl.org/dc/elements/1.1/rights
 </dt>
 <dd>
  Contient souvent une affirmation permettant de savoir qui est
        propriétaire du travail (détenteur du droit d'auteur).
 </dd>
 <dt>
  http://purl.org/dc/elements/1.1/source
 </dt>
 <dd>
  Résumé du travail de quelqu'un d'autre. Cet URI permet de pointer vers
        la source originale.
 </dd>
 <dt>
  http://purl.org/dc/elements/1.1/subject
 </dt>
 <dd>
  Généralement, une liste de mots clés.
 </dd>
 <dt>
  http://purl.org/dc/elements/1.1/title
 </dt>
 <dd>
  Titre du travail.
 </dd>
 <dt>
  http://purl.org/dc/elements/1.1/type
 </dt>
 <dd>
  Type de la ressource (texte, image, etc.). Notons que le
        « type » est différent du « format ».
        Par exemple, une image peut être en format Jpeg ou Gif, un texte peut
        être en format Word ou ASCII.
 </dd>
</dl>
<p>
 Voyons comment nous pouvons décrire ce texte que vous êtes en train de lire,
    en utilisant la norme
 <i>
  Dublin Core
 </i>
 .
    Attribuons-lui l'URI « http://teluq.ca/rdfexemples.html ».
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
     http://teluq.ca/ rdfexemples.html
    </td>
    <td>
     http://purl.org/ dc/elements/1.1/creator
    </td>
    <td>
     http://lemire.me/fr/
    </td>
   </tr>
   <tr>
    <td>
     http://teluq.ca/ rdfexemples.html
    </td>
    <td>
     http://purl.org/ dc/elements/1.1/date
    </td>
    <td>
     "2004-07-27"
    </td>
   </tr>
   <tr>
    <td>
     http://teluq.ca/ rdfexemples.html
    </td>
    <td>
     http://purl.org/ dc/elements/1.1/title
    </td>
    <td>
     "Introduction au RDF"
    </td>
   </tr>
   <tr>
    <td>
     http://teluq.ca/ rdfexemples.html
    </td>
    <td>
     http://purl.org/ dc/elements/1.1/type
    </td>
    <td>
     "text"
    </td>
   </tr>
   <tr>
    <td>
     http://teluq.ca/ rdfexemples.html
    </td>
    <td>
     http://purl.org/ dc/elements/1.1/Language
    </td>
    <td>
     "fr-CA"
    </td>
   </tr>
   <tr>
    <td>
     http://teluq.ca/ rdfexemples.html
    </td>
    <td>
     http://purl.org/ dc/elements/1.1/subject
    </td>
    <td>
     "RDF, Dublin Core, Creative Commons, FOAF, RSS/RDF"
    </td>
   </tr>
   <tr>
    <td>
     http://teluq.ca/ rdfexemples.html
    </td>
    <td>
     http://purl.org/ dc/elements/1.1/rights
    </td>
    <td>
     "Copyright 2005 Daniel Lemire"
    </td>
   </tr>
   <tr>
    <td>
     http://teluq.ca/ rdfexemples.html
    </td>
    <td>
     http://purl.org/ dc/elements/1.1/description
    </td>
    <td>
     "Un document comprenant des exemples d'utilisation du RDF en
                    gestion des connaissances."
    </td>
   </tr>
   <tr>
    <td>
     http://teluq.ca/ rdfexemples.html
    </td>
    <td>
     http://purl.org/ dc/elements/1.1/format
    </td>
    <td>
     "text/html"
    </td>
   </tr>
   <tr>
    <td>
     http://teluq.ca/ rdfexemples.html
    </td>
    <td>
     http://purl.org/ dc/elements/1.1/identifier
    </td>
    <td>
     http://teluq.ca/ rdfexemples.html
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 Nous pouvons aussi représenter ce tableau en XML comme ceci :
</p>
<pre><span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">dc</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">purl.org</span><span style="color:#40015a; ">/dc/elements/1.1/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://teluq.ca/rdfexemples.html</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">creator</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">date</span><span style="color:#a65700; ">&gt;</span>2004-07-27<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">date</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Introduction au RDF<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">type</span><span style="color:#a65700; ">&gt;</span>text<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">type</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Language</span><span style="color:#a65700; ">&gt;</span>fr-CA<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Language</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">subject</span><span style="color:#a65700; ">&gt;</span>RDF, Dublin Core, Creative Commons,
    FOAF, RSS/RDF<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">subject</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">rights</span><span style="color:#a65700; ">&gt;</span>Copyright 2005 Daniel Lemire<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">rights</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">description</span><span style="color:#a65700; ">&gt;</span>Un document comprenant des exemples
    d'utilisation du RDF en gestion des connaissances.<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">format</span><span style="color:#a65700; ">&gt;</span>text/html<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">format</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">identifier</span>
    <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://teluq.ca/rdfexemples.html</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Nous pouvons aussi représenter ce tableau sous la forme d'un graphe :
</p>
<svg contentstyletype="text/css" font-size="0.7em" height="500" preserveaspectratio="xMidYMid meet" version="1.0" width="600" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" zoomandpan="magnify">
 ../module5/dc.pdf
 <g class="graph" id="graph0" transform="scale(1)">
  <!-- 0 -->
  <g class="node" id="node1">
   <a xlink:actuate="onRequest" xlink:href="http%3A//www.uquebec.ca/rdfexemples.html" xlink:show="replace" xlink:title="rdfexemples.html" xlink:type="simple">
    <ellipse cx="67" cy="239" rx="62" ry="18" style="fill:none;stroke:black;">
    </ellipse>
    <text text-anchor="middle" x="67" y="244">
     rdfexemples.html
    </text>
   </a>
  </g>
  <!-- 0&#45;&gt;0 -->
  <g class="edge" id="edge20">
   <path d="M30,224C17,214 30,203 67,203 93,203 107,208 109,215" style="fill:none;stroke:black;">
   </path>
   <polygon points="112,217 104,224 106,214 112,217" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="67" y="200">
    identifier
   </text>
  </g>
  <!-- 1 -->
  <g class="node" id="node2">
   <ellipse cx="388" cy="23" rx="106" ry="18" style="fill:none;stroke:black;">
   </ellipse>
   <text font-size="0.9em" text-anchor="middle" x="388" y="28">
    http://lemire.me/fr/
   </text>
  </g>
  <!-- 0&#45;&gt;1 -->
  <g class="edge" id="edge2">
   <path d="M73,221C84,191 109,131 147,93 182,59 233,41 280,32" style="fill:none;stroke:black;">
   </path>
   <polygon points="280,29 290,30 281,35 280,29" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="179" y="52">
    creator
   </text>
  </g>
  <!-- 2 -->
  <g class="node" id="node4">
   <polygon points="428,59 348,59 348,95 428,95 428,59" style="fill:none;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="388" y="82">
    2004-07-27
   </text>
  </g>
  <!-- 0&#45;&gt;2 -->
  <g class="edge" id="edge4">
   <path d="M79,221C93,201 119,167 147,145 202,102 285,86 337,80" style="fill:none;stroke:black;">
   </path>
   <polygon points="337,77 347,79 337,83 337,77" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="179" y="110">
    date
   </text>
  </g>
  <!-- 3 -->
  <g class="node" id="node6">
   <polygon points="454,113 322,113 322,149 454,149 454,113" style="fill:none;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="388" y="136">
    Introduction au
                RDF
   </text>
  </g>
  <!-- 0&#45;&gt;3 -->
  <g class="edge" id="edge6">
   <path d="M92,222C108,212 128,200 147,190 183,173 192,169 229,158 255,151 285,145 311,141" style="fill:none;stroke:black;">
   </path>
   <polygon points="311,138 321,139 312,144 311,138" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="179" y="162">
    title
   </text>
  </g>
  <!-- 4 -->
  <g class="node" id="node8">
   <polygon points="415,167 361,167 361,203 415,203 415,167" style="fill:none;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="388" y="190">
    text
   </text>
  </g>
  <!-- 0&#45;&gt;4 -->
  <g class="edge" id="edge8">
   <path d="M114,227C125,224 136,221 147,219 220,206 303,195 351,189" style="fill:none;stroke:black;">
   </path>
   <polygon points="351,186 361,188 351,192 351,186" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="179" y="207">
    type
   </text>
  </g>
  <!-- 5 -->
  <g class="node" id="node10">
   <polygon points="415,221 361,221 361,257 415,257 415,221" style="fill:none;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="388" y="244">
    fr-CA
   </text>
  </g>
  <!-- 0&#45;&gt;5 -->
  <g class="edge" id="edge10">
   <path d="M129,239C195,239 296,239 351,239" style="fill:none;stroke:black;">
   </path>
   <polygon points="351,235 361,239 351,242 351,235" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="179" y="236">
    Language
   </text>
  </g>
  <!-- 6 -->
  <g class="node" id="node12">
   <polygon points="415,275 361,275 361,311 415,311 415,275" style="fill:none;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="388" y="298">
    RDF
   </text>
  </g>
  <!-- 0&#45;&gt;6 -->
  <g class="edge" id="edge12">
   <path d="M113,251C124,254 136,257 147,259 220,273 303,283 351,289" style="fill:none;stroke:black;">
   </path>
   <polygon points="351,286 361,290 351,292 351,286" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="179" y="256">
    subject
   </text>
  </g>
  <!-- 7 -->
  <g class="node" id="node14">
   <polygon points="482,329 294,329 294,365 482,365 482,329" style="fill:none;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="388" y="352">
    Copyright 2005 Daniel
                Lemire
   </text>
  </g>
  <!-- 0&#45;&gt;7 -->
  <g class="edge" id="edge14">
   <path d="M90,256C105,267 127,281 147,291 190,312 240,325 283,333" style="fill:none;stroke:black;">
   </path>
   <polygon points="284,330 293,335 283,336 284,330" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="179" y="288">
    rights
   </text>
  </g>
  <!-- 8 -->
  <g class="node" id="node16">
   <polygon points="547,383 229,383 229,423 547,423 547,383" style="fill:none;stroke:black;">
   </polygon>
   <text font-size="0.9em" text-anchor="middle" x="388" y="400">
    Un
                document comprenant des exemples
   </text>
   <text font-size="0.9em" text-anchor="middle" x="388" y="416">
    d'utilisation du RDF en gestion des connaissances.
   </text>
  </g>
  <!-- 0&#45;&gt;8 -->
  <g class="edge" id="edge16">
   <path d="M78,257C92,278 118,314 147,337 172,357 203,370 234,380" style="fill:none;stroke:black;">
   </path>
   <polygon points="235,377 244,383 233,383 235,377" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="179" y="334">
    description
   </text>
  </g>
  <!-- 9 -->
  <g class="node" id="node18">
   <polygon points="415,441 361,441 361,477 415,477 415,441" style="fill:none;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="388" y="464">
    html
   </text>
  </g>
  <!-- 0&#45;&gt;9 -->
  <g class="edge" id="edge18">
   <path d="M73,257C83,288 107,352 147,391 203,444 298,457 351,459" style="fill:none;stroke:black;">
   </path>
   <polygon points="351,455 361,459 351,462 351,455" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="179" y="388">
    format
   </text>
  </g>
 </g>
</svg>
<p>
 Évidemment,
 <i>
  Dublin Core
 </i>
 est une norme RDF et non pas une norme XML.
    Il est donc possible d'exprimer du contenu
 <i>
  Dublin Core
 </i>
 sans passer
    par le XML.
    Nous pourrions très bien nous en tenir au tableau sujet/verbe/complément ou
    utiliser une
    autre syntaxe. Un syntaxe plus populaire que le XML est sans doute celle
    décrite par la
 <a href="http://www.ietf.org/rfc/rfc2731.txt">
  RFC 2731
 </a>
 .
    Elle est facile à comprendre: il suffit d'utiliser des éléments meta avec
    les attributs name et content. La convention est que si l'attribute débute
    par le préfixe « DC.» ce qui suit est une information Dublin Core. Voici un
    exemple:
</p>
<pre><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">meta</span> <span style="color:#274796; ">name</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">DC.date</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">content</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">2004-07-27</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">meta</span> <span style="color:#274796; ">name</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">DC.title</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">content</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">Introduction au RDF</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">meta</span> <span style="color:#274796; ">name</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">DC.type</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">content</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">text</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">meta</span> <span style="color:#274796; ">name</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">DC.Language</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">content</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">fr-CA</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">meta</span> <span style="color:#274796; ">name</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">DC.subject</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">content</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">RDF,
        Dublin Core, Creative Commons, FOAF, RSS/RDF</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">meta</span> <span style="color:#274796; ">name</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">DC.rights</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">content</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">Copyright
        2005 Daniel Lemire</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">meta</span> <span style="color:#274796; ">name</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">DC.description</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">content</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">Un
        document comprenant des exemples</span>
    <span style="color:#0000e6; ">     d'utilisation du
        RDF en gestion des connaissances.</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">meta</span> <span style="color:#274796; ">name</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">DC.format</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">content</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">text/html</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
</pre>
<p>
 Notons aussi que les conventions d'espace de noms s'appliquent et que l'ordre
    n'est pas important.
    Nous pouvons donc remplacer le XML précédent par celui-ci :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">purl.org</span><span style="color:#40015a; ">/dc/elements/1.1/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://teluq.ca/rdfexemples.html</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">creator</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Introduction au RDF<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">date</span><span style="color:#a65700; ">&gt;</span>2004-07-27<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">date</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">type</span><span style="color:#a65700; ">&gt;</span>text<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">type</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">subject</span><span style="color:#a65700; ">&gt;</span>RDF, Dublin Core, Creative Commons,
    FOAF, RSS/RDF<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">subject</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">rights</span><span style="color:#a65700; ">&gt;</span>Copyright 2005 Daniel Lemire<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">rights</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">description</span><span style="color:#a65700; ">&gt;</span>Un document comprenant des exemples
    d'utilisation du RDF en gestion des connaissances.<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">format</span><span style="color:#a65700; ">&gt;</span>text/html<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">format</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">identifier</span>
    <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://teluq.ca/rdfexemples.html</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">Language</span><span style="color:#a65700; ">&gt;</span>fr-CA<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">Language</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Il existe des applications plus sophistiquées de la norme
 <i>
  Dublin Core
 </i>
 ,
    mais nous avons ici l'essentiel.
    Vous pouvez dès maintenant cataloguer les ressources d'une entreprise en
    utilisant simplement ce que nous venons de présenter.
    Comme la norme est utilisée partout dans le monde, il sera possible
    d'échanger ces
    descriptions ou d'utiliser des logiciels communs pour le traitement ou
    l'affichage des informations.
</p>
<h2>
 Un exemple :
 <i>
  Creative Commons
 </i>
</h2>
<p>
 Une des limites apparentes de la norme
 <i>
  Dublin Core
 </i>
 est son incapacité
    à spécifier de façon précise
    les droits accordés sur un travail. Le problème est particulièrement
    fréquent sur le web :
    a-t-on le droit d'utiliser telle ou telle image gratuitement, de la
    reproduire, de la modifier,
    et ainsi de suite.
</p>
<p>
 Pour résoudre cette difficulté, les gens font appel à la norme
 <i>
  Creative
        Commons
 </i>
 , qui
    utilise le préfixe « http://web.resource.org/cc/ ». Cette norme
    définit
    une classe « Work » (travail, en anglais, ici au sens d'oœuvre),
    mais emprunte pratiquement tout le reste
    à
 <i>
  Dublin Core
 </i>
 qu'elle vient compléter. La norme
 <i>
  Creative
        Commons
 </i>
 a été proposée en 2001
    par James Boyle, Michael Carroll, Lawrence Lessig, Hal Abelson, Eric
    Saltzman et Eric Eldred.
</p>
<p>
 Voici un exemple très simple d'une description utilisant
    la norme
 <i>
  Creative Commons
 </i>
 :
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
     http://teluq.ca/ rdfexemples.html
    </td>
    <td>
     http://www.w3.org/1999/ 02/22-rdf-syntax-ns#type
    </td>
    <td>
     http://web.resource.org/ cc/Work
    </td>
   </tr>
   <tr>
    <td>
     http://teluq.ca/ rdfexemples.html
    </td>
    <td>
     http://purl.org/ dc/elements/1.1/title
    </td>
    <td>
     "Le RDF par l'exemple"
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 Et voici la version XML correspondante :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">web.resource.org</span><span style="color:#40015a; ">/cc/</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">dc</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">purl.org</span><span style="color:#40015a; ">/dc/elements/1.1/</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">Work</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://teluq.ca/rdfexemples.html</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Le RDF par l'exemple<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">Work</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Tout ce que nous avons affirmé dans ce dernier document, c'est que la page
    actuelle
    appartient à la classe « Work ». Dans l'état actuel des choses,
    nous affirmons par défaut qu'il
    n'est pas permis d'utiliser cette page, car nous n'avons attribué aucune
    permission.
</p>
<p>
 Supposons que l'auteur désire accorder le droit au lecteur de redistribuer,
    de modifier et
    de partager cette page, pour autant qu'il utilise la même licence. Nous
    pourrions alors utiliser la licence
    « Attribution-ShareAlike 2.0 » dont l'URI est
    « http://creativecommons.org/licenses/by-sa/2.0/ ».
    Évidemment, nous pouvons aussi créer notre licence de toute pièce, mais dans
    l'exemple,
    nous utiliserons la licence « Attribution-ShareAlike 2.0 ».
    Pour faire un lien entre notre travail et une licence, nous utilisons le
    verbe dont
    l'URI est « http://web.resource.org/cc/license »,
    comme ce qui suit; observez bien la dernière ligne du tableau.
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
     http://teluq.ca/ rdfexemples.html
    </td>
    <td>
     http://www.w3.org/1999/ 02/22-rdf-syntax-ns#type
    </td>
    <td>
     http://web.resource.org/ cc/Work
    </td>
   </tr>
   <tr>
    <td>
     http://teluq.ca/ rdfexemples.html
    </td>
    <td>
     http://purl.org/ dc/elements/1.1/title
    </td>
    <td>
     "Le RDF par l'exemple"
    </td>
   </tr>
   <tr>
    <td>
     http://teluq.ca/ rdfexemples.html
    </td>
    <td>
     http://web.resource.org/ cc/license
    </td>
    <td>
     http://creativecommons.org/licenses/by-sa/2.0/
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 Nous pouvons aussi utiliser le XML correspondant :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">web.resource.org</span><span style="color:#40015a; ">/cc/</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">dc</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">purl.org</span><span style="color:#40015a; ">/dc/elements/1.1/</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">Work</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://teluq.ca/rdfexemples.html</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Le RDF par l'exemple<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">license</span>
    <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://creativecommons.org/licenses/by-sa/2.0/</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">Work</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Voici la représentation sous la forme d'un graphe :
</p>
<svg contentstyletype="text/css" font-size="0.7em" height="150" version="1.0" width="600" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" zoomandpan="magnify">
 <g class="graph" id="graph0" transform="scale(1)">
  ../module5/cc.pdf
  <!-- 0 -->
  <g class="node" id="node1">
   <a xlink:actuate="onRequest" xlink:href="http%3A//teluq.ca/rdfexemples.html" xlink:show="replace" xlink:title="rdfexemples.html\n{Work}" xlink:type="simple">
    <ellipse cx="71" cy="50" rx="64" ry="28" style="fill:none;stroke:black;">
    </ellipse>
    <text text-anchor="middle" x="71" y="47">
     rdfexemples.html
    </text>
    <text text-anchor="middle" x="71" y="63">
     {Work}
    </text>
   </a>
  </g>
  <!-- 1 -->
  <g class="node" id="node2">
   <polygon points="427,5 287,5 287,41 427,41 427,5" style="fill:none;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="357" y="28">
    Le RDF par
                l'exemple
   </text>
  </g>
  <!-- 0&#45;&gt;1 -->
  <g class="edge" id="edge2">
   <path d="M135,44C177,40 232,35 277,31" style="fill:none;stroke:black;">
   </path>
   <polygon points="277,28 287,30 277,34 277,28" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="175" y="37">
    title
   </text>
  </g>
  <!-- 2 -->
  <g class="node" id="node4">
   <ellipse cx="357" cy="77" rx="143" ry="18" style="fill:none;stroke:black;">
   </ellipse>
   <text font-size="0.9em" text-anchor="middle" x="357" y="82">
    http://creativecommons.org/licenses/by-sa/2.0/
   </text>
  </g>
  <!-- 0&#45;&gt;2 -->
  <g class="edge" id="edge4">
   <path d="M132,60C140,61 148,62 155,63 175,66 195,67 215,69" style="fill:none;stroke:black;">
   </path>
   <polygon points="215,66 225,70 215,72 215,66" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="175" y="60">
    license
   </text>
  </g>
 </g>
</svg>
<p>
 Nous avons alors un document
 <i>
  Creative Commons
 </i>
 complet. Cependant, un
    problème demeure.
    Supposons qu'un logiciel fasse automatiquement une recherche pour vous et
    que vous ne désiriez obtenir
    que les textes que vous pouvez modifier librement. Il n'est pas évident pour
    une machine
    de comprendre que l'URI
    « http://creativecommons.org/licenses/by-sa/2.0/ » vous donne ce
    droit;
    d'ailleurs, une telle recherche n'est peut-être pas très simple pour un
    humain...
</p>
<p>
 <i>
  Creative Commons
 </i>
 définit trois verbes et des objets permettant de
    décrire une licence et une classe.
    Toutes les licences appartiennent à la classe ayant pour URI
    « http://web.resource.org/cc/License ».
    Les URI des trois verbes sont :
</p>
<dl>
 <dt>
  http://web.resource.org/cc/permits
 </dt>
 <dd>
  <b>
   La licence le permet.
  </b>
  <i>
   Creative Commons
  </i>
  définit trois URI
        pouvant être utilisés comme objet de ce verbe.
        Il y a d'abord « http://web.resource.org/cc/Reproduction », le
        droit de reproduire en tout ou en partie le travail.
        Il y a ensuite « http://web.resource.org/cc/Distribution », le
        droit de redistribuer le travail.
        Finalement, il y a
        « http://web.resource.org/cc/DerivativeWorks », le droit de
        modifier le travail.
        Évidemment, il est possible de définir ses propres objets.
 </dd>
 <dt>
  http://web.resource.org/cc/requires
 </dt>
 <dd>
  <b>
   La licence pose comme condition.
  </b>
  <i>
   Creatives Commons
  </i>
  définit
        quatre URI pouvant être utilisés
        comme objet de ce verbe :
        « http://web.resource.org/cc/Notice » pour spécifier qu'il
        faut reproduire
        intégralement les notes légales (licence et droits d'auteurs);
        « http://web.resource.org/cc/Attribution » pour spécifier
        qu'il
        faut attribuer à l'auteur le crédit du travail;
        « http://web.resource.org/cc/ShareAlike » pour spécifier que
        si l'on redistribue le travail, il faut
        le faire en gardant la même licence;
        « http://web.resource.org/cc/SourceCode »
        pour spécifier que le code source doit être redistribué.
 </dd>
 <dt>
  http://web.resource.org/cc/prohibits
 </dt>
 <dd>
  <b>
   La licence interdit.
  </b>
  Il n'y a qu'un seul URI défini par
  <i>
   Creative Commons
  </i>
  qui peut être utilisé
        avec ce verbe :
        « http://web.resource.org/cc/CommercialUse »; cela permet
        d'interdire l'utilisation à des fins
        commerciales. Encore une fois, il est possible de définir ses propres
        objets.
 </dd>
</dl>
<p>
 Dans le cas de la licence « Attribution-ShareAlike 2.0 », nous
    pouvons la décrire comme suit :
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
     http://creativecommons.org/ licenses/by-sa/2.0/
    </td>
    <td>
     http://www.w3.org/1999/ 02/22-rdf-syntax-ns#type
    </td>
    <td>
     http://web.resource.org/ cc/License
    </td>
   </tr>
   <tr>
    <td>
     http://creativecommons.org/ licenses/by-sa/2.0/
    </td>
    <td>
     http://web.resource.org/ cc/permits
    </td>
    <td>
     http://web.resource.org/ cc/Reproduction
    </td>
   </tr>
   <tr>
    <td>
     http://creativecommons.org/ licenses/by-sa/2.0/
    </td>
    <td>
     http://web.resource.org/ cc/permits
    </td>
    <td>
     http://web.resource.org/ cc/Distribution
    </td>
   </tr>
   <tr>
    <td>
     http://creativecommons.org/ licenses/by-sa/2.0/
    </td>
    <td>
     http://web.resource.org/ cc/requires
    </td>
    <td>
     http://web.resource.org/ cc/Notice
    </td>
   </tr>
   <tr>
    <td>
     http://creativecommons.org/ licenses/by-sa/2.0/
    </td>
    <td>
     http://web.resource.org/ cc/requires
    </td>
    <td>
     http://web.resource.org/ cc/Attribution
    </td>
   </tr>
   <tr>
    <td>
     http://creativecommons.org/ licenses/by-sa/2.0/
    </td>
    <td>
     http://web.resource.org/ cc/permits
    </td>
    <td>
     http://web.resource.org/ cc/DerivativeWorks
    </td>
   </tr>
   <tr>
    <td>
     http://creativecommons.org/ licenses/by-sa/2.0/
    </td>
    <td>
     http://web.resource.org/ cc/requires
    </td>
    <td>
     http://web.resource.org/ cc/ShareAlike
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 Nous pouvons aussi utiliser le XML suivant :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">web.resource.org</span><span style="color:#40015a; ">/cc/</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">dc</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">purl.org</span><span style="color:#40015a; ">/dc/elements/1.1/</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">License</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://creativecommons.org/licenses/by-sa/2.0/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">permits</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://web.resource.org/cc/Reproduction</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">permits</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://web.resource.org/cc/Distribution</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">requires</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://web.resource.org/cc/Notice</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">requires</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://web.resource.org/cc/Attribution</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">permits</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://web.resource.org/cc/DerivativeWorks</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">requires</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://web.resource.org/cc/ShareAlike</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">License</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 En pratique, nous combinons souvent le tout (description du travail et
    description de la licence) pour obtenir le XML suivant :
</p>
<pre><span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">web.resource.org</span><span style="color:#40015a; ">/cc/</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">dc</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">purl.org</span><span style="color:#40015a; ">/dc/elements/1.1/</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">Work</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://teluq.ca/rdfexemples.html</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Le RDF par l'exemple<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">license</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://creativecommons.org/licenses/by-sa/2.0/</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">Work</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">License</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://creativecommons.org/licenses/by-sa/2.0/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">permits</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://web.resource.org/cc/Reproduction</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">permits</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://web.resource.org/cc/Distribution</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">requires</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://web.resource.org/cc/Notice</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">requires</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://web.resource.org/cc/Attribution</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">permits</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://web.resource.org/cc/DerivativeWorks</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">requires</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://web.resource.org/cc/ShareAlike</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">License</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Voilà! De cette manière, une machine pourra automatiquement déterminer quels
    droits l'utilisateur a sur une œuvre.
    Un logiciel pourrait automatiquement avertir l'utilisateur de ses
    obligations si jamais il tentait d'enregistrer sur son
    disque une copie de l'œuvre. Dans le cas d'une entreprise qui utilise
    beaucoup de contenu multimédia,
    l'utilisation de cette norme pourrait être très utile pour détecter
    automatiquement les violations des droits d'auteur.
</p>
<h2>
 Un exemple :
 <i>
  FOAF
 </i>
</h2>
<p>
 Les personnes sont souvent ce qu'il y a de plus important dans une
    organisation; il n'est donc pas étonnant
    qu'on veuille utiliser le RDF pour les décrire. Pour ce faire, on utilise
    souvent la norme
 <i>
  FOAF
 </i>
 pour « Friend-Of-A-Friend », ou un ami d'un ami, en français,
    (préfixe http://xmlns.com/foaf/0.1/)
    qui définit la classe « Person » (personne, en anglais).
</p>
<p>
 Le projet
 <i>
  FOAF
 </i>
 a été lancé de façon informelle par Daniel Brickley en
    1998. À l'époque, il
    avait mis un texte RDF ressemblant à ceci sur sa page personnelle :
    (
 <b>
  Attention.- Il ne s'agit pas de RDF/XML valable.
 </b>
 )
</p>
<pre><span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">RDF</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#40015a; ">vocabdemo.rdf</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    xmlns:rdf="http://www.w3.org/TR/WD-rdf-syntax#"&gt;
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">Person</span> <span style="color:#274796; ">ID</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">dan</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">name</span><span style="color:#a65700; ">&gt;</span> Dan Brickley <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">name</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">Email</span><span style="color:#a65700; ">&gt;</span> daniel.brickley@bristol.ac.uk <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">Email</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">telephone</span> <span style="color:#274796; ">rdf:resource</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">phone:44-1-+44(0)117-9287493</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">pager</span> <span style="color:#274796; ">rdf:resource</span> <span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">phone:44-1-+44(0)2523-1781115</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">homePage</span>
    <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://purl.org/net/danbri/</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">homePage</span>
    <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.ilrt.bris.ac.uk/about/staff/dan.html</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">Person</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">RDF</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 La norme
 <i>
  FOAF
 </i>
 est très riche; mais à la base, on trouve les verbes
    suivants :
</p>
<dl>
 <dt>
  http://xmlns.com/foaf/0.1/name
 </dt>
 <dd>
  Verbe pointant vers le nom de la personne (John Smith)
 </dd>
 <dt>
  http://xmlns.com/foaf/0.1/nick
 </dt>
 <dd>
  Verbe pointant vers le surnom informel de la personne (joblo).
 </dd>
 <dt>
  http://xmlns.com/foaf/0.1/title
 </dt>
 <dd>
  Verbe pointant vers le titre de la personne (docteur, monsieur, madame).
 </dd>
 <dt>
  http://xmlns.com/foaf/0.1/homepage
 </dt>
 <dd>
  Verbe pointant vers la page personnelle de la personne.
 </dd>
 <dt>
  http://xmlns.com/foaf/0.1/mbox
 </dt>
 <dd>
  Verbe pointant vers l'adresse électronique de la personne.
 </dd>
 <dt>
  http://xmlns.com/foaf/0.1/img
 </dt>
 <dd>
  Verbe pointant vers une image de la personne, la représentant
        spécifiquement.
 </dd>
 <dt>
  http://xmlns.com/foaf/0.1/depiction
 </dt>
 <dd>
  Verbe pointant vers une image représentant la personne. Contrairement à
        « img », l'image
        peut être une photo de groupe.
 </dd>
 <dt>
  http://xmlns.com/foaf/0.1/family_name
 </dt>
 <dd>
  Verbe pointant vers le nom de famille de la personne (Smith).
 </dd>
 <dt>
  http://xmlns.com/foaf/0.1/givenname
 </dt>
 <dd>
  Verbe pointant vers le prénom de la personne (John).
 </dd>
</dl>
<p>
 En XML, une description de l'auteur de ce document pourrait se présenter
    comme suit :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">foaf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">xmlns.com</span><span style="color:#40015a; ">/foaf/0.1/</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">foaf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Person</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">foaf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">givenname</span><span style="color:#a65700; ">&gt;</span>Daniel<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">foaf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">givenname</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">foaf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">family_name</span><span style="color:#a65700; ">&gt;</span>Lemire<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">foaf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">family_name</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">foaf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">homepage</span> <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">foaf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">mbox</span><span style="color:#a65700; ">&gt;</span>lemire@uqam.ca<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">foaf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">mbox</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">foaf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">img</span>
    <span style="color:#274796; ">rdf:resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://lemire.me/fr/images/GIF/zel2p.gif</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">foaf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Person</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Voici le graphe équivalent :
</p>
<svg contentstyletype="text/css" font-size="0.7em" height="300" preserveaspectratio="xMidYMid meet" version="1.0" width="500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" zoomandpan="magnify">
 <g class="graph" id="graph0" transform="scale(1)">
  <!-- 0 -->
  ../module5/foaf.pdf
  <g class="node" id="node1">
   <a xlink:actuate="onRequest" xlink:href="http%3A//4suite.org/rdf/anonymous/61841b36-5a83-4833-9526-85153a4c3704" xlink:show="replace" xlink:title="Anonymous\nPerson" xlink:type="simple">
    <ellipse cx="56" cy="131" rx="50" ry="28" style="fill:none;stroke:black;">
    </ellipse>
    <text text-anchor="middle" x="56" y="128">
     (anonyme)
    </text>
    <text text-anchor="middle" x="56" y="144">
     Person
    </text>
   </a>
  </g>
  <!-- 1 -->
  <g class="node" id="node2">
   <polygon points="350,5 296,5 296,41 350,41 350,5" style="fill:none;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="323" y="28">
    Daniel
   </text>
  </g>
  <!-- 0&#45;&gt;1 -->
  <g class="edge" id="edge2">
   <path d="M83,107C95,97 110,86 125,78 177,51 244,36 285,29" style="fill:none;stroke:black;">
   </path>
   <polygon points="285,26 295,27 286,32 285,26" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="162" y="50">
    givenname
   </text>
  </g>
  <!-- 2 -->
  <g class="node" id="node4">
   <polygon points="351,59 295,59 295,95 351,95 351,59" style="fill:none;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="323" y="82">
    Lemire
   </text>
  </g>
  <!-- 0&#45;&gt;2 -->
  <g class="edge" id="edge4">
   <path d="M101,117C109,115 117,113 125,111 180,98 244,88 284,82" style="fill:none;stroke:black;">
   </path>
   <polygon points="284,79 294,81 284,85 284,79" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="162" y="95">
    family_name
   </text>
  </g>
  <!-- 3 -->
  <g class="node" id="node6">
   <ellipse cx="323" cy="131" rx="106" ry="18" style="fill:none;stroke:black;">
   </ellipse>
   <text font-size="0.9em" text-anchor="middle" x="323" y="136">
    http://lemire.me/fr/
   </text>
  </g>
  <!-- 0&#45;&gt;3 -->
  <g class="edge" id="edge6">
   <path d="M107,131C135,131 172,131 207,131" style="fill:none;stroke:black;">
   </path>
   <polygon points="207,127 217,131 207,134 207,127" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="162" y="128">
    homepage
   </text>
  </g>
  <!-- 4 -->
  <g class="node" id="node8">
   <polygon points="379,167 267,167 267,203 379,203 379,167" style="fill:none;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="323" y="190">
    lemire@uqam.ca
   </text>
  </g>
  <!-- 0&#45;&gt;4 -->
  <g class="edge" id="edge8">
   <path d="M101,145C109,147 117,149 125,151 169,161 218,170 257,175" style="fill:none;stroke:black;">
   </path>
   <polygon points="258,172 267,177 257,178 258,172" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="162" y="148">
    mbox
   </text>
  </g>
  <!-- 5 -->
  <g class="node" id="node10">
   <ellipse cx="323" cy="239" rx="38" ry="18" style="fill:none;stroke:black;">
   </ellipse>
   <text text-anchor="middle" x="323" y="244">
    zel2p.gif
   </text>
  </g>
  <!-- 0&#45;&gt;5 -->
  <g class="edge" id="edge10">
   <path d="M81,156C93,167 109,179 125,187 174,212 235,226 276,232" style="fill:none;stroke:black;">
   </path>
   <polygon points="277,229 286,234 276,235 277,229" style="fill:black;stroke:black;">
   </polygon>
   <text text-anchor="middle" x="162" y="184">
    img
   </text>
  </g>
 </g>
</svg>
<p>
 Notez que la balise « Person » n'a pas d'attribut
    « rdf:about ». Actuellement, il existe
    un débat sur cette question : Peut-on attribuer un URI unique à chaque
    individu et si oui,
    comment le choisir? C'est un cas où l'URI du sujet est
    « implicite » : cela signifie que dans les triplets
    sujet/verbe/objet, le sujet a un URI « fictif », qui n'est valable
    que dans le cadre du document
    que l'on traite. Autrement dit, le programme qui traite le document doit
    allouer dynamiquement un URI au sujet
    pour la durée du traitement. Rappelons-nous, en effet, que la norme RDF
    permet d'omettre le sujet,
    mais que si le sujet est spécifié, il doit être un URI.
</p>
<p>
 Nous pouvons imaginer que la norme
 <i>
  FOAF
 </i>
 sera éventuellement utilisée
    pour représenter les réseaux sociaux, les
    organisations, et ainsi de suite. Une fois l'information sociale représentée
    de façon formelle, nous pouvons croire qu'il
    sera possible de poser des questions à un ordinateur de l'ordre
    suivant : Est-ce que je connais quelqu'un
    qui connaît quelqu'un travaillant chez IBM?
</p>
<h2>
 Un exemple :
 <i>
  RSS/RDF
 </i>
</h2>
<p>
 La version 1.0 de la norme
 <i>
  RSS
 </i>
 est un exemple de RDF. Cette norme dont
    l'acronyme n'a pas de définition établie,
    sert à représenter des fils de nouvelles. Elle a été imaginée par la
    compagnie Netscape et servait alors à la
    production du portail Netscape (1999). Elle est devenue très populaire et on
    trouve maintenant des milliers
    de fils de nouvelles en format
 <i>
  RSS
 </i>
 dans le monde. Par exemple,
    sur
 <a href="http://www.yulblog.org/">
  http://www.yulblog.org/
 </a>
 , il y a
    des centaines de
    blogues écrits par des Montréalais et la plupart ont un fil de nouvelles en
    format
 <i>
  RSS
 </i>
 .
</p>
<p>
 Une nouvelle, appelée « item » en
 <i>
  RSS
 </i>
 , prend la forme
    suivante :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">purl.org</span><span style="color:#40015a; ">/rss/1.0/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">item</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.nouvelles.com/nouvelles1</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>La bourse fait faillite<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">link</span><span style="color:#a65700; ">&gt;</span>http://www.nouvelles.com/nouvelles1.html<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">link</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">description</span><span style="color:#a65700; ">&gt;</span>
    Aujourd'hui, on a appris que la bourse a fait faillite.
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">item</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Nous constatons qu'il y a une classe (item) et trois verbes (title, link,
    description) qui représentent
    respectivement le titre, l'URL et le contenu de la nouvelle.
</p>
<p>
 Un document
 <i>
  RSS
 </i>
 est une liste d'items. Voici un document
 <i>
  RSS
 </i>
 :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">purl.org</span><span style="color:#40015a; ">/rss/1.0/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">channel</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.nouvelles.com/nouvelles.rss</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Un site de nouvelles<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">link</span><span style="color:#a65700; ">&gt;</span>http://www.nouvelles.com/<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">link</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">description</span><span style="color:#a65700; ">&gt;</span>
    Nouvelles.com est un superbe site de nouvelles
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#696969; ">&lt;!--</span><span style="color:#696969; ">
        Ensuite, on place une séquence de nouvelles,</span>
    <span style="color:#696969; ">    les unes après les
        autres</span><span style="color:#696969; ">--&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">items</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Seq</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#696969; ">&lt;!--</span><span style="color:#696969; ">
        chaque nouvelle a un URI </span><span style="color:#696969; ">--&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span>
    <span style="color:#274796; ">resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.nouvelles.com/nouvelles1</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span>
    <span style="color:#274796; ">resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.nouvelles.com/nouvelles2</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Seq</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">items</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">channel</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Nous constatons une classe « channel » (canal, en anglais) qui
    contient un titre, un URL (link) et une description.
    Il y a aussi une liste de nouvelles (item). Généralement, nous combinons le
    tout dans un seul fichier, comme ceci :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#800080; ">:</span><span style="color:#074726; ">rdf</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/1999/02/22-rdf-syntax-ns</span><span style="color:#800000; font-weight:bold; ">#</span><span style="color:#0000e6; ">"</span>
    <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">purl.org</span><span style="color:#40015a; ">/rss/1.0/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">channel</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.nouvelles.com/nouvelles.rss</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Un site de nouvelles<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">link</span><span style="color:#a65700; ">&gt;</span>http://www.nouvelles.com/<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">link</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">description</span><span style="color:#a65700; ">&gt;</span>
    Nouvelles.com est un superbe site de nouvelles
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#696969; ">&lt;!--</span><span style="color:#696969; ">
        Ensuite, on place une séquence de nouvelles,</span>
    <span style="color:#696969; ">    les unes après les
        autres</span><span style="color:#696969; ">--&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">items</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Seq</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#696969; ">&lt;!--</span><span style="color:#696969; ">
        chaque nouvelle a un URI </span><span style="color:#696969; ">--&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span>
    <span style="color:#274796; ">resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.nouvelles.com/nouvelles1</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">li</span>
    <span style="color:#274796; ">resource</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.nouvelles.com/nouvelles2</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">Seq</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">items</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">channel</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">item</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.nouvelles.com/nouvelles1</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>La bourse fait faillite<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">link</span><span style="color:#a65700; ">&gt;</span>http://www.nouvelles.com/nouvelles1.html<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">link</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">description</span><span style="color:#a65700; ">&gt;</span>
    Aujourd'hui, on a appris que la bourse a fait faillite.
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">item</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">item</span> <span style="color:#274796; ">rdf:about</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.nouvelles.com/nouvelles2</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Rien ne va plus à l'école<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">link</span><span style="color:#a65700; ">&gt;</span>http://www.nouvelles.com/nouvelles2.html<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">link</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">description</span><span style="color:#a65700; ">&gt;</span>
    Un étudiant se serait rendu coupable d'apprentissage.
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">description</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">item</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">rdf</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">RDF</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Les applications du
 <i>
  RSS
 </i>
 sont multiples. Supposons que votre
    organisation collabore avec plusieurs autres organisations
    et que vous vouliez rendre disponibles, sur une seule page web, toutes les
    nouvelles
    de toutes les organisations dont vous faites partie. Si chaque organisation
    rend disponible sur le web un document
 <i>
  RSS
 </i>
 toujours mis à jour, vous pouvez facilement récupérer les
    nouvelles de chacun et les afficher à un
    seul endroit. Au lieu de solliciter tous les membres par courriel, les fils
    de nouvelles
 <i>
  RSS
 </i>
 permettent
    à une machine de faire un tri et de personnaliser le contenu.
</p>
<p>
 La norme RSS est en voie d'être remplacée par la norme
 <a href="http://en.wikipedia.org/wiki/Atom_(standard)">
  Atom
 </a>
 . Un des
    avantages du nouveau format Atom est que chaque nouvelle doit avoir un
    identifiant unique ce qui permet d'éviter les doublons. Cependant, la norme
    RSS risque d'être toujours utile pendant bien des années. Atom n'est pas en
    RDF/XML. En voici un exemple :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">utf-8</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">feed</span> <span style="color:#666616; ">xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#666616; ">http</span><span style="color:#800080; ">:</span><span style="color:#800000; font-weight:bold; ">//</span><span style="color:#5555dd; ">www.w3.org</span><span style="color:#40015a; ">/2005/Atom</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Un site de nouvelles<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">subtitle</span><span style="color:#a65700; ">&gt;</span>Nouvelles.com est un superbe site de
    nouvelles<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">subtitle</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">link</span> <span style="color:#274796; ">href</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.nouvelles.com/</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">updated</span><span style="color:#a65700; ">&gt;</span>2003-12-13T18:30:02Z<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">updated</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">author</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">name</span><span style="color:#a65700; ">&gt;</span>John Doe<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">name</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">email</span><span style="color:#a65700; ">&gt;</span>johndoe@example.com<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">email</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">author</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">id</span><span style="color:#a65700; ">&gt;</span>urn:uuid:60a76c80-d399-11d9-b91C-0003939e0af6<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">id</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">entry</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>La bourse fait faillite<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">link</span> <span style="color:#274796; ">href</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">http://www.nouvelles.com/nouvelles1.html</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">id</span><span style="color:#a65700; ">&gt;</span>urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">id</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">updated</span><span style="color:#a65700; ">&gt;</span>2003-12-13T18:30:02Z<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">updated</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">summary</span><span style="color:#a65700; ">&gt;</span>Aujourd'hui, on a appris que la
    bourse a fait faillite.
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">summary</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">entry</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">feed</span><span style="color:#a65700; ">&gt;</span>
</pre>
<h2>
 Conclusion
</h2>
<p>
 Nous avons étudié quatre applications importantes du RDF sur le web.
    Le nombre d'applications est toutefois beaucoup plus important. Par exemple,
    Facebook fait la promotion de la norme
 <a href="http://ogp.me">
  Open
        Graph
 </a>
 .
</p>
<p>
 Il faut garder à l'esprit que le RDF n'est pas le XML et que le XML ne sert
    qu'à représenter le RDF
    (et encore, ce n'est pas toujours possible).
</p>
<p>
 Pour en apprendre davantage sur le RDF, nous vous suggérons le livre de
    Shelley Powers,
 <i>
  <a href="http://www.amazon.ca/Practical-RDF-Shelley-Powers/dp/0596002637">
   Practical
            RDF
  </a>
 </i>
 ,
    publié chez O'Reilly.
</p>
