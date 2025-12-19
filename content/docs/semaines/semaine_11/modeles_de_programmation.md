---
title: "Modèles de programmation"
weight: 20
---

# Modèles de programmation XML

Il y a plusieurs façons de traiter du XML. Chaque méthode a ses avantages et ses inconvénients. Bien que ce module s'intéresse surtout à l'approche DOM, il est important de connaître l'ensemble des méthodologies possibles et d'avoir une idée des forces et faiblesses relatives de chacune.


### Traitement du XML comme du texte

Le traitement du XML comme du texte consiste à manipuler les fichiers XML en utilisant les fonctions de traitement de chaînes de caractères disponibles dans les langages de programmation. Cette approche est simple à implémenter mais peut être source d'erreurs si le XML n'est pas correctement formé.

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

Le traitement événementiel, comme SAX, lit le document XML de manière séquentielle et génère des événements à chaque élément rencontré. Cette méthode est efficace pour les gros fichiers mais nécessite une gestion manuelle de l'état.

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

StAX (Streaming API for XML) offre une approche "pull" plus intuitive que SAX, permettant au programmeur de contrôler la lecture du document XML de manière itérative.

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

Le modèle DOM (Document Object Model) charge l'intégralité du document XML en mémoire sous forme d'arbre d'objets, permettant une navigation et une manipulation faciles mais consommatrice de ressources.
Un document XML peut être vu comme un arbre. Le DOM charge tout le document en mémoire sous forme d'objets.
Le DOM sera vu en détail la semaine prochaine.

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

XSLT (eXtensible Stylesheet Language Transformations) est un langage de transformation XML qui permet de convertir des documents XML vers d'autres formats comme HTML ou texte de manière déclarative.
XSLT est idéal pour les transformations simples (XML → HTML, XML → texte…). Pour des traitements complexes avec bases de données, il est insuffisant.



### XPath
XPath est un langage d'expression qui permet de naviguer et d'extraire des données spécifiques dans un document XML de manière concise et puissante.
XPath permet d'extraire très simplement des données depuis Java.

```java
import javax.xml.parsers.*;
import javax.xml.xpath.*;

DocumentBuilder builder = DocumentBuilderFactory.newInstance()
    .newDocumentBuilder();
Document doc = builder.parse("http://www.mondomaine.com/monfichier.xml");

XPath xpath = XPathFactory.newInstance().newXPath();
String title = xpath.evaluate("//nom/text()", doc);
```

### Sérialization Java

La sérialisation en Java permet de convertir l'état d'un objet en un flux d'octets, afin de le stocker (par exemple dans un fichier) ou de le transmettre sur un réseau. Le processus inverse, la désérialisation, recrée l'objet à partir de ce flux. Ce mécanisme est particulièrement utile pour persister des données ou échanger des objets entre applications.

L'interface centrale est `java.io.Serializable`, située dans le package `java.io`. Il s'agit d'une interface marqueur : elle ne contient aucune méthode ni champ à implémenter. Une classe devient sérialisable simplement en l'implémentant. Toutes ses sous-classes héritent automatiquement de cette propriété. Si un objet référencé n'implémente pas `Serializable`, une exception `NotSerializableException` est levée lors de la sérialisation.

Pour effectuer la sérialisation, on utilise `ObjectOutputStream` avec sa méthode `writeObject()`. Pour la désérialisation, `ObjectInputStream` et `readObject()`. Les champs statiques ne sont pas sérialisés, car ils appartiennent à la classe, pas à l'instance. Les champs marqués `transient` sont exclus du processus ; ils reprennent leur valeur par défaut lors de la désérialisation.

Un aspect important est la gestion des versions avec `serialVersionUID`. Il s'agit d'un champ `private static final long` que l'on déclare explicitement dans la classe. Sans cela, la JVM calcule une valeur par défaut basée sur la structure de la classe (méthodes, champs, etc.). Toute modification de la classe peut changer cette valeur, provoquant une `InvalidClassException` lors de la désérialisation d'un ancien flux. Il est recommandé de toujours définir un `serialVersionUID` explicite pour assurer la compatibilité.

Pour un contrôle plus fin, on peut implémenter des méthodes privées comme `writeObject()` et `readObject()` pour personnaliser le processus, ou utiliser `Externalizable` pour une implémentation complète (avec `writeExternal()` et `readExternal()`).

Voici un exemple complet et fonctionnel de sérialisation/désérialisation en Java utilisant l'interface Serializable. Le programme crée un objet, le sérialise dans un fichier, puis le désérialise et l'affiche.

{{<inlineJava path="ExempleSerializable.java">}}
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

class Personne implements Serializable {
    private static final long serialVersionUID = 1L;
    
    private String nom;
    private int age;
    private transient String motDePasse; // ne sera pas sérialisé
    
