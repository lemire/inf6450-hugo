---
title: "Des pages web dynamiques avec JavaScript"
weight: 40
---
<h1 class="">
 Des pages web dynamiques avec JavaScript
</h1>
<div class="">
 <p>
  Dans ce cours, vous serez amené à utiliser le language JavaScript, aussi parfois appelé JavaScript. Il s’agit du langage de programmation utilisé par tous les navigateurs au sein des pages.
 </p>
 <p>
  Même s’il s’agit d’un langage de programmation complètement différent du Java, la syntaxe est similaire. Puisque vous maîtrisez Java, vous devriez être capable d’utiliser le JavaScript sans grand mal.
 </p>
 <p>
  Il n’est pas nécessaire de devenir un exemple en la matière, mais nous vous invitons tout de même à vous familiariser avec la langage au besoin. Un point d’entrée est le livre en ligne
  <a class="spip_out" href="https://fr.wikibooks.org/wiki/Programmation_JavaScript" rel="noopener noreferrer external" target="_blank">
   Programmation JavaScript
  </a>
  chez wikibooks (gratuit).
 </p>
 <p>
  Par ailleurs, dans ce cas il vous faudra apprendre à manipuler des documents XML, notamment en utilisant l’interface DOM. Cette même interface est utilisée en Java et en JavaScript. Nous y reviendrons.
 </p>
 <p>
  Pour l’instant, faites l’exercice suivant. Enregistrez le fichier XHTML suivant sur disque et consultez-le.
 </p>

 
```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Un petit test</title>
</head>
<body>
  <p>Honoré de Balzac est né en...</p>
  <ol>
    <li>
      <input type="radio" name="agebalzac" 
       onclick="javascript:document.getElementById('reponse1').style.display = 'block';" />
      1799.
      <span id="reponse1" style="display:none;font-weight:bold;" class="feedback">
      <br />
        (Réponse correcte!)
      </span>
    </li>
    <li>
      <input type="radio" name="agebalzac" 
       onclick="javascript:document.getElementById('reponse2').style.display = 'block';" />
      1832.
      <span id="reponse2" style="display:none;font-weight:bold;" class="feedback">
      <br />
        (Réponse incorrecte!)
      </span>
    </li>
    <li>
      <input type="radio" name="agebalzac" 
       onclick="javascript:document.getElementById('reponse3').style.display = 'block';" />
      1910.
      <span id="reponse3" style="display:none;font-weight:bold;" class="feedback">
      <br />
        (Réponse incorrecte!)
      </span>
    </li>
  </ol>
</body>
</html>
```


 <p>
  Enregistrez le contenu dans un fichier avec l’encodage UTF-8. Le résultat devrait avoir la forme suivante :
 </p>
 <p>
  Honoré de Balzac est né en...
 </p>
 <ol>
  <li>
   <input name="agebalzac" onclick="javascript:document.getElementById('reponse1').style.display = 'block';" type="radio"/>
   1799.
   <span class="feedback" id="reponse1" style="display: none;font-weight:bold;">
    <br/>
    (Réponse correcte!)
   </span>
  </li>
  <li>
   <input name="agebalzac" onclick="javascript:document.getElementById('reponse2').style.display = 'block';" type="radio"/>
   1832.
   <span class="feedback" id="reponse2" style="display: none;font-weight:bold;">
    <br/>
    (Réponse incorrecte!)
   </span>
  </li>
  <li>
   <input name="agebalzac" onclick="javascript:document.getElementById('reponse3').style.display = 'block';" type="radio"/>
   1910.
   <span class="feedback" id="reponse3" style="display: none;font-weight:bold;">
    <br/>
    (Réponse incorrecte!)
   </span>
  </li>
 </ol>
 <p>
  Familiarisez-vous avec le code JavaScript en ajoutant une seconde question. Peut-être est-ce que vous pourriez demander où Balzac a vécu. Portez une attention particulière aux attributs « id » ainsi qu’à la fonction « document.getElementById ».
 </p>
</div>
<hr/>
