---
title: "XPath : second laboratoire"
weight: 40
---
<h1 class="">
 XPath : second laboratoire
</h1>
<div class="">
 <p>
  Il est temps de refaire un laboratoire XPath. Utilisez ce nouveau document XML et tentez de sélectionner différents numéros de téléphones, listes de clients, etc. en utilisant des expressions XPath appropriées.
 </p>
 <p>
  Instructions : il suffit de saisir un document XML source et une expression XPath et d'appuyer sur le bouton. Le contenu textuel de chaque résultat est retourné. L'expression XPath est toujours appliquée à partir du noeud-racine. Cette petite application est limitée: elle suppose que le résultat prend une certaine forme (un  ensemble de noeuds ou node set).
 </p>
 <form action="">
  <p>
   Fichier XML:
  </p>
  <textarea cols="75" id="xmlsource" rows="20">&lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
 &lt;listes&gt;
 &lt;vendeur nom="Jean"&gt;
 &lt;client telephone="543-5454"&gt;&lt;nom&gt;Jacques&lt;/nom&gt;&lt;/client&gt;
 &lt;client telephone="545-5455"&gt;&lt;nom&gt;Sylvain&lt;/nom&gt;&lt;/client&gt;
 &lt;client telephone="443-4456"&gt;&lt;nom&gt;Claude&lt;/nom&gt;&lt;/client&gt;
 &lt;client telephone="533-3445"&gt;&lt;nom&gt;Yvon&lt;/nom&gt;&lt;/client&gt;
 &lt;/vendeur&gt;
 &lt;vendeur nom="Raymond"&gt;
 &lt;client telephone="432-2145"&gt;&lt;nom&gt;Arthur&lt;/nom&gt;&lt;/client&gt;
 &lt;client telephone="545-5456"&gt;&lt;nom&gt;Sylvain&lt;/nom&gt;&lt;/client&gt;
 &lt;client telephone="443-4556"&gt;&lt;nom&gt;Claudette&lt;/nom&gt;&lt;/client&gt;
 &lt;client telephone="533-3445"&gt;&lt;nom&gt;Yvon&lt;/nom&gt;&lt;/client&gt;
 &lt;/vendeur&gt;
 &lt;/listes&gt;
</textarea>
  <p>
   Sélection XPath:
  </p>
  <input id="myxpath" size="80" type="text" value='//vendeur[@nom="Raymond"]/client[nom="Arthur"]/@telephone'/>
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
