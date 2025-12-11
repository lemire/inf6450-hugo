---
title: "Autoévaluation"
weight: 70
---
<h1 class="">
 Autoévaluation
</h1>
<div class="">
 <p>
  Le bouton « Vérifier ma réponse » donne accès à un script qui, en plus de vous permettre 
	de vérifier vos réponses, fournit une courte explication. 
	Si tous les commentaires sont en
  <span style="color:blue">
   bleu
  </span>
  , c'est que vous avez la bonne réponse; 
	sinon, lisez les commentaires en
  <span style="color:red">
   rouge
  </span>
  pour comprendre votre erreur. 
	Puis, essayez de nouveau en cliquant sur le bouton « Recommencer ».
 </p>
 <div style="margin-left:1cm">
  <div style="background-color:#E0EAF0">
   <b>
    Question 1
   </b>
   .
		Parmi les documents suivants, lesquels sont du XHTML valable?
  </div>
  <p style="width:90%;">
   Choisissez toutes les réponses qui s'appliquent, puis appuyez sur le bouton « Vérifier ma réponse ».
  </p>
  <form id="idp140549857061152">
   <ol>
    <li>
     <input name="idp140549857061152" type="checkbox" value="idp140549857061920false"/>
     <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
      &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
 &lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"&gt;
 &lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
 &lt;head&gt;
 &lt;title&gt;Un titre&lt;/title&gt;
 &lt;/head&gt;
 &lt;body&gt;
 &lt;p&gt;Voici mon document
 &lt;/body&gt;
 &lt;/html&gt;
     </p>
     <span class="feedback" id="idp140549857061920false" style="display: none;font-weight:bold;">
      <br/>
      Non. La balise « p » doit être fermée.
     </span>
    </li>
    <li>
     <input name="idp140549857061152" type="checkbox" value="idp140549857064080false"/>
     <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
      &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
 &lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"&gt;
 &lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
 &lt;head&gt;
 &lt;title&gt;Un titre&lt;/title&gt;
 &lt;/head&gt;
 &lt;body&gt;
 &lt;P&gt;Voici mon document&lt;/P&gt;
 &lt;/body&gt;
 &lt;/html&gt;
     </p>
     <span class="feedback" id="idp140549857064080false" style="display: none;font-weight:bold;">
      <br/>
      Non. La balise « P » n'existe pas en XHTML : le XML tient compte 
de la casse et l'élément « p » n'est pas la même chose que l'élément « P ».
     </span>
    </li>
    <li>
     <input name="idp140549857061152" type="checkbox" value="idp140549857066656true"/>
     <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
      &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
 &lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd" [
 &lt;!ENTITY texte  "&lt;p&gt;Note légale: vous pouvez faire ce que vous voulez&lt;/p&gt;
 &lt;p&gt;Copyright 2004&lt;/p&gt;"&gt;
 ]&gt;
 &lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
 &lt;head&gt;
 &lt;title&gt;Un titre&lt;/title&gt;
 &lt;/head&gt;
 &lt;body&gt;
 &amp;texte;
 &lt;/body&gt;
 &lt;/html&gt;
     </p>
     <span class="feedback" id="idp140549857066656true" style="display: none;font-weight:bold;">
      <br/>
      Oui. L'entité contient deux éléments bien formés et le résultat est du XHTML valable.
     </span>
    </li>
    <li>
     <input name="idp140549857061152" type="checkbox" value="idp140549857069264false"/>
     <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
      &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
 &lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd" [
 &lt;!ENTITY texte  "Voici mon document&lt;/p&gt;"&gt;
 ]&gt;
 &lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
 &lt;head&gt;
 &lt;title&gt;Un titre&lt;/title&gt;
 &lt;/head&gt;
 &lt;body&gt;
 &lt;p&gt;&amp;texte;
 &lt;/body&gt;
 &lt;/html&gt;
     </p>
     <span class="feedback" id="idp140549857069264false" style="display: none;font-weight:bold;">
      <br/>
      Non. Une entité doit être du XML bien formé et si une entité contient des balises, 
