---
title: "Serveur Web Java"
weight: 35
---

# Serveur Web Java



Le protocole HTTP (HyperText Transfer Protocol) est un protocole de communication standard utilisé pour transférer des données sur le web. Il définit comment les clients, tels que les navigateurs web, peuvent demander des ressources aux serveurs et comment ces derniers répondent. HTTP repose sur un modèle requête-réponse, où le client envoie une requête et le serveur renvoie une réponse.

Une requête HTTP est une demande initiée par le client pour accéder à une ressource spécifique sur le serveur. Elle comprend généralement une méthode (comme GET pour récupérer des données, POST pour envoyer des données), une URL pointant vers la ressource, des en-têtes contenant des informations supplémentaires (comme le type de contenu accepté), et parfois un corps pour les données envoyées. Le serveur traite la requête et renvoie une réponse avec un code de statut (par exemple, 200 pour succès, 404 pour non trouvé) et le contenu demandé.

Il arrive que l'on souhaite lancer rapidement un petit serveur web. Il est
facile d'y arriver avec Java.
Créez un fichier `ExempleServeurFichiersSimple.java`
avec le contenu suivant, compilez et exécutez-le dans un dossier. Si le port 8000 n'est pas utilisé sur votre ordinateur
vous aurez un serveur web fonctionnant sur votre machine. (Dans le cas contraire, remplacez le port 8000 par 8001 ou 8002.) Vous pouvez déposer des fichiers HTML
dans ce répertoire et les chargez dans votre navigateur.


```java {style=github}
import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.SimpleFileServer;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.file.Path;

public class ExempleServeurFichiersSimple {
    public static void main(String[] args) throws IOException {
        int port = 8000;
        Path repertoireCourant = Path.of(".").toAbsolutePath();  // Répertoire courant

        HttpServer serveur = HttpServer.create(new InetSocketAddress(port), 0);
        serveur.createContext("/", SimpleFileServer.createFileHandler(repertoireCourant));
        serveur.start();

        System.out.println("Serveur démarré sur le port " + port + ", servant les fichiers depuis " 
            + repertoireCourant.toAbsolutePath());
        System.out.println("Accédez-y via http://localhost:" + port + "/");
    }
}
```

Essayez de déposer ce dossier un fichier nommé `test.html` avec le contenu suivant.

```html
<html>
    <body>
        <p>Allo!</p>
    </body>
</html>
```

Vous devriez pouvoir charger ce fichier dans votre navigateur.