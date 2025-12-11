---
title: "Travail 3"
weight: 80
---
<h1>
 Travail 3
</h1>
<h2>
 Consignes
</h2>
<p>
 Faites les exercices et répondez aux questions en utilisant
 <i>
  Chrome
 </i>
 comme moteur XSLT et
    comme navigateur.
    En effectuant les exercices, n'utilisez que des fonctions disponibles dans
 <i>
  Chrome
 </i>
 .
</p>
<p>
 Une fois votre travail terminé, transmettez à votre personne tutrice, un
    document (Word 97/2000/XP,
 <a href="https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=office">
  ODF
 </a>
 ,
    PDF, RTF ou en format texte) en fichier attaché.
    Il s'agit d'un travail personnel et vous ne devez pas partager vos
    solutions. Cette activité notée compte pour 15% de la note globale.
</p>
<p>
 Vous devez transmettre votre travail en utilisant l'outil de dépôt de
    l'Université.
</p>
<p>
 Bon travail!
</p>
<h2>
 Exercice 1
</h2>
<p>
 Étant donné le document XML suivant, rédigez le contenu du document CSS
    « test.css »,
    de telle sorte que les mots « Rouge » s'affichent en rouge, les
    mots « Noir » s'affichent en noir,
    les mots « majuscule » s'affichent en majuscule et ainsi de suite.
    Votre document CSS doit contenir au plus 5 instructions CSS de la
    forme « quelque chose {autre chose} ».
</p>
<p>
 <b>
  Indice
 </b>
 : Vous pouvez utiliser « color:red »,
    « color:olive »,
    « color:black », « color:blue »,
    et ainsi de suite pour fixer la couleur du texte.
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml-stylesheet</span><span style="color:#004a43; "> </span><span style="color:#074726; ">type</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">text/css</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">href</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#40015a; ">test.css</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">b</span><span style="color:#a65700; ">&gt;</span>Rouge<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">b</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">c</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>Olive<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">b</span><span style="color:#a65700; ">&gt;</span>Bleu<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">b</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>Noir<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>
    Olive
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">b</span><span style="color:#a65700; ">&gt;</span>Bleu<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">b</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>Rouge<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>Noir<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">c</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">b</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>Rouge<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">b</span><span style="color:#a65700; ">&gt;</span>Noir<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">b</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">b</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">d</span><span style="color:#a65700; ">&gt;</span>majuscule<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">d</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Vous pouvez tester votre solution en ligne:
</p>
<textarea cols="45" id="xmlsource" rows="15" style="display:none;">&lt;?xml
    version="1.0" ?&gt;
    &lt;a&gt;
    &lt;b&gt;Rouge&lt;/b&gt;
    &lt;c&gt;&lt;a&gt;Olive&lt;/a&gt;
    &lt;b&gt;Bleu&lt;/b&gt;
    &lt;a&gt;&lt;a&gt;Noir&lt;/a&gt;
    Olive
    &lt;b&gt;Bleu&lt;/b&gt;
    &lt;a&gt;Rouge&lt;/a&gt;
    &lt;a&gt;Noir&lt;/a&gt;
    &lt;/a&gt;&lt;/c&gt;
    &lt;b&gt;&lt;a&gt;Rouge&lt;/a&gt;
    &lt;b&gt;Noir&lt;/b&gt;&lt;/b&gt;
    &lt;d&gt;majuscule&lt;/d&gt;
    &lt;/a&gt;
</textarea>
<p>
 Document CSS:
</p>
<textarea cols="45" id="csssource" rows="15"> a {
    display: block;
    color: red;
    }
</textarea>
<br/>
<input onclick="
    var xt='',h3OK=1
    function checkErrorXML(x)
    {
    xt=''
    h3OK=1
    checkXML(x)
    }
    function checkXML(n)
    {
    var l,i,nam
    nam=n.nodeName
    if (nam=='h3')
        {
        if (h3OK==0)
            {
            return;
            }
        h3OK=0
        }
    if (nam=='#text')
        {
        xt=xt + n.nodeValue + '\n'
        }
    l=n.childNodes.length
    for (i=0;i&lt;l;i++)
        {
        checkXML(n.childNodes[i])
        }
    }
    function chargeXML(txt)
    {
      console.log('chargeXML ');
       var parser=new DOMParser();
      console.log('loading xml from id '+txt);
      var text=document.getElementById(txt).value;
      console.log('text from id '+text);
      try {
        var xmlDoc=parser.parseFromString(text,'application/xml');
        if (xmlDoc.documentElement.nodeName=='parsererror')
        {
          alert(xmlDoc.documentElement.childNodes[0].nodeValue);
        }
       if (xmlDoc.getElementsByTagName('parsererror').length&gt;0)
       {
       checkErrorXML(xmlDoc.getElementsByTagName('parsererror')[0]);
       alert(xt)
       } else {
        return xmlDoc;
       }
      }
      catch(err)
      {
      alert(err.message)
      }
    }
    var mondom = chargeXML('xmlsource');
    var pi = mondom.createProcessingInstruction('xml-stylesheet',
                                         'type=&quot;text/css&quot; href=&quot;data:text/css;charset=utf-8,' + encodeURI(document.getElementById('csssource').value)+'&quot;');
    var root = mondom.firstChild;
    mondom.insertBefore(pi, root);
    var serializer = new XMLSerializer();
    var resultatTexte = serializer.serializeToString(mondom);
    document.getElementById('dis').src = 'data:application/xml;charset=utf-8,' + encodeURI(resultatTexte);
    " type="button" value="Mise en forme"/>
