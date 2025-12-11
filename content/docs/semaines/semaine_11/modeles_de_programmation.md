---
title: "Modèles de programmation"
weight: 20
---

# Modèles de programmation XML

Il y a plusieurs façons de traiter du XML. Chaque méthode a ses avantages et ses inconvénients. Bien que ce module s'intéresse surtout à l'approche DOM, il est important de connaître l'ensemble des méthodologies possibles et d'avoir une idée des forces et faiblesses relatives de chacune.
### Traitement du XML comme du texte

Un fichier XML est d'abord un fichier texte. Comme certains langages, tel Java, savent bien traiter les fichiers en format texte, ils peuvent directement traiter le XML.

```java
int montant = 10;
String nom = "Gérard Beauford";
System.out.println("<?xml version=\"1.0\" ?>\n<facture><montant>" + montant +
    "</montant><nom>" + nom + "</nom></facture>");
```

Cependant, comment savoir si le XML produit est bien formé ? Dans l'exemple précédent, le document affiché ne sera pas du XML bien formé à cause de l'accent dans « Gérard » si l'environnement n'utilise pas UTF-8. Il est donc préférable d'utiliser des librairies dédiées au XML.

```xml
<?xml version="1.0" encoding="ISO-8859-1" standalone="no"?>
<facture>
  <montant>432</montant>
  <nom>Gérard Beauford</nom>
</facture>
```

```xml
<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>
<!DOCTYPE facture [
  <!ELEMENT facture (montant, nom)>
  <!ELEMENT montant (#PCDATA)>
  <!ELEMENT nom (#PCDATA)>
  <!ATTLIST nom surnom CDATA "Joe">
]>
<facture><montant>432</montant><nom>Gérard Beauford</nom></facture>
```

### Traitement événementiel

Le traitement événementiel (SAX, XNI…) lit le document séquentiellement et déclenche des événements.

Pour le document suivant :

```xml
<facture><montant>432</montant><nom>Maman</nom></facture>
```

Événements SAX générés :

1. Début du document
2. Début d'un élément « facture »
3. Début d'un élément « montant »
4. Texte « 432 »
5. Fin d'un élément « montant »
6. Début d'un élément « nom »
7. Texte « Maman »
8. Fin d'un élément « nom »
9. Fin d'un élément « facture »
10. Fin du document

```java
import java.io.*;
import org.xml.sax.*;
import org.xml.sax.helpers.*;

public class MonApplicationSAX extends DefaultHandler {

    public void startElement(String uri, String name, String qName, Attributes atts) {
        if (uri.length() > 0)
            System.out.println("Début de l'élément " + uri + ":" + qName);
        else
            System.out.println("Début de l'élément " + name);
    }

    public void endElement(String uri, String name, String qName) {
        if (uri.length() > 0)
            System.out.println("Fin de l'élément " + uri + ":" + qName);
        else
            System.out.println("Fin de l'élément " + name);
    }

    public void characters(char[] ch, int start, int length) {
        System.out.print(new String(ch, start, length));
    }

    public static void main(String[] args) throws Exception {
        XMLReader xr = XMLReaderFactory.createXMLReader();
        xr.setContentHandler(new MonApplicationSAX());
        xr.parse(new InputSource(new FileReader(args[0])));
    }
}
```

### Traitement avec itérateurs (StAX)

StAX propose une approche « pull » plus intuitive.

```java
import javax.xml.stream.*;
import java.net.*;
import java.io.*;

public class staxex {
    public static void main(String[] args) {
        String input = args[0];
        try {
            URL u = new URL(input);
            InputStream in = u.openStream();
            XMLInputFactory factory = XMLInputFactory.newInstance();
            XMLStreamReader parser = factory.createXMLStreamReader(in);
            for (int event = parser.next();
                 event != XMLStreamConstants.END_DOCUMENT;
                 event = parser.next()) {
                switch (event) {
                    case XMLStreamConstants.START_ELEMENT:
                        System.out.println(parser.getLocalName());
                        break;
                    case XMLStreamConstants.END_ELEMENT:
                        System.out.println(parser.getLocalName());
                        break;
                    case XMLStreamConstants.CDATA:
                        System.out.print(parser.getText());
                        break;
                }
            }
            parser.close();
        } catch (Exception ex) { System.out.println(ex); }
    }
}
```

