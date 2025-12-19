---
title: "Serveur Web Java"
weight: 35
---

# Serveur Web Java



Le protocole HTTP (HyperText Transfer Protocol) est un protocole de communication standard utilisé pour transférer des données sur le web. Il définit comment les clients, tels que les navigateurs web, peuvent demander des ressources aux serveurs et comment ces derniers répondent. HTTP repose sur un modèle requête-réponse, où le client envoie une requête et le serveur renvoie une réponse.

Une requête HTTP est une demande initiée par le client pour accéder à une ressource spécifique sur le serveur. Elle comprend généralement une méthode (GET, PUT, etc.), une URL pointant vers la ressource, des en-têtes contenant des informations supplémentaires (comme le type de contenu accepté), et parfois un corps pour les données envoyées. Le serveur traite la requête et renvoie une réponse avec un code de statut (par exemple, 200 pour succès, 404 pour non trouvé) et le contenu demandé.

Parmi les méthodes HTTP les plus courantes, GET est utilisée pour récupérer des données d’un serveur sans modifier l’état de la ressource : les paramètres sont appendus à l’URL sous forme de chaîne de requête, ce qui les rend visibles, limités en taille et propices à la mise en cache, mais moins sécurisés pour des informations sensibles ; elle est idempotente, c’est-à-dire que plusieurs appels identiques produisent le même résultat sans effet secondaire. À l’opposé, POST sert à envoyer des données au serveur pour créer ou mettre à jour une ressource, en plaçant les paramètres dans le corps de la requête, ce qui les rend invisibles dans l’URL, permet de transmettre des volumes plus importants (y compris des fichiers) et offre une meilleure confidentialité, bien que la sécurité réelle repose sur l’utilisation de HTTPS ; contrairement à GET, POST n’est pas idempotente et n’est généralement pas mise en cache. En pratique, on privilégie GET pour des opérations de lecture simples comme des recherches ou des filtres, et POST pour des soumissions de formulaires ou des envois de données confidentielles.

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