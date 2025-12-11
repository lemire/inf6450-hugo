---
title: "HTML 5"
weight: 30
---
<h1 class="">
 HTML 5
</h1>
<div class="">
 <p>
  Un document HTML 5 peut
        prendre la forme d'un document XML ou d'un document HTML. La déclaration doctype n'est utilisée que
        dans le cas où le document n'est pas un document XML et a été grandement simplifiée : il suffit d'inclure
        la ligne &lt;!DOCTYPE html&gt; au début du fichier. Voici un exemple de document HTML 5 :
 </p>
 <pre style=" white-space: pre-wrap;    "><span style="color:#004a43; ">&lt;!doctype html&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">html</span><span style="color:#a65700; ">&gt;</span>
  <span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">head</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">meta</span><span style="color:#274796; "> </span><span style="color:#074726; ">charset</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"UTF-8"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">title</span><span style="color:#a65700; ">&gt;</span>Ceci est un exemple<span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">title</span><span style="color:#a65700; ">&gt;</span>
  <span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">head</span><span style="color:#a65700; ">&gt;</span>
  <span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">body</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">p</span><span style="color:#a65700; ">&gt;</span>Voici un paragraphe<span style="color:#008c00; ">.</span><span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">p</span><span style="color:#a65700; ">&gt;</span>
  <span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">html</span><span style="color:#a65700; ">&gt;</span>
</pre>
 <p>
  Un document HTML 5 en XML ne nécessite pas de déclaration doctype :
 </p>
 <pre>&lt;?xml version="<span style="color:#008c00; ">1.0</span>" encoding="UTF-<span style="color:#008c00; ">8</span>"?&gt;
<span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">html</span><span style="color:#274796; "> xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"http://www.w3.org/1999/xhtml"</span><span style="color:#a65700; ">&gt;</span>
  <span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">head</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">title</span><span style="color:#a65700; ">&gt;</span>Ceci est un exemple<span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">title</span><span style="color:#a65700; ">&gt;</span>
  <span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">head</span><span style="color:#a65700; ">&gt;</span>
  <span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">body</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">p</span><span style="color:#a65700; ">&gt;</span>Voici un paragraphe<span style="color:#008c00; ">.</span><span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">p</span><span style="color:#a65700; ">&gt;</span>
  <span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">html</span><span style="color:#a65700; ">&gt;</span>
</pre>
 <p>
  En HTML 5, on n'utilise plus les éléments acronym et plusieurs autres
        éléments moins utiles (basefont, big, center, s, strike, tt, u, frame, frameset, noframe, applet, isindex, dir).
        Plusieurs nouveaux éléments ont été ajoutés notamment les éléments section et article. Ces éléments permettent d'organiser le contenu de manière logique.
 </p>
 <ul>
  <li>
   Élément section: permet de regrouper du contenu dans une section contenant peut-être plusieurs paragraphes ou articles ayant un thème commun.
  </li>
  <li>
   Élément article: permet d'indiquer que le contenu est un article. Un article peut disposer d'une entête (header) comprenant un titre.
  </li>
  <li>
   Élément aside: permet d'ajouter une note optionnelle au contenu.
  </li>
  <li>
   Élément footer: permet d'indiquer une section dédiée aux métadonnées du document. Chaque section peut avoir son élément footer.
  </li>
 </ul>
 <p>
  Voici un exemple de HTML 5 valable:
 </p>
 <pre>&lt;?xml version="<span style="color:#008c00; ">1.0</span>" encoding="UTF-<span style="color:#008c00; ">8</span>"?&gt;
