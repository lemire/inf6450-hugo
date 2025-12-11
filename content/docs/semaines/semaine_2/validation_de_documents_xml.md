---
title: "Validation de documents XML"
weight: 30
---
## Objectif

Valider des documents XML avec Java.

## Activité de validation

On peut facilement vérifier si un document XML est « bien formé ». Il suffit de lui donner l’extension «&nbsp;.xml&nbsp;» (ou « .xhtml ») et de l’ouvrir dans un navigateur, par exemple.

Cependant, il arrive qu’on veuille vérifier que le document est non seulement bien formé, mais aussi valable par rapport à des documents DTD locaux. Apprenons donc à valider des documents XML, en exécutant les directives qui suivent, car cela vous sera très utile dans vos travaux en XML.

La procédure que nous proposons suppose que vous connaissez bien les éléments de base d’un système d’exploitation, comme l’utilisation de la ligne de commande et l’exécution de programmes. Nous ne donnons la procédure que pour Windows, mais elle est très similaire sous macOS ou Linux.

## Demonstration en ligne


Vous pouvez valider le fichier XML en ligne, en appuyant sur le bouton *exécuter*.

{{< javaMultiRunner files="Validateur.java;fichieravalider.xml;monfichier.dtd" >}}


## Application de bureau (optionnelle)

Nous vous invitons à mettre à l'essai notre application de bureau Java pour la validation des documents XML. [Il vous suffit de suivre nos consignes en ligne](https://github.com/lemire/javavalid).

## Procédure pour valider des documents XML

Avant de procéder à la validation, préparons notre environnement. Allez dans un répertoire, par exemple « C:\XML », et créez le fichier « monfichier.dtd » avec le contenu suivant, en utilisant le bloc-notes :
```xml
<!ELEMENT etudiant (numero, nom, age)>
<!ELEMENT numero (#PCDATA)>
<!ELEMENT nom (#PCDATA)>
<!ELEMENT age (#PCDATA)>
```

Puis, créez un document appelé « mauvais.xml » avec le contenu suivant, toujours à l’aide du bloc-notes :
```xml
<?xml version="1.0" encoding="ISO-8859-1" standalone="no"?>
<!DOCTYPE etudiant SYSTEM "monfichier.dtd">
<etudiant>
    <numero>123456</numero>
    <nom>Jean Dupont</nom>
</etudiant>
```

Il est important que les deux fichiers soient dans le même répertoire. En effet, la ligne DOCTYPE etudiant SYSTEM "monfichier.dtd" dans le fichier « mauvais.xml » indique qu’il devrait y avoir un fichier « monfichier.dtd » dans le même répertoire.

Vérifions maintenant si le fichier « mauvais.xml » est valable.

