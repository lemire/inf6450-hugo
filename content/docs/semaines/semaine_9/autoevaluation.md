---
title: "Autoévaluation"
weight: 110
---
<h1 class="">
 Autoévaluation
</h1>
<h2>
 Questionnaire d'autoévaluation
</h2>
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
        Parmi les suivants, quels sont les documents XSLT corrects?
 </div>
 <p style="width:90%;">
  Choisissez toutes les réponses qui s'appliquent, puis
        appuyez sur le bouton « Vérifier ma réponse ».
 </p>
 <form id="idp140293223359968">
  <ol>
   <li>
    <input name="idp140293223359968" type="checkbox" value="idp140293223360736true"/>
    <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
     &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
                    &lt;xsl:stylesheet version="1.0"
                    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
                    &lt;xsl:text&gt; &lt;/xsl:text&gt;
                    &lt;/xsl:stylesheet&gt;
    </p>
    <span class="feedback" id="idp140293223360736true" style="display: none;font-weight:bold;">
     <br/>
     Oui, c'est correct : le résultat
                    sera un document vide (contenant un espace).
    </span>
   </li>
   <li>
    <input name="idp140293223359968" type="checkbox" value="idp140293223363008false"/>
    <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
     &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
    </p>
    <span class="feedback" id="idp140293223363008false" style="display: none;font-weight:bold;">
     <br/>
     Non. Ce n'est pas un document XML
                    bien formé, car il n'y a pas d'élément-racine.
                    Un document XSLT doit être un document XML bien
                    formé.
    </span>
   </li>
   <li>
    <input name="idp140293223359968" type="checkbox" value="idp140293223365088false"/>
    <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
     &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
                    &lt;xsl:text
                    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;&lt;/xsl:text&gt;
    </p>
    <span class="feedback" id="idp140293223365088false" style="display: none;font-weight:bold;">
     <br/>
     Non. Bien qu'il s'agisse d'un
                    document XML bien formé,
                    l'élément-racine « text » n'est pas autorisé, il
                    devrait être « transform »
                    ou bien « stylesheet ».
    </span>
   </li>
   <li>
    <input name="idp140293223359968" type="checkbox" value="idp140293223367200true"/>
    <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
     &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
                    &lt;xsl:transform
                    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
                    &lt;/xsl:transform&gt;
    </p>
    <span class="feedback" id="idp140293223367200true" style="display: none;font-weight:bold;">
     <br/>
     Oui. Il s'agit d'un document XML bien
                    formé et l'élément-racine est « transform », ce
                    qui est autorisé.
    </span>
   </li>
  </ol>
  <input class="button" onclick="javascript:var formid = 'idp140293223359968';var myform = document.getElementById(formid);var inputs = myform.getElementsByTagName('input'); for(inputscount = 0; inputscount &lt; inputs.length; ++inputscount){var spanel = document.getElementById(inputs[inputscount].value);if(inputs[inputscount].checked) {if(/true/.test(inputs[inputscount].value)) { spanel.style.color = &quot;blue&quot;;} else {spanel.style.color = &quot;red&quot;;}} else {if(/true/.test(inputs[inputscount].value)) { spanel.style.color = &quot;red&quot;;} else { spanel.style.color = &quot;blue&quot;;}}spanel.style.display=&quot;&quot;;}" type="button" value="Vérifier ma réponse"/>
  <input class="button" onclick="javascript:var formid = 'idp140293223359968';var myform = document.getElementById(formid);myform.reset();var inputs = myform.getElementsByTagName('input');for(inputscount = 0; inputscount &lt; inputs.length; ++inputscount){var spanel = document.getElementById(inputs[inputscount].value);spanel.style.display=&quot;none&quot;;}" type="button" value="Recommencer"/>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 2
  </b>
  .
        Étant donné le document XML suivant...
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;source&gt;
            &lt;employe&gt;
            &lt;prenom&gt;Jean&lt;/prenom&gt;
            &lt;nom&gt;Graton&lt;/nom&gt;
            &lt;/employe&gt;
            &lt;/source&gt;
  </p>
  et le fichier XSLT suivant...
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version = '1.0'
            xmlns:xsl='http://www.w3.org/1999/XSL/Transform'&gt;
            &lt;xsl:template match="employe"&gt;
            &lt;b&gt;
            &lt;xsl:value-of select="."/&gt;
            &lt;/b&gt;
            &lt;/xsl:template&gt;
            &lt;xsl:template match="prenom"&gt;
            &lt;i&gt;
            &lt;xsl:value-of select="."/&gt;
            &lt;/i&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
  Qu'est-ce qui s'affichera à l'écran?
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223369360">
  <ol>
   <li>
    <input name="idp140293223369360" onclick="javascript:var Click_MenuId='idp140293223371216true';var formid='idp140293223369360'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223371216true"/>
    <b>
     Jean
                    Graton
    </b>
    <span class="feedback" id="idp140293223371216true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement. Le
                    modèle « employe » sera utilisé, mais pas le
                    modèle « prenom ».
                    Il y aura bel et bien un espace entre « Jean » et
                    « Graton », parce qu'il y a un
                    retour de chariot entre les éléments « prenom » et
                    « nom ». Par défaut, les espaces et les retours de
                    chariot
                    entre les éléments ne sont pas ignorés dans le document XML
                    qui est traité, mais ils le sont
                    dans le document XSLT. Un retour de chariot, en HTML ou
                    XHTML, s'affiche à l'écran comme un espace.
    </span>
   </li>
   <li>
    <input name="idp140293223369360" onclick="javascript:var Click_MenuId='idp140293223374000false';var formid='idp140293223369360'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223374000false"/>
    <b>
     JeanGraton
    </b>
    <span class="feedback" id="idp140293223374000false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
                    L'instruction « value-of » va reproduire le
                    contenu de l'élément, moins les balises,
                    mais en respectant les espaces entre les éléments. Il n'y
                    aurait pas d'espace entre les éléments
                    si le document XML avait pris le forme
                    « &lt;prenom&gt;Jean&lt;/prenom&gt;&lt;nom&gt;Graton&lt;/nom&gt; »
                    (sans espace entre les deux éléments).
    </span>
   </li>
   <li>
    <input name="idp140293223369360" onclick="javascript:var Click_MenuId='idp140293223376016false';var formid='idp140293223369360'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223376016false"/>
    <b>
     Jean
     <i>
      Graton
     </i>
    </b>
    <span class="feedback" id="idp140293223376016false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Le modèle
                    « prénom » n'est pas utilisé.
    </span>
   </li>
   <li>
    <input name="idp140293223369360" onclick="javascript:var Click_MenuId='idp140293223377808false';var formid='idp140293223369360'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223377808false"/>
    Jean
                Graton
    <span class="feedback" id="idp140293223377808false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Le modèle
                    « employe » sera utilisé; le texte sera donc en
                    caractères gras.
    </span>
   </li>
   <li>
    <input name="idp140293223369360" onclick="javascript:var Click_MenuId='idp140293223379280false';var formid='idp140293223369360'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223379280false"/>
    <b>
     Jean
    </b>
    <i>
     Graton
    </i>
    <span class="feedback" id="idp140293223379280false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Le modèle
                    « employe » sera utilisé; il n'y aura donc pas
                    d'italique.
    </span>
   </li>
   <li>
    <input name="idp140293223369360" onclick="javascript:var Click_MenuId='idp140293223381360false';var formid='idp140293223369360'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223381360false"/>
    <b>
     Jean
    </b>
    Graton
    <span class="feedback" id="idp140293223381360false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Le modèle
                    « employe » sera utilisé; on n'aura donc pas un
                    mélange de texte normal
                    et de texte en caractères gras.
    </span>
   </li>
   <li>
    <input name="idp140293223369360" onclick="javascript:var Click_MenuId='idp140293223383280false';var formid='idp140293223369360'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223383280false"/>
    Rien
    <span class="feedback" id="idp140293223383280false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Le modèle
                    « employe » sera utilisé et « value-of »
                    donnera
                    le contenu textuel sans les balises.
    </span>
   </li>
   <li>
    <input name="idp140293223369360" onclick="javascript:var Click_MenuId='idp140293223384784false';var formid='idp140293223369360'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223384784false"/>
    <b>
     <i>
      Jean
     </i>
    </b>
    <span class="feedback" id="idp140293223384784false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Le modèle
                    « employe » sera utilisé; on n'aura donc pas de
                    texte en italique.
    </span>
   </li>
   <li>
    <input name="idp140293223369360" onclick="javascript:var Click_MenuId='idp140293223386608false';var formid='idp140293223369360'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223386608false"/>
    Graton
    <span class="feedback" id="idp140293223386608false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Le modèle
                    « employe » sera utilisé; « value-of »
                    sélectionne
                    tout le texte, et non seulement « Graton ».
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
        Étant donné le document XML suivant...
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;source&gt;
            &lt;employe&gt;
            &lt;prenom&gt;Jean&lt;/prenom&gt;
            &lt;nom&gt;Graton&lt;/nom&gt;
            &lt;/employe&gt;
            &lt;/source&gt;
  </p>
  et le fichier XSLT suivant...
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version = '1.0'
            xmlns:xsl='http://www.w3.org/1999/XSL/Transform'&gt;
            &lt;xsl:template match="employe"&gt;
            &lt;b&gt;
            &lt;xsl:apply-templates select="prenom"/&gt;
            &lt;/b&gt;
            &lt;/xsl:template&gt;
            &lt;xsl:template match="prenom"&gt;
            &lt;i&gt;
            &lt;xsl:value-of select="."/&gt;
            &lt;/i&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
  Qu'est-ce qui s'affichera à l'écran?
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223388368">
  <ol>
   <li>
    <input name="idp140293223388368" onclick="javascript:var Click_MenuId='idp140293223390224false';var formid='idp140293223388368'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223390224false"/>
    <b>
     Jean
                    Graton
    </b>
    <span class="feedback" id="idp140293223390224false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223388368" onclick="javascript:var Click_MenuId='idp140293223392272false';var formid='idp140293223388368'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223392272false"/>
    <b>
     Jean
     <i>
      Graton
     </i>
    </b>
    <span class="feedback" id="idp140293223392272false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223388368" onclick="javascript:var Click_MenuId='idp140293223394032false';var formid='idp140293223388368'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223394032false"/>
    Jean
                Graton
    <span class="feedback" id="idp140293223394032false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223388368" onclick="javascript:var Click_MenuId='idp140293223395408false';var formid='idp140293223388368'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223395408false"/>
    <b>
     Jean
    </b>
    <i>
     Graton
    </i>
    <span class="feedback" id="idp140293223395408false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223388368" onclick="javascript:var Click_MenuId='idp140293223397296false';var formid='idp140293223388368'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223397296false"/>
    <b>
     Jean
    </b>
    Graton
    <span class="feedback" id="idp140293223397296false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223388368" onclick="javascript:var Click_MenuId='idp140293223398928false';var formid='idp140293223388368'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223398928false"/>
    Rien
    <span class="feedback" id="idp140293223398928false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223388368" onclick="javascript:var Click_MenuId='idp140293223400304true';var formid='idp140293223388368'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223400304true"/>
    <b>
     <i>
      Jean
     </i>
    </b>
    <span class="feedback" id="idp140293223400304true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement. Le
                    modèle « employe » est appelé et lui-même appelle
                    le modèle « prenom ».
    </span>
   </li>
   <li>
    <input name="idp140293223388368" onclick="javascript:var Click_MenuId='idp140293223402160false';var formid='idp140293223388368'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223402160false"/>
    Graton
    <span class="feedback" id="idp140293223402160false" style="display: none;font-weight:bold;">
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
   Question 4
  </b>
  .
        Étant donné le document XML suivant...
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;source&gt;
            &lt;employe&gt;
            &lt;prenom&gt;Jean&lt;/prenom&gt;
            &lt;nom&gt;Graton&lt;/nom&gt;
            &lt;/employe&gt;
            &lt;/source&gt;
  </p>
  et le fichier XSLT suivant...
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version = '1.0'
            xmlns:xsl='http://www.w3.org/1999/XSL/Transform'&gt;
            &lt;xsl:template match="prenom"&gt;
            &lt;i&gt;
            &lt;xsl:value-of select="."/&gt;
            &lt;/i&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
  Qu'est-ce qui s'affichera à l'écran?
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223403664">
  <ol>
   <li>
    <input name="idp140293223403664" onclick="javascript:var Click_MenuId='idp140293223405520false';var formid='idp140293223403664'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223405520false"/>
    <i>
     Jean
                    Graton
    </i>
    <span class="feedback" id="idp140293223405520false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223403664" onclick="javascript:var Click_MenuId='idp140293223407472false';var formid='idp140293223403664'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223407472false"/>
    <i>
     Jean
     <i>
      Graton
     </i>
    </i>
    <span class="feedback" id="idp140293223407472false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223403664" onclick="javascript:var Click_MenuId='idp140293223409232false';var formid='idp140293223403664'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223409232false"/>
    Jean
                Graton
    <span class="feedback" id="idp140293223409232false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223403664" onclick="javascript:var Click_MenuId='idp140293223410608false';var formid='idp140293223403664'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223410608false"/>
    <i>
     Jean
    </i>
    <i>
     Graton
    </i>
    <span class="feedback" id="idp140293223410608false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223403664" onclick="javascript:var Click_MenuId='idp140293223412496true';var formid='idp140293223403664'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223412496true"/>
    <i>
     Jean
    </i>
    Graton
    <span class="feedback" id="idp140293223412496true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement.
                    Comme il n'y a pas de modèle pour l'élément
                    « nom »,
                    le modèle par défaut s'applique et le contenu du texte est
                    reproduit. Par contre, le modèle « prenom » est
                    utilisé.
    </span>
   </li>
   <li>
    <input name="idp140293223403664" onclick="javascript:var Click_MenuId='idp140293223414752false';var formid='idp140293223403664'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223414752false"/>
    Rien
    <span class="feedback" id="idp140293223414752false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223403664" onclick="javascript:var Click_MenuId='idp140293223416128false';var formid='idp140293223403664'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223416128false"/>
    <b>
     <i>
      Jean
     </i>
    </b>
    <span class="feedback" id="idp140293223416128false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223403664" onclick="javascript:var Click_MenuId='idp140293223417760false';var formid='idp140293223403664'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223417760false"/>
    Graton
    <span class="feedback" id="idp140293223417760false" style="display: none;font-weight:bold;">
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
   Question 5
  </b>
  .
        Étant donné le document XML suivant...
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;budget&gt;
            &lt;item montant="50 $"&gt;
            &lt;titre&gt;lait&lt;/titre&gt;
            &lt;description&gt;Je dois acheter beaucoup de
            lait.&lt;/description&gt;
            &lt;/item&gt;
            &lt;item montant="20 $"&gt;
            &lt;titre&gt;pomme de terre&lt;/titre&gt;
            &lt;description&gt;Même si la pomme de terre est mauvaise pour la
            santé,
            je dois en acheter beaucoup.&lt;/description&gt;
            &lt;/item&gt;
            &lt;/budget&gt;
  </p>
  et le fichier XSLT suivant...
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
            &lt;xsl:template match="budget"&gt;
            &lt;ul&gt;
            &lt;xsl:apply-templates select="item" /&gt;
            &lt;/ul&gt;
            &lt;/xsl:template&gt;
            &lt;xsl:template match="item"&gt;
            &lt;li&gt;
            &lt;xsl:value-of select="titre" /&gt;
            (&lt;xsl:value-of select="@montant" /&gt;)
            &lt;/li&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
  Qu'est-ce qui s'affichera à l'écran?
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223419264">
  <ol>
   <li>
    <input name="idp140293223419264" onclick="javascript:var Click_MenuId='idp140293223421360false';var formid='idp140293223419264'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223421360false"/>
    lait (50 $) pomme de terre
    <span class="feedback" id="idp140293223421360false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Le modèle
                    « budget » s'applique; il doit y avoir création
                    d'une liste.
    </span>
   </li>
   <li>
    <input name="idp140293223419264" onclick="javascript:var Click_MenuId='idp140293223423376true';var formid='idp140293223419264'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223423376true"/>
    <ul>
     <li>
      lait
                        (50 $)
     </li>
     <li>
      pomme de terre
                        (20 $)
     </li>
    </ul>
    <span class="feedback" id="idp140293223423376true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement. Le
                    modèle « budget » s'applique et il y a création
                    d'une liste.
    </span>
   </li>
   <li>
    <input name="idp140293223419264" onclick="javascript:var Click_MenuId='idp140293223425472false';var formid='idp140293223419264'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223425472false"/>
    <ul>
     <li>
      lait
                        (50 $)Je dois acheter beaucoup de lait.
     </li>
     <li>
      pomme de terre
                        (20 $)Même si la pomme de terre est mauvaise pour la
                        santé,
                        je dois en acheter beaucoup.
     </li>
    </ul>
    <span class="feedback" id="idp140293223425472false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Les éléments
                    « item » sont traités par le modèle
                    « item »
                    qui n'inclut pas l'élément « description ».
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
        Qu'est-ce qui décrit le mieux le document XSLT suivant?
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
            &lt;xsl:template match="*"&gt;
            &lt;xsl:apply-templates select="." mode="a" /&gt;
            &lt;/xsl:template&gt;
            &lt;xsl:template match="*" mode="a"&gt;
            &lt;xsl:apply-templates select="." mode="b" /&gt;
            &lt;/xsl:template&gt;
            &lt;xsl:template match="*" mode="b"&gt;
            &lt;xsl:value-of select="." /&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223427872">
  <ol>
   <li>
    <input name="idp140293223427872" onclick="javascript:var Click_MenuId='idp140293223429568false';var formid='idp140293223427872'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223429568false"/>
    Il
                va produire la liste des balises des documents XML.
    <span class="feedback" id="idp140293223429568false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Au
                    contraire, car « value-of » enlève toutes les
                    balises.
    </span>
   </li>
   <li>
    <input name="idp140293223427872" onclick="javascript:var Click_MenuId='idp140293223431200false';var formid='idp140293223427872'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223431200false"/>
    Il
                va produire des documents vides.
    <span class="feedback" id="idp140293223431200false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Le modèle
                    « b » s'applique.
    </span>
   </li>
   <li>
    <input name="idp140293223427872" onclick="javascript:var Click_MenuId='idp140293223432320true';var formid='idp140293223427872'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223432320true"/>
    Il
                va produire des versions des documents XML, mais sans les
                balises.
    <span class="feedback" id="idp140293223432320true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Exactement. Le
                    modèle « b » s'applique, après l'application du
                    modèle par défaut et du
                    modèle « a ».
    </span>
   </li>
   <li>
    <input name="idp140293223427872" onclick="javascript:var Click_MenuId='idp140293223433776false';var formid='idp140293223427872'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223433776false"/>
    Ce
                document XSLT n'est pas valable.
    <span class="feedback" id="idp140293223433776false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Il s'agit d'un
                    document XSLT valable.
    </span>
   </li>
   <li>
    <input name="idp140293223427872" onclick="javascript:var Click_MenuId='idp140293223434992false';var formid='idp140293223427872'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223434992false"/>
    Ce
                document XSLT est valable, mais ne pourra pas s'exécuter.
    <span class="feedback" id="idp140293223434992false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) L'utilisation de
                    « mode » est effectivement dangereuse et peut
                    mener à des boucles sans fin,
                    mais ce n'est pas le cas pour ce document.
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
        Si on applique le document XSLT suivant...
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
            &lt;xsl:template match="*"&gt;
            &lt;xsl:value-of select="count(cours)"/&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
  au document XML suivant...
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1" ?&gt;
            &lt;universite&gt;
            &lt;cours&gt;&lt;nom&gt;INF 102 Introduction avancée&lt;/nom&gt;
            &lt;lien&gt;&lt;cours&gt;INF 101
            Introduction&lt;/cours&gt;&lt;/lien&gt;
            &lt;description&gt;Un cours d'introduction à l'informatique pour
            futurs
            ingénieurs.&lt;/description&gt;&lt;/cours&gt;
            &lt;cours&gt;&lt;nom&gt;INF 101 Introduction&lt;/nom&gt;
            &lt;description&gt;Un cours d'introduction à l'informatique pour les
            étudiants en éducation.&lt;/description&gt;&lt;/cours&gt;
            &lt;cours&gt;&lt;nom&gt;INF 103 Java&lt;/nom&gt;
            description&gt;Un cours d'introduction au
            Java&lt;/description&gt;&lt;/cours&gt;
            &lt;/universite&gt;
  </p>
  Quel sera le résultat?
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223436768">
  <ol>
   <li>
    <input name="idp140293223436768" onclick="javascript:var Click_MenuId='idp140293223437824false';var formid='idp140293223436768'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223437824false"/>
    Le
                chiffre « 1 ».
    <span class="feedback" id="idp140293223437824false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Le modèle compte
                    le nombre d'éléments « cours » dans
                    l'élément-racine et il y a plus d'un élément
                    « cours ».
    </span>
   </li>
   <li>
    <input name="idp140293223436768" onclick="javascript:var Click_MenuId='idp140293223440896false';var formid='idp140293223436768'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223440896false"/>
    Le
                chiffre « 2 ».
    <span class="feedback" id="idp140293223440896false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Le modèle compte
                    le nombre d'éléments « cours » dans
                    l'élément-racine et il y a plus de deux éléments
                    « cours ».
    </span>
   </li>
   <li>
    <input name="idp140293223436768" onclick="javascript:var Click_MenuId='idp140293223442320true';var formid='idp140293223436768'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223442320true"/>
    Le
                chiffre « 3 ».
    <span class="feedback" id="idp140293223442320true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Comme le modèle
                    « * » ne s'applique qu'à l'élément-racine qui
                    contient 3 éléments « cours »,
                    le résultat sera effectivement le chiffre 3.
    </span>
   </li>
   <li>
    <input name="idp140293223436768" onclick="javascript:var Click_MenuId='idp140293223443584false';var formid='idp140293223436768'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223443584false"/>
    Le
                chiffre « 4 ».
    <span class="feedback" id="idp140293223443584false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Il y a bien 4
                    éléments « cours », mais le modèle « * »
                    ne s'applique
                    qu'à l'élément-racine qui lui contient 3 éléments
                    « cours ».
    </span>
   </li>
   <li>
    <input name="idp140293223436768" onclick="javascript:var Click_MenuId='idp140293223444960false';var formid='idp140293223436768'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223444960false"/>
    Un
                document vide.
    <span class="feedback" id="idp140293223444960false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
                    L'instruction « &lt;xsl:value-of
                    select="count(cours)"/&gt; » sera exécutée
                    et le résultat doit être un nombre.
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
        Qu'est-ce qui décrit le mieux le document XSLT suivant?
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
            &lt;xsl:template match="*"&gt;
            &lt;xsl:value-of select="name(.)"/&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223446448">
  <ol>
   <li>
    <input name="idp140293223446448" onclick="javascript:var Click_MenuId='idp140293223448016false';var formid='idp140293223446448'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223448016false"/>
    Il
                donne le nom de tous les éléments dans le document.
    <span class="feedback" id="idp140293223448016false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Le modèle
                    « * » ne s'applique qu'à l'élément-racine.
    </span>
   </li>
   <li>
    <input name="idp140293223446448" onclick="javascript:var Click_MenuId='idp140293223449568false';var formid='idp140293223446448'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223449568false"/>
    Il
                donne le nom de tous les éléments et attributs dans le
                document.
    <span class="feedback" id="idp140293223449568false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Le modèle
                    « * » ne s'applique qu'à l'élément-racine et la
                    fonction « name »,
                    appliquée à un élément, ne donne que le nom de
                    l'élément.
    </span>
   </li>
   <li>
    <input name="idp140293223446448" onclick="javascript:var Click_MenuId='idp140293223451008true';var formid='idp140293223446448'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223451008true"/>
    Il
                donne le nom de l'élément-racine.
    <span class="feedback" id="idp140293223451008true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) C'est vrai. Le
                    modèle « * » ne s'applique qu'à
                    l'élément-racine.
    </span>
   </li>
   <li>
    <input name="idp140293223446448" onclick="javascript:var Click_MenuId='idp140293223452320false';var formid='idp140293223446448'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223452320false"/>
    Il
                donne le nom de l'élément-racine et de tout attribut qu'il
                pourrait avoir.
    <span class="feedback" id="idp140293223452320false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) La fonction
                    « name » appliquée à un élément ne donne que le
                    nom de l'élément.
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
        Qu'est-ce qui décrit le mieux le document XSLT suivant?
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
            &lt;xsl:template match="cours|universite"&gt;
            &lt;xsl:value-of select="name(.)"/&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223453920">
  <ol>
   <li>
    <input name="idp140293223453920" onclick="javascript:var Click_MenuId='idp140293223455488false';var formid='idp140293223453920'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223455488false"/>
    Il
                donne le contenu textuel (sans les balises) de tous les éléments
                « cours »
                ou « universite » du document XML.
    <span class="feedback" id="idp140293223455488false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Si un
                    élément « cours » ou « universite » est
                    rencontré, seul son nom s'affiche.
    </span>
   </li>
   <li>
    <input name="idp140293223453920" onclick="javascript:var Click_MenuId='idp140293223457072false';var formid='idp140293223453920'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223457072false"/>
    Il
                donne « cours » si l'élément-racine est de type
                « cours ».
    <span class="feedback" id="idp140293223457072false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!)
    </span>
   </li>
   <li>
    <input name="idp140293223453920" onclick="javascript:var Click_MenuId='idp140293223458192false';var formid='idp140293223453920'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223458192false"/>
    Il
                donne « cours » ou « universite », autant de
                fois qu'il y a d'éléments
                « cours » ou « universite » dans le
                document, et rien d'autre.
    <span class="feedback" id="idp140293223458192false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. La règle par
                    défaut s'applique aux autres éléments et leur contenu
                    textuel sera affiché.
    </span>
   </li>
   <li>
    <input name="idp140293223453920" onclick="javascript:var Click_MenuId='idp140293223459744true';var formid='idp140293223453920'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223459744true"/>
    Il
                donne « cours » ou « universite », autant de
                fois qu'il y a
                d'éléments « cours » ou « universite » dans
                le document, et le contenu textuel de tous les
                autres éléments qui ne sont pas contenus dans un élément
                « cours » ou dans un élément
                « université ».
    <span class="feedback" id="idp140293223459744true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Exactement. La
                    règle par défaut s'applique à tous les éléments, sauf aux
                    éléments « cours »
                    dont on ne visite pas les nœuds.
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 10
  </b>
  .
        Qu'est-ce qui décrit le mieux le document XSLT suivant?
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
            &lt;xsl:template match="/"&gt;
            &lt;xsl:value-of select="name(*)" /&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223461968">
  <ol>
   <li>
    <input name="idp140293223461968" onclick="javascript:var Click_MenuId='idp140293223463440false';var formid='idp140293223461968'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223463440false"/>
    Il
                donne le nom de tous les éléments contenus dans
                l'élément-racine.
    <span class="feedback" id="idp140293223463440false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non, car
                    « / » est le nœud-racine (le document lui-même) et
                    non pas l'élément-racine.
    </span>
   </li>
   <li>
    <input name="idp140293223461968" onclick="javascript:var Click_MenuId='idp140293223465072true';var formid='idp140293223461968'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223465072true"/>
    Il
                donne le nom de l'élément-racine.
    <span class="feedback" id="idp140293223465072true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement, car
                    « / » est le nœud-racine (le document lui-même)
                    qui ne contient qu'un seul élément :
                    l'élément-racine.
    </span>
   </li>
   <li>
    <input name="idp140293223461968" onclick="javascript:var Click_MenuId='idp140293223466496false';var formid='idp140293223461968'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223466496false"/>
    Il
                donne le nom de tous les éléments du document XML.
    <span class="feedback" id="idp140293223466496false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Comme nous
                    avons une règle qui est appliquée au nœud-racine, le
                    traitement du processeur XSLT
                    va s'arrêter immédiatement après l'application du seul
                    modèle contenu dans le document XSLT.
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 11
  </b>
  .
        Qu'est-ce qui décrit le mieux le document XSLT suivant?
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
            &lt;xsl:template match="*"&gt;
            [&lt;xsl:value-of select="generate-id(.)" /&gt;]
            &lt;xsl:apply-templates select="*" /&gt;
            &lt;xsl:apply-templates select="*" mode="a"/&gt;
            &lt;/xsl:template&gt;
            &lt;xsl:template match="*" mode="a"&gt;
            [&lt;xsl:value-of select="generate-id(.)"
            /&gt;]&lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223468480">
  <ol>
   <li>
    <input name="idp140293223468480" onclick="javascript:var Click_MenuId='idp140293223470048false';var formid='idp140293223468480'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223470048false"/>
    Il
                donne une liste d'identifiants, un et un seul identifiant pour
                chaque élément du document XML.
                Il n'y a pas deux identifiants égaux.
    <span class="feedback" id="idp140293223470048false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. À cause de
                    l'utilisation du « mode », certains identifiants
                    sont répétés deux fois.
    </span>
   </li>
   <li>
    <input name="idp140293223468480" onclick="javascript:var Click_MenuId='idp140293223471920false';var formid='idp140293223468480'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223471920false"/>
    Il
                donne une liste d'identifiants, chacun étant répété deux
                fois.
    <span class="feedback" id="idp140293223471920false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Pour
                    l'élément-racine, il n'est pas répété deux fois.
    </span>
   </li>
   <li>
    <input name="idp140293223468480" onclick="javascript:var Click_MenuId='idp140293223473216true';var formid='idp140293223468480'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223473216true"/>
    Il
                donne une liste d'identifiants dont certains sont répétés deux
                fois.
    <span class="feedback" id="idp140293223473216true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Oui. Ils sont tous
                    répétés deux fois, sauf pour l'élément-racine.
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 12
  </b>
  .
        Qu'est-ce qui décrit le mieux le document XSLT suivant?
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
            &lt;xsl:template match="*"&gt;
            &lt;xsl:choose&gt;
            &lt;xsl:when test="name(.)='universite'" &gt;
            &lt;xsl:apply-templates select="*" /&gt;
            &lt;/xsl:when&gt;
            &lt;xsl:when test="name(.)='cours'" &gt;
            &lt;xsl:value-of select="nom" /&gt;
            &lt;/xsl:when&gt;
            &lt;xsl:otherwise /&gt;
            &lt;/xsl:choose&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223474768">
  <ol>
   <li>
    <input name="idp140293223474768" onclick="javascript:var Click_MenuId='idp140293223476464false';var formid='idp140293223474768'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223476464false"/>
    Il
                donne le contenu textuel de tous les éléments « nom »
                immédiatement contenus
                dans des éléments « cours »
    <span class="feedback" id="idp140293223476464false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Si un
                    élément « cours » était contenu dans un autre
                    élément « cours », il ne serait
                    jamais visité.
    </span>
   </li>
   <li>
    <input name="idp140293223474768" onclick="javascript:var Click_MenuId='idp140293223478464false';var formid='idp140293223474768'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223478464false"/>
    Il
                donne le contenu textuel de tous les éléments « nom »
                immédiatement contenus
                dans des éléments « cours », eux-mêmes immédiatement
                contenus dans des éléments « universite ».
    <span class="feedback" id="idp140293223478464false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Si l'élément
                    « universite » n'est pas l'élément-racine, il ne
                    sera jamais visité.
    </span>
   </li>
   <li>
    <input name="idp140293223474768" onclick="javascript:var Click_MenuId='idp140293223480144false';var formid='idp140293223474768'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223480144false"/>
    Il
                donne un document vide.
    <span class="feedback" id="idp140293223480144false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Seulement si les
                    éléments « cours » rencontrés dans les éléments
                    « universite »
                    n'ont pas de contenu textuel dans leurs éléments
                    « nom ».
    </span>
   </li>
   <li>
    <input name="idp140293223474768" onclick="javascript:var Click_MenuId='idp140293223481376true';var formid='idp140293223474768'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223481376true"/>
    Il
                donne le contenu textuel de tous les éléments « nom »
                immédiatement
                contenus dans des éléments « cours », eux-mêmes
                immédiatement contenus dans l'élément-racine
                « universite ».
    <span class="feedback" id="idp140293223481376true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement. Il
                    n'y a qu'un seul cas où d'autres éléments que
                    l'élément-racine sont visités
                    et c'est lorsque l'élément-racine est l'élément
                    « universite ».
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 13
  </b>
  .
        Qu'est-ce qui décrit le mieux le document XSLT suivant?
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
            &lt;xsl:template match="*"&gt;
            &lt;xsl:if test="count(.)=1" &gt;
            &lt;xsl:value-of select="name(.)" /&gt;
            &lt;xsl:apply-templates select="*" /&gt;
            &lt;/xsl:if&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223483376">
  <ol>
   <li>
    <input name="idp140293223483376" onclick="javascript:var Click_MenuId='idp140293223484848true';var formid='idp140293223483376'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223484848true"/>
    Il
                donne le nom de tous les éléments.
    <span class="feedback" id="idp140293223484848true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement, car
                    « . » n'est que l'élément courant (donc un
                    ensemble d'un seul élément);
                    « count(.) » vaut donc « 1 ».
    </span>
   </li>
   <li>
    <input name="idp140293223483376" onclick="javascript:var Click_MenuId='idp140293223486448false';var formid='idp140293223483376'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223486448false"/>
    Il
                donne le nom de l'élément-racine.
    <span class="feedback" id="idp140293223486448false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Oui, mais aussi
                    le nom des autres éléments.
    </span>
   </li>
   <li>
    <input name="idp140293223483376" onclick="javascript:var Click_MenuId='idp140293223487664false';var formid='idp140293223483376'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223487664false"/>
    Il
                donne un document vide.
    <span class="feedback" id="idp140293223487664false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Comme
                    « count(.) » vaut toujours « 1 », c'est
                    plutôt le nom de tous les éléments qui est donné.
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 14
  </b>
  .
        Qu'est-ce qui décrit le mieux le document XSLT suivant?
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
            &lt;xsl:template match="*"&gt;
            &lt;a valeur="{name(.)}"&gt;
            &lt;xsl:apply-templates select="*" /&gt;
            &lt;/a&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223489152">
  <ol>
   <li>
    <input name="idp140293223489152" onclick="javascript:var Click_MenuId='idp140293223490720false';var formid='idp140293223489152'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223490720false"/>
    Il
                donne le document XML original, où les éléments ont tous été
                remplacés par des éléments de nom « a ».
    <span class="feedback" id="idp140293223490720false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Le contenu
                    textuel ne sera jamais modifié.
    </span>
   </li>
   <li>
    <input name="idp140293223489152" onclick="javascript:var Click_MenuId='idp140293223492368true';var formid='idp140293223489152'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223492368true"/>
    Il
                remplace le document XML original par un document ne contenant
                que
                des éléments « a » sans contenu textuel.
    <span class="feedback" id="idp140293223492368true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement. Le
                    nom des éléments originaux est donné par la valeur de
                    l'attribut « valeur ».
    </span>
   </li>
   <li>
    <input name="idp140293223489152" onclick="javascript:var Click_MenuId='idp140293223493872false';var formid='idp140293223489152'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223493872false"/>
    Il
                donne le document XML original.
    <span class="feedback" id="idp140293223493872false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Absolument
                    pas : il n'y a plus que des éléments
                    « a ».
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 15
  </b>
  .
        Que signifie XSL?
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223557968">
  <ol>
   <li>
    <input name="idp140293223557968" onclick="javascript:var Click_MenuId='idp140293223558880true';var formid='idp140293223557968'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223558880true"/>
    eXtensible
                Stylesheet Language
    <span class="feedback" id="idp140293223558880true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement.
    </span>
   </li>
   <li>
    <input name="idp140293223557968" onclick="javascript:var Click_MenuId='idp140293223560320false';var formid='idp140293223557968'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223560320false"/>
    eXtensible
                Style Language
    <span class="feedback" id="idp140293223560320false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223557968" onclick="javascript:var Click_MenuId='idp140293223561760false';var formid='idp140293223557968'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223561760false"/>
    eXtensible
                Style Laboratory
    <span class="feedback" id="idp140293223561760false" style="display: none;font-weight:bold;">
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
   Question 16
  </b>
  .
        Comment fait-on appel à un fichier XSLT?
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223563328">
  <ol>
   <li>
    <input name="idp140293223563328" onclick="javascript:var Click_MenuId='idp140293223564336false';var formid='idp140293223563328'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223564336false"/>
    &lt;stylesheet
                type="text/xsl" href="mystyle.xsl" /&gt;
    <span class="feedback" id="idp140293223564336false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223563328" onclick="javascript:var Click_MenuId='idp140293223565856true';var formid='idp140293223563328'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223565856true"/>
    &lt;?xml-stylesheet
                type="text/xsl" href="mystyle.xsl" ?&gt;
    <span class="feedback" id="idp140293223565856true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!)
                    Effectivement.
    </span>
   </li>
   <li>
    <input name="idp140293223563328" onclick="javascript:var Click_MenuId='idp140293223567344false';var formid='idp140293223563328'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223567344false"/>
    &lt;link
                type="text/xsl" href="mystyle.xsl" /&gt;
    <span class="feedback" id="idp140293223567344false" style="display: none;font-weight:bold;">
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
   Question 17
  </b>
  .
        Le XSLT transforme les documents XML en d'autres documents XML.
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223575312">
  <ol>
   <li>
    <input name="idp140293223575312" onclick="javascript:var Click_MenuId='idp140293223576176false';var formid='idp140293223575312'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223576176false"/>
    Vrai
    <span class="feedback" id="idp140293223576176false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Le XSLT n'a
                    pas à produire du XML. On peut déclarer que l'on souhaite
                    produire
                    du texte avec une telle instruction :
                    &lt;xslt:output method="text" omit-xml-declaration="yes"
                    /&gt;.
    </span>
   </li>
   <li>
    <input name="idp140293223575312" onclick="javascript:var Click_MenuId='idp140293223577856true';var formid='idp140293223575312'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223577856true"/>
    Faux
    <span class="feedback" id="idp140293223577856true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!)
                    Effectivement.
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 18
  </b>
  .
        Le XSLT ne s'applique qu'à des fichiers XML valide.
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223583920">
  <ol>
   <li>
    <input name="idp140293223583920" onclick="javascript:var Click_MenuId='idp140293223584896false';var formid='idp140293223583920'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223584896false"/>
    Vrai
    <span class="feedback" id="idp140293223584896false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Il suffit
                    que le fichier XML soit bien formé.
    </span>
   </li>
   <li>
    <input name="idp140293223583920" onclick="javascript:var Click_MenuId='idp140293223586496true';var formid='idp140293223583920'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223586496true"/>
    Faux
    <span class="feedback" id="idp140293223586496true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!)
                    Effectivement.
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 19
  </b>
  .
        Étant donné le fichier XML suivant.
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="UTF-8"?&gt;
            &lt;addresses&gt;
            &lt;vendeur&gt;
            &lt;prenom&gt;Jean&lt;/prenom&gt;
            &lt;nom&gt;Coutu&lt;/nom&gt;
            &lt;/vendeur&gt;
            &lt;/addresses&gt;
  </p>
  Quel sera le résultat de la transformation XSLT suivante?
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
            &lt;xsl:variable name="var"
            select="/addresses/vendeur[prenom='Jean']"/&gt;
            &lt;xsl:template match="/"&gt;
            &lt;xsl:value-of select="$var"/&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223588016">
  <ol>
   <li>
    <input name="idp140293223588016" onclick="javascript:var Click_MenuId='idp140293223590256false';var formid='idp140293223588016'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223590256false"/>
    Rien
                du tout
    <span class="feedback" id="idp140293223590256false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223588016" onclick="javascript:var Click_MenuId='idp140293223591696false';var formid='idp140293223588016'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223591696false"/>
    Jean
    <span class="feedback" id="idp140293223591696false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) La variable
                    sélectionne plutôt l'élément vendeur.
    </span>
   </li>
   <li>
    <input name="idp140293223588016" onclick="javascript:var Click_MenuId='idp140293223592800false';var formid='idp140293223588016'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223592800false"/>
    <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
     &lt;vendeur&gt;
                    &lt;prenom&gt;Jean&lt;/prenom&gt;
                    &lt;nom&gt;Coutu&lt;/nom&gt;
                    &lt;/vendeur&gt;
    </p>
    <span class="feedback" id="idp140293223592800false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Il s'agit bien du
                    contenu de la variable, mais l'instruction value-of
                    va extraire le contenu du texte.
    </span>
   </li>
   <li>
    <input name="idp140293223588016" onclick="javascript:var Click_MenuId='idp140293223594256true';var formid='idp140293223588016'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223594256true"/>
    Jean
                Coutu
    <span class="feedback" id="idp140293223594256true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Correct.
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 20
  </b>
  .
        Étant donné le fichier XML suivant.
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="UTF-8"?&gt;
            &lt;addresses&gt;
            &lt;vendeur&gt;
            &lt;prenom&gt;Jean&lt;/prenom&gt;
            &lt;nom&gt;Coutu&lt;/nom&gt;
            &lt;/vendeur&gt;
            &lt;/addresses&gt;
  </p>
  Quel sera le résultat de la transformation XSLT suivante?
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
            &lt;xsl:variable name="var"
            select="/addresses/vendeur[prenom='Jean']"/&gt;
            &lt;xsl:template match="/"&gt;
            &lt;xsl:copy-of select="$var"/&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223595504">
  <ol>
   <li>
    <input name="idp140293223595504" onclick="javascript:var Click_MenuId='idp140293223597680false';var formid='idp140293223595504'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223597680false"/>
    Rien
                du tout
    <span class="feedback" id="idp140293223597680false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223595504" onclick="javascript:var Click_MenuId='idp140293223599120false';var formid='idp140293223595504'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223599120false"/>
    Jean
    <span class="feedback" id="idp140293223599120false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) La variable
                    sélectionne plutôt l'élément vendeur.
    </span>
   </li>
   <li>
    <input name="idp140293223595504" onclick="javascript:var Click_MenuId='idp140293223600224false';var formid='idp140293223595504'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223600224false"/>
    Jean
                Coutu
    <span class="feedback" id="idp140293223600224false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non, ce n'est pas
                    l'effet de l'instruction copy-of.
    </span>
   </li>
   <li>
    <input name="idp140293223595504" onclick="javascript:var Click_MenuId='idp140293223601344true';var formid='idp140293223595504'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223601344true"/>
    <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
     &lt;vendeur&gt;
                    &lt;prenom&gt;Jean&lt;/prenom&gt;
                    &lt;nom&gt;Coutu&lt;/nom&gt;
                    &lt;/vendeur&gt;
    </p>
    <span class="feedback" id="idp140293223601344true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement,
                    l'instruction copy-of donne une copie intégrale du contenu
                    de la variable.
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 21
  </b>
  .
        Étant donné le fichier XML suivant.
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="UTF-8"?&gt;
            &lt;addresses&gt;
            &lt;vendeur&gt;
            &lt;prenom&gt;Jean&lt;/prenom&gt;
            &lt;nom&gt;Coutu&lt;/nom&gt;
            &lt;/vendeur&gt;
            &lt;vendeur&gt;
            &lt;prenom&gt;Marie&lt;/prenom&gt;
            &lt;nom&gt;Vanasse&lt;/nom&gt;
            &lt;/vendeur&gt;
            &lt;vendeur&gt;
            &lt;prenom&gt;Pierre&lt;/prenom&gt;
            &lt;nom&gt;Coutu&lt;/nom&gt;
            &lt;/vendeur&gt;
            &lt;/addresses&gt;
  </p>
  Quel sera le résultat de la transformation XSLT suivante?
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
            &lt;xsl:template match="/"&gt;
            &lt;xsl:value-of select="//vendeur"/&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223603200">
  <ol>
   <li>
    <input name="idp140293223603200" onclick="javascript:var Click_MenuId='idp140293223605472false';var formid='idp140293223603200'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223605472false"/>
    Rien
                du tout
    <span class="feedback" id="idp140293223605472false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223603200" onclick="javascript:var Click_MenuId='idp140293223606880false';var formid='idp140293223603200'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223606880false"/>
    Jean
                Coutu
                Marie
                Vanasse
                Pierre
                Coutu
    <span class="feedback" id="idp140293223606880false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Ce n'est pas
                    l'effet de l'instruction value-of.
    </span>
   </li>
   <li>
    <input name="idp140293223603200" onclick="javascript:var Click_MenuId='idp140293223608080true';var formid='idp140293223603200'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223608080true"/>
    Jean
                Coutu
    <span class="feedback" id="idp140293223608080true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement, seul
                    le contenu textuel du premier élément vendeur sera
                    donné.
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 22
  </b>
  .
        Étant donné le fichier XML suivant.
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="UTF-8"?&gt;
            &lt;addresses&gt;
            &lt;vendeur&gt;
            &lt;prenom&gt;Jean&lt;/prenom&gt;
            &lt;nom&gt;Coutu&lt;/nom&gt;
            &lt;/vendeur&gt;
            &lt;vendeur&gt;
            &lt;prenom&gt;Marie&lt;/prenom&gt;
            &lt;nom&gt;Vanasse&lt;/nom&gt;
            &lt;/vendeur&gt;
            &lt;vendeur&gt;
            &lt;prenom&gt;Pierre&lt;/prenom&gt;
            &lt;nom&gt;Coutu&lt;/nom&gt;
            &lt;/vendeur&gt;
            &lt;/addresses&gt;
  </p>
  Quel sera le résultat de la transformation XSLT suivante?
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
            &lt;xsl:template match="/"&gt;
            &lt;xsl:value-of select="//vendeur[preceding::vendeur/nom=nom]"/&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223609472">
  <ol>
   <li>
    <input name="idp140293223609472" onclick="javascript:var Click_MenuId='idp140293223611744false';var formid='idp140293223609472'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223611744false"/>
    Rien
                du tout
    <span class="feedback" id="idp140293223611744false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223609472" onclick="javascript:var Click_MenuId='idp140293223613184false';var formid='idp140293223609472'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223613184false"/>
    Jean
                Coutu
    <span class="feedback" id="idp140293223613184false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non, seul le
                    dernier élément vendeur est sélectionné, car lui seul est
                    précédé par un élément vendeur ayant un sous-élément nom de
                    même valeur.
    </span>
   </li>
   <li>
    <input name="idp140293223609472" onclick="javascript:var Click_MenuId='idp140293223614496true';var formid='idp140293223609472'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223614496true"/>
    Pierre
                Coutu
    <span class="feedback" id="idp140293223614496true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement, seul
                    le dernier élément vendeur est sélectionné.
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 23
  </b>
  .
        Étant donné le fichier XML suivant.
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="UTF-8"?&gt;
            &lt;addresses&gt;
            &lt;vendeur&gt;
            &lt;prenom&gt;Jean&lt;/prenom&gt;
            &lt;nom&gt;Coutu&lt;/nom&gt;
            &lt;/vendeur&gt;
            &lt;vendeur&gt;
            &lt;prenom&gt;Marie&lt;/prenom&gt;
            &lt;nom&gt;Vanasse&lt;/nom&gt;
            &lt;/vendeur&gt;
            &lt;vendeur&gt;
            &lt;prenom&gt;Pierre&lt;/prenom&gt;
            &lt;nom&gt;Coutu&lt;/nom&gt;
            &lt;/vendeur&gt;
            &lt;/addresses&gt;
  </p>
  Quel sera le résultat de la transformation XSLT suivante?
  <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
   &lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
            &lt;xsl:stylesheet version="1.0"
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
            &lt;xsl:template match="/"&gt;
            &lt;xsl:copy-of
            select="//vendeur[not(preceding::vendeur/nom=nom)]"/&gt;
            &lt;/xsl:template&gt;
            &lt;/xsl:stylesheet&gt;
  </p>
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223615888">
  <ol>
   <li>
    <input name="idp140293223615888" onclick="javascript:var Click_MenuId='idp140293223618208false';var formid='idp140293223615888'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223618208false"/>
    Rien
                du tout
    <span class="feedback" id="idp140293223618208false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non.
    </span>
   </li>
   <li>
    <input name="idp140293223615888" onclick="javascript:var Click_MenuId='idp140293223619648false';var formid='idp140293223615888'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223619648false"/>
    <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
     &lt;vendeur&gt;
                    &lt;prenom&gt;Jean&lt;/prenom&gt;
                    &lt;nom&gt;Coutu&lt;/nom&gt;
                    &lt;/vendeur&gt;
    </p>
    <span class="feedback" id="idp140293223619648false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non, le deuxième
                    élément est aussi sélectionné.
    </span>
   </li>
   <li>
    <input name="idp140293223615888" onclick="javascript:var Click_MenuId='idp140293223621216true';var formid='idp140293223615888'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223621216true"/>
    <p style="border:solid 1px black;white-space:pre; font-size:0.85em">
     &lt;vendeur&gt;
                    &lt;prenom&gt;Jean&lt;/prenom&gt;
                    &lt;nom&gt;Coutu&lt;/nom&gt;
                    &lt;/vendeur&gt;&lt;vendeur&gt;
                    &lt;prenom&gt;Marie&lt;/prenom&gt;
                    &lt;nom&gt;Vanasse&lt;/nom&gt;
                    &lt;/vendeur&gt;
    </p>
    <span class="feedback" id="idp140293223621216true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement, le
                    dernier élément n'est pas sélectionné.
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
<div style="margin-left:1cm">
 <div style="background-color:#E0EAF0">
  <b>
   Question 24
  </b>
  .
        Que vaut l'expression « //a[1]=current() »?
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140293223628896">
  <ol>
   <li>
    <input name="idp140293223628896" onclick="javascript:var Click_MenuId='idp140293223629872false';var formid='idp140293223628896'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223629872false"/>
    Vrai
                si le nœud courant est le premier élément a rencontré, faux
                autrement.
    <span class="feedback" id="idp140293223629872false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. L'égalité
                    compare plutôt le contenu des éléments, pas la position dans
                    le document.
    </span>
   </li>
   <li>
    <input name="idp140293223628896" onclick="javascript:var Click_MenuId='idp140293223631440false';var formid='idp140293223628896'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223631440false"/>
    Vrai
                si le nœud courant est le premier élément a rencontré au sein
                d'un même élément, faux autrement.
    <span class="feedback" id="idp140293223631440false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. L'égalité
                    compare plutôt le contenu des éléments, pas la position au
                    sein d'un élément.
    </span>
   </li>
   <li>
    <input name="idp140293223628896" onclick="javascript:var Click_MenuId='idp140293223632992true';var formid='idp140293223628896'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140293223632992true"/>
    Aucune
                de ces réponses.
    <span class="feedback" id="idp140293223632992true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement,
                    l'expression n'a la valeur vraie que si l'élément courant
                    est un élément « a » ayant le même contenu que le
                    premier élément « a » dans le document.
    </span>
   </li>
  </ol>
 </form>
</div>
<hr style="margin-bottom:1cm; margin-top:1cm;color: #0f0; background-color: #ccc; height: 5px;"/>
