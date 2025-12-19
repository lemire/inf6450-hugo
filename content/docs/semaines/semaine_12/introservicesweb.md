---
title: "Introduction aux services web"
weight: 72
---


## Introduction aux services web

Les services web sont des applications ou des ressources accessibles via Internet qui permettent à des programmes (clients) de communiquer avec des serveurs distants pour échanger des données ou exécuter des fonctionnalités. Ils reposent principalement sur le protocole HTTP (HyperText Transfer Protocol), un protocole de communication client-serveur sans état : chaque requête est traitée indépendamment, sans mémoire des échanges précédents. Un client envoie une requête comportant une méthode (comme GET ou POST), une adresse (URI), des en-têtes et éventuellement un corps, tandis que le serveur répond avec un code de statut, des en-têtes et un corps contenant les données demandées.

Dans le contexte moderne, la grande majorité des services web sont des API (interfaces de programmation applicatives) qui exposent des fonctionnalités sous forme de points d’accès (endpoints). Ces API permettent à une application Java, par exemple, de récupérer des informations (prévisions météo, profils utilisateurs) ou d’envoyer des données (création de ressources) sans connaître les détails d’implémentation du serveur. Le format d’échange le plus répandu est JSON (JavaScript Object Notation), un format texte léger, lisible par l’homme et la machine, composé de paires clé-valeur, de tableaux et d’objets imbriqués. JSON est devenu le standard pour les services web car il est simple, flexible et supporté nativement par la plupart des langages.


*Exemple de structure JSON typique renvoyée par un service web :*
```json
{
  "nom": "Alice",
  "age": 30,
  "estEtudiant": false,
  "competences": ["Java", "HTML", "JavaScript"]
}
```


### Exemple avec l’API Open-Meteo (requête GET et traitement JSON manuel)

Le programme suivant récupère et affiche les prévisions météo horaires pour Montréal en interrogeant l’API Open-Meteo. Il illustre l’utilisation de l’API HttpClient, la construction d’une requête GET, la gestion des réponses JSON de manière manuelle (sans bibliothèque externe), ainsi que le traitement des dates avec java.time.

