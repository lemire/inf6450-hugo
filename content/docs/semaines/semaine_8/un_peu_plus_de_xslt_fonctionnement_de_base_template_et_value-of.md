---
title: "Un peu plus de XSLT : fonctionnement de base, template et value-of"
weight: 40
---
<h1>
 Un peu plus de XSLT : fonctionnement de base, template et value-of
</h1>
<h2 class="recall">
 « Éléments xsl:template »
</h2>
<p>
 Modifions maintenant le fichier « xslt.xml » de façon à rendre l'expérience plus intéressante. 
     Tout d'abord, traitons tous les éléments « facture » du document XML. 
     Pour obtenir le résultat, il faut placer un élément « &lt;xsl:template match="facture"&gt; » 
     dans l'élément-racine du document XSLT comme ceci :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
     &lt;xsl:stylesheet version="1.0" 
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
     &lt;xsl:template match="facture"&gt;
     On doit mettre quelque chose ici!!!
     &lt;/xsl:template&gt;
     &lt;/xsl:stylesheet&gt;
</p>
<p>
 Il faut voir l'élément « xsl:template » comme une règle 
       qui dit : à chaque fois qu'on rencontre un élément qui s'appelle « facture », faisons ceci. 
       Le modèle est inclus dans l'élément « xsl:template ». Dans l'exemple de 
       document XSLT que nous venons de voir, le processeur XSLT remplacerait tous les 
       éléments « facture » qu'il rencontre par le texte « On doit mettre quelque chose ici!!! », 
       ce qui donnerait comme résultat le fichier suivant (le résultat exact peut varier un peu selon le processeur XSLT) :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
      On doit mettre quelque chose ici!!!
</p>
<p>
 Malheureusement, ce n'est pas du HTML valable et votre navigateur devrait n'afficher 
     qu'un écran vide ou une erreur si vous tentez d'ouvrir le fichier « test.xml » avec un lien 
     vers un tel fichier XSLT. (En pratique, le navigateur peut interpréter le résultat différemment.) Notre laboratoire XSLT en ligne risque d'ailleurs de vous donner une erreur, car il ne comprendra pas que vous génériez autre chose que du XML ou du HTML (mais on peut remédier à ce problème avec une instruction output, nous y reviendrons). Nous allons donc modifier le fichier XSLT, en ajoutant des balises, comme ceci :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
     &lt;xsl:stylesheet version="1.0" 
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
     &lt;xsl:template match="facture"&gt;
     &lt;html&gt;&lt;body&gt;On doit mettre quelque chose ici!!!&lt;/body&gt;&lt;/html&gt;
     &lt;/xsl:template&gt;
     &lt;/xsl:stylesheet&gt;
</p>
<p>
 Cette fois, si vous ouvrez le document « test.xml », vous devriez voir le texte « On doit 
     mettre quelque chose ici!!! » s'afficher dans votre navigateur. Faites l'expérience.
</p>
<p>
 Dans les exemples que nous allons proposer, nous omettons les éléments « html » et « body » 
     par souci de simplicité. La présence de ces éléments n'est pas nécessaire et n'est utile que pour 
     afficher le résultat dans un navigateur. À vous de les ajouter si vous désirez afficher le résultat.
</p>
<p>
 <b>
  Pour résumer, chaque fois que le processeur XSLT rencontre un élément « facture », 
     il applique le modèle qui se trouve dans l'élément « &lt;xsl:template match="facture"&gt; ».
 </b>
 Notez que si l'élément « facture » contient lui-même des éléments, ils ne sont pas automatiquement 
     visités par le processeur XSLT. Ce dernier considère que dès qu'un modèle est appliqué à un élément, 
     il peut alors parcourir le reste du document sans se soucier du contenu de cet élément 
     qui est maintenant « couvert », à moins qu'on lui dise explicitement de traiter les noeuds-enfants avec une instruction comme apply-template. Le XSLT est très bête: il part de la racine et applique les règles à ce qu'il rencontre.
</p>
<h3 class="recall">
 « Éléments xsl:value-of »
