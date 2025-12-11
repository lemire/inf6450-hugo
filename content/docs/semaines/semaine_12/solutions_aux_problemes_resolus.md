---
title: "Solutions aux problèmes résolus"
weight: 50
---
<h1>
 Solutions aux problèmes résolus
</h1>
<h2>
 Solution du problème 1
</h2>
<p>
 Voici une solution possible (affichage récursif de l’arbre DOM avec indentation) :
</p>

```java
import org.w3c.dom.*;
import javax.xml.parsers.*;

public class Arbre {

    public static void traite(Node node, int niveau) {
        String indent = "";
        for (int i = 0; i < niveau; i++) {
            indent += "    "; // 4 spaces per level
        }

        System.out.println(indent + "Nom : " + node.getNodeName() +
                           " | Valeur : " + node.getNodeValue());

        NodeList enfants = node.getChildNodes();
        if (enfants != null) {
            for (int i = 0; i < enfants.getLength(); i++) {
                traite(enfants.item(i), niveau + 2);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder parser = factory.newDocumentBuilder();
        Document doc = parser.parse(args[0]);

        traite(doc, 0);
    }
}
```

<h3>
 Solution du problème 2
</h3>

```java
import org.w3c.dom.*;
import java.io.*;
import javax.xml.parsers.*;
import javax.xml.transform.*;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
public class Bottin {
    public static void main(String[] args) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        factory.setNamespaceAware(true);
        DocumentBuilder parser = factory.newDocumentBuilder();
        Document doc = parser.parse("bottin.xml");
        Element racine = doc.getDocumentElement();
        NodeList personnes = racine.getChildNodes();
        if (args[0].equals("efface")) {
            for (int i = 0; i < personnes.getLength(); i++) {
                Node n = personnes.item(i);
                if (n.getNodeType() == Node.ELEMENT_NODE) {
                    Element e = (Element) n;
                    if (e.getAttribute("nom").equals(args[1])) {
                        e.getParentNode().removeChild(e);
                    }
                }
            }
        }
        else if (args[0].equals("cherche")) {
            for (int i = 0; i < personnes.getLength(); i++) {
                Node n = personnes.item(i);
                if (n.getNodeType() == Node.ELEMENT_NODE) {
                    Element e = (Element) n;
                    if (e.getAttribute("nom").equals(args[1])) {
                        System.out.println(e.getAttribute("téléphone"));
                    }
                }
            }
        }
        else if (args[0].equals("ajoute")) {
            boolean existe = false;
            for (int i = 0; i < personnes.getLength(); i++) {
                Node n = personnes.item(i);
                if (n.getNodeType() == Node.ELEMENT_NODE) {
                    Element e = (Element) n;
                    if (e.getAttribute("nom").equals(args[1])) {
                        e.setAttribute("téléphone", args[2]);
                        existe = true;
                    }
                }
            }
            if (!existe) {
                Element p = doc.createElement("personne");
                p.setAttribute("nom", args[1]);
                p.setAttribute("téléphone", args[2]);
                racine.appendChild(p);
            }
        }
        // Sauvegarde du fichier modifié
        TransformerFactory tf = TransformerFactory.newInstance();
        Transformer t = tf.newTransformer();
        t.setOutputProperty(OutputKeys.ENCODING, "ISO-8859-1");
        DOMSource source = new DOMSource(doc);
        StreamResult result = new StreamResult(new FileWriter("bottin.xml"));
        t.transform(source, result);
    }
}
```

<p>
 Utilisation :
</p>
<ul style="margin: 1em 0; padding-left: 2em;">
 <li>
  <code>
   java Bottin cherche Dupont
  </code>
  → affiche le téléphone
 </li>
 <li>
  <code>
   java Bottin ajoute Martin 555-1234
  </code>
  → ajoute ou met à jour
 </li>
 <li>
  <code>
   java Bottin efface Martin
  </code>
  → supprime la personne
 </li>
</ul>
