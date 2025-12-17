---
title: "Activité JSON/XML avec Jackson"
weight: 30
---

# Activité JSON/XML avec Jackson

<p>
 <a href="https://github.com/lemire/javajackson">
  Nous vous invitons maintenant à faire une activité avec la librairie Java Jackson.
 </a>
 Dans cette activité, vous verrez comment on peut créer et analyser des documents JSON et XML avec une librairie dédiée en Java.
</p>


## En ligne

Une fois que vous aurez complété l'activité, vous pouvez explorer davantage
Jackson dans votre navigateur.

{{<inlineJava path="fr/example/jackson/App.java">}}
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