</h3>
<p>
 Jusqu'à présent, le résultat n'est pas très fascinant parce que 
     les éléments « xsl:template » ont été utilisés comme des outils pour faire du « Rechercher/Remplacer ». 
     Le contenu de l'élément « facture » n'est pas traité, on le remplace bêtement par autre chose.
</p>
<p>
 Nous pouvons traiter le contenu d'un élément à l'aide d'un élément « xsl:value-of » 
     avec la syntaxe &lt;xsl:value-of select="..." /&gt;. La valeur de l'élément « select » 
     est une expression XPath.
            Par exemple, si le processeur traite un élément « facture » qui contient un élément « montant », 
     alors l'élément &lt;xsl:value-of select="montant" /&gt; nous donne le contenu de l'élément « montant ».
            C'est ainsi que nous pouvons trouver le nom de la personne devant recevoir une facture, 
     en utilisant &lt;xsl:value-of select="personne" /&gt;.
</p>
<p>
 Voyons maintenant un exemple plus complexe de fichier XSLT :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
     &lt;xsl:stylesheet version="1.0" 
      xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
     &lt;xsl:template match="facture"&gt;
     &lt;html&gt;
     &lt;head&gt;
     &lt;title&gt;Facture de &lt;xsl:value-of select="personne" /&gt;&lt;/title&gt;
     &lt;/head&gt;
     &lt;body&gt;
     &lt;p&gt;Ceci est une facture pour &lt;xsl:value-of select="personne" /&gt;
      de &lt;xsl:value-of select="montant" /&gt;$ pour: 
     &lt;xsl:value-of select="raison" /&gt;.&lt;/p&gt;
     &lt;/body&gt;
     &lt;/html&gt;
     &lt;/xsl:template&gt;
     &lt;/xsl:stylesheet&gt;
</p>
<p>
 Si vous modifiez le fichier « xslt.xml » et que vous ouvrez le fichier « test.xml » 
          dans un navigateur supportant le XSLT, vous devriez voir s'afficher à l'écran 
          la ligne « Ceci est une facture pour Jean Rochond de 10.10$ pour: Achat d'ordinateur. ».
          Il faut avouer que c'est déjà beaucoup plus intéressant comme application!
</p>
<p>
 Ce qui se passe, c'est que le nouveau document XSLT transforme notre document XML en un document HTML :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;html&gt;
         &lt;head&gt;
         &lt;meta http-equiv="Content-Type" content="text/html; charset=UTF-8"&gt;
         &lt;title&gt;Facture de  Jean Rochond&lt;/title&gt;
         &lt;/head&gt;
         &lt;body&gt;&lt;p&gt;Ceci est une facture pour Jean Rochond
         de 10.10$ pour: Achat d'ordinateur.&lt;/p&gt;&lt;/body&gt;
         &lt;/html&gt;
</p>
<p>
 <b>
  Pour résumer, nous pouvons aller chercher le contenu textuel d'une expression XPath avec une 
     instruction comme « &lt;xsl:value-of select="..." /&gt; » où « ... » est une expression XPath comme le nom 
     de l'élément.
 </b>
</p>
<h3 class="recall">
 Modèle de traitement XSLT
</h3>
<p>
 Une source de confusion commune avec le XSLT est une mauvaise appréciation du modèle de traitement. Certains s'imaginent que le XSLT visite les règles une à une, les appliquant à tout le document. Ainsi, la  règle  de type «xsl:template match="facture"» devrait, selon eux, s'appliquer à tous les éléments de type facture. Or, ce n'est pas le cas du tout en général. Le processeur XSLT visite les noeuds un à un. Quand il visite un noeud, il cherche la règle qui s'applique. Il est donc parfaitement possible que plusieurs des règles inscrites dans un document XSLT ne s'appliquent jamais.
</p>
<p>
 Un processeur XSLT traite un fichier XML en partant du début et en appliquant ses règles 
    au fur et à mesure qu'il rencontre des noeuds. Rappelons que  
    si le processeur XSLT rencontre un élément pour lequel il n'a aucune règle (modèle),
    il visite les sous-éléments à leur tour, c'est une de ses règles par défaut.
