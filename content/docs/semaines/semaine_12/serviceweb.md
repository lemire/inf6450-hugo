---
title: "Création d'un service web"
weight: 75
---


# Projet de création d'un service web

Dans ce projet, le serveur utilise la notion de "contexte" ou "route" pour diriger les requêtes vers différents gestionnaires. Un contexte est défini par un chemin d'URL, comme "/" pour la racine du site ou "/heure" pour une ressource spécifique. Chaque contexte est associé à une fonction qui gère les requêtes entrantes, permettant au serveur de servir différents contenus ou d'exécuter différentes actions en fonction de l'URL demandée.

Ce projet est un serveur simple en Java qui sert une page HTML sur la racine (`/`) et fournit l'heure actuelle en XML sur `/heure`.

## Fichiers

Copiez ces fichiers dans un répertoire.

`ServeurHeure.java`&nbsp;:

```java
import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpExchange;

import javax.xml.stream.XMLOutputFactory;
import javax.xml.stream.XMLStreamWriter;
import java.io.IOException;
import java.io.OutputStream;
import java.io.StringWriter;
import java.net.InetSocketAddress;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class ServeurHeure {
    private static final XMLOutputFactory xmlFactory = XMLOutputFactory.newFactory();

    private static String genererXmlHeure() throws Exception {
        StringWriter stringWriter = new StringWriter();
        XMLStreamWriter xml = xmlFactory.createXMLStreamWriter(stringWriter);

        xml.writeStartDocument("UTF-8", "1.0");
        xml.writeStartElement("heure");
        xml.writeCharacters(DateTimeFormatter.ISO_LOCAL_DATE_TIME.format(LocalDateTime.now()));
        xml.writeEndElement();
        xml.writeEndDocument();

        xml.flush();
        xml.close();

        return stringWriter.toString();
    }

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);

        server.createContext("/", exchange -> {
            if ("GET".equals(exchange.getRequestMethod())) {
                try {
                    String html = new String(Files.readAllBytes(Paths.get("index.html")), "UTF-8");
                    byte[] response = html.getBytes("UTF-8");

                    exchange.getResponseHeaders().set("Content-Type", "text/html; charset=UTF-8");
                    exchange.sendResponseHeaders(200, response.length);
                    try (OutputStream os = exchange.getResponseBody()) {
                        os.write(response);
                    }
                } catch (Exception e) {
                    exchange.sendResponseHeaders(500, -1);
                }
            } else {
                exchange.sendResponseHeaders(405, -1);
            }
        });

        server.createContext("/heure", exchange -> {
            if ("GET".equals(exchange.getRequestMethod())) {
                try {
                    String xml = genererXmlHeure();
                    byte[] response = xml.getBytes("UTF-8");

                    exchange.getResponseHeaders().set("Content-Type", "application/xml; charset=UTF-8");
                    exchange.sendResponseHeaders(200, response.length);
                    try (OutputStream os = exchange.getResponseBody()) {
                        os.write(response);
                    }
                } catch (Exception e) {
                    exchange.sendResponseHeaders(500, -1);
                }
            } else {
                exchange.sendResponseHeaders(405, -1);
            }
        });

        server.setExecutor(null);
        server.start();
        System.out.println("Serveur démarré sur http://localhost:8000/");
    }
}
```

`index.html`&nbsp;:
```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Serveur d'Heure</title>
</head>
<body>
    <h1>Serveur d'heure</h1>
    <p>Heure actuelle: <span id="time"></span></p>
    <button id="fetchBtn">Obtenir l'heure</button>
    <h2>XML brut:</h2>
    <pre id="rawXml"></pre>
    <script>
        document.getElementById('fetchBtn').addEventListener('click', function() {
            fetch('/heure')
                .then(response => response.text())
                .then(xmlString => {
                    const parser = new DOMParser();
                    const xmlDoc = parser.parseFromString(xmlString, 'application/xml');
                    const time = xmlDoc.getElementsByTagName('heure')[0].textContent;
                    document.getElementById('time').textContent = time;
                    document.getElementById('rawXml').textContent = xmlString;
                })
                .catch(error => console.error('Erreur:', error));
        });
    </script>
</body>
</html>
```

## Utilisation

1. Compilez le programme Java :
   ```
   javac ServeurHeureStax.java
   ```

2. Lancez le serveur :
   ```
   java ServeurHeureStax
   ```
   Attention. Si un autre serveur sur votre machine utilise le port 8000, le serveur ne pourra pas démarrer correctement. Vous pouvez changer le port dans le programme ou mettre fin à l'autre serveur.

3. Ouvrez un navigateur et allez à `http://localhost:8000/`. Cliquez sur le bouton "Obtenir l'heure" pour récupérer et afficher l'heure actuelle. Le XML brut est également affiché en bas de la page.

4. Vous pouvez également accéder directement à `http://localhost:8000/heure` pour obtenir l'XML de l'heure.

## Description du code

### ServeurHeureStax.java
Ce fichier contient la classe principale `ServeurHeureStax`. Il utilise l'API `HttpServer` de Java pour créer un serveur HTTP simple écoutant sur le port 8000.

- **Imports** : Inclut les classes nécessaires pour le serveur HTTP, la génération XML avec StAX, la lecture de fichiers, et la manipulation des dates.
- **Méthode `genererXmlHeure()`** : Génère un document XML simple avec l'heure actuelle au format ISO. Utilise `XMLOutputFactory` et `XMLStreamWriter` pour construire le XML de manière programmatique.
- **Méthode `main()`** : 
  - Crée une instance d'`HttpServer`.
  - Définit deux contextes de gestion des requêtes :
    - Pour `/` : Lit le fichier `index.html` et le sert avec le type MIME `text/html`.
    - Pour `/heure` : Appelle `genererXmlHeure()` et sert le XML avec le type MIME `application/xml`.
  - Démarre le serveur et affiche un message de confirmation.

### index.html
Page web statique servie par le serveur.

- **Structure HTML** : Titre, paragraphe pour afficher l'heure, bouton pour déclencher la requête, et section pour afficher le XML brut.
- **JavaScript** : 
  - Écouteur d'événement sur le bouton qui effectue une requête `fetch` vers `/heure`.
  - Analyse la réponse XML avec `DOMParser`.
  - Extrait le contenu de l'élément `<heure>` pour l'afficher.
  - Affiche également le XML brut dans un élément `<pre>`.

## Activités suggérées

1. **Modifier le format XML** : Changez la structure du XML généré (par exemple, ajoutez des éléments pour la date et l'heure séparément) et mettez à jour le JavaScript pour analyser la nouvelle structure.

2. **Ajouter un endpoint pour la date** : Créez un nouveau contexte `/date` qui retourne la date actuelle en JSON, et ajoutez un bouton dans l'HTML pour le récupérer et l'afficher.

3. **Améliorer l'interface utilisateur** : Ajoutez du CSS pour styliser la page (par exemple, centrer le contenu, changer les couleurs) et peut-être une fonctionnalité pour rafraîchir l'heure automatiquement toutes les minutes.

4. **Convertissez le service en JSON** : Pouvez-vous remplacer le serveur basé sur XML par un serveur basé sur JSON?