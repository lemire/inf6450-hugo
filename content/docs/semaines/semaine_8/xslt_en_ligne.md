---
title: "XSLT en ligne"
weight: 30
---

<h1 style="font-size: 2rem; font-weight: bold; color: #1f2937; text-align: center; margin-bottom: 1.5rem;">
 XSLT en ligne
</h1>
<p style="color: #4b5563; margin-bottom: 1rem; line-height: 1.5;">
 Testez vos transformations XSLT directement dans votre navigateur ! Cet outil vous permet de traiter n'importe quel fichier XML avec une feuille de style XSLT sans utiliser l'instruction
 <code style="background-color: #f3f4f6; padding: 2px 4px; border-radius: 4px; font-family: monospace;">
  xml-stylesheet
 </code>
 . C'est une alternative pratique pour programmer et expérimenter avec XSLT sans charger de fichiers externes.
</p>
<p style="color: #4b5563; margin-bottom: 1rem; line-height: 1.5;">
 Essayez la transformation XSLT proposée ci-dessous. Pouvez-vous repérer l'expression XPath dans le script ? Modifiez-la pour voir comment le résultat change. La pratique est essentielle pour maîtriser XSLT, alors n'hésitez pas à expérimenter !
</p>
<p style="color: #4b5563; margin-bottom: 1rem; line-height: 1.5;">
 <strong>
  Instructions :
 </strong>
 Saisissez un fichier XML source et une transformation XSLT valide, puis cliquez sur « Transformer ». Vous pouvez réinitialiser les champs avec le bouton « Réinitialiser ».
</p>
<div style="margin-bottom: 1rem;">
 <label for="xmlsource" style="display: block; font-weight: 600; color: #374151; margin-bottom: 0.5rem; font-family: system-ui, sans-serif;">
  Document XML source
 </label>
 <textarea id="xmlsource" rows="14" style="width: 100%; font-family: ui-monospace, monospace; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; resize: vertical; box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);">&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;monmessage&gt;
    &lt;de&gt;Jean&lt;/de&gt;
    &lt;a&gt;Pierre&lt;/a&gt;
    &lt;titre type="émotion"&gt;Ouch!&lt;/titre&gt;
    &lt;corps&gt;Maman!&lt;/corps&gt;
&lt;/monmessage&gt;</textarea>
</div>
<div style="margin-bottom: 1rem;">
 <label for="xstlsource" style="display: block; font-weight: 600; color: #374151; margin-bottom: 0.5rem; font-family: system-ui, sans-serif;">
  Feuille de style XSLT (ex. 1.0)
 </label>
 <textarea id="xstlsource" rows="14" style="width: 100%; font-family: ui-monospace, monospace; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; resize: vertical; box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);">&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;xsl:output method="text"/&gt;
  &lt;xsl:template match="/"&gt;
    Résultat de l'attribut type : &lt;xsl:value-of select="//titre/@type"/&gt;
    &lt;xsl:text&gt;
&lt;/xsl:text&gt;
    Nombre d'éléments enfants du document : &lt;xsl:value-of select="count(//*)"/&gt;
  &lt;/xsl:template&gt;
&lt;/xsl:stylesheet&gt;</textarea>
</div>
<div style="margin-top:1rem;">
 <div style="font-weight: 600; font-family: system-ui, sans-serif;">
  Résultat
 </div>
 <div aria-live="polite" id="sol" style="min-height: 140px; background: #ffffff; border: 1px solid #e5e7eb; border-radius: 8px; padding: 16px; white-space: pre-wrap; overflow: auto; margin-top: 0.5rem;">
  Cliquez sur « Transformer ».
 </div>
 <div aria-live="assertive" id="error" style="color: #b91c1c; margin-top: 0.5rem; display: none; font-weight: 500; white-space: pre-wrap;">
 </div>
</div>
<div style="text-align:center; margin-top:1rem;">
 <button class="btn-primary" onclick="transform()" style="padding: 10px 18px; font-weight: 600; border: none; border-radius: 6px; cursor: pointer; background: #10b981; color: white;">
  Transformer
 </button>
 <button class="btn-secondary" onclick="resetFields()" style="padding: 10px 18px; font-weight: 600; border: none; border-radius: 6px; cursor: pointer; background: #6b7280; color: white;">
  Réinitialiser
 </button>
</div>
<script>
const defaultXML=document.getElementById('xmlsource').value;
const defaultXSLT=document.getElementById('xstlsource').value;
async function transform(){
const xmlText=document.getElementById('xmlsource').value;
const xsltText=document.getElementById('xstlsource').value;
const resultDiv=document.getElementById('sol');
const errorDiv=document.getElementById('error');
resultDiv.textContent='Transformation en cours…';
errorDiv.style.display='none';
try{
const xmlParser=new DOMParser();
const xsltParser=new DOMParser();
const xmlDoc=xmlParser.parseFromString(xmlText,'application/xml');
const xsltDoc=xsltParser.parseFromString(xsltText,'application/xml');
if(xmlDoc.querySelector('parsererror')){throw new Error('Erreur dans le XML source: '+xmlDoc.querySelector('parsererror').textContent);}
if(xsltDoc.querySelector('parsererror')){throw new Error('Erreur dans la feuille XSLT: '+xsltDoc.querySelector('parsererror').textContent);}
const xsltProcessor=new XSLTProcessor();
xsltProcessor.importStylesheet(xsltDoc);
const resultDoc=xsltProcessor.transformToDocument(xmlDoc);
const serializer=new XMLSerializer();
let out=serializer.serializeToString(resultDoc);
if(resultDoc.querySelector('output[method="text"]')||out.includes('<output method="text"')){out=resultDoc.documentElement.textContent;}
if(typeof out==='string'&&/<\/?\w+/.test(out)){resultDiv.innerHTML=out;}else{resultDiv.textContent=out||'(résultat vide)';}
}catch(err){
console.error('Erreur de transformation :',err);
errorDiv.textContent=(err&&err.message)?err.message:String(err);
if(err&&err.stack)errorDiv.textContent+='\n\n'+err.stack;
errorDiv.style.display='block';
resultDiv.textContent='';}
}
function resetFields(){
document.getElementById('xmlsource').value=defaultXML;
document.getElementById('xstlsource').value=defaultXSLT;
document.getElementById('sol').textContent='Cliquez sur « Transformer ».';
document.getElementById('error').style.display='none';
}
</script>