</p>
<p>
 Une autre façon de décrire ce comportement est de dire que le XSLT utilise un modèle de 
    fichiers XML « en arbre de nœuds ». Imaginons un arbre où, à la racine, se trouve un nœud 
    spécial représentant le document dans son ensemble. Avec XPath, nous pouvons pointer 
    directement sur le nœud-racine (le document lui-même) en utilisant la barre oblique « / » que nous 
    plaçons au début de l'expression XPath, comme dans « &lt;xsl:value-of select="/" /&gt; ». 
    Dans ce cas, « &lt;xsl:value-of select="/jean" /&gt; » donne la valeur de l'élément-racine, 
    si celui-ci se nomme « jean ».
</p>
<p>
 Le nœud-racine contient lui-même l'élément-racine. Chaque élément et chaque élément de texte 
    sont aussi des nœuds dans ce modèle d'arbre XSLT. Alors que les nœuds de texte ne 
    peuvent pas contenir d'autres nœuds, les nœuds d'élément peuvent contenir plusieurs autres nœuds 
    dont d'autres nœuds d'élément et de texte.
</p>
<p>
 Ainsi, par défaut, le processeur XSLT qui atteint un élément visite tous les  éléments et les nœuds de texte qu'il contient. 
    Un nœud de texte rencontré est simplement recopié, par défaut, alors que pour les éléments, 
    on visite également leur contenu. C'est ce qui explique que, par défaut, s'il n'y a aucune règle dans le document XSLT, 
    un document XML est recopié sans les balises.
</p>
<p>
 D'autres nœuds existent comme les nœuds de commentaire, les nœuds 
    d'instructions de traitement et les nœuds d'espaces de noms,   
    mais ils sont moins importants que le nœud du document (nœud-racine), 
    les nœuds d'attribut, les nœuds de texte ou les nœuds d'élément. Dans le modèle d'arbre, les nœuds d'espaces de noms et
    les nœuds d'attribut sont attachés à l'élément, mais ne sont pas
    un enfant (« child »).
</p>
<p>
 Nous avons déjà vu que « * » et « @* » permettaient de sélectionner les sous-éléments et attributs d'un élément. On peut sélectionner 
    les nœuds de texte avec la fonction XPath « text() ». Notons aussi que l'élément « &lt;xsl:apply-templates/&gt; » signifie que les modèles s'appliquent à tous les nœuds contenus dans le nœud courant. Les règles
    par défaut qui s'appliquent en XSLT sont :
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;xsl:template match="*|/"&gt;
       &lt;xsl:apply-templates/&gt;
     &lt;/xsl:template&gt;
    
     &lt;xsl:template match="text()|@*"&gt;
       &lt;xsl:value-of select="."/&gt;
     &lt;/xsl:template&gt;
    
     &lt;xsl:template match="processing-instruction()|comment()"  /&gt;
</p>
<p>
 La première règle (ou instruction) indique que si on rencontre un élément ou la racine du document, on applique tout simplement les autres instructions aux noeuds que l'on y trouve. La seconde règle indique que si on trouve un noeud de texte ou un attribut, on retourne tout simplement la valeur textuelle du noeud. Finalement, la dernière règle indique que si on trouve un commentaire ou une instruction de traitement, on n'en traite pas le contenu.
</p>
<p>
 Un processeur XSLT représente un document XML comme un arbre et 
    tente de le visiter de la racine vers les feuilles. Lorsqu'il rencontre un modèle pour un nœud, 
    il l'applique et ne poursuit pas automatiquement la visite des nœuds qui y sont contenus, 
    à moins de rencontrer un élément « xsl:apply-templates ».
</p>
<p>
 Par défaut, un traitement XSLT va extraire le contenu textuel du document XML provenant des noeuds de texte et des attributs. Le produit final sera un aggrégat de tout le contenu textuel ainsi extrait.
</p>
<p>
 Récapitulons. Le XSLT fait ce qu'on lui dit de faire, rien de plus, rien de moins. Il commence avec la racine du document et applique les règles. Il est muni de règles de base lui indiquant quoi faire avec des éléments, des attributs, etc. Vous pouvez ajouter de nouvelles règles ou remplacer les règles de base.
