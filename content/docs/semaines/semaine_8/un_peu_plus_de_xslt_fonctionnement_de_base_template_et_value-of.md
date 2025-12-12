---
title: "Un peu plus de XSLT : fonctionnement de base, template et value-of"
weight: 40
---

# Un peu plus de XSLT : fonctionnement de base, template et value-of

## « Éléments xsl:template »

Dans cette section, nous explorons les éléments xsl:template, qui sont essentiels pour définir des règles de transformation personnalisées dans les feuilles de style XSLT.

Modifions maintenant le fichier « xslt.xml » de façon à rendre l'expérience plus intéressante. Tout d'abord, traitons tous les éléments « facture » du document XML. Pour obtenir le résultat, il faut placer un élément « <xsl:template match="facture"> » dans l'élément-racine du document XSLT comme ceci :

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
    <xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="facture">
    On doit mettre quelque chose ici!!!
    </xsl:template>
    </xsl:stylesheet>
```

Il faut voir l'élément « xsl:template » comme une règle qui dit : à chaque fois qu'on rencontre un élément qui s'appelle « facture », faisons ceci. Le modèle est inclus dans l'élément « xsl:template ». Dans l'exemple de document XSLT que nous venons de voir, le processeur XSLT remplacerait tous les éléments « facture » qu'il rencontre par le texte « On doit mettre quelque chose ici!!! », ce qui donnerait comme résultat le fichier suivant (le résultat exact peut varier un peu selon le processeur XSLT) :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
     On doit mettre quelque chose ici!!!
```

Malheureusement, ce n'est pas du HTML valide et votre navigateur devrait n'afficher qu'un écran vide ou une erreur si vous tentez d'ouvrir le fichier « test.xml » avec un lien vers un tel fichier XSLT. (En pratique, le navigateur peut interpréter le résultat différemment.) Notre laboratoire XSLT en ligne risque d'ailleurs de vous donner une erreur, car il ne comprendra pas que vous génériez autre chose que du XML ou du HTML (mais on peut remédier à ce problème avec une instruction output, nous y reviendrons). Nous allons donc modifier le fichier XSLT, en ajoutant des balises, comme ceci :
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
    <xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="facture">
    <html><body>On doit mettre quelque chose ici!!!</body></html>
    </xsl:template>
    </xsl:stylesheet>
```

Cette fois, si vous ouvrez le document « test.xml », vous devriez voir le texte « On doit mettre quelque chose ici!!! » s'afficher dans votre navigateur. Faites l'expérience.

Dans les exemples que nous allons proposer, nous omettons les éléments « html » et « body » par souci de simplicité. La présence de ces éléments n'est pas nécessaire et n'est utile que pour afficher le résultat dans un navigateur. À vous de les ajouter si vous désirez afficher le résultat.

**Pour résumer, chaque fois que le processeur XSLT rencontre un élément « facture », il applique le modèle qui se trouve dans l'élément « <xsl:template match="facture"> ».** Notez que si l'élément « facture » contient lui-même des éléments, ils ne sont pas automatiquement visités par le processeur XSLT. Ce dernier considère que dès qu'un modèle est appliqué à un élément, il peut alors parcourir le reste du document sans se soucier du contenu de cet élément qui est maintenant « couvert », à moins qu'on lui dise explicitement de traiter les noeuds-enfants avec une instruction comme apply-template. Le XSLT est très bête: il part de la racine et applique les règles à ce qu'il rencontre.

## « Éléments xsl:value-of »

Dans cette section, nous découvrons les éléments xsl:value-of, qui permettent d'extraire et d'insérer le contenu textuel des éléments XML dans le résultat de la transformation.

Jusqu'à présent, le résultat n'est pas très fascinant parce que les éléments « xsl:template » ont été utilisés comme des outils pour faire du « Rechercher/Remplacer ». Le contenu de l'élément « facture » n'est pas traité, on le remplace bêtement par autre chose.

Nous pouvons traiter le contenu d'un élément à l'aide d'un élément « xsl:value-of » avec la syntaxe <xsl:value-of select="..." />. La valeur de l'élément « select » est une expression XPath. Par exemple, si le processeur traite un élément « facture » qui contient un élément « montant », alors l'élément <xsl:value-of select="montant" /> nous donne le contenu de l'élément « montant ». C'est ainsi que nous pouvons trouver le nom de la personne devant recevoir une facture, en utilisant <xsl:value-of select="personne" />.

Voyons maintenant un exemple plus complexe de fichier XSLT :

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
    <xsl:stylesheet version="1.0" 
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="facture">
    <html>
    <head>
    <title>Facture de <xsl:value-of select="personne" /></title>
    </head>
    <body>
    <p>Ceci est une facture pour <xsl:value-of select="personne" />
     de <xsl:value-of select="montant" />$ pour: 
    <xsl:value-of select="raison" />.</p>
    </body>
    </html>
    </xsl:template>
    </xsl:stylesheet>
```