{{<inlineJava path="WeatherForecast.java" lang="java">}}
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
public class WeatherForecast {
    public static void main(String[] args) {
        // Coordonnées de Montréal
        double latitude = 45.5017;
        double longitude = -73.5673;
        String url = "https://api.open-meteo.com/v1/forecast?latitude=" + latitude +
                     "&longitude=" + longitude + "&hourly=temperature_2m,precipitation";
        try {
            // Créer un client HTTP
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .GET()
                    .build();
            // Envoyer la requête et obtenir la réponse
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            String json = response.body();
            // Extraire les tableaux horaires
            String hourly = json.substring(json.indexOf("\"hourly\":{"));
            String times = extractArray(hourly, "\"time\":");
            String temperatures = extractArray(hourly, "\"temperature_2m\":");
            String precipitations = extractArray(hourly, "\"precipitation\":");
            // Formatter pour les dates
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm");
            // Afficher les prévisions pour les 12 prochaines heures
            System.out.println("Prévisions météo pour Montréal (prochaines 12 heures) :");
            LocalDateTime now = LocalDateTime.now();
            String[] timeArray = times.split(",");
            String[] tempArray = temperatures.split(",");
            String[] precipArray = precipitations.split(",");
            int count = 0;
            for (int i = 0; i < timeArray.length && count < 12; i++) {
                String time = timeArray[i].replace("[\"","").replace("\"]","").replace("\"","");
                LocalDateTime forecastTime = LocalDateTime.parse(time, formatter);
                if (forecastTime.isAfter(now)) {
                    double temp = Double.parseDouble(tempArray[i].replace("[","").replace("]",""));
                    double precip = Double.parseDouble(precipArray[i].replace("[","").replace("]",""));
                    System.out.printf("%s : %.1f°C, Précipitations : %.1f mm%n",
                            forecastTime.format(DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm")),
                            temp, precip);
                    count++;
                }
            }
        } catch (Exception e) {
            System.err.println("Erreur lors de la récupération des données : " + e.getMessage());
        }
    }
    // Méthode pour extraire un tableau JSON spécifique
    private static String extractArray(String json, String key) {
        int start = json.indexOf(key) + key.length();
        int end = json.indexOf("]", start) + 1;
        return json.substring(start, end);
    }
}
{{</inlineJava>}}


Ce programme Java récupère les prévisions météo horaires pour Montréal en interrogeant l’API publique Open-Meteo via une requête HTTP GET construite avec l’API HttpClient de Java 11. Il définit d’abord les coordonnées géographiques de la ville et assemble l’URL de requête demandant spécifiquement les températures à 2 mètres et les précipitations. Dans un bloc try-catch pour gérer les erreurs réseau ou de traitement, il crée un client HTTP, bâtit et envoie la requête, puis récupère la réponse sous forme de chaîne JSON. Le parsing du JSON est réalisé manuellement : une sous-chaîne isole la section "hourly", et une méthode auxiliaire extractArray extrait les tableaux correspondants aux horaires, températures et précipitations en repérant les crochets. Les dates au format ISO sont ensuite parsées avec DateTimeFormatter pour comparer chaque prévision à l’heure actuelle (via LocalDateTime.now()), filtrant ainsi les entrées futures. Enfin, une boucle affiche les 12 prochaines heures valides au format lisible, avec température en degrés Celsius et précipitations en millimètres, en nettoyant les chaînes pour convertir les valeurs numériques. 

### Exemple avec l’API Open-Meteo (requête GET et traitement JSON avec Jackson)

Le programme suivant récupère et affiche les prévisions météo horaires pour Montréal en interrogeant l’API Open-Meteo. Contrairement à la version manuelle, il utilise la bibliothèque Jackson pour parser la réponse JSON de manière robuste et structurée. Jackson permet de mapper directement le JSON vers des classes Java dédiées, évitant ainsi le parsing fragile basé sur des chaînes de caractères. Cela rend le code plus lisible, plus maintenable et moins sujet aux erreurs en cas de modifications mineures dans la structure du JSON.

Pour utiliser Jackson, ajoutez la dépendance suivante à votre projet (par exemple via Maven) :
```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.17.2</version>
</dependency>
```

Le programme définit deux classes internes : Hourly pour représenter la section "hourly" contenant les listes de données, et ForecastResponse pour l'objet racine de la réponse. Jackson désérialise automatiquement les tableaux en listes Java, et nous pouvons ensuite itérer facilement sur les données synchronisées (les indices correspondent entre time, temperature_2m et precipitation).

{{<inlineJava path="WeatherForecastJackson.java" lang="java">}}
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

public class WeatherForecastJackson {