</p>
<p>
 Si vous utilisez la règle suivant, indiquant au XSLT de ne rien faire à partir de la racine, alors il ne fera rien (rien ne sera généré).
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;xsl:template match="/"&gt;
     &lt;/xsl:template&gt;
</p>
<p>
 Le XSLT applique de préférence vos règles plutôt que celles par défaut. Ainsi donc, si vous ajoutez la règle suivante...
</p>
<p style="border:solid 1px black;white-space:pre; font-size:0.85em">
 &lt;xsl:template match="*"&gt;
       &lt;xsl:value-of select="."/&gt;
     &lt;/xsl:template&gt;
</p>
<p>
 ... alors elle s'appliquera quand l'élément-racine (ou tout autre élément) de votre document sera visité. Comme cette règle n'indique pas de visiter les sous-éléments (par l'instruction apply-templates), ceux-ci ne seront pas visités. Dans un tel cas, tout ce qui sera produit sera la valeur textuelle de l'élément-racine. Le traitement XSLT s'arrêtera alors.
</p>
<p>
 Cela illustre que le XSLT ne génère pas nécessairement du XML valable. Certains moteurs XSLT s'attendent à obtenir du XML ou du HTML (si l'élément-racine est nommé en conséquence) et peuvent générer une erreur dans le cas contraire. Certains moteurs peuvent même modifier le résultat de manière à ce qu'il s'agisse de XML ou du HTML valable. D'autres processeurs vont refuser de produire autre chose que du XML ou du HTML, à moins d'indication contraire.
</p>
<p>
 Les règles s'appliquent selon un ordre de priorité. Vos règles s'appliquent avant celles par défaut. Les règles spécifiques (nommant un élément XML par son nom) s'appliquent avant les règles génériques (par exemple, celles spécifiant le type de noeud comme « * »). Une disjonction ( « | ») est traitée comme un ensemble de règles distinctes.  Si deux règles ont une priorité égale, le moteur XSLT peut choisir arbitrairement un des deux règles ou générer une erreur.
</p>
<h3>
 Un exemple
</h3>
<p>
 Pour illustrer le fonctionnement du XSLT, prenons un example. Soit ce document XML:
</p>
<!-- HTML generated using hilite.me -->
<div style="background: #ffffff; overflow:auto;width:auto;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
 <pre style="margin: 0; line-height: 125%"><span style="color: #007700">&lt;racine&gt;</span>
        <span style="color: #007700">&lt;element&gt;</span>
            <span style="color: #007700">&lt;souselement&gt;</span>
            <span style="color: #007700">&lt;/souselement&gt;</span>
        <span style="color: #007700">&lt;/element&gt;</span>
        <span style="color: #007700">&lt;element2&gt;</span>
            <span style="color: #007700">&lt;souselement2&gt;</span>
            <span style="color: #007700">&lt;/souselement2&gt;</span>
        <span style="color: #007700">&lt;/element2&gt;</span>
    <span style="color: #007700">&lt;/racine&gt;</span>
    </pre>
</div>
<p>
 Soit ce document XSLT:
</p>
<!-- HTML generated using hilite.me -->
<div style="background: #ffffff; overflow:auto;width:auto;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
 <pre style="margin: 0; line-height: 125%"><span style="color: #007700">&lt;xsl:stylesheet</span> <span style="color: #0000CC">version=</span><span style="background-color: #fff0f0">"1.0"</span>
      <span style="color: #0000CC">xmlns:xsl=</span><span style="background-color: #fff0f0">"http://www.w3.org/1999/XSL/Transform"</span><span style="color: #007700">&gt;</span>
        <span style="color: #007700">&lt;xsl:template</span> <span style="color: #0000CC">match=</span><span style="background-color: #fff0f0">"element"</span> <span style="color: #007700">&gt;</span>
            Transformation 1
        <span style="color: #007700">&lt;/xsl:template&gt;</span>
        <span style="color: #007700">&lt;xsl:template</span> <span style="color: #0000CC">match=</span><span style="background-color: #fff0f0">"souselement"</span><span style="color: #007700">&gt;</span>
            Transformation 2
        <span style="color: #007700">&lt;/xsl:template&gt;</span>
        <span style="color: #007700">&lt;xsl:template</span> <span style="color: #0000CC">match=</span><span style="background-color: #fff0f0">"souselement2"</span><span style="color: #007700">&gt;</span>
            transformation3
        <span style="color: #007700">&lt;/xsl:template&gt;</span>
    <span style="color: #007700">&lt;/xsl:stylesheet&gt;</span>
    </pre>
