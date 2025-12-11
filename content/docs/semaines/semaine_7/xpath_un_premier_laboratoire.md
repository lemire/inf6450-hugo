---
title: "XPath : un premier laboratoire"
weight: 20
---
<h1 class="">
 XPath : un premier laboratoire
</h1>
<div class="">
 <p>
  Étant donné un document XML, on peut sélectionner un noeud au sein du document avec une expression XPath. Plus généralement, étant donné un document XML et un noeud courant, on peut sélectionner, relativement à ce noeud, tout autre noeud ou ensemble de noeuds correspondant à un certain motif régulier.
 </p>
 <p>
  Dans cette première activité de familiarisation avec XPath, nous allons d’abord passer en revue rapidement les éléments de base et vous inviter à faire un petit laboratoire.
 </p>
 <p>
  Les expressions XPath les plus simples comprennent seulement un nom XML. Dans ce cas, on sélectionne l’élément ayant le nom correspondant.  Par exemple, l’expression « chien » va sélectionner tout élément nommé « chien » et contenu dans le noeud courant. S’il y en a plus d’un, plusieurs éléments pourront être sélectionnés. On peut utiliser l’astérisque (*) pour sélectionner tous les éléments du context courant, peu importe leur nom. Les deux points (..) permettent de sélectionner le parent du noeud courant (indiqué par « . »), ainsi « ../chien » permet de sélectionner les éléments « chien » dans le noeud parent. Si on veut ignorer le noeud courant et sélectionner tous les éléments chien, on peut obtenir ce résultat avec l’expression « //chien ». On peut aussi sélectionner le noeud racine... avec l’expression XPath « / ». Ainsi donc, « /* » sélectionnera toujours l’élément-racine. L’instruction « //* » va sélectionner tous les noeuds du document. On peut sélectionner un attribut avec le symbole « @ ». Ainsi, on peut sélectionner le contenu de l’attribut race de tous les éléments chien avec l’expression « //chien/@race ».
 </p>
 <pre style="color:#000000;background:#ffffff;"><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">animaux</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">chien</span> <span style="color:#274796; ">race</span><span style="color:#808030; ">=</span><span style="color:#800000; ">"</span><span style="color:#0000e6; ">caniche</span><span style="color:#800000; ">"</span> <span style="color:#a65700; ">/&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">animaux</span><span style="color:#a65700; ">&gt;</span>
</pre>
 <p>
  Avant de continuer plus loin avec la syntaxe XPath, nous vous invitons à utiliser le petit script suivant pour vous familiariser davantage avec la syntaxe :
 </p>
 <h1>
  XPath en ligne
 </h1>
 <p>
  Instructions : il suffit de saisir un document XML source et une expression XPath et d'appuyer sur le bouton. Le contenu textuel de chaque résultat est retourné. L'expression XPath est toujours appliquée à partir du noeud-racine.  Cette petite application est limitée: elle suppose que le résultat prend une certaine forme (un  ensemble de noeuds ou node set).
 </p>
 <form action="">
  <p>
   Fichier XML:
  </p>
  <textarea cols="75" id="xmlsource" rows="20">&lt;?xml version="1.0" ?&gt; 
&lt;boite&gt;
&lt;monmessage&gt;
&lt;de&gt;Jean&lt;/de&gt; 
&lt;a&gt;Pierre&lt;/a&gt; 
&lt;titre type="émotion"&gt;Ouch!&lt;/titre&gt; 
&lt;corps&gt;Maman!&lt;/corps&gt; 
&lt;/monmessage&gt;
&lt;monmessage&gt;
&lt;de&gt;Marie&lt;/de&gt; 
&lt;a&gt;Jean&lt;/a&gt; 
&lt;titre type="émotion"&gt;Bah!&lt;/titre&gt; 
&lt;corps&gt;Papa!&lt;/corps&gt; 
&lt;/monmessage&gt;
&lt;/boite&gt;
</textarea>
  <p>
   Sélection XPath:
  </p>
  <input id="myxpath" type="text" value="//titre/@type"/>
  <input onclick="
function sel(doc,path) {
  var snapshot = doc.evaluate(path, doc, null, 7, null);
  var nodes = [];
  for (var i = 0; i &lt; snapshot.snapshotLength; i++) {
    nodes.push(snapshot.snapshotItem(i));
  }
  return nodes;
}
function applyXPath(xmlsource,myxpath,xmlout) {
    var wheretowrite = document.getElementById(xmlout);
    var xpathexpr = document.getElementById(myxpath).value;
	var xmlsourceDOM = chargeXML(xmlsource);
	var n = sel(xmlsourceDOM,xpathexpr);
	if(n.length == 0) n[0] = '(je ne trouve pas)';
	var i;
	var mout = '&lt;ol&gt;';
	for(i = 0; i &lt; n.length; ++i) {
	   mout += '&lt;li&gt;';
	   if(n[i].textContent !== undefined)
	     mout += n[i].textContent;
	   else 
	     mout += '(je ne trouve pas)'
	   mout += '&lt;/li&gt;';
	}
	mout += '&lt;/ol&gt;';
	wheretowrite.innerHTML = mout;
}
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
   var parser=new DOMParser();
  var text=document.getElementById(txt).value;
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
try{
applyXPath('xmlsource','myxpath','sol')
} catch(err)
  {
  alert(err.message);
  }" type="button" value="Sélection"/>
  <p>
   Résultat :
  </p>
  <p id="sol" style="width:300px;background:#ccc">
  </p>
 </form>
</div>
<hr/>
