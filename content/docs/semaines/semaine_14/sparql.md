---
title: "Activité SPARQL"
weight: 35
---

# Activité SPARQL

SPARQL (acronyme récursif de SPARQL Protocol and RDF Query Language) est le langage de requête standard pour interroger des données exprimées en RDF (Resource Description Framework). Il a été standardisé par le W3C en 2008 et sa version actuelle la plus utilisée est SPARQL 1.1 (2013).  

Il permet de récupérer et de manipuler des données stockées dans des triplestores ou dans n’importe quel graphe RDF, que ce soit sur le web (Linked Data), dans une base locale ou via un endpoint SPARQL public comme DBpedia, Wikidata ou data.gouv.fr.

SPARQL ressemble beaucoup à SQL, mais au lieu de tables et colonnes, on travaille avec des triplets de la forme **sujet – prédicat – objet** (ex. : <http://example.org/Paris> rdf:type dbo:City).

Il existe quatre formes principales de requêtes SPARQL :
- SELECT : retourne un tableau de résultats (le plus courant)
- CONSTRUCT : crée un nouveau graphe RDF à partir des résultats
- ASK : retourne simplement vrai ou faux
- DESCRIBE : retourne une description RDF d’une ressource

### Syntaxe de base

Une requête SELECT classique ressemble à ceci :

```sparql
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?ville ?population WHERE {
  ?ville a dbo:City ;
         dbo:populationTotal ?population ;
         rdfs:label "Paris"@fr .
  FILTER(?population > 1000000)
}
ORDER BY DESC(?population)
LIMIT 10
```

### Exemples concrets

#### 1. Exemple très simple – capitale de la France (sur DBpedia)

```sparql
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?capitale WHERE {
  <http://dbpedia.org/resource/France> dbo:capital ?capitale .
  ?capitale rdfs:label ?label .
  FILTER(lang(?label) = "fr")
}
```

Résultat attendu : http://dbpedia.org/resource/Paris avec le label "Paris".

#### 2. Trouver tous les films réalisés par Quentin Tarantino (Wikidata)

```sparql
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?film ?filmLabel ?annee WHERE {
  ?film wdt:P57 wd:Q3772 .        # P57 = réalisateur, Q3772 = Tarantino
  ?film wdt:P577 ?date .         # date de publication
  BIND(YEAR(?date) AS ?annee)
  SERVICE wikibase:label { bd:serviceParam wikibase:language "fr". }
}
ORDER BY ?annee
```

#### 3. Exemple avec OPTIONAL (données facultatives)

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX schema: <http://schema.org/>

SELECT ?personne ?nom ?email ?site WHERE {
  ?personne a foaf:Person ;
            foaf:name ?nom .
  OPTIONAL { ?personne foaf:mbox ?email }
  OPTIONAL { ?personne foaf:homepage ?site }
}
LIMIT 20
```

Si une personne n’a pas d’email ou de site web, la ligne apparaît quand même avec les cellules vides.

#### 4. Exemple CONSTRUCT – créer un petit graphe

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

CONSTRUCT {
  ?ami foaf:knows ?ami2 .
  ?ami2 foaf:name ?nom2 .
} WHERE {
  <http://example.org/alice> foaf:knows ?ami .
  ?ami foaf:knows ?ami2 .
  ?ami2 foaf:name ?nom2 .
  FILTER(?ami2 != <http://example.org/alice>)
}
```

Cela génère un nouveau graphe contenant les amis des amis d’Alice.

#### 5. Exemple avec FILTER, LANG et REGEX (recherche de labels en français contenant “église”)

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema/>

SELECT ?monument ?label WHERE {
  ?monument a <http://dbpedia.org/ontology/Monument> ;
            rdfs:label ?label .
  FILTER(LANG(?label) = "fr")
  FILTER(REGEX(?label, "église", "i"))
}
LIMIT 15
```

#### 6. Exemple d’agrégation (GROUP BY, COUNT)

```sparql
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

SELECT ?pays ?paysLabel (COUNT(?ville) AS ?nbVilles) WHERE {
  ?ville wdt:P31 wd:Q515 ;          # instance de "city"
         wdt:P17 ?pays .           # pays
  SERVICE wikibase:label { bd:serviceParam wikibase:language "fr". }
}
GROUP BY ?pays ?paysLabel
HAVING(?nbVilles > 100)
ORDER BY DESC(?nbVilles)
LIMIT 10
```

Ce dernier exemple montre les 10 pays ayant le plus de villes recensées dans Wikidata.






Voici la présentation mise à jour avec trois questions d’auto-évaluation ajoutées à la fin.

### Présentation de SPARQL

SPARQL (acronyme récursif de SPARQL Protocol and RDF Query Language) est le langage de requête standard pour interroger des données exprimées en RDF (Resource Description Framework). Il a été standardisé par le W3C en 2008 et sa version actuelle la plus utilisée est SPARQL 1.1 (2013).  

Il permet de récupérer et de manipuler des données stockées dans des triplestores ou dans n’importe quel graphe RDF, que ce soit sur le web (Linked Data), dans une base locale ou via un endpoint SPARQL public comme DBpedia, Wikidata ou data.gouv.fr.

SPARQL ressemble beaucoup à SQL, mais au lieu de tables et colonnes, on travaille avec des triplets de la forme **sujet – prédicat – objet** (ex. : <http://example.org/Paris> rdf:type dbo:City).

Il existe quatre formes principales de requêtes SPARQL :
- SELECT : retourne un tableau de résultats (le plus courant)
- CONSTRUCT : crée un nouveau graphe RDF à partir des résultats
- ASK : retourne simplement vrai ou faux
- DESCRIBE : retourne une description RDF d’une ressource

(suivent tous les exemples déjà fournis dans le message précédent…)

### Questions d’auto-évaluation

1. Écrivez une requête SPARQL qui retourne le nom (en français) et la date de naissance de toutes les personnes nées à Paris et décédées après 1950, en utilisant l’endpoint Wikidata. Utilisez le service wikibase:label et ordonnez les résultats par date de naissance décroissante.

2. À l’aide d’une requête de type ASK, écrivez une requête qui vérifie simplement si Albert Einstein a gagné un prix Nobel (propriété Wikidata P166). La requête doit retourner true ou false.

3. Écrivez une requête CONSTRUCT qui, à partir de Wikidata, génère un petit graphe contenant :
   - Toutes les capitales européennes (P31/Q6465 ou instance de capitale + située dans un pays d’Europe)
   - Leur population (P1082)
   - Le nom du pays dont elles sont la capitale  
   Le graphe résultant devra utiliser les prédicats schema:population et schema:country (http://schema.org/).


<details>
<summary>
(Solutions ci-dessous – à ne regarder qu’après avoir essayé !)
</summary>

**Solution 1**
```sparql
SELECT ?personne ?nom ?naissance WHERE {
  ?personne wdt:P19 wd:Q90 .           # né à Paris
  ?personne wdt:P570 ?mort .           # date de décès
  ?personne wdt:P569 ?naissance .
  FILTER(YEAR(?mort) > 1950)
  SERVICE wikibase:label { bd:serviceParam wikibase:language "fr". }
}
ORDER BY DESC(?naissance)
```

**Solution 2**
```sparql
ASK {
  wd:Q937 wdt:P166 wd:Q38104 .   # Einstein a reçu le prix Nobel de physique
}
```

**Solution 3**
```sparql
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX schema: <http://schema.org/>

CONSTRUCT {
  ?capitale schema:name ?nomCapitale ;
            schema:population ?pop ;
            schema:country ?pays .
  ?pays schema:name ?nomPays .
} WHERE {
  ?capitale wdt:P31/wdt:P279* wd:Q5119 .     # capitale (et sous-classes)
  ?capitale p:P17 ?statement .
  ?statement ps:P17 ?pays .
  ?pays wdt:P30 wd:Q46 .                     # continent Europe
  ?capitale wdt:P1082 ?pop .
  SERVICE wikibase:label { 
    bd:serviceParam wikibase:language "fr".
    ?capitale rdfs:label ?nomCapitale .
    ?pays rdfs:label ?nomPays .
  }
}
```
</<details>


## Activité avec Java

Effectuez maintenant [l'activité RDF avec Java](https://github.com/lemire/javardf).

