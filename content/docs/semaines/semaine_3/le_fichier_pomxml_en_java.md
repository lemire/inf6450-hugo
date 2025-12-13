---
title: "Le fichier pom.xml en Java"
weight: 30
---

# Le fichier pom.xml en Java

Le fichier pom.xml (Project Object Model) est le cœur de tout projet Maven. C’est un fichier de configuration écrit en XML qui décrit complètement le projet : ses coordonnées, ses dépendances, les plugins utilisés, la version de Java ciblée, les profils d’exécution, etc. Il est utilisé par Maven et par la plupart des outils de build modernes (Gradle peut aussi le lire dans certains cas) ainsi que par les IDE comme IntelliJ IDEA ou Eclipse.

Parmi les informations principales qu’il contient, on trouve la version du projet, le groupId et l’artifactId qui forment son identité unique, le packaging (jar, war, pom…), la liste des dépendances gérées avec leurs versions, les repositories additionnels, les plugins de compilation, de test, d’empaquetage, etc.
## Structure XML

La racine du fichier est toujours l’élément `<project>` avec les namespaces Maven :

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                             https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  ...
</project>
```

Les sections les plus courantes à l’intérieur sont :
`<groupId>`, `<artifactId>`, `<version>`, `<packaging>` : les coordonnées Maven du projet.

`<properties>` : permet de définir des variables réutilisables (version de Java, version des plugins, etc.).

`<dependencies>` : liste toutes les bibliothèques nécessaires.

`<dependencyManagement>` : centralise la gestion des versions (souvent utilisé dans un pom parent).

`<build>` et `<plugins>` : configuration du processus de compilation et des plugins Maven.
### Exemple de fichier pom.xml

Voici un exemple simple d’un projet Java console (application Spring Boot minimaliste) utilisant Java 17 et Maven :
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                             https://maven.apache.org/xsd/maven-4.0.0.xsd">

  <modelVersion>4.0.0</modelVersion>

  <groupId>com.example</groupId>
  <artifactId>demo-app</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  <packaging>jar</packaging>

  <name>Demo App</name>
  <description>Application de démonstration</description>

  <properties>
    <java.version>17</java.version>
    <spring-boot.version>3.3.0</spring-boot.version>
  </properties>

  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter</artifactId>
      <version>${spring-boot.version}</version>
    </dependency>
    <dependency>
      <groupId>com.fasterxml.jackson.core</groupId>
      <artifactId>jackson-databind</artifactId>
      <version>2.17.2</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.13.0</version>
        <configuration>
          <release>${java.version}</release>
        </configuration>
      </plugin>
      <plugin>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
        <version>${spring-boot.version}</version>
      </plugin>
    </plugins>
  </build>

</project>
```
Cet exemple montre comment le XML organise toutes les informations nécessaires à Maven : coordonnées du projet, propriétés réutilisables, dépendances avec gestion de version centralisée, et configuration des plugins de compilation et d’exécution. Vous pouvez bien entendu l’étendre avec des profils, des modules enfants, des repositories personnalisés, etc.

Plus loin dans le cours, vous verrez des exemples concrets de fichiers pom.xml.