    public Personne(String nom, int age, String motDePasse) {
        this.nom = nom;
        this.age = age;
        this.motDePasse = motDePasse;
    }
    
    @Override
    public String toString() {
        return "Personne{nom='" + nom + "', age=" + age + ", motDePasse='" + motDePasse + "'}";
    }
}

public class ExempleSerializable {
    private static final String FICHIER = "personne.ser";
    
    public static void main(String[] args) {
        // Sérialisation
        Personne originale = new Personne("Alice", 30, "secret123");
        System.out.println("Objet original : " + originale);
        
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(FICHIER))) {
            oos.writeObject(originale);
            System.out.println("Sérialisation réussie dans " + FICHIER);
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        // Désérialisation
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(FICHIER))) {
            Personne recuperee = (Personne) ois.readObject();
            System.out.println("Objet désérialisé : " + recuperee);
            // Note : motDePasse vaut null car il était transient
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
{{</inlineJava>}}

### Réflexion

La réflexion joue un rôle crucial dans les mécanismes de sérialisation et de désérialisation en Java, permettant un traitement générique et dynamique des objets sans nécessiter de code spécifique pour chaque classe. Par exemple, la sérialisation native de Java (via `java.io.Serializable`) utilise la réflexion pour inspecter automatiquement les champs d'une classe, y compris les champs privés, et les écrire dans un flux binaire. Lors de la désérialisation, elle crée une instance vide de la classe (sans appeler de constructeur) et remplit les champs via la réflexion, en ignorant les validations potentielles des constructeurs.

Cette approche rend la sérialisation transparente.Des bibliothèques tierces comme Gson ou Jackson exploitent également la réflexion pour des formats comme JSON ou XML. Elles inspectent les champs (via `getDeclaredFields()`) ou les méthodes getter/setter, lisent ou écrivent leurs valeurs dynamiquement, et gèrent récursivement les objets imbriqués, les collections ou les types génériques.

Voici un exemple simple illustrant comment implémenter une sérialisation basique vers JSON en utilisant la réflexion. Considérons à nouveau la classe `Personne` :

```java
public class Personne {
    private String nom;
    private int age;

    public Personne(String nom, int age) {
        this.nom = nom;
        this.age = age;
    }

    // Getters pour l'exemple
    public String getNom() { return nom; }
    public int getAge() { return age; }

    @Override
    public String toString() {
        return "Personne{nom='" + nom + "', age=" + age + "}";
    }
}
```

Une méthode de sérialisation personnalisée en JSON via réflexion pourrait ressembler à ceci (simplifiée, sans gestion des cycles ou des types complexes).

{{<inlineJava path="SimpleJsonSerializer.java">}}
import java.lang.reflect.Field;
import java.util.StringJoiner;

class Personne {
    private String nom;
    private int age;

    public Personne(String nom, int age) {
        this.nom = nom;
        this.age = age;
    }

    // Getters pour l'exemple
    public String getNom() { return nom; }
    public int getAge() { return age; }

    @Override
    public String toString() {
        return "Personne{nom='" + nom + "', age=" + age + "}";
    }
}

public class SimpleJsonSerializer {
    public static String serialize(Object obj) throws IllegalAccessException {
        Class<?> classe = obj.getClass();
        StringJoiner json = new StringJoiner(", ", "{", "}");
        
        for (Field field : classe.getDeclaredFields()) {
            field.setAccessible(true); // Accès aux champs privés
            Object value = field.get(obj);
            String valueStr = value instanceof String ? "\"" + value + "\"" : String.valueOf(value);
            json.add("\"" + field.getName() + "\": " + valueStr);
        }
        
        return json.toString();
    }

    public static void main(String[] args) throws Exception {
        Personne p = new Personne("Alice", 30);
        String json = serialize(p);
        System.out.println(json); // Affiche : {"nom": "Alice", "age": 30}
    }
}
{{</inlineJava>}}




Pour la désérialisation, on pourrait instancier la classe via réflexion (`classe.getDeclaredConstructor().newInstance()`), puis setter les valeurs des champs de la même manière. Des bibliothèques comme Jackson font cela de façon beaucoup plus robuste, en gérant les annotations (comme `@JsonProperty`) pour personnaliser le mapping. (Les annotations en Java sont des métadonnées prenant la forme `@...` que l'on peut ajouter au code source pour fournir des informations supplémentaires au compilateur, aux outils de développement ou aux programmes exécutés à l'exécution. 
Vous pouvez même définir vos propres annotations.)



### Traitement par abstraction

Le traitement par abstraction utilise des bibliothèques de haut niveau qui masquent la complexité du XML, permettant de travailler avec des objets métier sans se soucier du format de sérialisation. 
De nombreuses bibliothèques (JAXB, bases de données, frameworks) manipulent du XML sans jamais vous forcer à écrire du XML à la main. Ils utilisent souvent
la réflexion.



### Sérialisation XML Java Beans

La sérialisation XML d'objet Java avec Bean permet de convertir des objets Java en XML et vice-versa, facilitant la persistance et l'échange de données.
Prenez quelques secondes pour exécuter le programme suivant.

{{<inlineJava path="Serialization.java">}}
import java.beans.*;
import java.io.*;

public class Serialization {
    public static void main(String[] args) {
        try {
            String o = new String("Un objet java");
            File f = new File("test.xml");

            // Sérialisation en XML
            XMLEncoder e = new XMLEncoder(
                new BufferedOutputStream(new FileOutputStream(f)));
            e.writeObject(o);
            e.close();

            // Désérialisation
            XMLDecoder d = new XMLDecoder(
                new BufferedInputStream(new FileInputStream(f)));
            Object lu = d.readObject();
            d.close();

            // Affichage clair du résultat
            System.out.println("Objet original : " + o);
            System.out.println("Objet lu depuis le fichier XML : " + lu);
            System.out.println("Les deux objets sont égaux : " + lu.equals(o));
            System.out.println("Type de l'objet lu : " + lu.getClass().getName());

        } catch (Exception ex) {
            System.err.println("Erreur lors de la sérialisation/désérialisation :");
            ex.printStackTrace();
        }
    }
}
{{</inlineJava>}}




Ce programme montre un exemple simple de sérialisation et de désérialisation d’un objet Java en format XML à l’aide des classes XMLEncoder et XMLDecoder du package java.beans. Contrairement à la sérialisation binaire classique avec ObjectOutputStream, ces deux classes permettent de transformer des objets Java en un fichier XML lisible par un humain, puis de reconstruire l’objet à partir de ce fichier. Elles sont particulièrement pratiques pour sauvegarder l’état d’objets simples (String, collections, beans Java standards) de façon portable et modifiable manuellement.

Dans la méthode main, on commence par créer un objet  simple : une instance de String contenant le texte "Un objet java". Ensuite, on crée un fichier nommé "test.xml". C’est dans ce fichier que l’objet sera sauvegardé au format XML. On utilise un XMLEncoder enveloppé dans un BufferedOutputStream et un FileOutputStream pour écrire efficacement les données. La méthode writeObject(o) déclenche la conversion de l’objet String en une représentation XML complète, puis e.close() ferme proprement le flux et écrit effectivement le contenu dans le fichier.

Immédiatement après la sérialisation, le programme passe à la désérialisation. On ouvre le même fichier "test.xml" en lecture avec un XMLDecoder, également entouré d’un BufferedInputStream pour optimiser les performances. L’appel à d.readObject() lit le premier (et ici unique) objet présent dans le XML et le reconstruit en mémoire sous forme d’objet Java. Comme le fichier a été généré par XMLEncoder, la reconstruction est parfaitement fidèle : on retrouve exactement le même String d’origine.

Pour vérifier que tout a fonctionné correctement, le programme affiche plusieurs informations : l’objet original, l’objet reconstitué, le résultat du test d’égalité avec equals() (qui renvoie true), et enfin le type réel de l’objet lu (java.lang.String). Cela prouve que non seulement la valeur est identique, mais que l’objet a bien été recréé avec son vrai type et non comme un type générique Object ou autre.

Enfin, tout le code est placé dans un bloc try-catch qui attrape n’importe quelle Exception (problème d’accès au fichier, erreur de parsing XML, etc.) et affiche la stack trace complète sur la sortie d’erreur. Cela rend le programme robuste et facile à déboguer. En exécutant ce code, vous obtiendrez un fichier test.xml contenant une représentation XML claire de la String, et vous verrez dans la console que l’objet a été parfaitement sauvegardé et restauré sans aucune perte d’information.

Cette approche ne fonctionne pas avec tout objet Java, et c’est une limitation importante de XMLEncoder/XMLDecoder.
Ces classes ne gèrent correctement que les objets dits « Java Beans » ou les types primitifs et leurs wrappers, les String, les collections standards (List, Map, Set…), les arrays, les Date, et quelques autres classes courantes du JDK. Pour qu’un objet soit sérialisable en XML avec ce mécanisme, il doit respecter les propriétés suivantes : il doit avoir un constructeur sans argument (constructor par défaut), ses propriétés doivent être accessibles via des getters et setters respectant la convention JavaBeans (getNom() / setNom() ou isNom() pour les boolean), et il ne doit pas contenir de références circulaires complexes ni de champs transient qui seraient ignorés.


En Java, les getters et setters sont des méthodes conventionnelles utilisées pour accéder et modifier les attributs privés d'une classe, dans le cadre de l'encapsulation, un principe fondamental de la programmation orientée objet. Un getter, souvent préfixé par "get", permet de récupérer la valeur d'un attribut sans exposer directement celui-ci, tandis qu'un setter, préfixé par "set", autorise la modification de cette valeur tout en pouvant inclure des validations ou des contrôles pour garantir l'intégrité des données. Par exemple, considérons une classe simple représentant une personne.

```java
public class Personne {
    private String nom;
    private int age;

    // Getter pour nom
    public String getNom() {
        return nom;
    }

    // Setter pour nom
    public void setNom(String nom) {
        this.nom = nom;
    }

    // Getter pour age
    public int getAge() {
        return age;
    }

    // Setter pour age avec validation
    public void setAge(int age) {
        if (age >= 0 && age <= 150) {
            this.age = age;
        } else {
            throw new IllegalArgumentException("L'âge doit être entre 0 et 150");
        }
    }
}
```

Si vous essayez de sérialiser un objet personnalisé qui ne respecte pas ces règles (par exemple une classe sans constructeur vide, avec des champs private sans getters/setters, ou contenant des objets tiers comme une connexion JDBC, un Thread, un Socket, ou une classe du type java.awt.Component), XMLEncoder lèvera généralement une exception ou produira un XML incomplet, voire ignorera silencieusement certaines parties de l’objet.

De plus, XMLEncoder ne conserve pas l’identité des objets en cas de références partagées : chaque occurrence d’un même objet sera dupliquée lors de la désérialisation, contrairement à la sérialisation binaire classique qui préserve les références. Cela peut poser problème pour des structures de données complexes avec des graphes d’objets.

### Services web


Les services web REST utilisent les méthodes HTTP standard pour exposer des ressources XML via des API web, permettant l'interopérabilité entre différentes plateformes.

Les services web REST utilisent simplement HTTP (GET, POST, PUT, DELETE).
| Méthode | Description |
|---------|-------------|
| GET | Récupérer une ressource (sûre et idempotente) |
| POST | Créer ou modifier (non idempotente) |
| PUT | Créer/remplacer une ressource à l'URI donnée |
| DELETE | Supprimer une ressource |


Le programme Java suivant interroge le service de recherche SRU (Search/Retrieve via URL) de la Bibliothèque du Congrès américain pour récupérer l’enregistrement bibliographique MARC21 correspondant au titre exact « First Impressions of the New World ». Il construit une requête HTTP contenant les paramètres nécessaires (opération de recherche, version du protocole, critère de recherche sur le titre Dublin Core, limitation à un seul résultat et demande du format MARCXML), ouvre la connexion réseau, télécharge la réponse XML directement depuis l’URL, la parse en tenant compte des espaces de noms, puis utilise une expression XPath pour extraire précisément la chaîne du « leader » (les 24 premiers caractères de l’enregistrement MARC qui décrivent le type de document, son statut, sa longueur, etc.) et l’affiche dans la console. En résumé, il effectue une recherche catalographique distante et récupère un élément technique clé de la notice MARC correspondante.


{{<inlineJava path="Exemple.java">}}
import org.w3c.dom.Document;
import javax.xml.parsers.*;
import javax.xml.xpath.*;
import javax.xml.namespace.NamespaceContext;
import java.net.URL;
import java.util.Iterator;

public class Exemple {
    public static void main(String[] args) throws Exception {
        String base = "http://z3950.loc.gov:7090/voyager?";
        String requete = "operation=searchRetrieve&version=1.1" +
                         "&query=(dc.title=%22First%20Impressions%20of%20the%20New%20World%22)" +
                         "&maximumRecords=1&recordSchema=marcxml";

        String urlComplete = base + requete;

        // Création du parseur XML avec prise en charge des espaces de noms
        DocumentBuilderFactory fabrique = DocumentBuilderFactory.newInstance();
        fabrique.setNamespaceAware(true); // Indispensable pour les réponses MARCXML/SRU
        Document document = fabrique.newDocumentBuilder().parse(new URL(urlComplete).openStream());

        XPath xpath = XPathFactory.newInstance().newXPath();

        // Définition de l'espace de noms MARC21
        xpath.setNamespaceContext(new NamespaceContext() {
            @Override
            public String getNamespaceURI(String prefixe) {
                return "marc".equals(prefixe) ? "http://www.loc.gov/MARC21/slim" : null;
            }

            @Override
            public String getPrefix(String uri) { return null; }

            @Override
            public Iterator<String> getPrefixes(String uri) { return null; }
        });

        // Extraction du leader MARC
        String leader = xpath.evaluate("//marc:leader/text()", document);

        System.out.println("Leader MARC : " + leader);
    }
}
{{</inlineJava>}}