<span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">html</span><span style="color:#274796; "> xmlns</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"http://www.w3.org/1999/xhtml"</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">title</span><span style="color:#a65700; ">&gt;</span>Ceci est un exemple<span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">title</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">head</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">h1</span><span style="color:#a65700; ">&gt;</span>Un article sur le XML<span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">h1</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">section</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">article</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">header</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">h2</span><span style="color:#a65700; ">&gt;</span>La magie du XML<span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">h2</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">p</span><span style="color:#a65700; ">&gt;</span>J'aime le XML<span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">p</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">header</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">p</span><span style="color:#a65700; ">&gt;</span>Nous aimons tous le XML<span style="color:#008c00; ">...</span><span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">p</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">article</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">section</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">footer</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">h3</span><span style="color:#a65700; ">&gt;</span>Une annexe<span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">h3</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">p</span><span style="color:#a65700; ">&gt;</span>Cet article a été écrit par Daniel<span style="color:#008c00; ">...</span><span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">p</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">footer</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">aside</span><span style="color:#a65700; ">&gt;</span>
En passant, ce n'est pas un vrai article<span style="color:#008c00; ">...</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">aside</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">body</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">html</span><span style="color:#a65700; ">&gt;</span>
</pre>
 <p>
  On peut facilement créer des indicateurs de progression:
 </p>
 <meter max="10" min="0" value="2">
  2 sur 10
 </meter>
 <br/>
 <meter value="0.66">
  66%
 </meter>
 <pre><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">meter</span><span style="color:#274796; "> </span><span style="color:#074726; ">value</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"2"</span><span style="color:#274796; "> min</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"0"</span><span style="color:#274796; "> max</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"10"</span><span style="color:#a65700; ">&gt;</span><span style="color:#008c00; ">2</span> sur <span style="color:#008c00; ">10</span><span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">meter</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">br /</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">meter</span><span style="color:#274796; "> </span><span style="color:#074726; ">value</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"0.66"</span><span style="color:#a65700; ">&gt;</span><span style="color:#008c00; ">66</span>%<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">meter</span><span style="color:#a65700; ">&gt;</span>
</pre>
 <p>
  On peut
        aussi ajouter une figure à un document avec une légende:
 </p>
 <figure>
  <img src="https://www.teluq.ca/siteweb/univ/fichiers/images/profs/dlemire.jpg"/>
  <legend>
   Photo du professeur
  </legend>
 </figure>
 <pre><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">figure</span><span style="color:#a65700; ">&gt;</span>
 <span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">img</span><span style="color:#274796; "> </span><span style="color:#074726; ">src</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"http://lemire.me/fr/images/JPG/profile2011B_152.jpg"</span><span style="color:#274796; "> </span><span style="color:#a65700; ">/&gt;</span>
 <span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">legend</span><span style="color:#a65700; ">&gt;</span>Photo du professeur<span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">legend</span><span style="color:#a65700; ">&gt;</span>
<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">figure</span><span style="color:#a65700; ">&gt;</span>
</pre>
 <p>
  On peut aussi créer rapidement des formulaires en ligne:
 </p>
 <form id="inscription" onsubmit="return false;">
  <h1>
   Inscription au cours de XML
  </h1>
  <fieldset>
   <legend>
    Information personnelle
   </legend>
   <label>
    Nom
    <input autofocus="" id="nom" name="nom" placeholder="Votre nom" required="" type="text"/>
   </label>
   <br/>
   <label>
    Date de naissance
    <input id="courriel" name="ddn" required="" type="date"/>
   </label>
   <br/>
   <label>
    Courriel
    <input id="courriel" name="courriel" placeholder="lemire@jo.com" required="" type="email"/>
   </label>
   <br/>
   <label>
    Site personnel
    <input id="url" name="url" placeholder="http://monsite.com" type="url"/>
   </label>
   <br/>
   <label>
    Téléphone
    <input id="telephone" name="telephone" placeholder="Par ex. 450 111-4444" required="" type="tel"/>
   </label>
   <br/>
   <label>
    Nombre de cours suivis précédemment
    <input id="cours" max="50" min="0" name="cours" step="0.5" type="number" value="1"/>
   </label>
   <br/>
   <label>
    Aptitude en informatique
    <input id="aptitude" max="100" min="1" name="aptitude" type="range" value="0"/>
    <output name="output" onforminput="value=a.value">
     0
    </output>
   </label>
   <br/>
   <label>
    Adresse
    <textarea id="adresse" name="address" required="" rows="5"></textarea>
   </label>
   <br/>
   <label>
    Pays
    <input id="pays" list="nomsdepays" name="pays" required="" type="text"/>
    <datalist id="nomsdepays">
     <option label="États-Unis" value="us">
     </option>
     <option label="Canada" value="ca">
     </option>
     <option label="France" value="fr">
     </option>
    </datalist>
   </label>
  </fieldset>
  <fieldset>
   <button type="submit">
    S'inscrire
   </button>
  </fieldset>
 </form>


