---
title: "Le fichier sitemap.xml"
weight: 40
---

# Le fichier sitemap.xml

Le sitemap.xml est un fichier au format XML qui liste les URLs importantes d'un site web afin d'aider les moteurs de recherche (Google, Bing, etc.) à découvrir et indexer plus efficacement ses pages. Il est particulièrement utile pour les sites volumineux, les nouveaux sites ou ceux qui possèdent beaucoup de contenu difficilement accessible par les liens internes classiques. Bien qu'il ne garantisse pas l'indexation de toutes les pages listées, il constitue un signal fort pour les crawlers et améliore généralement la couverture du site.
Ce fichier doit être placé à la racine du site[](https://example.com/sitemap.xml) et suivre le protocole officiel défini sur sitemaps.org. On peut y indiquer pour chaque URL la date de dernière modification (`<lastmod>`), la fréquence de mise à jour estimée (`<changefreq>`), et une priorité relative (`<priority>`) entre 0.0 et 1.0. Depuis quelques années, il est aussi possible d'utiliser des sitemaps vidéo, image, news ou même des index de sitemaps quand le fichier dépasse 50 000 URLs ou 50 Mo.
Voici un exemple simple de sitemap.xml contenant quatre pages :
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

  <url>
    <loc>https://www.example.com/</loc>
    <lastmod>2025-12-01</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>

  <url>
    <loc>https://www.example.com/a-propos/</loc>
    <lastmod>2025-11-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>

  <url>
    <loc>https://www.example.com/blog/</loc>
    <lastmod>2025-12-04</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>

  <url>
    <loc>https://www.example.com/contact/</loc>
    <changefreq>yearly</changefreq>
    <priority>0.5</priority>
  </url>

</urlset>
```
## Activité

Pouvez-vous vérifier si le site de teluq.ca a un fichier sitemap.xml?

{{<inlineJava path="SitemapViewer.java">}}
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

public class SitemapViewer {

    public static void main(String[] args) {
        String urlString = "https://teluq.ca/sitemap.xml";

        try {
            URL url = new URL(urlString);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setInstanceFollowRedirects(true);

            // Ouvrir la connexion et lire le contenu ligne par ligne
            try (BufferedReader reader = new BufferedReader(
                    new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {

                System.out.println("Contenu de " + urlString + " (premières 20 lignes) :\n");
                String line;
                int count = 0;
                while ((line = reader.readLine()) != null && count < 20) {
                    System.out.println(line);
                    count++;
                }
                if (count == 20) {
                    System.out.println("... (tronqué pour la démonstration)");
                }
            }

        } catch (Exception e) {
            System.err.println("Erreur lors du chargement du sitemap : " + e.getMessage());
            e.printStackTrace();
        }
    }
}
{{</inlineJava>}}
