---
title: "DOM"
weight: 20
---
# DOM

## Introduction

Nous supposons que vous disposez d’un environnement de développement Java et que vous ferez les exemples de ce tutoriel afin de mieux comprendre. Notre objectif est avant tout de vous rendre suffisamment à l’aise avec DOM pour pouvoir l’utiliser ; nous vous invitons toutefois à naviguer sur le web pour en apprendre davantage sur le sujet, au besoin.

L’API Java elle-même est disponible sur le [site d’Oracle](http://docs.oracle.com/javase/8/docs/api/). Pour pouvoir faire vos propres programmes, consultez l’API Java qui comprend tous les objets et fonctions du tutoriel.

## Notions de base

On dit qu’un modèle DOM est une structure en arbre. En informatique, un arbre est un graphe ou une structure constituée de nœuds, de façon telle que chaque nœud a un et un seul parent — ou aucun —, lequel a un seul ou plusieurs enfants. Un seul nœud est autorisé à ne pas avoir de parent : c’est le nœud-racine.

## Point de vue critique

L’API DOM est très utilisée et supportée dans de nombreux langages (Java, JavaScript, C#, C++, etc.). Cependant, elle consomme beaucoup de mémoire et nécessite souvent beaucoup de code pour des opérations simples. Malgré ces défauts, sa large adoption en fait une référence incontournable.

## Un document XML

Créons d’abord un document XML nommé « test.xml » :

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<liste>
    <joueur>
        <nom surnom="jojo">Jean</nom>
        <buts>32</buts>
    </joueur>
    <joueur>
        <nom surnom="Ma">Marie</nom>
        <buts>54</buts>
    </joueur>
</liste>
```

## Charger un document XML en Java

```java
import org.w3c.dom.*;
import javax.xml.parsers.*;

public class Test {
    public static void main(String[] args) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder parser = factory.newDocumentBuilder();
        Document doc = parser.parse(args[0]);
    }
}
```

## Accès à l’élément-racine

```java
import org.w3c.dom.*;
import javax.xml.parsers.*;

public class Test {
    public static void main(String[] args) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder parser = factory.newDocumentBuilder();
        Document doc = parser.parse(args[0]);

        Element racine = doc.getDocumentElement();
        System.out.println(racine.getTagName()); // affiche : liste
    }
}
```

## L’interface Node

| Type de nœud | getNodeName() | getNodeValue() |
|--------------|---------------|---------------|
| Attribut | nom de l’attribut | valeur de l’attribut |
| Élément | nom de l’élément | null |
| Texte | #text | le texte |

## Parcourir les enfants

{{<inlineJava path="Test.java">}}
import org.w3c.dom.*;
import javax.xml.parsers.*;
import java.io.StringReader;
import org.xml.sax.InputSource;
public class Test {
    public static void main(String[] args) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder parser = factory.newDocumentBuilder();
        String xml = """
<?xml version="1.0" encoding="ISO-8859-1"?>
<liste>
    <joueur>
        <nom surnom="jojo">Jean</nom>
        <buts>32</buts>
    </joueur>
    <joueur>
        <nom surnom="Ma">Marie</nom>
        <buts>54</buts>
    </joueur>
</liste>
""";
        Document doc = parser.parse(new InputSource(new StringReader(xml)));
        Element racine = doc.getDocumentElement();
        NodeList joueurs = racine.getElementsByTagName("joueur");
        for (int i = 0; i < joueurs.getLength(); i++) {
            Element joueur = (Element) joueurs.item(i);
            Element nom = (Element) joueur.getElementsByTagName("nom").item(0);
            Element buts = (Element) joueur.getElementsByTagName("buts").item(0);
            String nomJoueur = nom.getFirstChild().getNodeValue();
            String surnom = nom.getAttribute("surnom");
            String nbButs = buts.getFirstChild().getNodeValue();
            System.out.println(nomJoueur + " (" + surnom + ") : " + nbButs + " buts");
        }
    }
}
{{</inlineJava>}}


## Création d’un document XML depuis zéro

{{<inlineJava path="CreationDOM.java">}}
import org.w3c.dom.*;
import javax.xml.parsers.*;
import javax.xml.transform.*;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import java.io.FileWriter;
public class CreationDOM {
    public static void main(String[] args) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        Document doc = builder.newDocument();
        Element liste = doc.createElement("liste");
        doc.appendChild(liste);
        Element joueur1 = doc.createElement("joueur");
        Element nom1 = doc.createElement("nom");
        nom1.appendChild(doc.createTextNode("Jean"));
        nom1.setAttribute("surnom", "jojo");
        Element buts1 = doc.createElement("buts");
        buts1.appendChild(doc.createTextNode("32"));
        joueur1.appendChild(nom1);
        joueur1.appendChild(buts1);
        liste.appendChild(joueur1);
        TransformerFactory tf = TransformerFactory.newInstance();
        Transformer t = tf.newTransformer();
        t.setOutputProperty(OutputKeys.ENCODING, "ISO-8859-1");
        t.setOutputProperty(OutputKeys.INDENT, "yes");
        DOMSource source = new DOMSource(doc);
        StreamResult result = new StreamResult(new FileWriter("nouveau.xml"));
        t.transform(source, result);

        StreamResult consoleResult = new StreamResult(System.out);
        t.transform(source, consoleResult);
    }
}
{{</inlineJava>}}