### Traitement avec modèle en arbre (DOM)

Un document XML peut être vu comme un arbre. Le DOM charge tout le document en mémoire sous forme d'objets.

```xml
<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>
<!DOCTYPE facture [...]>
<facture><montant>432</montant>
<nom>Gérard Beauford</nom></facture>
```

Représentation en arbre :

```
 Document
 └─ facture
     ├─ montant → "432"
     └─ nom (surnom="Joe") → "Gérard Beauford"
```

### Transformations (XSLT)

XSLT est idéal pour les transformations simples (XML → HTML, XML → texte…). Pour des traitements complexes avec bases de données, il est insuffisant.

### XPath

XPath permet d'extraire très simplement des données depuis Java :

```java
import javax.xml.parsers.*;
import javax.xml.xpath.*;

DocumentBuilder builder = DocumentBuilderFactory.newInstance()
    .newDocumentBuilder();
Document doc = builder.parse("http://www.mondomaine.com/monfichier.xml");

XPath xpath = XPathFactory.newInstance().newXPath();
String title = xpath.evaluate("//nom/text()", doc);
```

### XML comme extension d'un langage (E4X)
```

JavaScript for XML permet d'écrire directement du XML dans le code :

```xml
 var sales = <sales vendor="John">
  <item type="peas" price="4" quantity="6"/>
  <item type="carrot" price="3" quantity="10"/>
  <item type="chips" price="5" quantity="3"/>
</sales>;
```

### Traitement par abstraction

De nombreuses bibliothèques (JAXB, bases de données, frameworks) manipulent du XML sans jamais vous forcer à écrire du XML à la main.

### Sérialisation XML (Java Beans)
```java
import java.beans.*;
import java.io.*;

public class Serialization {
    public static void main(String[] args) throws IOException {
        String o = new String("Un objet java");
        File f = new File("test.xml");
        XMLEncoder e = new XMLEncoder(
            new BufferedOutputStream(new FileOutputStream(f)));
        e.writeObject(o); e.close();
        XMLDecoder d = new XMLDecoder(
            new BufferedInputStream(new FileInputStream(f)));
        Object lu = d.readObject(); d.close();
        System.out.println(lu.equals(o)); // true
    }
}
```
```xml
<?xml version="1.0" encoding="UTF-8"?>
<java version="21" class="java.beans.XMLDecoder">
  <string>Un objet java</string>
</java>
```

### Services web

Les services web REST utilisent simplement HTTP (GET, POST, PUT, DELETE).
| Méthode | Description |
|---------|-------------|
| GET | Récupérer une ressource (sûre et idempotente) |
| POST | Créer ou modifier (non idempotente) |
| PUT | Créer/remplacer une ressource à l'URI donnée |
| DELETE | Supprimer une ressource |

Exemple de requête vers la Library of Congress :


{{<inlineJava path="example.java">}}
import org.w3c.dom.*;
import javax.xml.parsers.*;
import javax.xml.xpath.*;

public class example {
    public static void main(String[] args) throws Exception {
        String base = "http://z3950.loc.gov:7090/voyager?";
        String query = "operation=searchRetrieve&version=1.1&query=(dc.title=%22First Impressions of the New World%22)";
        Document doc = DocumentBuilderFactory.newInstance()
            .newDocumentBuilder().parse(base + query);
        XPath xpath = XPathFactory.newInstance().newXPath();
        System.out.println("leader : " + xpath.evaluate("//leader/text()", doc));
    }
}
{{</inlineJava>}}

