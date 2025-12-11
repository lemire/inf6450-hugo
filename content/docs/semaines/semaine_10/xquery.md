---
title: "XQuery"
weight: 20
---

# XQuery

XSLT peut servir pour extraire des informations d'un document XML. On peut trouver tous les noms des étudiants répondant à certains critères. Dans un sens, XSLT peut être utilisé comme langage dans le contexte des bases de données. Cependant, pour cette fin spécifique, un nouveau langage appelé XQuery a été proposé. La syntaxe du XQuery est un mélange de XPath et de [SQL](http://fr.wikipedia.org/wiki/SQL) et ressemble davantage à ce que les spécialistes des bases de données connaissent bien.

Pour tester les requêtes XQuery, Saxon est un outil pratique écrit en java. Pour utiliser Saxon, 
suivez d'abord les consignes à l'adresse [https://github.com/lemire/javasaxon](https://github.com/lemire/javasaxon).


Pour rendre nos exemples plus concrets, prenez le fichier etu.xml suivant.

```xml
<liste>
    <etudiant>
    <nom>Laroche</nom>
    <prenom>Pierre</prenom>
    <statut>inscrit</statut>
    <cours>
    <sigle>INF 6460</sigle>
    <note>54</note>
    </cours>
    <cours>
    <sigle>INF 6450</sigle>
    <note>44</note>
    </cours>
    </etudiant>
    <etudiant>
    <nom>Aaron</nom>
    <prenom>Jean</prenom>
    <statut>inscrit</statut>
    <cours>
    <sigle>INF 6460</sigle>
    <note>56</note>
    </cours>
    <cours>
    <sigle>INF 6450</sigle>
    <note>46</note>
    </cours>
    </etudiant>
    <etudiant>
    <nom>Pouf</nom>
    <prenom>Jean</prenom>
    <statut>non-inscrit</statut>
    </etudiant>
</liste>
```

Vous pouvez créer un fichier etu.xml sur votre disque dans le même dossier que le fichier query, et remplacer partout l'URI par le nom du fichier (tel que « etu.xml »).

Parce que XQuery, tout comme XSLT 2.0, s'appuie sur XPath 2.0, il est facile de calculer la liste des cours :

```xquery
for $s in distinct-values(doc("etu.xml")//sigle)
    return $s
```

Cette requête donnera « INF 6460 INF 6450 ».

Voici un exemple de requête XQuery pour extraire d'un document XML tous les étudiants inscrits en supposant que le fichier XML se trouve à l'adresse http://universite.com/etu.xml.

```xquery
<maliste>
    {let $inscription := "inscrit"
    for $b in doc("http://universite.com/etu.xml")/liste/etudiant
    where $b/statut = $inscription
    order by $b/nom ascending
    return <etudiant>
    { $b/prenom }
    { $b/nom }
    </etudiant>}
    </maliste>
```

Cet exemple est une requête de type FLWOR parce qu'elle ne contient que des instructions « for », « let », « where », « order by », et « return ». L'instruction « for » sert à définir une boucle, l'instruction « where » sert à poser une condition, l'instruction « order by » permet de trier le résultat, alors que l'instruction « return » définit le résultat. L'instruction « let » permet de définir une constante. Notez que XQuery utilise les accolades pour distinguer les requêtes XQuery et XPath du texte. La requête considère tous les éléments etudiant contenus dans l'élément-racine liste, pour chacun d'entre eux, elle vérifie qu'il contient un élément statut contenant le texte « inscrit », puis elle donne la liste des noms et prénoms triée selon le nom. Voici quel sera le résultat :

```xml
<maliste>
    <etudiant>
    <prenom>Jean</prenom>
    <nom>Aaron</nom>
    </etudiant>
    <etudiant>
    <prenom>Pierre</prenom>
    <nom>Laroche</nom>
    </etudiant>
</maliste>
```

On peut attribuer un compteur aux nœuds :

```xquery
<maliste>
    {
    for $b at $pos in doc("http://universite.com/etu.xml")/liste/etudiant
    order by $b/nom descending
    return
    <etudiant> $pos -
    { $b/prenom }
    { $b/nom }
    </etudiant>
    }
</maliste>
```

Le résultat sera alors :

```xml
<maliste>
    <etudiant>3-
    <prenom>Jean</prenom>
    <nom>Pouf</nom>
    </etudiant>
    <etudiant>1-
    <prenom>Pierre</prenom>
    <nom>Laroche</nom>
    </etudiant>
    <etudiant>2-
    <prenom>Jean</prenom>
    <nom>Aaron</nom>
    </etudiant>
    </maliste>
```

On peut combiner les requêtes FLWOR, comme dans cet exemple :

```xquery
<maliste>
    {for $e in doc("http://universite.com/etu.xml")//etudiant
    return
    <etudiant nom="{$e/nom}">
    { for $v in $e/cours return
    <note>{number($v/note)}</note>
    }
    </etudiant>
    }
</maliste>
```

Cette requête va considérer chaque élément etudiant du document XML et créer une liste de notes obtenues pour cet étudiant, dans ce cas, le résultat sera :

```xml
<maliste>
    <etudiant nom="Laroche">
    <note>54</note>
    <note>44</note>
    </etudiant>
    <etudiant nom="Aaron">
    <note>56</note>
    <note>46</note>
    </etudiant>
    <etudiant nom="Pouf"/>
</maliste>
```

L'expression suivante va calculer la moyenne de notes (50) :

```xquery
<maliste>
    {avg(
    for $n in doc("http://universite.com/etu.xml")//note
    return $n
    )}
</maliste>
```

Par défaut, les documents XQuery utilisent le jeu de caractères Unicode UTF-8. On peut stipuler un jeu de caractères différent dans la déclaration XQuery optionnelle comme dans cet exemple :

```xquery
xquery version "1.0" encoding "utf-8";
    for $s in distinct-values(doc("etu.xml")//sigle)
    return $s
```

Elliotte Rusty Harold nous offre une excellente [page sur XQuery](http://www.cafeconleche.org/slides/albany/xquery/) qui résume bien les points essentiels avec des exemples.