<p>
 Résultat :
</p>
<iframe height="300" id="dis" src="data:application/xml;charset=utf-8,%3C?xml%20version=%221.0%22?%3E%3C?xml-stylesheet%20type=%22text/css%22%20href=%22data:text/css;charset=utf-8,%2520%2520a%2520%257B%250A%2520%2520display:%2520block;%250A%2520%2520color:%2520red;%250A%2520%2520%257D%250A%2520%22?%3E%3Ca%3E%0A%20%3Cb%3ERouge%3C/b%3E%0A%20%3Cc%3E%3Ca%3EOlive%3C/a%3E%0A%20%3Cb%3EBleu%3C/b%3E%0A%20%3Ca%3E%3Ca%3ENoir%3C/a%3E%20%0A%20Olive%20%0A%20%3Cb%3EBleu%3C/b%3E%0A%20%3Ca%3ERouge%3C/a%3E%0A%20%3Ca%3ENoir%3C/a%3E%0A%20%3C/a%3E%3C/c%3E%0A%20%3Cb%3E%3Ca%3ERouge%3C/a%3E%0A%20%3Cb%3ENoir%3C/b%3E%3C/b%3E%0A%3Cd%3Emajuscule%3C/d%3E%0A%3C/a%3E" width="300">
</iframe>
<h2>
 Exercice 2
</h2>
<p>
 Supposons que toutes les notes des étudiants, dans différents cours, se
    trouvent dans le document XML suivant :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml-stylesheet</span><span style="color:#004a43; "> </span><span style="color:#074726; ">href</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#40015a; ">class.xsl</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">type</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">text/xsl</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">universite</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">etudiant</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>Réjean Tremblay<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">cours</span> <span style="color:#274796; ">sigle</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">INF8430</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">note</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">89</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">cours</span> <span style="color:#274796; ">sigle</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">INF1030</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">note</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">69</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">cours</span> <span style="color:#274796; ">sigle</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">INF1230</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">note</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">75</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span><span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">etudiant</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">etudiant</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>Martin Lambert<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">cours</span> <span style="color:#274796; ">sigle</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">INF8430</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">note</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">75</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">cours</span> <span style="color:#274796; ">sigle</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">INF1030</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">note</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">72</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">cours</span> <span style="color:#274796; ">sigle</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">INF1230</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">note</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">73</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span><span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">etudiant</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">etudiant</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>Luc Alain<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">cours</span> <span style="color:#274796; ">sigle</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">INF9430</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">note</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">39</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">cours</span> <span style="color:#274796; ">sigle</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">INF1030</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">note</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">89</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">cours</span> <span style="color:#274796; ">sigle</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">INF1230</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">note</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">79</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span><span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">etudiant</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">etudiant</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>Olive Saint-Amant<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">cours</span> <span style="color:#274796; ">sigle</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">INF8430</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">note</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">91</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">cours</span> <span style="color:#274796; ">sigle</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">INF1230</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">note</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">99</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span><span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">etudiant</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">universite</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 À partir de ce document XML, fournissez le document XSLT
    « class.xsl » qui calcule les moyennes
    des étudiants, d'après les éléments « cours » associés aux
    éléments « étudiant »,
    et qui trie les étudiants par ordre alphabétique de leur nom de famille.
    Votre document XSLT doit fonctionner même si on change le nom des étudiants,
    l'ordre des éléments et le nom des cours. En conséquence, le nom des
    étudiants ou le nom des cours
    ne peuvent apparaître dans votre document XSLT. En outre, vous ne devez
    pas
    utiliser les crochets « [ ] » dans votre solution.
</p>
<p>
 <a href="$@PAGEVIEWBYID*131060@$">
  Vous pouvez
        tester votre solution en ligne à l'aide du laboratoire XSLT
 </a>
 .
</p>
<h4>
 Indices
