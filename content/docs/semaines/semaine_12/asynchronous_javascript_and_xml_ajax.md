---
title: "Asynchronous JavaScript And XML (AJAX)"
weight: 70
---

# Asynchronous JavaScript And XML (AJAX)

Normalement, pour récupérer des données sur le serveur (description d’un produit, horaire, etc.), il faut recharger une nouvelle page. Avec **AJAX** (*Asynchronous JavaScript And XML*), un script JavaScript peut charger un fichier XML (ou JSON) en arrière-plan, sans recharger la page. L’utilisateur a l’impression que l’application est beaucoup plus rapide.

Exemples célèbres : Gmail, Google Maps, Facebook (à l’époque), etc.

## Exemple simple : charger et afficher le titre d’un document XHTML

```xhtml
<?xml version="1.0" encoding="ISO-8859-1"?>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Exemple AJAX</title>
    <script>
      // Charge un document XML/XHTML et appelle afficheTitre()
      function chargeDocument(uri) {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open("GET", uri, true);
        xmlhttp.onreadystatechange = function() {
          if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
            afficheTitre(xmlhttp.responseXML);
          }
        };
        xmlhttp.send(null);
      }
      // Affiche le contenu de l'élément <title>
      function afficheTitre(doc) {
        var titre = doc.getElementsByTagName("title")[0];
        var texte = titre.firstChild ? titre.firstChild.nodeValue : "";
        var p = document.createElement("p");
        p.appendChild(document.createTextNode(texte));
        document.getElementsByTagName("body")[0].appendChild(p);
      }
    </script>
  </head>
  <body>
    <p>Cliquez plusieurs fois sur les liens ci-dessous :</p>
    <ul>
      <li><a href="javascript:chargeDocument('domtutoriel.xhtml')">domtutoriel.xhtml</a></li>
      <li><a href="javascript:chargeDocument('travail5.xhtml')">travail5.xhtml</a></li>
    </ul>
  </body>
</html>
```

Dans cet exemple, la fonction `chargeDocument` utilise `XMLHttpRequest` pour effectuer une requête GET asynchrone vers une URI. Lorsque la réponse est reçue (readyState === 4 et status === 200), elle appelle `afficheTitre` qui extrait le contenu de l'élément `<title>` du document XML chargé et l'ajoute dynamiquement à la page.

## Exemple avancé : afficher les titres d’un flux RSS (Le Devoir)

Sélectionnez un fichier XML RSS pour afficher ses titres.

```xhtml
<?xml version="1.0" encoding="ISO-8859-1"?>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Exemple AJAX – Flux RSS</title>
    <script>
      function chargeDocumentFromFile(input) {
        var file = input.files[0];
        if (file) {
          var reader = new FileReader();
          reader.onload = function(e) {
            var doc = new DOMParser().parseFromString(e.target.result, "application/xml");
            afficheTitres(doc);
          };
          reader.readAsText(file);
        }
      }
    </script>
  </head>
  <body>
    <input type="file" accept=".xml" onchange="chargeDocumentFromFile(this)">
  </body>
</html>
```

Cet exemple avancé montre comment parser un fichier XML RSS sélectionné localement. L'utilisateur choisit un fichier via un input de type file, qui est lu avec FileReader, puis parsé avec DOMParser. La fonction `afficheTitres` récupère tous les éléments `<title>` et les affiche dans une liste ordonnée. Cela illustre comment AJAX peut être utilisé pour traiter des fichiers locaux sans serveur.


## Utiliser importNode() pour insérer tout un fragment XML

```javascript
function afficheListe(doc) {
  var ul = doc.getElementsByTagName("ul")[0];
  var copie = document.importNode(ul, true);   // true = copie profonde
  document.body.appendChild(copie);
}
```

La méthode `importNode()` permet d'importer un nœud d'un document XML externe vers le document HTML courant. Le paramètre `true` indique une copie profonde, incluant tous les nœuds enfants. Cela est utile pour éviter les conflits d'espaces de noms et pour intégrer des fragments XML complexes sans altérer le document source.

## Chargement de fichiers locaux (Chrome, Edge, etc.)

La plupart du temps, les pages web ne peuvent pas charger du contenu provenant d'un autre serveur. Il est donc
pratique de demander à l'utilisateur de charger un fichier qui se trouve sur son disque.

```javascript
<input type="file" onchange="chargeFichier(this.files[0])">
function chargeFichier(fichier) {
  var lecteur = new FileReader();
  lecteur.onload = function(e) {
    var doc = new DOMParser().parseFromString(e.target.result, "application/xml");
    afficheTitres(doc);
  };
  lecteur.readAsText(fichier);
}
```

Ce code permet de charger un fichier XML local sélectionné par l'utilisateur via un input de type file. Il utilise `FileReader` pour lire le contenu du fichier en texte, puis `DOMParser` pour le parser en document XML. Cela évite les restrictions de sécurité des navigateurs qui empêchent le chargement direct de fichiers locaux via XMLHttpRequest.

## En résumé

AJAX permet de créer des applications web plus interactives en chargeant des données en arrière-plan sans recharger la page entière. L'objet `XMLHttpRequest` est au cœur de cette technologie, permettant d'envoyer des requêtes HTTP asynchrones. Combiné avec l'API DOM pour manipuler le contenu de la page, AJAX offre une expérience utilisateur fluide.

- AJAX = `XMLHttpRequest` + DOM + un peu de JavaScript
- Très simple avec les navigateurs modernes (Firefox, Chrome, Edge)
- Problèmes de compatibilité avec les anciennes versions d'Internet Explorer
- De nos jours, on utilise souvent `fetch()` ou des bibliothèques comme **jQuery**, **axios** ou **React**

L'exemple simple montre comment charger un document XHTML et extraire son titre pour l'afficher dynamiquement. L'exemple avancé démontre le parsing d'un flux RSS pour afficher une liste de titres. La méthode `importNode()` permet d'importer des fragments XML d'un document à un autre, utile pour intégrer du contenu externe sans conflits d'espaces de noms.