    // Ignore extra fields in the JSON response to avoid crashes
    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class Hourly {
        public List<String> time;
        public List<Double> temperature_2m;
        public List<Double> precipitation;
    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class ForecastResponse {
        public Hourly hourly;
    }

    public static void main(String[] args) {
        double latitude = 45.5017;
        double longitude = -73.5673;
        String url = "https://api.open-meteo.com/v1/forecast?latitude=" + latitude +
                     "&longitude=" + longitude + "&hourly=temperature_2m,precipitation";

        try {
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .GET()
                    .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            // Jackson Mapper
            ObjectMapper mapper = new ObjectMapper();
            ForecastResponse forecast = mapper.readValue(response.body(), ForecastResponse.class);

            // Formatters
            DateTimeFormatter inputFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm");
            DateTimeFormatter outputFormatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");

            System.out.println("Prévisions météo pour Montréal (prochaines 12 heures) :");
            LocalDateTime now = LocalDateTime.now();

            if (forecast.hourly != null) {
                List<String> times = forecast.hourly.time;
                List<Double> temperatures = forecast.hourly.temperature_2m;
                List<Double> precipitations = forecast.hourly.precipitation;

                int count = 0;
                for (int i = 0; i < times.size() && count < 12; i++) {
                    LocalDateTime forecastTime = LocalDateTime.parse(times.get(i), inputFormatter);
                    
                    // Filter for future forecasts
                    if (forecastTime.isAfter(now)) {
                        System.out.printf("%s : %.1f°C, Précipitations : %.1f mm%n",
                                forecastTime.format(outputFormatter),
                                temperatures.get(i),
                                precipitations.get(i));
                        count++;
                    }
                }
            }

        } catch (Exception e) {
            System.err.println("Erreur : " + e.getMessage());
            e.printStackTrace();
        }
    }
}
{{</inlineJava>}}

Cette approche avec Jackson est nettement plus élégante que le parsing manuel : elle gère automatiquement les structures imbriquées et les tableaux, tolère mieux les champs supplémentaires dans le JSON, et facilite l’extension du programme (par exemple, ajouter d’autres variables météo). En production, il est recommandé d’utiliser une bibliothèque comme Jackson ou Gson plutôt qu’un parsing texte maison.

### Exemple avec requêtes GET et POST (HttpClientExample)

Ce second programme montre deux usages classiques : une requête GET pour récupérer des données publiques depuis l’API GitHub, et une requête POST pour simuler l’envoi de données JSON vers une API de test. Il met en évidence la construction des en-têtes, du corps de requête et la gestion des réponses.

{{<inlineJava path="HttpClientExample.java" lang="java">}}
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
public class HttpClientExample {
    public static void main(String[] args) {
        // Création du client HTTP
        HttpClient client = HttpClient.newBuilder()
                .build();
        try {
            // Exemple de requête GET
            HttpRequest getRequest = HttpRequest.newBuilder()
                    .uri(URI.create("https://api.github.com/users/octocat"))
                    .header("Accept", "application/json")
                    .GET()
                    .build();
            HttpResponse<String> getResponse = client.send(getRequest,
                    HttpResponse.BodyHandlers.ofString());
            System.out.println("GET Response Status: " + getResponse.statusCode());
            System.out.println("GET Response Body: " + getResponse.body());
            // Exemple de requête POST
            String jsonPayload = "{\"title\": \"Test\", \"body\": \"Test request\"}";
            HttpRequest postRequest = HttpRequest.newBuilder()
                    .uri(URI.create("https://jsonplaceholder.typicode.com/posts"))
                    .header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(jsonPayload, StandardCharsets.UTF_8))
                    .build();
            HttpResponse<String> postResponse = client.send(postRequest,
                    HttpResponse.BodyHandlers.ofString());
            System.out.println("\nPOST Response Status: " + postResponse.statusCode());
            System.out.println("POST Response Body: " + postResponse.body());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
{{</inlineJava>}}


Ce programme Java démontre l’utilisation de l’API HttpClient introduite en Java 11 pour effectuer des requêtes HTTP synchrones, en illustrant deux méthodes courantes : GET pour récupérer des données et POST pour en envoyer. Il commence par créer un client HTTP configurable via HttpClient.newBuilder(), ici avec les paramètres par défaut. Dans un bloc try-catch capturant les exceptions potentielles (erreurs réseau, interruptions ou problèmes de réponse), il construit et envoie d’abord une requête GET vers l’API GitHub pour obtenir les informations publiques de l’utilisateur "octocat", en spécifiant l’en-tête "Accept: application/json" pour demander une réponse au format JSON ; le code de statut (généralement 200 en cas de succès) et le corps de la réponse (un objet JSON décrivant l’utilisateur) sont ensuite affichés. La seconde partie concerne une requête POST vers l’API de test jsonplaceholder.typicode.com, où un corps JSON simple est préparé comme payload, encodé en UTF-8, et envoyé avec l’en-tête "Content-Type: application/json" pour indiquer le format des données ; le serveur simule la création d’une ressource et renvoie un code de statut (typiquement 201 pour création) accompagné d’un corps JSON enrichi (par exemple avec un ID généré), qui est également affiché. Ce code met en évidence la simplicité de construction des requêtes (via un builder), la gestion des en-têtes et du corps, ainsi que le traitement basique des réponses, tout en soulignant l’importance de la gestion d’exceptions dans les communications réseau.