</h4>
<ol>
 <li>
  <p>
   Le tableau ci-dessous devrait vous permettre de vérifier votre
            réponse.
  </p>
  <table border="1">
   <tbody>
    <tr>
     <td>
      Étudiant
     </td>
     <td>
      Moyenne
     </td>
    </tr>
    <tr>
     <td>
      Luc Alain
     </td>
     <td>
      69.0
     </td>
    </tr>
    <tr>
     <td>
      Martin Lambert
     </td>
     <td>
      73.3
     </td>
    </tr>
    <tr>
     <td>
      Olive Saint-Amant
     </td>
     <td>
      95.0
     </td>
    </tr>
    <tr>
     <td>
      Réjean Tremblay
     </td>
     <td>
      77.7
     </td>
    </tr>
   </tbody>
  </table>
 </li>
 <li>
  <p>
   Vous pouvez trier les étudiants selon leur nom de famille, en
            remplaçant
            « &lt;xsl:apply-templates select="etudiant" /&gt; »
            par :
  </p>
  <pre><span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">apply-templates</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">etudiant</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">&gt;</span>
            <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">sort</span> <span style="color:#274796; ">select</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">substring-after(nom,' ')</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">order</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ascending</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">/&gt;</span>
            <span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">xsl</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">apply-templates</span><span style="color:#a65700; ">&gt;</span>
        </pre>
 </li>
 <li>
  <p>
   Vous pouvez formater les nombres à virgule flottante comme dans le
            tableau, en utilisant
            des appels de fonction XSLT tels que « format-number(10.1324,
            '##.0') ».
  </p>
 </li>
</ol>
<h2>
 Exercice 3
</h2>
<p>
 Utilisez le même document XML qu'à l'exercice précédent. Cette fois-ci,
    comptez le nombre d'étudiants dans chaque cours et calculez la moyenne par
    cours.
    Encore une fois, les noms des cours ou des étudiants ne doivent pas
    apparaître dans votre document XSLT.
</p>
<p>
 Le tableau qui suit présente le résultat.
</p>
<div class="tableau style1">
 <table border="1">
  <tbody>
   <tr>
    <td>
     Sigle
    </td>
    <td>
     Nombre d'étudiants
    </td>
    <td>
     Moyenne du cours
    </td>
   </tr>
   <tr>
    <td>
     INF8430
    </td>
    <td>
     3
    </td>
    <td>
     85.0
    </td>
   </tr>
   <tr>
    <td>
     INF1030
    </td>
    <td>
     3
    </td>
    <td>
     76.7
    </td>
   </tr>
   <tr>
    <td>
     INF1230
    </td>
    <td>
     4
    </td>
    <td>
     81.5
    </td>
   </tr>
   <tr>
    <td>
     INF9430
    </td>
    <td>
     1
    </td>
    <td>
     39.0
    </td>
   </tr>
  </tbody>
 </table>
</div>
<p>
 Bien que cet exercice soit très similaire au précédent et que la solution
    soit de même longueur,
    vous le trouverez probablement plus difficile.
</p>
<p>
 <strong>
  Note
 </strong>
 . Si vous aviez le droit d'utiliser XSLT 2.0,
    la nouvelle instruction « xsl:for-each-group » rendrait ce
    problème plus facile.
    Mais rappelez-vous que vous devez vous limiter à XSLT 1.0.
</p>
<h2>
 Exercice 4
</h2>
<p>
 Supposons que vous ayiez des documents contenant exclusivement une
    déclaration XML, des éléments
    et des attributs. Il n'y a pas d'espace de noms.
    Vous souhaitez filtrer les documents XML de telle manière que seuls les
    éléments dont le nom contient la lettre a sont inclus. Naturellement, les
    éléments, peu importe
    leur nom, qui ne sont pas contenus dans un élément dont le nom contient la
    lettre a doivent être
    omis. Le document XML devra contenir une instruction xml-stylesheet, mais
    elle ne doit pas être
    reproduite dans le document sortant.
</p>
<p>
 Si on prend cet exemple:
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml-stylesheet</span><span style="color:#004a43; "> </span><span style="color:#074726; ">href</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#40015a; ">monfichier.xsl</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">type</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">text/xsl</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">ab</span> <span style="color:#274796; ">x</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">x</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">b</span><span style="color:#a65700; ">&gt;</span>Test<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">b</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>z<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">ab</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">z</span> <span style="color:#274796; ">x</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">x</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>z<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">z</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 On souhaite que le document sortant soit celui-ci:
</p>
<pre><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">ab</span> <span style="color:#274796; ">x</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">x</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>z<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">ab</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span>/<span style="color:#5f5035; ">a</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Vous devez proposer deux documents XSLT permettant de réaliser ce filtrage.
    Le premier document ne devra pas contenir d'élément
    « xsl:element », alors que le second
    ne contiendra pas d'élément « xsl:copy ».
</p>
<p>
 Comme précédemment, vous pouvez vérifier votre solution en ligne.
</p>
<h2>
 Exercice 5
</h2>
<p>
 Considérez le fichier XML de la question 2 comprenant les notes des
    étudiants. Écrivez une requête XQuery qui calcule la moyenne des
    notes de chaque cours et la présente sous cette forme :
</p>
<pre><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">maliste</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">cours</span> <span style="color:#274796; ">sigle</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">INF8430</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>85<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">cours</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">cours</span> <span style="color:#274796; ">sigle</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">INF1030</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>76.66666666666667<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">cours</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">cours</span> <span style="color:#274796; ">sigle</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">INF1230</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>81.5<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">cours</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">cours</span> <span style="color:#274796; ">sigle</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">INF9430</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>39<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">cours</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">maliste</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Vous pouvez utiliser la fonction avg qui calcule la moyenne.
</p>
