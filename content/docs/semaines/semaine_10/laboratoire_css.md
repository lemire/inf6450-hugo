---
title: "Laboratoire CSS"
weight: 50
---
<h1>
 Laboratoire CSS
</h1>
<p>
 Il peut être fastidieux d’apprendre le CSS en manipulant des fichiers. Heureusement, on peut le faire au sein d’un navigateur.
</p>
<p>
 Dans ce laboratoire, nous vous demandons d’expérimenter avec les notions de CSS vue jusqu’à présent. Partez du document XML et tentez de le mettre en forme de différentes manières.
</p>
<div style="max-width: 1000px; margin: 0 auto; background-color: #ffffff; padding: 24px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
 <h1 style="font-size: 24px; font-weight: bold; margin-bottom: 16px; color: #1f2937;">
  Mise en Forme XML avec CSS
 </h1>
 <p style="margin-bottom: 16px; color: #4b5563;">
  Entrez un contenu XML et un style CSS dans les champs ci-dessous, puis cliquez sur "Mise en forme" pour afficher le résultat stylisé dans l'iframe. Exemples :
 </p>
 <div style="display: flex; gap: 16px; margin-bottom: 24px;">
  <div style="flex: 1;">
   <h2 style="font-size: 18px; font-weight: bold; color: #374151; margin-bottom: 8px;">
    Exemple XML :
   </h2>
   <pre style="background-color: #e6f4ea; padding: 12px; border: 1px solid #15803d; border-radius: 4px; font-family: monospace; font-size: 14px; color: #374151;"><!--?xml version="1.0" ?-->
<comptearecevoir>
    <facture>
        <personne>Jean Rochond</personne>
        <montant>10.10</montant>
        <raison>Achat d'ordinateur</raison>
    </facture>
    <facture>
        <personne>Madeleine Bédard</personne>
        <montant>20.10</montant>
        <raison>Achat d'un crayon</raison>
    </facture>
</comptearecevoir>
                </pre>
  </div>
  <div style="flex: 1;">
   <h2 style="font-size: 18px; font-weight: bold; color: #374151; margin-bottom: 8px;">
    Exemple CSS :
   </h2>
   <pre style="background-color: #e6f4ea; padding: 12px; border: 1px solid #15803d; border-radius: 4px; font-family: monospace; font-size: 14px; color: #374151;">facture {
    display: block;
    margin-bottom: 30pt;
}
montant {
    color: red;
}
raison {
    display: block;
    font-style: italic;
    margin-left: 1cm;
}
                </pre>
  </div>
 </div>
 <div style="background-color: #f9fafb; padding: 16px; border: 1px solid #e5e7eb; border-radius: 8px;">
  <p style="font-size: 16px; font-weight: bold; color: #374151; margin-bottom: 8px;">
   Document XML :
  </p>
  <textarea cols="45" id="xmlsource" rows="25" style="width: 100%; padding: 8px; border: 1px solid #d1d5db; border-radius: 4px; font-family: monospace; font-size: 14px; margin-bottom: 16px;">&lt;?xml version="1.0" ?&gt;
&lt;comptearecevoir&gt;
    &lt;facture&gt;
        &lt;personne&gt;Jean Rochond&lt;/personne&gt;
        &lt;montant&gt;10.10&lt;/montant&gt;
        &lt;raison&gt;Achat d'ordinateur&lt;/raison&gt;
    &lt;/facture&gt;
    &lt;facture&gt;
        &lt;personne&gt;Madeleine Bédard&lt;/personne&gt;
        &lt;montant&gt;20.10&lt;/montant&gt;
        &lt;raison&gt;Achat d'un crayon&lt;/raison&gt;
    &lt;/facture&gt;
&lt;/comptearecevoir&gt;
            </textarea>
  <p style="font-size: 16px; font-weight: bold; color: #374151; margin-bottom: 8px;">
   Document CSS :
  </p>
  <textarea cols="45" id="csssource" rows="25" style="width: 100%; padding: 8px; border: 1px solid #d1d5db; border-radius: 4px; font-family: monospace; font-size: 14px; margin-bottom: 16px;">facture {
    display: block;
    margin-bottom: 30pt;
}
montant {
    color: red;
}
raison {
    display: block;
    font-style: italic;
    margin-left: 1cm;
}
            </textarea>
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
    var mondom = chargeXML('xmlsource');
    var pi = mondom.createProcessingInstruction('xml-stylesheet',
                                         'type=&quot;text/css&quot; href=&quot;data:text/css;charset=utf-8,' + encodeURI(document.getElementById('csssource').value)+'&quot;');
    var root = mondom.firstChild;
    mondom.insertBefore(pi, root);
    var serializer = new XMLSerializer();
    var resultatTexte = serializer.serializeToString(mondom);
    document.getElementById('dis').src = 'data:application/xml;charset=utf-8,' + encodeURI(resultatTexte);
    " style="width: 100%; background-color: #2563eb; color: #ffffff; padding: 10px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; transition: background-color 0.2s; margin-bottom: 16px;" type="button" value="Mise en forme"/>
  <div id="error" style="margin-bottom: 16px; color: #dc2626; font-size: 14px;">
  </div>
  <p style="font-size: 16px; font-weight: bold; color: #374151; margin-bottom: 8px;">
   Résultat :
  </p>
  <iframe id="dis" src="data:application/xml;charset=utf-8,%3C?xml%20version=%221.0%22?%3E%3C?xml-stylesheet%20type=%22text/css%22%20href=%22data:text/css;charset=utf-8,facture%2520%257B%250A%2520%2520%2520%2520display:%2520block;%250A%2520%2520%2520%2520margin-bottom:%252030pt;%250A%257D%250Amontant%2520%257B%250A%2520%2520%2520%2520color:%2520red;%250A%257D%250Araison%2520%257B%250A%2520%2520%2520%2520display:%2520block;%250A%2520%2520%2520%2520font-style:%2520italic;%250A%2520%2520%2520%2520margin-left:%25201cm;%250A%257D%250A%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%22?%3E%3Ccomptearecevoir%3E%0A%20%20%20%20%3Cfacture%3E%0A%20%20%20%20%20%20%20%20%3Cpersonne%3EJean%20Rochond%3C/personne%3E%0A%20%20%20%20%20%20%20%20%3Cmontant%3E10.10%3C/montant%3E%0A%20%20%20%20%20%20%20%20%3Craison%3EAchat%20d'ordinateur%3C/raison%3E%0A%20%20%20%20%3C/facture%3E%0A%20%20%20%20%3Cfacture%3E%0A%20%20%20%20%20%20%20%20%3Cpersonne%3EMadeleine%20B%C3%A9dard%3C/personne%3E%0A%20%20%20%20%20%20%20%20%3Cmontant%3E20.10%3C/montant%3E%0A%20%20%20%20%20%20%20%20%3Craison%3EAchat%20d'un%20crayon%3C/raison%3E%0A%20%20%20%20%3C/facture%3E%0A%3C/comptearecevoir%3E" style="width: 100%; height: 600px; border: 1px solid #d1d5db; border-radius: 4px;">
  </iframe>
 </div>
</div>
