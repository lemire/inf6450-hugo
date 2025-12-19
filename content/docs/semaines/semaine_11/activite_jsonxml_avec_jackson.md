---
title: "Activité JSON/XML avec Jackson"
weight: 30
---

# Activité JSON/XML avec Jackson

<p>
 <a href="https://github.com/lemire/javajackson">
  Nous vous invitons maintenant à faire une activité practice avec la librairie Java Jackson.
 </a>
</p>



## Utilisation de Jackson 

Jackson est une bibliothèque Java pour la manipulation du XML et du JSON, développée par FasterXML.

## Sérialisation et désérialisation de base

La sérialisation convertit un objet Java en JSON via `writeValueAsString`. La désérialisation utilise `readValue`. Jackson ignore les champs sans getters et omet les valeurs null par défaut.

Voici un exemple.

{{<inlineJava path="ExempleBasique.java">}}
import com.fasterxml.jackson.databind.ObjectMapper;

class Personne {
    private String nom;
    private int age;

    public Personne() {} // Nécessaire pour la désérialisation

    public Personne(String nom, int age) {
        this.nom = nom;
        this.age = age;
    }

    public String getNom() { return nom; }
    public void setNom(String nom) { this.nom = nom; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
}

public class ExempleBasique {
    public static void main(String[] args) throws Exception {
        ObjectMapper mapper = new ObjectMapper();

        Personne personne = new Personne("Alice", 30);

        // Sérialisation
        String json = mapper.writeValueAsString(personne);
        System.out.println("JSON sérialisé :");
        System.out.println(json);

        // Désérialisation
        Personne deserialisee = mapper.readValue(json, Personne.class);
        System.out.println("\nObjet désérialisé : nom=" + deserialisee.getNom() + ", age=" + deserialisee.getAge());
    }
}
{{</inlineJava>}}

Ce code affiche un JSON compact et reconstruit l'objet.
La version XML est similaire.

{{<inlineJava path="ExempleXmlBasique.java">}}
import com.fasterxml.jackson.dataformat.xml.XmlMapper;

class Personne {
    private String nom;
    private int age;

    public Personne() {} // Nécessaire pour la désérialisation

    public Personne(String nom, int age) {
        this.nom = nom;
        this.age = age;
    }

    public String getNom() { return nom; }
    public void setNom(String nom) { this.nom = nom; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
}

public class ExempleXmlBasique {
    public static void main(String[] args) throws Exception {
        XmlMapper mapper = new XmlMapper();

        Personne personne = new Personne("Alice", 30);

        // Sérialisation en XML
        String xml = mapper.writeValueAsString(personne);
        System.out.println("XML sérialisé :");
        System.out.println(xml);

        // Désérialisation depuis XML
        Personne deserialisee = mapper.readValue(xml, Personne.class);
        System.out.println("\nObjet désérialisé : nom=" + deserialisee.getNom() + ", age=" + deserialisee.getAge());
    }
}
{{</inlineJava>}}


## Mise en forme jolie et inclusion des null

Pour un JSON lisible, activez l'indentation. Pour inclure les null, configurez la politique d'inclusion.

{{<inlineJava path="ExempleMiseEnForme.java">}}
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.fasterxml.jackson.annotation.JsonInclude;

@JsonInclude(JsonInclude.Include.ALWAYS)
class Livre {
    private String titre;
    private String auteur;
    private Integer pages; // Peut être null

    public Livre() {}

    public Livre(String titre, String auteur, Integer pages) {
        this.titre = titre;
        this.auteur = auteur;
        this.pages = pages;
    }

    public String getTitre() { return titre; }
    public void setTitre(String titre) { this.titre = titre; }
    public String getAuteur() { return auteur; }
    public void setAuteur(String auteur) { this.auteur = auteur; }
    public Integer getPages() { return pages; }
    public void setPages(Integer pages) { this.pages = pages; }
}

public class ExempleMiseEnForme {
    public static void main(String[] args) throws Exception {
        ObjectMapper mapper = new ObjectMapper()
                .enable(SerializationFeature.INDENT_OUTPUT);

        Livre livre = new Livre("Programmation Java", "John Doe", null);

        String json = mapper.writeValueAsString(livre);
        System.out.println("JSON mis en forme avec nulls :");
        System.out.println(json);
    }
}
{{</inlineJava>}}

Cela produit un JSON indenté incluant les champs null grâce à l'annotation.

## Gestion des collections

Jackson gère nativement les collections Java.

{{<inlineJava path="ExempleCollections.java">}}
import com.fasterxml.jackson.databind.ObjectMapper;
import java.util.ArrayList;
import java.util.List;

public class ExempleCollections {
    public static void main(String[] args) throws Exception {
        ObjectMapper mapper = new ObjectMapper();

        List<String> fruits = new ArrayList<>();
        fruits.add("Pomme");
        fruits.add("Banane");
        fruits.add("Orange");

        // Sérialisation
        String json = mapper.writeValueAsString(fruits);
        System.out.println("Liste sérialisée :");
        System.out.println(json);

        // Désérialisation
        List<String> deserialisee = mapper.readValue(json, List.class);
        System.out.println("\nListe désérialisée :");
        System.out.println(deserialisee);
    }
}
{{</inlineJava>}}



## Objets imbriqués

Jackson traite les hiérarchies d'objets de manière transparente.

{{<inlineJava path="ExempleObjetsImbriques.java">}}
import com.fasterxml.jackson.databind.ObjectMapper;

class Adresse {
    private String ville;
    private String pays;