1. D’abord, vous devez disposer d’une machine virtuelle Java récente (Java 21 ou mieux) sur votre ordinateur, incluant le compilateur Java : « javac ». Si vous n’en avez pas, il faut effectuer un enregistrement et une installation ([adoptium.net](https://adoptium.net)) d’une telle machine. En outre, vous devez avoir sur votre ordinateur le SDK (aussi appelé JDK), pas uniquement le JRE. Sur la page qui se trouve à l’adresse le téléchargement peut prendre plusieurs minutes. Il suffit ensuite de lancer le fichier exécutable que vous venez d’enregistrer sur votre ordinateur pour installer le SDK. Une fois le SDK installé, vous pouvez poursuivre l’activité de vérification. Si l’outil d’installation vous propose de modifier les variables PATH et JAVAHOME, vous devez l’y autoriser. Si vous êtes incapable d’installer un logiciel sur votre ordinateur, nous vous invitons à joindre un technicien et à obtenir de l’aide. Nous ne pouvons pas, au sein du cours, vous offrir un soutien technique spécifique à votre ordinateur.
2. Placez le fichier Validateur.java dans le répertoire où se trouvent déjà vos fichiers « mauvais.xml » et « monfichier.dtd », soit dans « C:\XML ». Votre fichier « Validateur.java » devrait avoir le contenu suivant :

```java
import org.xml.sax.*;
import javax.xml.parsers.*;
import java.io.IOException;

public class Validateur {
    public static void main(String[] args) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        factory.setValidating(true);
        DocumentBuilder parser = factory.newDocumentBuilder();
        parser.setErrorHandler(new org.xml.sax.ErrorHandler() {
            public void warning(SAXParseException ex) throws SAXException {
                System.err.println("Avertissement : " + ex.getMessage());
            }
            public void error(SAXParseException ex) throws SAXException {
                System.err.println("Erreur : " + ex.getMessage());
            }
            public void fatalError(SAXParseException ex) throws SAXException {
                System.err.println("Erreur fatale : " + ex.getMessage());
                throw ex;
            }
        });
        parser.parse(args[0]);
        System.out.println("Le document est valide.");
    }
}
```

3. Ensuite, lancez la machine virtuelle Java avec une ligne de commande. Pour cela, il faut ouvrir une fenêtre de commande. Sous Windows 8 et versions ultérieures, cliquez en bas à gauche avec le bouton droit de la souris et sélectionnez « invite de commandes ». Sous les versions précédentes de Windows, dans le menu « Démarrer », cliquez sur « Exécuter » ; une fenêtre s’ouvre, tapez le nom de programme « cmd » pour ouvrir une fenêtre de commande. Notez qu’avec les versions plus anciennes de Windows, comme Windows 98, il faut taper « command.com ». Une fenêtre s’ouvre alors avec un fond noir, c’est la fenêtre de commande. Vous allez pouvoir y taper des lignes de commande pour vérifier si votre document XML est valable. Les commandes de base sont : « dir » (affiche le contenu d’un répertoire), « cd » (change de répertoire), « cd .. » (répertoire parent), « mkdir » (création d’un nouveau répertoire), « copy » (copie d’un fichier), « move » (déplacement d’un fichier), et « del » (supprime un fichier).
4. Testez l’installation de votre machine virtuelle en tapant « java » suivi du retour de chariot. Vous devriez recevoir un message qui commence par quelque chose comme « Usage: java [-options] class [args...] ». Testez aussi l’installation du compilateur en tapant « javac » ; vous devriez voir un message qui commence par quelque chose comme « Usage: javac &lt;options&gt; &lt;source files&gt; ». Si ce n’est pas le cas, nous vous conseillons de vérifier l’installation de votre machine virtuelle et de procéder à sa réinstallation au besoin. Si tout est bien installé et que ça ne fonctionne toujours pas, vous devrez indiquer le chemin pour trouver le compilateur en tapant la ligne de commande « set PATH=%PATH%;adresse_du_fichier_javac.exe ». Le fichier « javac.exe » se trouve dans le dossier « bin » du dossier où vous avez installé le SDK. Par défaut, ce fichier se trouve dans le « C: ». L’adresse du répertoire contenant le fichier « javac.exe » est donc souvent de la forme « C:\Program Files\Java\jdkXXXX\bin ». Si vous ne savez plus où est installé le SDK, vous pouvez faire une recherche, à partir du menu « Démarrer » de Windows. Une fois le chemin indiqué, retapez la commande « javac » et cette fois, tout devrait fonctionner. Comme il peut être lourd de modifier la variable d’environnement PATH chaque fois, il est possible de la modifier une fois pour toutes : allez dans « Démarrer », choisissez « Paramètres », puis « Panneau de configuration », et ouvrez « Système », cliquez sur l’onglet « Avancé » ; cliquez ensuite sur le bouton « Variables d’environnement », sélectionnez « PATH » dans la liste des variables, cliquez sur le bouton « Modifier » et ajoutez, à la fin du contenu de la variable, « ;adresse_du_fichier_javac.exe », par exemple « ;C:\Program Files\Java\jdk21\bin ».

5. Ensuite, placez-vous dans le dossier où se trouvent votre fichier XML et sa DTD. Vous savez toujours où vous vous trouvez dans l’arborescence de votre ordinateur, puisque chaque ligne de commande commence par l’adresse où vous êtes. La commande pour se déplacer est « cd adresse ». Par exemple, si la ligne commence par « C:\Documents and Settings\lucie&gt; », vous êtes dans le dossier de lucie. Pour aller au dossier XML qui se trouve sur le disque C, il faut taper : « cd C:\XML », puis faire le retour de chariot. Une nouvelle ligne apparaît et commence par : « C:\XML&gt; ». Maintenant que vous êtes dans le dossier où se trouve votre fichier XML, vous pouvez vérifier s’il est valable.

6. Faites « javac Validateur.java » pour compiler le petit programme qui pourra vous servir à vérifier la validité des documents XML. Vous ne devriez pas avoir de mal avec la compilation. Par exemple, vous pourriez voir à l’écran quelque chose comme « Note: Validateur.java uses or overrides a deprecated API. Note: Recompile with -Xlint:deprecation for details. ». Vous pouvez ignorer les avertissements vous incitant à utiliser l’option « -deprecation ».

7. Tapez la ligne de commande « java Validateur mauvais.xml », puis faites un retour de chariot. Il est important de respecter la casse dans les lignes de commande. Si rien de significatif ne s’affiche, votre fichier est valable, sinon, une description des erreurs s’affichera (en anglais). Si la machine virtuelle quitte avec l’erreur « java.lang.NoClassDefFoundError » alors que vous êtes bien dans le bon répertoire, faites alors « java -cp . Validateur mauvais.xml ».

8. Pour quitter, vous n’avez qu’à fermer la fenêtre de commande.

## Vérification de la procédure

Après avoir tapé la commande « java Validateur mauvais.xml » pour vérifier si le fichier « mauvais.xml » est valable, vous devriez obtenir le message d’erreur suivant indiquant qu’il manque un élément « numero » (le message exact peut varier et il pourrait être en français) :
```
mauvais.xml:7:1: Élément "etudiant" doit contenir un élément "numero".
```

Pour vous assurer de bien comprendre, reprenez la procédure ; créez un autre document appelé « bon.xml » avec le contenu suivant :
```xml
<?xml version="1.0" encoding="ISO-8859-1" standalone="no"?>
<!DOCTYPE etudiant SYSTEM "monfichier.dtd">
<etudiant>
    <numero>123456</numero>
    <nom>Jean Dupont</nom>
    <age>20</age>
</etudiant>
```

Cette fois-ci, vous devriez, en vérifiant que le document est valable, obtenir le message suivant :
```
Le document est valide.
```

> Est-ce que vous avez pu vérifier si les fichiers « mauvais.xml » et « bon.xml » étaient valables ? Si oui, passez aux autres activités, sinon cherchez encore un peu.