Si vous modifiez le fichier « xslt.xml » et que vous ouvrez le fichier « test.xml » dans un navigateur supportant le XSLT, vous devriez voir s'afficher à l'écran la ligne « Ceci est une facture pour Jean Rochond de 10.10$ pour: Achat d'ordinateur. ». Il faut avouer que c'est déjà beaucoup plus intéressant comme application!

Ce qui se passe, c'est que le nouveau document XSLT transforme notre document XML en un document HTML :

```xml
<html>
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Facture de  Jean Rochond</title>
        </head>
        <body><p>Ceci est une facture pour Jean Rochond
        de 10.10$ pour: Achat d'ordinateur.</p></body>
        </html>
```
**Pour résumer, nous pouvons aller chercher le contenu textuel d'une expression XPath avec une instruction comme « <xsl:value-of select="..." /> » où « ... » est une expression XPath comme le nom de l'élément.**

### Modèle de traitement XSLT

Dans cette section, nous examinons le modèle de traitement sous-jacent du XSLT, expliquant comment le processeur parcourt le document XML et applique les règles de transformation.

Une source de confusion commune avec le XSLT est une mauvaise appréciation du modèle de traitement. Certains s'imaginent que le XSLT visite les règles une à une, les appliquant à tout le document. Ainsi, la  règle  de type «xsl:template match="facture"» devrait, selon eux, s'appliquer à tous les éléments de type facture. Or, ce n'est pas le cas du tout en général. Le processeur XSLT visite les noeuds un à un. Quand il visite un noeud, il cherche la règle qui s'applique. Il est donc parfaitement possible que plusieurs des règles inscrites dans un document XSLT ne s'appliquent jamais.
Un processeur XSLT traite un fichier XML en partant du début et en appliquant ses règles 
   au fur et à mesure qu'il rencontre des noeuds. Rappelons que  
   si le processeur XSLT rencontre un élément pour lequel il n'a aucune règle (modèle),
   il visite les sous-éléments à leur tour, c'est une de ses règles par défaut.

Une autre façon de décrire ce comportement est de dire que le XSLT utilise un modèle de 
   fichiers XML « en arbre de nœuds ». Imaginons un arbre où, à la racine, se trouve un nœud 
   spécial représentant le document dans son ensemble. Avec XPath, nous pouvons pointer 
   directement sur le nœud-racine (le document lui-même) en utilisant la barre oblique « / » que nous 
   plaçons au début de l'expression XPath, comme dans « <xsl:value-of select="/" /> ». 
   Dans ce cas, « <xsl:value-of select="/jean" /> » donne la valeur de l'élément-racine, 
   si celui-ci se nomme « jean ».

Le nœud-racine contient lui-même l'élément-racine. Chaque élément et chaque élément de texte 
   sont aussi des nœuds dans ce modèle d'arbre XSLT. Alors que les nœuds de texte ne 
   peuvent pas contenir d'autres nœuds, les nœuds d'élément peuvent contenir plusieurs autres nœuds 
   dont d'autres nœuds d'élément et de texte.

Ainsi, par défaut, le processeur XSLT qui atteint un élément visite tous les  éléments et les nœuds de texte qu'il contient. 
   Un nœud de texte rencontré est simplement recopié, par défaut, alors que pour les éléments, 
   on visite également leur contenu. C'est ce qui explique que, par défaut, s'il n'y a aucune règle dans le document XSLT, 
   un document XML est recopié sans les balises.

D'autres nœuds existent comme les nœuds de commentaire, les nœuds 
   d'instructions de traitement et les nœuds d'espaces de noms,   
   mais ils sont moins importants que le nœud du document (nœud-racine), 
   les nœuds d'attribut, les nœuds de texte ou les nœuds d'élément. Dans le modèle d'arbre, les nœuds d'espaces de noms et
   les nœuds d'attribut sont attachés à l'élément, mais ne sont pas
   un enfant (« child »).

Nous avons déjà vu que « * » et « @* » permettaient de sélectionner les sous-éléments et attributs d'un élément. On peut sélectionner 
   les nœuds de texte avec la fonction XPath « text() ». Notons aussi que l'élément « <xsl:apply-templates/> » signifie que les modèles s'appliquent à tous les nœuds contenus dans le nœud courant. Les règles
   par défaut qui s'appliquent en XSLT sont :
```xml
<xsl:template match="*|/">
      <xsl:apply-templates/>
    </xsl:template>
   
    <xsl:template match="text()|@*">
      <xsl:value-of select="."/>
    </xsl:template>
   
    <xsl:template match="processing-instruction()|comment()" />
```

La première règle (ou instruction) indique que si on rencontre un élément ou la racine du document, on applique tout simplement les autres instructions aux noeuds que l'on y trouve. La seconde règle indique que si on trouve un noeud de texte ou un attribut, on retourne tout simplement la valeur textuelle du noeud. Finalement, la dernière règle indique que si on trouve un commentaire ou une instruction de traitement, on n'en traite pas le contenu.
Un processeur XSLT représente un document XML comme un arbre et tente de le visiter de la racine vers les feuilles. Lorsqu'il rencontre un modèle pour un nœud, il l'applique et ne poursuit pas automatiquement la visite des nœuds qui y sont contenus, à moins de rencontrer un élément « xsl:apply-templates ».