    public Adresse() {}
    public Adresse(String ville, String pays) {
        this.ville = ville;
        this.pays = pays;
    }

    public String getVille() { return ville; }
    public void setVille(String ville) { this.ville = ville; }
    public String getPays() { return pays; }
    public void setPays(String pays) { this.pays = pays; }
}

class Employe {
    private String nom;
    private Adresse adresse;

    public Employe() {}
    public Employe(String nom, Adresse adresse) {
        this.nom = nom;
        this.adresse = adresse;
    }

    public String getNom() { return nom; }
    public void setNom(String nom) { this.nom = nom; }
    public Adresse getAdresse() { return adresse; }
    public void setAdresse(Adresse adresse) { this.adresse = adresse; }
}

public class ExempleObjetsImbriques {
    public static void main(String[] args) throws Exception {
        ObjectMapper mapper = new ObjectMapper();

        Adresse adresse = new Adresse("New York", "USA");
        Employe employe = new Employe("Bob", adresse);

        String json = mapper.writeValueAsString(employe);
        System.out.println("Objet imbriqué sérialisé :");
        System.out.println(json);

        Employe deserialise = mapper.readValue(json, Employe.class);
        System.out.println("\nDésérialisé : nom=" + deserialise.getNom() + ", ville=" + deserialise.getAdresse().getVille());
    }
}
{{</inlineJava>}}


## Noms de champs personnalisés avec @JsonProperty

Utilisez l'annotation `@JsonProperty` pour renommer les champs dans le JSON.

{{<inlineJava path="ExempleJsonProperty.java">}}
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.ObjectMapper;

class Produit {
    @JsonProperty("product_id")
    private int id;

    @JsonProperty("product_name")
    private String nom;

    public Produit() {}
    public Produit(int id, String nom) {
        this.id = id;
        this.nom = nom;
    }

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public String getNom() { return nom; }
    public void setNom(String nom) { this.nom = nom; }
}

public class ExempleJsonProperty {
    public static void main(String[] args) throws Exception {
        ObjectMapper mapper = new ObjectMapper();

        Produit produit = new Produit(101, "Ordinateur portable");

        String json = mapper.writeValueAsString(produit);
        System.out.println("JSON avec noms personnalisés :");
        System.out.println(json);
    }
}
{{</inlineJava>}}


## Ignorer des champs avec @JsonIgnore

Pour exclure un champ, utilisez `@JsonIgnore`.

{{<inlineJava path="ExempleJsonIgnore.java">}}
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.databind.ObjectMapper;

class Utilisateur {
    private String nomUtilisateur;
    @JsonIgnore
    private String motDePasse;

    public Utilisateur() {}
    public Utilisateur(String nomUtilisateur, String motDePasse) {
        this.nomUtilisateur = nomUtilisateur;
        this.motDePasse = motDePasse;
    }

    public String getNomUtilisateur() { return nomUtilisateur; }
    public void setNomUtilisateur(String nomUtilisateur) { this.nomUtilisateur = nomUtilisateur; }
    public String getMotDePasse() { return motDePasse; }
    public void setMotDePasse(String motDePasse) { this.motDePasse = motDePasse; }
}

public class ExempleJsonIgnore {
    public static void main(String[] args) throws Exception {
        ObjectMapper mapper = new ObjectMapper();

        Utilisateur utilisateur = new Utilisateur("charlie", "caché");

        String json = mapper.writeValueAsString(utilisateur);
        System.out.println("JSON sans le champ ignoré :");
        System.out.println(json);
    }
}
{{</inlineJava>}}


## XML et JSON

L'exemple suivant qui montre à la fois JSON et XML.

{{<inlineJava path="App.java">}}
package fr.example.jackson;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;
class Person {
    private String name;
    private int age;
    public Person() {}
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
    @Override
    public String toString() {
        return "Person{name='" + name + "', age=" + age + "}";
    }
}
public class App {
    public static void main(String[] args) throws Exception {
        Person person = new Person("Jean Dupont", 30);
        // Sérialisation JSON
        ObjectMapper jsonMapper = new ObjectMapper();
        String json = jsonMapper.writeValueAsString(person);
        System.out.println("JSON: " + json);
        // Désérialisation JSON
        Person fromJson = jsonMapper.readValue(json, Person.class);
        System.out.println("Depuis JSON: " + fromJson);
        // Sérialisation XML
        XmlMapper xmlMapper = new XmlMapper();
        String xml = xmlMapper.writeValueAsString(person);
        System.out.println("XML: " + xml);
        // Désérialisation XML
        Person fromXml = xmlMapper.readValue(xml, Person.class);
        System.out.println("Depuis XML: " + fromXml);
    }
}
{{</inlineJava>}}

