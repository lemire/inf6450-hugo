---
title: "Accueil"
---

# Mot de bienvenue


{{< youtube id="biMsiwqAfso" >}}

Bienvenue ! Mon nom est [Daniel Lemire](http://lemire.me/fr/). Je travaille comme professeur et chercheur en informatique.

Ce cours porte sur le XML et les concepts associés (CSS, XSLT, HTML, MathML, etc.).
Le XML vous permet de générer des graphiques de grande qualité (SVG) que vous pouvez inclure au sein de pages web ou de document Word. Le XML vous permet de produire des équations mathématiques. 
Nous couvrons aussi des formats comme JSON, YAML et Base64. Vous apprendrez comment créez un document Word à partir d'un programme Java. Bref, le cours fait le tour généralement des formats de données et de documents.

Avant de suivre ce cours, vous devez normalement avoir un suivi au moins un cours de Java ou l'équivalent.



## Attention : Java

Ce cours suppose que vous êtes capable d'utiliser et de compiler un programme Java en ligne de commande. Avant de commencer le cours, créez un fichier intitulé « HelloWorld.java » avec le contenu suivant.

{{<inlineJava path="HelloWorld.java">}}
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
{{</inlineJava>}}


Il est de votre responsabilité de vous assurer que vous avez les connaissances requises pour réussir ce cours.
Vous ne devriez pas être intimidé par l'exemple suivant. Prenez quelques secondes pour l'exécuter dans
votre navigateur.


{{<inlineJava path="JsonSimple.java">}}
public class JsonSimple {

    public static void main(String[] args) {
        Person p = new Person("Alice", 30, true);
        System.out.println(toJson(p));
    }

    // Très petit convertisseur manuel
    public static String toJson(Object o) {
        if (o == null) return "null";
        if (o instanceof String) return "\"" + o + "\"";
        if (o instanceof Number || o instanceof Boolean) return o.toString();
        if (o instanceof Person p) {
            return String.format(
                "{\"nom\":\"%s\",\"age\":%d,\"majeur\":%b}",
                p.nom, p.age, p.majeur
            );
        }
        return "\"?\"";
    }

    // Classe simple (sans getters/setters)
    static class Person {
        String nom;
        int age;
        boolean majeur;

        Person(String nom, int age, boolean majeur) {
            this.nom = nom;
            this.age = age;
            this.majeur = majeur;
        }
    }
}
{{</inlineJava>}}


Nous recommandons comme référence pour la programmation Java le manuel [Java pas à pas](https://www.amazon.ca/Java-pas-Introduction-programmation-langage/dp/B0CR7RW87Y/) de Godin et Lemire.



## Mathématiques

Ce cours ne nécessite pas beaucoup de mathématiques en dehors de celles déjà couvertes au secondaire. Par exemple, il faut être familier avec la théorie des ensembles (incluant les notions d'union et d'intersection) et la théorie des graphes.

Un site d'aide aux devoirs pour les étudiants du secondaires comme [Allô prof](https://www.alloprof.qc.ca) devrait vous permettre de faire une rapide mise à niveau si ces notions ne vous sont plus familières.


## Charge de travail

Le cours exige une charge de travail d'environ 9 heures par semaine pendant 15 semaines. Vous devez donc prévoir une à deux journées pleine à consacrer au cours par semaine.

Il est de votre responsabilité de vous assurer que vous avez assez de temps dans votre horaire pour réussir ce cours.

## Politique concernant le plagiat

L'utilisation de textes ou de travaux écrits par autrui sans attribution, est du plagiat, même dans le cas où l'emprunt se limite à des fragments. En cas de plagiat, une note de zéro peut être accordée. De plus, l'offense peut être rapportée à l'Université qui appliquera des mesures disciplinaires.

## L'environnement technologique du cours

Un cours en ligne est beaucoup plus qu'un simple site web. Par exemple, le présent cours comprend des dizaine d'articles, plus d'une centaine de problèmes avec solutions, beaucoup de logiciel, des dizaines d'exemples, et des dizaines de liens vers des sites externes. Le professeur ou une personne tutrice sera également à votre disposition pour répondre à vos questions.

**Navigation**

Le menu à gauche de l'écran présente l'organisation du cours en semaines. Vous devez suivre le cours
de la première semaine à le dernière.

## L'approche pédagogique du cours

Le présent cours repose sur des lectures qui sont suivies d'activités d'autoévaluation. Contrairement à un cours donné en salle de classe, vous pouvez progresser à votre rythme et travailler où vous le voulez. Le cours s'échelonne sur 15 semaines, comme un cours en salle de classe, pour vous donner une idée du travail à faire par tranches successives. Si vous n'avez jamais suivi de cours en ligne, vous constaterez rapidement que la formule présente des avantages et se rapproche du travail en milieu professionnel.

Un cours en ligne n'est pas pour autant plus facile. Si votre progression est trop lente ou que vous sautez trop d'étapes, vous risquez de vous décourager : le cours a été conçu pour que vous progressiez régulièrement pendant les 15 semaines de sa durée.

**Les activités d'autoévaluation sont obligatoires.**

L'une des plus grandes sources de frustration est la difficulté des travaux notés. Plusieurs étudiants espèrent gagner du temps en faisant rapidement les lectures et en omettant les activités d'autoévaluation. C'est une mauvaise idée, parce que vous arriverez alors aux activités notées mal préparé.

Lorsque vous passerez l'examen à la fin du cours, il sera tenu pour acquis que vous aurez fait toutes les activités d'autoévaluation et que vous en maîtriserez donc la matière.

**Note sur l'encadrement**

En tout temps, vous pourrez communiquer avec le professeur ou la personne tutrice par courriel. Pour lui permettre de classer rapidement ses messages, inscrivez le sigle du cours dans l'objet de votre message (« [INF6450] »).

Il n'y a pas de contact de démarrage dans ce cours contrairement à ce que la documentation de la Télé-université peut suggérer. Vous devez commencer le cours dès que possible.

# Intelligence artificielle

Dans ce cours, l'utilisation de l'intelligence artificielle (Claude, ChatGPT, Copilot, Grok, etc.) est permise et même recommandée (mais optionnelle). Cependant, vous devez l'utiliser de manière responsable :

- Décrivez votre utilisation de l'IA. Une utilisation de l'IA sans déclaration peut être considérée comme une forme de faute. Contrairement à ce que vous pourriez croire, déclarer votre utilisation de l'IA vous protège.

- Expliquez votre démarche. Qu'est-ce que vous avez fait avec l'IA ? Nous vous encourageons à inclure des copies des résultats de vos interactions avec l'IA.

- Assurez-vous de bien expliquer vos résultats, en vos propres mots.



## Quelque chose vous déplaît ? Vous avez remarqué une erreur ?

En tout temps, vous pouvez laisser un mot anonyme au sujet du cours sur [le formulaire prévu à cet effet](https://docs.google.com/forms/d/1emnei-XQua_DaLPXxMby-SCI9UMbQgSiilKOCRNhUZQ/viewform). Ce formulaire nous permet de réagir rapidement quand un problème survient dans le cadre du cours. Bien entendu, vous pouvez aussi aviser la personne qui vous encadre de tout problème que vous rencontrez.

Nous portons attention à tous vos commentaires et tâchons d'améliorer le cours en conséquence.