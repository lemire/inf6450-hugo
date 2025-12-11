---
title: "Autoévaluation"
weight: 40
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
        Si vous faites la lecture d'un document XML avec une librairie
        supportant DOM et que, par la suite,
        vous utilisez la même librairie pour sauvegarder exactement le même
        modèle en arbre, est-ce
        que le fichier nouvellement produit sera identique au fichier d'origine?
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140312857418832">
  <ol>
   <li>
    <input name="idp140312857418832" onclick="javascript:var Click_MenuId='idp140312857419808false';var formid='idp140312857418832'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140312857419808false"/>
    Oui
    <span class="feedback" id="idp140312857419808false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Il y a plusieurs
                    façons de représenter un même arbre XML. Par exemple,
                    l'espace entre les éléments
                    n'est pas significatif en XML et
                    « &lt;toto&gt;fds&lt;/toto&gt;&lt;toto&gt;fds&lt;/toto&gt; »
                    est équivalent à
                    « &lt;toto&gt;fds&lt;/toto&gt;
                    &lt;toto&gt;fds&lt;/toto&gt; ».
    </span>
   </li>
   <li>
    <input name="idp140312857418832" onclick="javascript:var Click_MenuId='idp140312857422304true';var formid='idp140312857418832'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140312857422304true"/>
    Non
    <span class="feedback" id="idp140312857422304true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement, il
                    peut y avoir des différences.
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
        Si vous voulez absolument produire du XML bien formé, quelle est la
        meilleure méthode?
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140312857423808">
  <ol>
   <li>
    <input name="idp140312857423808" onclick="javascript:var Click_MenuId='idp140312857424864false';var formid='idp140312857423808'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140312857424864false"/>
    En
                traitant le XML comme du texte (System.out en Java).
    <span class="feedback" id="idp140312857424864false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) S'il est
                    important que votre document soit bien formé, ce n'est
                    probablement pas la meilleure
                    méthode, à moins que le travail ne soit relativement
                    simple.
    </span>
   </li>
   <li>
    <input name="idp140312857423808" onclick="javascript:var Click_MenuId='idp140312857426560false';var formid='idp140312857423808'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140312857426560false"/>
    En
                utilisant le XSLT.
    <span class="feedback" id="idp140312857426560false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Le XSLT ne
                    permet pas de vérifier que le document produit est du XML
                    bien formé.
                    Il est possible de générer du XML incorrect à partir du
                    XSLT : par exemple, ayant deux éléments-racines.
    </span>
   </li>
   <li>
    <input name="idp140312857423808" onclick="javascript:var Click_MenuId='idp140312857428320true';var formid='idp140312857423808'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140312857428320true"/>
    En
                utilisant une librairie avec modèle DOM.
    <span class="feedback" id="idp140312857428320true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Oui. Une bonne
                    librairie devrait nous assurer que le document produit est
                    du XML bien formé.
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
        Est-ce qu'une librairie événementielle nous avertit de la présence d'un
        commentaire dans le texte XML? Est-ce
        que le modèle en arbre doit contenir les commentaires?
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140312857430192">
  <ol>
   <li>
    <input name="idp140312857430192" onclick="javascript:var Click_MenuId='idp140312857431312false';var formid='idp140312857430192'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140312857431312false"/>
    Oui.
                Dans les deux cas.
    <span class="feedback" id="idp140312857431312false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. C'est
                    pourquoi les commentaires ne devraient pas contenir des
                    informations importantes, car les parseurs peuvent
                    omettre les commentaires.
    </span>
   </li>
   <li>
    <input name="idp140312857430192" onclick="javascript:var Click_MenuId='idp140312857432992true';var formid='idp140312857430192'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140312857432992true"/>
    Non.
                Dans les deux cas.
    <span class="feedback" id="idp140312857432992true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement.
                    Certains parseurs omettent les commentaires; si les
                    les commentaires XML servent à stocker des informations
                    importantes, cela peut entraîner un problème.
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
        Quel type de modèle est le DOM?
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140312857434784">
  <ol>
   <li>
    <input name="idp140312857434784" onclick="javascript:var Click_MenuId='idp140312857435712true';var formid='idp140312857434784'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140312857435712true"/>
    En
                arbre
    <span class="feedback" id="idp140312857435712true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Oui. C'est même le
                    modèle en arbre de référence.
    </span>
   </li>
   <li>
    <input name="idp140312857434784" onclick="javascript:var Click_MenuId='idp140312857437200false';var formid='idp140312857434784'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140312857437200false"/>
    Événementiel
    <span class="feedback" id="idp140312857437200false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non, mais on peut
                    utiliser un traitement événementiel pour produire
                    un DOM.
    </span>
   </li>
   <li>
    <input name="idp140312857434784" onclick="javascript:var Click_MenuId='idp140312857438736false';var formid='idp140312857434784'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140312857438736false"/>
    Texte
    <span class="feedback" id="idp140312857438736false" style="display: none;font-weight:bold;">
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
        Si, dans un document XML, seule la valeur des attributs
        « montant » vous intéresse, quelle serait
        le meilleur modèle de programmation?
 </div>
 <p style="width:90%;">
  Choisissez la bonne réponse parmi les suivantes.
 </p>
 <form id="idp140312857440240">
  <ol>
   <li>
    <input name="idp140312857440240" onclick="javascript:var Click_MenuId='idp140312857441616false';var formid='idp140312857440240'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140312857441616false"/>
    En
                arbre
    <span class="feedback" id="idp140312857441616false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Non. Il peut être
                    fastidieux et coûter beaucoup de mémoire que de tout mettre
                    dans un arbre
                    pour n'aller chercher que quelques valeurs.
    </span>
   </li>
   <li>
    <input name="idp140312857440240" onclick="javascript:var Click_MenuId='idp140312857443152true';var formid='idp140312857440240'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140312857443152true"/>
    Événementiel
    <span class="feedback" id="idp140312857443152true" style="display: none;font-weight:bold;">
     <br/>
     (Réponse correcte!) Effectivement. Vous
                    pourriez ainsi aller chercher que ce dont vous avez
                    besoin.
    </span>
   </li>
   <li>
    <input name="idp140312857440240" onclick="javascript:var Click_MenuId='idp140312857444528false';var formid='idp140312857440240'; var Click_Menu = document.getElementById(Click_MenuId);var myform = document.getElementById(formid);var spans = myform.getElementsByTagName('span');for (spancount=0; spancount&lt;spans.length;++spancount) spans[spancount].style.display='none';if(/true/.test(Click_MenuId)) Click_Menu.style.color = 'blue'; else Click_Menu.style.color = 'red';Click_Menu.style.display = '';" type="radio" value="idp140312857444528false"/>
    Texte
    <span class="feedback" id="idp140312857444528false" style="display: none;font-weight:bold;">
     <br/>
     (Réponse incorrecte!) Le traitement du
                    XML comme texte peut fonctionner dans certains cas simples,
                    mais pas en général.
    </span>
   </li>
  </ol>
 </form>
</div>
