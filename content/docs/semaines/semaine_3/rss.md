---
title: "Les formats RSS et Atom"
weight: 50
---

# Les formats RSS et Atom

RSS (Really Simple Syndication) et Atom sont deux formats de syndication de contenu web qui permettent de diffuser automatiquement des mises à jour (articles, billets de blog, balados, vidéos, etc.) sans avoir à visiter manuellement chaque site. Ils sont nés au début des années 2000, à une époque où les blogs explosaient et où les lecteurs voulaient centraliser leurs sources d’information.

#### RSS : l’original
La première version de RSS est apparue en 1999 (Netscape), mais c’est la version RSS 2.0 (2002, publiée par Dave Winer sous licence Creative Commons) qui s’est imposée comme le standard le plus utilisé.  
Un flux RSS est un fichier XML structuré contenant :
- les métadonnées du site (titre, description, lien, langue)  
- une liste d’« items » (articles) avec titre, lien, description, date de publication, et souvent un GUID unique.


#### Atom : le successeur normalisé
Atom 1.0 a été standardisé en 2005 par l’IETF (RFC 4287). Il corrige les ambiguïtés de RSS et apporte :
- une séparation claire entre le flux (feed) et les entrées (entry)  
- un support natif des résumés et du contenu complet  
- une gestion plus rigoureuse des dates, des auteurs, des identifiants permanents  
- un protocole de publication (AtomPub, RFC 5023) qui permet aussi de créer ou modifier du contenu à distance.

Atom est un peu plus verbeux que RSS, mais plus propre et plus extensible. 

#### Quelques exemples

Prenez le temps de consulter les sources suivantes.

1. **Le Devoir** – format RSS 2.0  
   https://www.ledevoir.com/flux-rss 

2. **Ici Radio-Canada Infos** – format Atom 1.0  
   https://ici.radio-canada.ca/rss/4159  

3. **La Presse** – format RSS 2.0  
   https://www.lapresse.ca/rss.php  
   (flux généraux et par section, par exemple : https://www.lapresse.ca/actualites/rss.xml)

4. **Journal de Montréal** (groupe Quebecor) – format RSS 2.0  
   https://www.journaldemontreal.com/rss  



#### Exemple Java (Radio-Canada)

Prenez quelques secondes pour exécuter ce programme qui charge les dernières nouvelles de Radio-Canada 
en utilisant le XML.

{{<inlineJava path="RadioCanadaCinqDernieres.java">}}
import java.io.InputStream;
import java.net.URL;
import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.XMLStreamReader;

public class RadioCanadaCinqDernieres {

    public static void main(String[] args) {
        String rssUrl = "https://ici.radio-canada.ca/info/rss/info/a-la-une";

        try {
            System.out.println("Les 5 dernières nouvelles de Radio-Canada :\n");

            URL url = new URL(rssUrl);
            try (InputStream in = url.openStream()) {
                XMLInputFactory factory = XMLInputFactory.newInstance();
                XMLStreamReader reader = factory.createXMLStreamReader(in, "UTF-8");

                int compteur = 0;
                String titreCourant = null;

                while (reader.hasNext() && compteur < 5) {
                    int event = reader.next();

                    if (event == XMLStreamReader.START_ELEMENT && "title".equals(reader.getLocalName())) {
                        reader.next(); // passer aux caractères
                        if (reader.getEventType() == XMLStreamReader.CHARACTERS) {
                            titreCourant = reader.getText().trim();
                        }
                    }

                    if (event == XMLStreamReader.END_ELEMENT && "item".equals(reader.getLocalName()) && titreCourant != null) {
                        compteur++;
                        System.out.println(compteur + ". " + titreCourant);
                        titreCourant = null;
                    }
                }
                reader.close();
            }

        } catch (Exception e) {
            System.err.println("Erreur lors du chargement du flux : " + e.getMessage());
        }
    }
}
{{</inlineJava>}}



#### Exemple Java (Blogue de Daniel Lemire)

Prenez quelques secondes pour exécuter ce programme qui charge les dernières nouvelles du blogue de Daniel Lemire
en utilisant le XML.

{{<inlineJava path="RssFeedReader.java">}}
import java.io.InputStream;
import java.net.URL;
import java.net.HttpURLConnection;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
public class RssFeedReader {
    public static void main(String[] args) {
        try {
            // Connexion au flux RSS
            String rssUrl = "https://lemire.me/blog/feed/";
            URL url = new URL(rssUrl);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            // Vérification de la réponse
            int responseCode = connection.getResponseCode();
            if (responseCode != HttpURLConnection.HTTP_OK) {
                System.out.println("Erreur : Code de réponse " + responseCode);
                return;
            }
            // Parsing du XML
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            InputStream inputStream = connection.getInputStream();
            Document doc = builder.parse(inputStream);
            doc.getDocumentElement().normalize();
            // Extraction des informations du channel
            NodeList channelList = doc.getElementsByTagName("channel");
            if (channelList.getLength() > 0) {
                Element channel = (Element) channelList.item(0);
                String channelTitle = getElementValue(channel, "title");
                String channelDescription = getElementValue(channel, "description");
                String channelLink = getElementValue(channel, "link");
                System.out.println("Flux RSS : " + channelTitle);
                System.out.println("Description : " + channelDescription);
                System.out.println("Lien : " + channelLink);
                System.out.println("Articles :");
            }
            // Extraction des items (articles)
            NodeList itemList = doc.getElementsByTagName("item");
            for (int i = 0; i < itemList.getLength(); i++) {
                Element item = (Element) itemList.item(i); 
                String title = getElementValue(item, "title");
                String link = getElementValue(item, "link");
                String pubDate = getElementValue(item, "pubDate");
                System.out.println("Article " + (i + 1) + ":");
                System.out.println("  Titre : " + title);
                System.out.println("  Lien : " + link);
                System.out.println("  Date de publication : " + pubDate);
                System.out.println();
            }
            inputStream.close();
            connection.disconnect();
        } catch (Exception e) {
            System.out.println("Erreur lors de la récupération du flux RSS : " + e.getMessage());
            e.printStackTrace();
        }
    }
    // Méthode utilitaire pour extraire la valeur d'un élément
    private static String getElementValue(Element parent, String tagName) {
        NodeList nodeList = parent.getElementsByTagName(tagName);
        if (nodeList.getLength() > 0 && nodeList.item(0).getFirstChild() != null) {
            return nodeList.item(0).getFirstChild().getNodeValue();
        }
        return "";
    }
}
{{</inlineJava>}}