</div>
<p>
 Par souci de simplicité, nous allons ignorer les noeuds de texte de cet exemple. Il n'y a donc que des éléments.
</p>
<ol>
 <li>
  <p>
   Le processeur débute au noeud racine. La règle par défaut s'applique et on l'instruit (avec apply-templates) de traiter tous les noeuds qu'il contient en séquence.
  </p>
 </li>
 <li>
  <p>
   Le processeur trouve alors l'élément nommé « racine ». La règle par défaut s'applique encore et le processeur visite simplement les noeuds contenus. Dans ce cas, il y en a deux (deux éléments).
  </p>
  <ol>
   <li>
    Le processeur va alors traiter l'élément nommé « element ». Dans ce cas, la règle que nous avons introduite dans notre document XSLT s'applique et le processeur XSLT émet la chaîne de caractères « Transformation 1 ». Notez que l'élément nommé souselement ne sera pas traité.
   </li>
   <li>
    Le processeur traite alors l'élément nommé « element2 ». La règle par défaut s'applique. Il visite donc l'élément «souselement2». La règle que nous avons introduite s'applique et le processeur émet «transformation3 ».
   </li>
  </ol>
 </li>
</ol>
<p>
 Le résultat produit sera donc la chaîne de caractères «Transformation 1 transformation3 ».
</p>
<p>
 Vous pouvez mettre cet exemple en marche dans votre navigateur.
</p>




<div style="margin-bottom: 1rem;">
 <label for="xmlsource" style="display: block; font-weight: 600; color: #374151; margin-bottom: 0.5rem; font-family: system-ui, sans-serif;">
  Document XML source
 </label>
 <textarea id="xmlsource" rows="14" style="width: 100%; font-family: ui-monospace, monospace; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; resize: vertical; box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);">&lt;?xml version="1.0" ?&gt; 
    &lt;racine&gt;
        &lt;element&gt;
            &lt;souselement&gt;
            &lt;/souselement&gt;
        &lt;/element&gt;
        &lt;element2&gt;
            &lt;souselement2&gt;
            &lt;/souselement2&gt;
        &lt;/element2&gt;
    &lt;/racine&gt;</textarea>
</div>
<div style="margin-bottom: 1rem;">
 <label for="xstlsource" style="display: block; font-weight: 600; color: #374151; margin-bottom: 0.5rem; font-family: system-ui, sans-serif;">
  Feuille de style XSLT (ex. 1.0)
 </label>
 <textarea id="xstlsource" rows="14" style="width: 100%; font-family: ui-monospace, monospace; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; resize: vertical; box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);">&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;xsl:output method="text"/&gt;
  &lt;xsl:template match="element" &gt;
    Transformation 1
  &lt;/xsl:template&gt;
  &lt;xsl:template match="souselement"&gt;
    Transformation 2
  &lt;/xsl:template&gt;
  &lt;xsl:template match="souselement2"&gt;
    transformation3
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



<p>
 Notez que nous avons ajouté une instruction «output» spécifiant un contenu textuel. Sans cette instruction, plusieurs processeurs XSLT seront confus par le résultat généré (celui-ci n'étant pas du XML) et ils peuvent générer une erreur. Vous noterez peut-être aussi que votre navigateur met le résultat textuel dans un document HTML. C'est un cas particulier où le processeur prend sur lui d'imposer un format. Dans le cas d'un navigateur web, il est justifiable d'exiger que le document produit soit du XML ou du HTML.
</p>
<p>
 Assurez-vous de bien comprendre cet exemple avant de continuer. Vous devez avoir une bonne représentation mentale de la manière dont fonctionne un processeur XSLT.
</p>