```html
<form id="inscription">
<h1>Inscription au cours de XML</h1>
  <fieldset> 
    <legend>Information personnelle</legend> 
        <label>Nom
        <input id="nom" name="nom" type="text" placeholder="Votre nom" required autofocus> 
		</label>
		<br /> 
    	<label>Date de naissance
        <input id="courriel" name="ddn" type="date" required>
		</label>
		<br />
        <label>Courriel 
        <input id="courriel" name="courriel" type="email" placeholder="lemire@jo.com" required>
		</label>
		<br />  
        <label>Site personnel 
        <input id="url" name="url" type="url" placeholder="http://monsite.com">
		</label>
		<br /> 
        <label>Téléphone  
        <input id="telephone" name="telephone" type="tel" placeholder="Par ex. 450 111-4444" required>
		</label>
		<br />  
		<label>Nombre de cours suivis précédemment
		<input id="cours" name="cours" type="number" min="0" max="50" step="0.5" value="1">
		</label>
		<br /> 
		<label>Aptitude en informatique 
		<input id="aptitude" name="aptitude" type="range" min="1" max="100" value="0">
		<output name="output" onforminput="value=a.value">0</output>
		</label>
		<br /> 
        <label>Adresse 
        <textarea id="adresse" name="address" rows=5 required></textarea>
		</label>
		<br />  
        <label>Pays
        <input id="pays" name="pays" list="nomsdepays" type="text" required> 
        <datalist id="nomsdepays"> 
        	<option label="États-Unis" value="us"></option> 
        	<option label="Canada" value="ca"></option> 
        	<option label="France" value="fr"></option> 
        </datalist>
		</label> 
  </fieldset> 
  <fieldset> 
	    <button type=submit>S'inscrire</button> 
  </fieldset> 
</form>
```



 <p>
  Les éléments canvas, video et audio sont aussi ajoutés : le HTML devient pleinement multimédia.
 </p>


L'exemple suivant illustre comment on peut combiner HTML et JavaScript pour dessiner.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exemple simple Canvas</title>
    <style>
        canvas { 
            border: 2px solid #333; 
            background: #f0f0f0;
        }
    </style>
</head>
<body>

<h2>Exemple basique de Canvas</h2>
<canvas id="monCanvas" width="400" height="300"></canvas>

<script>
// 1. On récupère l'élément canvas
const canvas = document.getElementById('monCanvas');
const ctx = canvas.getContext('2d'); // contexte 2d (le plus courant)

// 2. Carré rouge
ctx.fillStyle = 'red';
ctx.fillRect(50, 50, 100, 100); // x, y, largeur, hauteur

// 3. Cercle bleu
ctx.fillStyle = 'blue';
ctx.beginPath();
ctx.arc(280, 100, 50, 0, Math.PI * 2); // centre x, centre y, rayon, angle départ, angle fin
ctx.fill();

// 4. Ligne verte
ctx.strokeStyle = 'green';
ctx.lineWidth = 8;
ctx.beginPath();
ctx.moveTo(50, 200);   // point de départ
ctx.lineTo(350, 200);  // point d'arrivée
ctx.stroke();

// 5. Texte
ctx.font = '30px Arial';
ctx.fillStyle = 'black';
ctx.fillText('Hello Canvas !', 90, 260);
</script>

</body>
</html>
```



<canvas id="monCanvas" width="400" height="300"></canvas>

<script>
// 1. On récupère l'élément canvas
const canvas = document.getElementById('monCanvas');
const ctx = canvas.getContext('2d'); // contexte 2d (le plus courant)

// 2. Carré rouge
ctx.fillStyle = 'red';
ctx.fillRect(50, 50, 100, 100); // x, y, largeur, hauteur

// 3. Cercle bleu
ctx.fillStyle = 'blue';
ctx.beginPath();
ctx.arc(280, 100, 50, 0, Math.PI * 2); // centre x, centre y, rayon, angle départ, angle fin
ctx.fill();

// 4. Ligne verte
ctx.strokeStyle = 'green';
ctx.lineWidth = 8;
ctx.beginPath();
ctx.moveTo(50, 200);   // point de départ
ctx.lineTo(350, 200);  // point d'arrivée
ctx.stroke();

// 5. Texte
ctx.font = '30px Arial';
ctx.fillStyle = 'black';
ctx.fillText('Hello Canvas !', 90, 260);
</script>

 <p>
  Pour en savoir plus, consulter le guide du
  <a href="https://developer.mozilla.org/fr/docs/Web/Guide/HTML/HTML5">
   HTML 5 chez Mozilla
  </a>
  .
 </p>
</div>
<hr/>