il doit s'agir d'éléments avec balise ouvrante et balise fermante.
     </span>
    </li>
    <li>
     <input name="idp140549857061152" type="checkbox" value="idp140549854439456false"/>
     <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
      &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
 &lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd" &gt;
 &lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
 &lt;head&gt;
 &lt;title&gt;Un titre&lt;/title&gt;
 &lt;/head&gt;
 &lt;body&gt;
 &lt;img src=http://www.uqam.ca/img/logo/logo.jpg 
 alt="logo de l'UQÀM" /&gt;
 &lt;/body&gt;
 &lt;/html&gt;
     </p>
     <span class="feedback" id="idp140549854439456false" style="display: none;font-weight:bold;">
      <br/>
      Non, les attributs doivent être entre guillemets comme ceci :
      <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
       &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
 &lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd" &gt;
 &lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
 &lt;head&gt;
 &lt;title&gt;Un titre&lt;/title&gt;
 &lt;/head&gt;
 &lt;body&gt;
 &lt;img src="http://www.uqam.ca/img/logo/logo.jpg" 
 alt="logo de l'UQÀM" /&gt;
 &lt;/body&gt;
 &lt;/html&gt;
      </p>
     </span>
    </li>
   </ol>
   <input class="button" onclick="javascript:var formid = 'idp140549857061152';var myform = document.getElementById(formid);var inputs = myform.getElementsByTagName('input'); for(inputscount = 0; inputscount &lt; inputs.length; ++inputscount){var spanel = document.getElementById(inputs[inputscount].value);if(inputs[inputscount].checked) {if(/true/.test(inputs[inputscount].value)) { spanel.style.color = &quot;blue&quot;;} else {spanel.style.color = &quot;red&quot;;}} else {if(/true/.test(inputs[inputscount].value)) { spanel.style.color = &quot;red&quot;;} else { spanel.style.color = &quot;blue&quot;;}}spanel.style.display=&quot;&quot;;}" type="button" value="Vérifier ma réponse"/>
   <input class="button" onclick="javascript:var formid = 'idp140549857061152';var myform = document.getElementById(formid);myform.reset();var inputs = myform.getElementsByTagName('input');for(inputscount = 0; inputscount &lt; inputs.length; ++inputscount){var spanel = document.getElementById(inputs[inputscount].value);spanel.style.display=&quot;none&quot;;}" type="button" value="Recommencer"/>
  </form>
 </div>
 <hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
 <div style="margin-left:1cm">
  <div style="background-color:#E0EAF0">
   <b>
    Question 2
   </b>
   .
		Quel énoncé décrit le mieux le XHTML?
  </div>
  <p style="width:90%;">
   Choisissez la bonne réponse parmi les suivantes.
  </p>
  <form id="idp140549854443296">
   <ol>
    <li>
     <input name="idp140549854443296" onclick="javascript:var Click_MenuId='idp140549854444064true';var formid='idp140549854443296'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854444064true"/>
     Un document XHTML est du XML bien formé.
     <span class="feedback" id="idp140549854444064true" style="display: none;font-weight:bold;">
      <br/>
      (Réponse correcte!) 
  Effectivement. Du XHTML doit absolument être bien formé.
     </span>
    </li>
    <li>
     <input name="idp140549854443296" onclick="javascript:var Click_MenuId='idp140549854445088false';var formid='idp140549854443296'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854445088false"/>
     Le document XHTML devrait être du XML bien formé, 
  mais le navigateur va tolérer de petites erreurs comme des balises 
  croisées &lt;b&gt;&lt;i&gt;test&lt;/b&gt;&lt;/i&gt;.
     <span class="feedback" id="idp140549854445088false" style="display: none;font-weight:bold;">
      <br/>
      (Réponse incorrecte!) Justement pas : 
  on ne tolère pas de telles erreurs en XHTML, car cela rend la vie plus difficile aux machines 
  et mène à des problèmes de compatibilité entre les navigateurs.
     </span>
    </li>
    <li>
     <input name="idp140549854443296" onclick="javascript:var Click_MenuId='idp140549854446656false';var formid='idp140549854443296'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854446656false"/>
     Le XHTML est une nouvelle technologie qui exige un 
  investissement important et une conversion coûteuse des documents.
     <span class="feedback" id="idp140549854446656false" style="display: none;font-weight:bold;">
      <br/>
      (Réponse incorrecte!) 
  Non. Le XHTML est très similaire au HTML.
     </span>
    </li>
   </ol>
  </form>
 </div>
 <hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
 <div style="margin-left:1cm">
  <div style="background-color:#E0EAF0">
   <b>
    Question 3
   </b>
   .
		Par rapport au XHTML, les énoncés suivants sont-ils justes?
  </div>
  <p style="width:90%;">
   Choisissez toutes les réponses qui s'appliquent, puis appuyez sur le bouton « Vérifier ma réponse ».
  </p>
  <form id="idp140549854448032">
   <ol>
    <li>
     <input name="idp140549854448032" type="checkbox" value="idp140549854448944true"/>
     Si mon entreprise utilise déjà beaucoup le XML, le XHTML est un 
  choix plus facile.
     <span class="feedback" id="idp140549854448944true" style="display: none;font-weight:bold;">
      <br/>
      Effectivement. On peut facilement transformer le XML en XHTML 
  et si vous connaissez les outils XML, vous pouvez les utiliser avec le XHTML.
     </span>
    </li>
    <li>
     <input name="idp140549854448032" type="checkbox" value="idp140549854450608false"/>
     Les navigateurs ne supportent pas encore XHTML.
     <span class="feedback" id="idp140549854450608false" style="display: none;font-weight:bold;">
      <br/>
      C'est faux. La plupart des navigateurs supportent bien le XHTML, mais tous ne supportent pas 
  l'ensemble des normes XML.
     </span>
    </li>
    <li>
     <input name="idp140549854448032" type="checkbox" value="idp140549854451872true"/>
     Le XHTML est une technologie favorisant la pérennité des 
  documents.
     <span class="feedback" id="idp140549854451872true" style="display: none;font-weight:bold;">
      <br/>
      Effectivement. Comme le XHTML suit une DTD fixe, 
  il sera possible dans le futur de bien interpréter les documents XHTML, alors que le HTML que 
  l'on trouve sur le web est souvent désuet après quelques mises à jour des navigateurs.
     </span>
    </li>
   </ol>
   <input class="button" onclick="javascript:var formid = 'idp140549854448032';var myform = document.getElementById(formid);var inputs = myform.getElementsByTagName('input'); for(inputscount = 0; inputscount &lt; inputs.length; ++inputscount){var spanel = document.getElementById(inputs[inputscount].value);if(inputs[inputscount].checked) {if(/true/.test(inputs[inputscount].value)) { spanel.style.color = &quot;blue&quot;;} else {spanel.style.color = &quot;red&quot;;}} else {if(/true/.test(inputs[inputscount].value)) { spanel.style.color = &quot;red&quot;;} else { spanel.style.color = &quot;blue&quot;;}}spanel.style.display=&quot;&quot;;}" type="button" value="Vérifier ma réponse"/>
   <input class="button" onclick="javascript:var formid = 'idp140549854448032';var myform = document.getElementById(formid);myform.reset();var inputs = myform.getElementsByTagName('input');for(inputscount = 0; inputscount &lt; inputs.length; ++inputscount){var spanel = document.getElementById(inputs[inputscount].value);spanel.style.display=&quot;none&quot;;}" type="button" value="Recommencer"/>
  </form>
 </div>
 <hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
 <div style="margin-left:1cm">
  <div style="background-color:#E0EAF0">
   <b>
    Question 4
   </b>
   .
		Quels énoncés, parmi les suivants, décrivent bien le XHTML dans le contexte du XML?
  </div>
  <p style="width:90%;">
   Choisissez toutes les réponses qui s'appliquent, puis appuyez sur le bouton « Vérifier ma réponse ».
  </p>
  <form id="idp140549854453536">
   <ol>
    <li>
     <input name="idp140549854453536" type="checkbox" value="idp140549854454496true"/>
     On peut utiliser les balises XHTML dans nos propres DTD.
     <span class="feedback" id="idp140549854454496true" style="display: none;font-weight:bold;">
      <br/>
      C'est sans problème. On peut recopier les parties des DTD XHTML et 
  les utiliser dans nos propres DTD. Cela peut être utile si un document XML doit être transformé en XHTML plus tard.
     </span>
    </li>
    <li>
     <input name="idp140549854453536" type="checkbox" value="idp140549854455872false"/>
     On peut utiliser nos propres balises en XHTML.
     <span class="feedback" id="idp140549854455872false" style="display: none;font-weight:bold;">
      <br/>
      Pas si nous utilisons les DTD officielles. Si nous écrivons vos propres DTD, il est possible 
  que notre navigateur ne reconnaisse pas le contenu comme étant du XHTML.
     </span>
    </li>
    <li>
     <input name="idp140549854453536" type="checkbox" value="idp140549854457216true"/>
     On peut définir ses propres entités en XHTML.
     <span class="feedback" id="idp140549854457216true" style="display: none;font-weight:bold;">
      <br/>
      Effectivement. Nous avons vu plus haut que les entités pouvaient être utilisées pour marquer le titre d'un 
  livre ou le nom d'un auteur, mais on peut aussi définir des entités 
  pour obtenir des caractères spéciaux, et ainsi de suite.
     </span>
    </li>
   </ol>
   <input class="button" onclick="javascript:var formid = 'idp140549854453536';var myform = document.getElementById(formid);var inputs = myform.getElementsByTagName('input'); for(inputscount = 0; inputscount &lt; inputs.length; ++inputscount){var spanel = document.getElementById(inputs[inputscount].value);if(inputs[inputscount].checked) {if(/true/.test(inputs[inputscount].value)) { spanel.style.color = &quot;blue&quot;;} else {spanel.style.color = &quot;red&quot;;}} else {if(/true/.test(inputs[inputscount].value)) { spanel.style.color = &quot;red&quot;;} else { spanel.style.color = &quot;blue&quot;;}}spanel.style.display=&quot;&quot;;}" type="button" value="Vérifier ma réponse"/>
   <input class="button" onclick="javascript:var formid = 'idp140549854453536';var myform = document.getElementById(formid);myform.reset();var inputs = myform.getElementsByTagName('input');for(inputscount = 0; inputscount &lt; inputs.length; ++inputscount){var spanel = document.getElementById(inputs[inputscount].value);spanel.style.display=&quot;none&quot;;}" type="button" value="Recommencer"/>
  </form>
 </div>
 <hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
 <div style="margin-left:1cm">
  <div style="background-color:#E0EAF0">
   <b>
    Question 5
   </b>
   .
		Parmi les énoncés suivants, lesquels s'appliquent à un document XHTML?
  </div>
  <p style="width:90%;">
   Choisissez toutes les réponses qui s'appliquent, puis appuyez sur le bouton « Vérifier ma réponse ».
  </p>
  <form id="idp140549854458928">
   <ol>
    <li>
     <input name="idp140549854458928" type="checkbox" value="idp140549854459952true"/>
     Il s'agit d'un document HTML pouvant s'afficher dans un navigateur.
     <span class="feedback" id="idp140549854459952true" style="display: none;font-weight:bold;">
      <br/>
      Oui. D'ailleurs, le texte d'introduction à HTML en est un exemple.
     </span>
    </li>
    <li>
     <input name="idp140549854458928" type="checkbox" value="idp140549854461472true"/>
     Il s'agit d'un document XML bien formé.
     <span class="feedback" id="idp140549854461472true" style="display: none;font-weight:bold;">
      <br/>
      Effectivement.
     </span>
    </li>
    <li>
     <input name="idp140549854458928" type="checkbox" value="idp140549854462944true"/>
     Il s'agit d'un document XML valable.
     <span class="feedback" id="idp140549854462944true" style="display: none;font-weight:bold;">
      <br/>
      Effectivement, avec une déclaration de type de document utilisant un identifiant public.
     </span>
    </li>
   </ol>
   <input class="button" onclick="javascript:var formid = 'idp140549854458928';var myform = document.getElementById(formid);var inputs = myform.getElementsByTagName('input'); for(inputscount = 0; inputscount &lt; inputs.length; ++inputscount){var spanel = document.getElementById(inputs[inputscount].value);if(inputs[inputscount].checked) {if(/true/.test(inputs[inputscount].value)) { spanel.style.color = &quot;blue&quot;;} else {spanel.style.color = &quot;red&quot;;}} else {if(/true/.test(inputs[inputscount].value)) { spanel.style.color = &quot;red&quot;;} else { spanel.style.color = &quot;blue&quot;;}}spanel.style.display=&quot;&quot;;}" type="button" value="Vérifier ma réponse"/>
   <input class="button" onclick="javascript:var formid = 'idp140549854458928';var myform = document.getElementById(formid);myform.reset();var inputs = myform.getElementsByTagName('input');for(inputscount = 0; inputscount &lt; inputs.length; ++inputscount){var spanel = document.getElementById(inputs[inputscount].value);spanel.style.display=&quot;none&quot;;}" type="button" value="Recommencer"/>
  </form>
 </div>
 <hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
 <div style="margin-left:1cm">
  <div style="background-color:#E0EAF0">
   <b>
    Question 6
   </b>
   .
		Combien de paragraphes compte le document XHTML suivant?
   <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
    &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
 &lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"&gt;
 &lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
 &lt;head&gt;
 &lt;title&gt;Titre de mon document&lt;/title&gt;
 &lt;/head&gt;
 &lt;body&gt;
 L'enfant pleure dans la rue. Subitement, le Soleil se lève.
 
 Ah! Que la vie est belle!
 &lt;/body&gt;
 &lt;/html&gt;
   </p>
  </div>
  <p style="width:90%;">
   Choisissez la bonne réponse parmi les suivantes.
  </p>
  <form id="idp140549854464640">
   <ol>
    <li>
     <input name="idp140549854464640" onclick="javascript:var Click_MenuId='idp140549854466608true';var formid='idp140549854464640'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854466608true"/>
     1
     <span class="feedback" id="idp140549854466608true" style="display: none;font-weight:bold;">
      <br/>
      (Réponse correcte!) Oui.
     </span>
    </li>
    <li>
     <input name="idp140549854464640" onclick="javascript:var Click_MenuId='idp140549854468272false';var formid='idp140549854464640'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854468272false"/>
     2
     <span class="feedback" id="idp140549854468272false" style="display: none;font-weight:bold;">
      <br/>
      (Réponse incorrecte!) Non.
     </span>
    </li>
    <li>
     <input name="idp140549854464640" onclick="javascript:var Click_MenuId='idp140549854469648false';var formid='idp140549854464640'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854469648false"/>
     3
     <span class="feedback" id="idp140549854469648false" style="display: none;font-weight:bold;">
      <br/>
      (Réponse incorrecte!) Non.
     </span>
    </li>
    <li>
     <input name="idp140549854464640" onclick="javascript:var Click_MenuId='idp140549854471024false';var formid='idp140549854464640'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854471024false"/>
     Aucune de ces réponses
     <span class="feedback" id="idp140549854471024false" style="display: none;font-weight:bold;">
      <br/>
      (Réponse incorrecte!) Non.
     </span>
    </li>
   </ol>
  </form>
 </div>
 <hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
 <div style="margin-left:1cm">
  <div style="background-color:#E0EAF0">
   <b>
    Question 7
   </b>
   .
		Combien de paragraphes compte le document XHTML suivant?
   <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
    &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
 &lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"&gt;
 &lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
 &lt;head&gt;
 &lt;title&gt;Titre de mon document&lt;/title&gt;
 &lt;/head&gt;
 &lt;body&gt;
 &lt;p&gt;L'enfant pleure dans la rue.
 Subitement, le Soleil se lève.&lt;p&gt;
 
 &lt;p&gt;Ah! Que la vie est belle!&lt;/P&gt;
 &lt;/body&gt;
 &lt;/html&gt;
   </p>
  </div>
  <p style="width:90%;">
   Choisissez la bonne réponse parmi les suivantes.
  </p>
  <form id="idp140549854472400">
   <ol>
    <li>
     <input name="idp140549854472400" onclick="javascript:var Click_MenuId='idp140549854474368false';var formid='idp140549854472400'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854474368false"/>
     1
     <span class="feedback" id="idp140549854474368false" style="display: none;font-weight:bold;">
      <br/>
      (Réponse incorrecte!) Non. Il ne s'agit pas de XHTML valable; la balise &lt;/P&gt; est incorrecte.
     </span>
    </li>
    <li>
     <input name="idp140549854472400" onclick="javascript:var Click_MenuId='idp140549854476176false';var formid='idp140549854472400'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854476176false"/>
     2
     <span class="feedback" id="idp140549854476176false" style="display: none;font-weight:bold;">
      <br/>
      (Réponse incorrecte!) Ce serait vrai s'il s'agissait de XHTML valable.
     </span>
    </li>
    <li>
     <input name="idp140549854472400" onclick="javascript:var Click_MenuId='idp140549854477552false';var formid='idp140549854472400'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854477552false"/>
     3
     <span class="feedback" id="idp140549854477552false" style="display: none;font-weight:bold;">
      <br/>
      (Réponse incorrecte!) Non.
     </span>
    </li>
    <li>
     <input name="idp140549854472400" onclick="javascript:var Click_MenuId='idp140549854478928true';var formid='idp140549854472400'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854478928true"/>
     Aucune de ces réponses
     <span class="feedback" id="idp140549854478928true" style="display: none;font-weight:bold;">
      <br/>
      (Réponse correcte!) Effectivement. Il ne s'agit pas de XHTML valable, la seconde balise paragraphe se terminant 
      par &lt;/P&gt;. Un logiciel compatible avec XHTML comme Google Chrome ou Firefox peut très bien ne rien afficher à l'écran.
     </span>
    </li>
   </ol>
  </form>
 </div>
 <hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
 <div style="margin-left:1cm">
  <div style="background-color:#E0EAF0">
   <b>
    Question 8
   </b>
   .
		Combien de lignes horizontales sont représentées par ce document XHTML?
   <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
    &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
 &lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"&gt;
 &lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
 &lt;head&gt;
 &lt;title&gt;Titre de mon document&lt;/title&gt;
 &lt;/head&gt;
 &lt;body&gt;
 &lt;hr /&gt;
 &lt;hr&gt;&lt;/hr&gt;
 &lt;/body&gt;
 &lt;/html&gt;
   </p>
  </div>
  <p style="width:90%;">
   Choisissez la bonne réponse parmi les suivantes.
  </p>
  <form id="idp140549854481952">
   <ol>
    <li>
     <input name="idp140549854481952" onclick="javascript:var Click_MenuId='idp140549854483072false';var formid='idp140549854481952'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854483072false"/>
     1
     <span class="feedback" id="idp140549854483072false" style="display: none;font-weight:bold;">
      <br/>
      (Réponse incorrecte!) Non.
     </span>
    </li>
    <li>
     <input name="idp140549854481952" onclick="javascript:var Click_MenuId='idp140549854485440true';var formid='idp140549854481952'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854485440true"/>
     2
     <span class="feedback" id="idp140549854485440true" style="display: none;font-weight:bold;">
      <br/>
      (Réponse correcte!) Oui.
     </span>
    </li>
    <li>
     <input name="idp140549854481952" onclick="javascript:var Click_MenuId='idp140549854486720false';var formid='idp140549854481952'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854486720false"/>
     3
     <span class="feedback" id="idp140549854486720false" style="display: none;font-weight:bold;">
      <br/>
      (Réponse incorrecte!) Non.
     </span>
    </li>
    <li>
     <input name="idp140549854481952" onclick="javascript:var Click_MenuId='idp140549854488096false';var formid='idp140549854481952'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854488096false"/>
     Aucune de ces réponses
     <span class="feedback" id="idp140549854488096false" style="display: none;font-weight:bold;">
      <br/>
      (Réponse incorrecte!) Non.
     </span>
    </li>
   </ol>
  </form>
 </div>
 <hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
 <div style="margin-left:1cm">
  <div style="background-color:#E0EAF0">
   <b>
    Question 9
   </b>
   .
		Comment représente-t-on une liste numérotée en XHTML?
  </div>
  <p style="width:90%;">
   Choisissez la bonne réponse parmi les suivantes.
  </p>
  <form id="idp140549854489472">
   <ol>
    <li>
     <input name="idp140549854489472" onclick="javascript:var Click_MenuId='idp140549854490464false';var formid='idp140549854489472'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854490464false"/>
     <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
      &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
 &lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
 "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"&gt;
 &lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
 &lt;head&gt;
 &lt;title&gt;Titre de mon document&lt;/title&gt;
 &lt;/head&gt;
 &lt;body&gt;
 &lt;li&gt;
  &lt;ul&gt;élément&lt;/ul&gt;
  &lt;ul&gt;élément&lt;/ul&gt;
  &lt;/li&gt;
 &lt;/body&gt;
 &lt;/html&gt;
     </p>
     <span class="feedback" id="idp140549854490464false" style="display: none;font-weight:bold;">
      <br/>
      (Réponse incorrecte!) Non. Ce n'est pas du XHTML valable.
     </span>
    </li>
    <li>
     <input name="idp140549854489472" onclick="javascript:var Click_MenuId='idp140549854493008false';var formid='idp140549854489472'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854493008false"/>
     <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
      &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
     &lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"&gt;
     &lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
     &lt;head&gt;
     &lt;title&gt;Titre de mon document&lt;/title&gt;
     &lt;/head&gt;
     &lt;body&gt;
     &lt;li&gt;
      &lt;ol&gt;élément&lt;/ol&gt;
  &lt;ol&gt;élément&lt;/ol&gt;
  &lt;/li&gt;
     &lt;/body&gt;
     &lt;/html&gt;
     </p>
     <span class="feedback" id="idp140549854493008false" style="display: none;font-weight:bold;">
      <br/>
      (Réponse incorrecte!) Non, ce n'est pas du XHTML valable.
     </span>
    </li>
    <li>
     <input name="idp140549854489472" onclick="javascript:var Click_MenuId='idp140549854495648true';var formid='idp140549854489472'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854495648true"/>
     <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
      &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
     &lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"&gt;
     &lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
     &lt;head&gt;
     &lt;title&gt;Titre de mon document&lt;/title&gt;
     &lt;/head&gt;
     &lt;body&gt;
     &lt;ol&gt;
      &lt;li&gt;élément&lt;/li&gt;
  &lt;li&gt;élément&lt;/li&gt;
  &lt;/ol&gt;
     &lt;/body&gt;
     &lt;/html&gt;
     </p>
     <span class="feedback" id="idp140549854495648true" style="display: none;font-weight:bold;">
      <br/>
      (Réponse correcte!) Oui.
     </span>
    </li>
    <li>
     <input name="idp140549854489472" onclick="javascript:var Click_MenuId='idp140549854498160false';var formid='idp140549854489472'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140549854498160false"/>
     <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
      &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
     &lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"&gt;
     &lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
     &lt;head&gt;
     &lt;title&gt;Titre de mon document&lt;/title&gt;
     &lt;/head&gt;
     &lt;body&gt;
     &lt;ul&gt;
      &lt;li&gt;élément&lt;/li&gt;
  &lt;li&gt;élément&lt;/li&gt;
  &lt;/ul&gt;
     &lt;/body&gt;
     &lt;/html&gt;
     </p>
     <span class="feedback" id="idp140549854498160false" style="display: none;font-weight:bold;">
      <br/>
      (Réponse incorrecte!) Non. C'est bien du XHTML valable, mais la liste n'est pas numérotée.
     </span>
    </li>
   </ol>
  </form>
 </div>
 <hr/>
</div>
