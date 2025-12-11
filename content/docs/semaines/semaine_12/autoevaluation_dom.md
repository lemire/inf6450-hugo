---
title: "Autoévaluation DOM"
weight: 30
---
<h1>
 Autoévaluation DOM
</h1>
<p>
 Le bouton « Vérifier ma réponse » donne accès à un script qui, en
    plus de vous permettre
    de vérifier vos réponses, fournit une courte explication.
    Si tous les commentaires sont en
 <span style="color:blue">
  bleu
 </span>
 , c'est
    que vous avez la bonne réponse;
    sinon, lisez les commentaires en
 <span style="color:red">
  rouge
 </span>
 pour
    comprendre votre erreur.
    Puis, essayez de nouveau en cliquant sur le bouton
    « Recommencer ».
</p>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 1
  </b>
  .
        Si j'ai une application DOM et que je charge 100 fichiers XML faisant un
        Mo chacun, je m'attends
        que mon programme utilise au moins 100 Mo.
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140356078637968">
  <ol>
   <li>
    <input name="idp140356078637968" onclick="javascript:var Click_MenuId='idp140356078638896true';var formid='idp140356078637968'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140356078638896true"/>
    Vrai
    <span class="feedback" id="idp140356078638896true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!)
                    Effectivement.
    </span>
   </li>
   <li>
    <input name="idp140356078637968" onclick="javascript:var Click_MenuId='idp140356078640176false';var formid='idp140356078637968'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140356078640176false"/>
    Faux
    <span class="feedback" id="idp140356078640176false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) L'affirmation est
                    correcte : DOM utilise beaucoup de mémoire.
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 2
  </b>
  .
        Un arbre DOM est constitué d'éléments contenant d'autres éléments.
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140356078641728">
  <ol>
   <li>
    <input name="idp140356078641728" onclick="javascript:var Click_MenuId='idp140356078642640false';var formid='idp140356078641728'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140356078642640false"/>
    Vrai
    <span class="feedback" id="idp140356078642640false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) L'affirmation est
                    techniquement incorrecte. C'est un arbre de nœuds et les
                    nœuds ne sont pas tous des éléments. Par exemple, une
                    instruction de traitement ou
                    une déclaration de type de document est un nœud.
    </span>
   </li>
   <li>
    <input name="idp140356078641728" onclick="javascript:var Click_MenuId='idp140356078644352true';var formid='idp140356078641728'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140356078644352true"/>
    Faux
    <span class="feedback" id="idp140356078644352true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement. XML
                    est une structure d'arbre en éléments, mais DOM utilise
                    une structure plus générale d'arbre de nœuds, où les nœuds
                    n'ont pas à être des éléments.
                    En général, par contre, seuls les éléments (et le document)
                    peuvent avoir des descendants.
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
        Dans un arbre DOM, que trouve-t-on à la racine?
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140356078645824">
  <ol>
   <li>
    <input name="idp140356078645824" onclick="javascript:var Click_MenuId='idp140356078647312false';var formid='idp140356078645824'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140356078647312false"/>
    L'élément-racine
                du document XML.
    <span class="feedback" id="idp140356078647312false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Si c'était
                    le cas, on ne pourrait avoir accès à la déclaration de type
                    de document, par exemple.
    </span>
   </li>
   <li>
    <input name="idp140356078645824" onclick="javascript:var Click_MenuId='idp140356078648816false';var formid='idp140356078645824'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140356078648816false"/>
    Il
                n'y a pas de racine unique.
    <span class="feedback" id="idp140356078648816false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Ce ne serait
                    alors pas un arbre.
    </span>
   </li>
   <li>
    <input name="idp140356078645824" onclick="javascript:var Click_MenuId='idp140356078650096true';var formid='idp140356078645824'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140356078650096true"/>
    Le
                document lui-même contenant, parmi d'autres choses,
                l'élément-racine du document XML.
    <span class="feedback" id="idp140356078650096true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement.
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 4
  </b>
  .
        Parmi les types de nœuds DOM suivants, quels sont ceux qui ne peuvent
        pas avoir d'enfants?
 </div>
 <p style="width:90%;">
  Choisissez toutes les réponses qui s'appliquent, puis
        appuyez sur le bouton « Vérifier ma réponse ».
 </p>
 <form id="idp140356078651696">
  <ol>
   <li>
    <input name="idp140356078651696" type="checkbox" value="idp140356078652464true"/>
    DocumentType (modèle pour une
                déclaration de type de document)
    <span class="feedback" id="idp140356078652464true" style="display: none;font-weight:bold;">
     <br/>
     La déclaration de type de document n'a
                    pas d'enfants; elle ne peut pas contenir, par exemple, des
                    éléments.
    </span>
   </li>
   <li>
    <input name="idp140356078651696" type="checkbox" value="idp140356078654112false"/>
    Element (modèle pour un
                élément)
    <span class="feedback" id="idp140356078654112false" style="display: none;font-weight:bold;">
     <br/>
     Un élément peut avoir des
                    enfants.
    </span>
   </li>
   <li>
    <input name="idp140356078651696" type="checkbox" value="idp140356078655392true"/>
    Comment (modèle pour un
                commentaire)
    <span class="feedback" id="idp140356078655392true" style="display: none;font-weight:bold;">
     <br/>
     Les commentaires ne peuvent pas avoir
                    d'enfants.
    </span>
   </li>
   <li>
    <input name="idp140356078651696" type="checkbox" value="idp140356078656672false"/>
    Document (modèle pour le document
                lui-même)
    <span class="feedback" id="idp140356078656672false" style="display: none;font-weight:bold;">
     <br/>
     Le document peut avoir des
                    enfants.
    </span>
   </li>
   <li>
    <input name="idp140356078651696" type="checkbox" value="idp140356078657952true"/>
    Text (modèle pour du texte contenu
                dans un élément)
    <span class="feedback" id="idp140356078657952true" style="display: none;font-weight:bold;">
     <br/>
     Du texte ne peut pas avoir
                    d'enfants.
    </span>
   </li>
  </ol>
  <input class="button" onclick="javascript:var formid = 'idp140356078651696';var myform = document.getElementById(formid);var inputs = myform.getElementsByTagName('input'); for(inputscount = 0; inputscount &lt; inputs.length; ++inputscount){var spanel = document.getElementById(inputs[inputscount].value);if(inputs[inputscount].checked) {if(/true/.test(inputs[inputscount].value)) { spanel.style.color = &quot;blue&quot;;} else {spanel.style.color = &quot;red&quot;;}} else {if(/true/.test(inputs[inputscount].value)) { spanel.style.color = &quot;red&quot;;} else { spanel.style.color = &quot;blue&quot;;}}spanel.style.display=&quot;&quot;;}" type="button" value="Vérifier ma réponse"/>
  <input class="button" onclick="javascript:var formid = 'idp140356078651696';var myform = document.getElementById(formid);myform.reset();var inputs = myform.getElementsByTagName('input');for(inputscount = 0; inputscount &lt; inputs.length; ++inputscount){var spanel = document.getElementById(inputs[inputscount].value);spanel.style.display=&quot;none&quot;;}" type="button" value="Recommencer"/>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 5
  </b>
  .
        Un arbre DOM donne accès à tout le contenu en information pertinente
        d'un document XML.
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140356078660176">
  <ol>
   <li>
    <input name="idp140356078660176" onclick="javascript:var Click_MenuId='idp140356078661008true';var formid='idp140356078660176'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140356078661008true"/>
    Vrai
    <span class="feedback" id="idp140356078661008true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) DOM est
                    complet : vous pouvez obtenir tout le contenu en
                    information du document XML.
                    Dans un logiciel normal, il ne devrait jamais être
                    nécessaire d'utiliser autre chose que DOM
                    pour extraire l'information contenue dans un document XML.
    </span>
   </li>
   <li>
    <input name="idp140356078660176" onclick="javascript:var Click_MenuId='idp140356078662608false';var formid='idp140356078660176'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140356078662608false"/>
    Faux
    <span class="feedback" id="idp140356078662608false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) L'affirmation
                    était correcte.
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 6
  </b>
  .
        Un arbre DOM correspond à un document XML unique.
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140356078664016">
  <ol>
   <li>
    <input name="idp140356078664016" onclick="javascript:var Click_MenuId='idp140356078664784false';var formid='idp140356078664016'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140356078664784false"/>
    Vrai
    <span class="feedback" id="idp140356078664784false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Il peut y avoir
                    plusieurs documents disposés différemment, mais contenant la
                    même information.
    </span>
   </li>
   <li>
    <input name="idp140356078664016" onclick="javascript:var Click_MenuId='idp140356078666272true';var formid='idp140356078664016'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140356078666272true"/>
    Faux
    <span class="feedback" id="idp140356078666272true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) C'est juste. Deux
                    librairies DOM pourraient, avec le même arbre, générer des
                    documents XML différents.
    </span>
   </li>
  </ol>
 </form>
</div>
