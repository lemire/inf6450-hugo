---
title: "XPath 2.0 et 3.0"
weight: 60
---

#  XPath 2.0 et 3.0


<div class="">
 <p>
 </p>
 <p>
  Jusqu'à présent, nous avons présenté XPath 1.0. Il s'agit de la version la plus largement supportée. Elle est la seule version supportée dans tous les grands navigateurs.
 </p>
 <p>
  XPath 2.0 ajoute de nombreuses
  <a href="http://www.w3.org/TR/xpath-functions/" shape="rect">
   fonctions et opérateurs
  </a>
  qui simplifient la vie du programmeur
        tels que empty, exists, intersect, except (pour calculer le complément),
        deep-equal (pour tester l'égalité entre deux séquences),
        index-of, reverse, subsequence, insert-before, remove, distinct-values,
        avg, max, min, etc. Alors que
        XPath 1.0 ne traite que des nombres, des chaînes de caractères, des valeurs booléennes et des ensembles de nœuds, XPath 2.0
        introduit la notion de séquence et plusieurs autres types
        de données pour noter les notes, la durée, les entiers,
        les nombres à virgule flottante, etc. XPath 2.0 supporte aussi
        les
  <a href="https://www.w3.org/TR/xpath-functions/#string.match" shape="rect">
   expressions régulières
  </a>
  avec les fonctions matches, replace, et tokenize. XPath 2.0 intègre maintenant
        une fonction fn:doc() équivalente à la fonction « document » du XSLT.
 </p>
 <p>
  XPath 2.0 comprend maintenant un syntaxe if/then/else comme dans cet exemple :
        « if ( @sexe eq 'm' ) then 'Monsieur' else 'Madame' ». On peut aussi utiliser des boucles :
        « for $i in //etudiant return $i/note ». On peut vérifier si au moins un (some) ou
        tous (every) les éléments d'une séquence satisfont une condition: « every $i in //etudiant
        satisfies $i/note &gt; 0 » ou « some $i in //etudiant
        satisfies $i/note &lt; 100 ». En somme, XPath 2.0 permet d'effectuer plusieurs traitement qui n'étaient possible
        qu'avec des instructions XSLT auparavant.
 </p>
 <p>
  XPath 3.0 quant à lui renforce la notion de fonction en XPath. On peut définir et exécuter ses propres fonctions. Par exemple, on peut définir (en XPath 3.0) une fonction qui ajoute 10 à un nombre: « let $ajoute := function($n) {$n+10} ».
 </p>
 <p>
 </p>
</div>
<hr/>


## XPath 2.0 et 3.0 en Java

Nous pouvons utiliser la librairie Saxon en Java pour illustrer les fonctions propres à XPath 2.0 et 3.0.

{{<inlineJava path="IllustrationXPathSaxon.java">}}

import net.sf.saxon.s9api.*;

import javax.xml.transform.stream.StreamSource;
import java.io.StringReader;
import java.util.Iterator;

public class IllustrationXPathSaxon {

    public static void main(String[] args) throws SaxonApiException {
        // Création du Processor (configuration Saxon)
        Processor processor = new Processor(false); // false pour édition HE

        // Chargement du document XML depuis une chaîne
        String xml = """
            <classe>
              <etudiant sexe="m">
                <nom>Jean</nom>
                <note>85</note>
                <note>92</note>
              </etudiant>
              <etudiant sexe="f">
                <nom>Marie</nom>
                <note>78</note>
                <note>95</note>
              </etudiant>
              <etudiant sexe="m">
                <nom>Paul</nom>
                <note>88</note>
              </etudiant>
            </classe>
            """;

        XdmNode document = processor.newDocumentBuilder().build(
            new StreamSource(new StringReader(xml))
        );

        // Création du compilateur XPath
        XPathCompiler xpathCompiler = processor.newXPathCompiler();

        // Démonstration des fonctionnalités XPath 2.0

        System.out.println("Fonctions agrégates (avg, max, min) :");
        XPathExecutable execAvg = xpathCompiler.compile("avg(//note)");
        XPathSelector selectorAvg = execAvg.load();
        selectorAvg.setContextItem(document);
        XdmValue resultAvg = selectorAvg.evaluate();
        System.out.println("Moyenne de toutes les notes : " + resultAvg);

        XPathExecutable execMax = xpathCompiler.compile("max(//note)");
        XPathSelector selectorMax = execMax.load();
        selectorMax.setContextItem(document);
        System.out.println("Note maximale : " + selectorMax.evaluate());

        XPathExecutable execMin = xpathCompiler.compile("min(//note)");
        XPathSelector selectorMin = execMin.load();
        selectorMin.setContextItem(document);
        System.out.println("Note minimale : " + selectorMin.evaluate());
        
        System.out.println("\nExpression conditionnelle if/then/else :");
        XPathExecutable execIf = xpathCompiler.compile("//etudiant ! ((if (@sexe eq 'm') then 'Monsieur' else 'Madame') || ' ' || nom)");
        XPathSelector selectorIf = execIf.load();
        selectorIf.setContextItem(document);
        XdmValue resultIf = selectorIf.evaluate();
        Iterator<XdmItem> itIf = resultIf.iterator();
        while (itIf.hasNext()) {
            System.out.println("Salutation : " + itIf.next());
        }
        System.out.println("\nBoucle for (retourner les notes) :");
        XPathExecutable execFor = xpathCompiler.compile("for $i in //etudiant return $i/note");
        XPathSelector selectorFor = execFor.load();
        selectorFor.setContextItem(document);
        XdmValue resultFor = selectorFor.evaluate();
        System.out.println("Toutes les notes (séquences aplaties) : " + resultFor);

        System.out.println("\nQuantificateurs some et every :");
        XPathExecutable execSome = xpathCompiler.compile("some $i in //etudiant satisfies $i/note < 80");
        XPathSelector selectorSome = execSome.load();
        selectorSome.setContextItem(document);
        System.out.println("Au moins un étudiant a une note < 80 : " + selectorSome.evaluate());

        XPathExecutable execEvery = xpathCompiler.compile("every $i in //etudiant satisfies $i/note > 0");
        XPathSelector selectorEvery = execEvery.load();
        selectorEvery.setContextItem(document);
        System.out.println("Tous les étudiants ont une note > 0 : " + selectorEvery.evaluate());

        System.out.println("\nExpressions régulières (matches) :");
        XPathExecutable execMatches = xpathCompiler.compile("//etudiant[matches(nom, '^M')] ! nom");
        XPathSelector selectorMatches = execMatches.load();
        selectorMatches.setContextItem(document);
        XdmValue resultMatches = selectorMatches.evaluate();
        System.out.println("Noms commençant par M : " + resultMatches);

        // Démonstration XPath 3.0 : fonction inline
        System.out.println("\nFonction inline XPath 3.0 (ajoute 10 à une note) :");
        XPathExecutable execFunc = xpathCompiler.compile("""
            let $ajoute10 := function($n as xs:integer) as xs:integer { $n + 10 }
            return //note ! $ajoute10(.)
            """);
        XPathSelector selectorFunc = execFunc.load();
        selectorFunc.setContextItem(document);
        XdmValue resultFunc = selectorFunc.evaluate();
        System.out.println("Notes + 10 : " + resultFunc);
    }
}
{{</inlineJava>}}
