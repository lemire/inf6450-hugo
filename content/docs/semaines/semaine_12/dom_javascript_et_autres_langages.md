---
title: "DOM : JavaScript et autres langages"
weight: 60
---
# DOM : JavaScript et autres langages

## DOM et JavaScript

JavaScript est un langage similaire au Java quant à sa syntaxe de base et qui s'exécute souvent dans un navigateur.
Les implémentations JavaScript supportent bien l'API DOM en général.  La principale différence entre DOM en JavaScript et DOM en Java est que certaines méthodes en Java deviennent des attributs ou des propriétés en JavaScript (getNodeValue() devient nodeValue).

JavaScript peut donc lire et traiter des documents XML avec l'API DOM. En particulier, si JavaScript est utilisé au sein d'une page XHTML, le script peut modifier la page dynamiquement en utilisant l'API DOM. La principale différence entre l'utilisation de DOM en Java et JavaScript est qu'à l'exception des méthodes getAttribute, setAttribute, getAttributeNS, setAttributeNS, getAttributeNode, setAttributeNode, getAttributeNodeNS, setAttributeNodeNS, getElementsByTagName et getElementById, toutes les méthodes dont le nom commence par « get » ou « set » sont remplacées par un attribut de l'objet (ou « property » en anglais). Au lieu d'écrire « e.getChildNodes(); », on écrit « e.childNodes; », au lieu d'écrire « e.setNodeValue("texte"); », on écrit « e.nodeValue="texte"; », et ainsi de suite.

Par exemple, le script suivant va ajouter du texte lorsque la souris passera sur l'élément ayant un attribut « id='javatest' ».

```javascript
monele=document.getElementById('javatest');
monele.childNodes.item(0).nodeValue+=' (passage de souris) ';
```

## DOM et autres langages

L'API DOM est supportée en C++ (voir [Xerces-C](http://xml.apache.org/xerces-c/)), en Python (paquetage xml.dom), en Perl (voir [Xerces-P](http://xml.apache.org/xerces-p/)), en JavaScript, etc. C'est d'ailleurs la principale force de cette API : peu importe le contexte, il y a fort à parier que vous aurez accès à l'API DOM. Ce n'est sans doute pas la meilleure API possible, mais son ubiquité fait en sorte qu'il vaut la peine d'apprendre à la connaître.