Par défaut, un traitement XSLT va extraire le contenu textuel du document XML provenant des noeuds de texte et des attributs. Le produit final sera un aggrégat de tout le contenu textuel ainsi extrait.

Récapitulons. Le XSLT fait ce qu'on lui dit de faire, rien de plus, rien de moins. Il commence avec la racine du document et applique les règles. Il est muni de règles de base lui indiquant quoi faire avec des éléments, des attributs, etc. Vous pouvez ajouter de nouvelles règles ou remplacer les règles de base.

Si vous utilisez la règle suivant, indiquant au XSLT de ne rien faire à partir de la racine, alors il ne fera rien (rien ne sera généré).

```xml
<xsl:template match="/">
    </xsl:template>
```

Le XSLT applique de préférence vos règles plutôt que celles par défaut. Ainsi donc, si vous ajoutez la règle suivante...

```xml
<xsl:template match="*">
      <xsl:value-of select="."/>
</xsl:template>
```

... alors elle s'appliquera quand l'élément-racine (ou tout autre élément) de votre document sera visité. Comme cette règle n'indique pas de visiter les sous-éléments (par l'instruction apply-templates), ceux-ci ne seront pas visités. Dans un tel cas, tout ce qui sera produit sera la valeur textuelle de l'élément-racine. Le traitement XSLT s'arrêtera alors.

Cela illustre que le XSLT ne génère pas nécessairement du XML valide. Certains moteurs XSLT s'attendent à obtenir du XML ou du HTML (si l'élément-racine est nommé en conséquence) et peuvent générer une erreur dans le cas contraire. Certains moteurs peuvent même modifier le résultat de manière à ce qu'il s'agisse de XML ou du HTML valide. D'autres processeurs vont refuser de produire autre chose que du XML ou du HTML, à moins d'indication contraire.

Les règles s'appliquent selon un ordre de priorité. Vos règles s'appliquent avant celles par défaut. Les règles spécifiques (nommant un élément XML par son nom) s'appliquent avant les règles génériques (par exemple, celles spécifiant le type de noeud comme « * »). Une disjonction ( « | ») est traitée comme un ensemble de règles distinctes. Si deux règles ont une priorité égale, le moteur XSLT peut choisir arbitrairement un des deux règles ou générer une erreur.

## Un exemple

Dans cette section, nous illustrons le fonctionnement du XSLT avec un exemple pratique montrant l'application des règles de transformation sur un document XML simple.

Pour illustrer le fonctionnement du XSLT, prenons un example. Soit ce document XML:

```xml
<racine>
       <element>
           <souselement>
           </souselement>
       </element>
       <element2>
            <souselement2>
            </souselement2>
        </element2>
</racine>
```

Soit ce document XSLT:
```xml
<xsl:stylesheet version="1.0"
      xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:template match="element">
            Transformation 1
        </xsl:template>
        <xsl:template match="souselement">
            Transformation 2
        </xsl:template>
        <xsl:template match="souselement2">
            transformation3
        </xsl:template>
    </xsl:stylesheet>
```
<p>
 Par souci de simplicité, nous allons ignorer les noeuds de texte de cet exemple. Il n'y a donc que des éléments.
</p>
<ol>
 <li>
Le processeur débute au noeud racine. La règle par défaut s'applique et on l'instruit (avec apply-templates) de traiter tous les noeuds qu'il contient en séquence.

Le processeur trouve alors l'élément nommé « racine ». La règle par défaut s'applique encore et le processeur visite simplement les noeuds contenus. Dans ce cas, il y en a deux (deux éléments).

1. Le processeur va alors traiter l'élément nommé « element ». Dans ce cas, la règle que nous avons introduite dans notre document XSLT s'applique et le processeur XSLT émet la chaîne de caractères « Transformation 1 ». Notez que l'élément nommé souselement ne sera pas traité.

2. Le processeur traite alors l'élément nommé « element2 ». La règle par défaut s'applique. Il visite donc l'élément «souselement2». La règle que nous avons introduite s'applique et le processeur émet «transformation3 ».

Le résultat produit sera donc la chaîne de caractères «Transformation 1 transformation3 ».

Vous pouvez mettre cet exemple en marche dans votre navigateur.




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



Notez que nous avons ajouté une instruction «output» spécifiant un contenu textuel. Sans cette instruction, plusieurs processeurs XSLT seront confus par le résultat généré (celui-ci n'étant pas du XML) et ils peuvent générer une erreur. Vous noterez peut-être aussi que votre navigateur met le résultat textuel dans un document HTML. C'est un cas particulier où le processeur prend sur lui d'imposer un format. Dans le cas d'un navigateur web, il est justifiable d'exiger que le document produit soit du XML ou du HTML.

Assurez-vous de bien comprendre cet exemple avant de continuer. Vous devez avoir une bonne représentation mentale de la manière dont fonctionne un processeur XSLT.
