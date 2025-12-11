---
title: "Espace de nom"
weight: 20
---
### Les vocabulaires XML

Un « vocabulaire XML » est un ensemble de noms de balises et d'attributs ayant une signification donnée. 
Par exemple, les gens de la comptabilité au sein d'une entreprise pourraient avoir un vocabulaire XML pour décrire 
certaines transactions, alors que les ingénieurs pourraient avoir leur propre vocabulaire pour 
décrire certains processus techniques. Les deux équipes pourraient utiliser les mêmes noms d'élément, 
comme « échéance », mais avec des significations différentes. On dira alors que 
nous avons deux **vocabulaires XML**.

Voyons un autre exemple. Imaginez que votre institution ait un vocabulaire XML pour les 
expéditions de marchandise et un vocabulaire XML pour la rédaction des factures. 
Un document XML combinant à la fois de l'information concernant une expédition et une facture 
devra utiliser deux vocabulaires.
Un vocabulaire XML peut être associé à un document DTD; il peut aussi être 
associé à un espace de noms.

### Les identificateurs de ressources uniformes (URI)

Un identificateur de ressources uniformes (*Uniform Resource Identifier* ou *URI*) est une adresse Internet 
composée d'un nom de protocole ou « schéma », comme file, http, ftp, news, mailto, gopher, urn, suivi d'un 
deux-points « : », lui-même suivi d'un chemin, comme « www.mondomain.com/fichier ». 
Un URI ne pointe pas nécessairement vers un fichier, mais peut très bien être une adresse purement fictive 
ou une adresse pointant vers une application logicielle sur un serveur.

Par exemple, « http://www.mondomain.com/fichier » et « mailto:billg@microsoft.com » 
sont des URI. Les URI ne doivent pas contenir d'accents, et la casse est significative sauf pour ce qui est du nom du protocole (HTTP versus http) et du nom de domaine (xerox.com versus XEROX.COM). Nous reviendrons sur les URI dans le module 5.

### Les espaces de noms

Un espace de noms est identifié par un URI; il y a correspondance unique entre 
les espaces de noms et les URI. Deux espaces de noms ayant le même URI sont identiques. 
Tous les utilisateurs d'un même vocabulaire XML devraient s'entendre sur un même URI. 
Par exemple, l'URI de l'espace de noms du XHTML est « http://www.w3.org/1999/xhtml ».
**L'URI agit un peu comme le numéro d'assurance sociale des vocabulaires XML.**
Il s'agit d'une analogie un peu étrange, voire originale, mais c'est ainsi.

Évidemment, la notion d'espace de noms n'a de sens que si l'on considère plusieurs espaces de noms 
et, par conséquent, plusieurs vocabulaires.

### Les DTD et les espaces de noms

Avant de préciser le lien entre les DTD et les espaces de noms, il importe de comprendre 
que les espaces de noms furent proposés après l'adoption des DTD. Il y a donc une certaine 
incompatibilité entre les DTD et les espaces de noms. C'est d'ailleurs l'une des raisons 
pour laquelle plusieurs organismes, dont OASIS et le W3C, tentent de proposer 
des solutions de remplacement pour les DTD.

Rappelons que l'on donne une DTD à un document, en ajoutant une déclaration de type de document, 
immédiatement après la déclaration XML, et dont la forme est :

```
<!DOCTYPE balise SYSTEM "http://www.mondomain.com/madtd.dtd">
```

C'est la même chose avec les espaces de noms. Si vous avez, par exemple, un vocabulaire pour 
les expéditions et un vocabulaire pour les factures, définis respectivement par des DTD situées à :

```
http://www.mondomain.com/expedition.dtd
```

et

```
http://www.mondomain.com/facture.dtd,
```

vous **ne pourriez pas** combiner les deux vocabulaires ainsi :
```
<!DOCTYPE balise SYSTEM "http://www.mondomain.com/expedition.dtd"
"http://www.mondomain.com/facture.dtd">
```

Même si l'on pouvait combiner deux DTD de la sorte, cela aurait plusieurs inconvénients : 
quoi faire si les deux DTD définissent un élément « client », mais de façon différente? 
La solution est de créer un nouveau vocabulaire XML qui combine
les deux et traite chaque vocabulaire comme un « espace de noms ».

Dans l'exemple qui suit, nous considérons deux vocabulaires, « facture » et « expedition »
qui ont les DTD suivantes :

```
<!ELEMENT facture (montant, nom)>
<!ELEMENT nom (#PCDATA)>
<!ELEMENT montant (#PCDATA)>
```

```
<!ELEMENT expedition (nom)>
<!ELEMENT nom (prenom, nomfamille, adresse)>
<!ELEMENT prenom (#PCDATA)> 
<!ELEMENT nomfamille (#PCDATA)>
<!ELEMENT adresse (#PCDATA)>
```

### Déclaration de l'espace de noms

On peut utiliser le symbole « : » dans les noms XML, mais on ne l'utilise généralement 
qu'une seule fois dans un nom donné. Tout ce qui précède le deux-points est appelé le « préfixe ».

On a vu qu'un espace de noms est identifié par un URI. À leur tour, les URI peuvent être associés à un « préfixe ». 
Tout attribut ou élément qui utilise un préfixe donné fait automatiquement partie de l'espace de noms 
identifié par l'URI. Seul l'URI identifie un espace de noms : le choix du préfixe est sans importance.
Un document peut avoir un seul espace de noms, mais douze préfixes différents.
On définit un « préfixe » à l'aide d'un attribut ayant comme préfixe « xmlns ». 
La définition du préfixe est alors valable pour l'ensemble de l'élément, y compris la balise où se situe 
l'attribut « xmlns: ». Ainsi, dans le document XML suivant :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<fact:facture xmlns:fact="http://www.domaine.com/facture">
<fact:montant>10$</fact:montant>
<fact:nom>Jean</fact:nom>
</fact:facture>
```

on reconnaît que l'élément « fact:facture » et tout son contenu utilisent l'espace de 
noms « http://www.domaine.com/facture » que nous avons décrit par une DTD plus haut. 
Le préfixe « fact » est ici associé à l'URI « http://www.domaine.com/facture » et 
tous les éléments et attributs ayant le préfixe « fact » sont considérés faire partie de 
l'espace de noms « http://www.domaine.com/facture ».

Il est « illégal » d'utiliser un préfixe qui n'a pas été défini... 
Ainsi, le document suivant est bien formé, mais il ne respecte pas les conventions des espaces de noms :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<fact:facture>
<fact:montant>10$</fact:montant>
<fact:nom>Jean</fact:nom>
</fact:facture>
```

Avez-vous remarqué que ces derniers documents n'ont pas de déclaration de type de document et ne peuvent 
donc pas être des documents XML valables? La plupart des documents XML utilisant les espaces 
de noms sont dans ce cas. Si jamais nous avions une déclaration de type de document, il faudrait une 
DTD qui contiennent les éléments « fact:facture », « fact:montant » et « fact:nom ». 
En d'autres mots, ce nouveau document XML ne peut utiliser la DTD facture décrite plus haut. 
Nous ne traiterons pas de cette approche ici, car on combine rarement les DTD de la sorte.

Le choix du préfixe « fact: » est arbitraire. On peut changer le nom du préfixe, 
car seul l'URI identifie de façon unique l'espace de noms. Par exemple, le document XML suivant est équivalent
à celui que nous venons de décrire.

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<facture:facture xmlns:facture="http://www.domaine.com/facture">
<facture:montant>10$</facture:montant>
<facture:nom>Jean</facture:nom>
</facture:facture>
```

On peut aussi redéfinir un préfixe comme dans l'exemple qui suit :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<facture:facture xmlns:facture="http://www.domaine.com/facture">
<facture:montant xmlns:facture="http://www.domaine.com/facture2">
10$</facture:montant>
<facture:nom>Jean</facture:nom>
</facture:facture>
```

Dans ce dernier cas, on dira que l'élément « montant » est dans l'espace de noms « http://www.domaine.com/facture2 »
et non pas dans l'espace de noms « http://www.domaine.com/facture ». Tout élément et attribut, utilisant le préfixe 
« facture » dans l'élément « montant », seraient eux aussi dans l'espace de 
noms « http://www.domaine.com/facture2 ».

L'endroit où apparaît la déclaration d'espace de noms est aussi sans conséquence. Par exemple, 
les deux documents suivants sont équivalents :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<enveloppe xmlns:facture="http://www.domaine.com/facture">
<facture:facture >
<facture:montant>10$</facture:montant>
<facture:nom>Jean</facture:nom>
</facture:facture>  
</enveloppe>
```

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<enveloppe>
<facture:facture xmlns:facture="http://www.domaine.com/facture">
<facture:montant>10$</facture:montant>
<facture:nom>Jean</facture:nom>
</facture:facture>  
</enveloppe>
```

On dit que deux documents sont équivalents, au sens des espaces de noms, s'ils ne diffèrent 
que par les préfixes d'espaces de noms et par les endroits où apparaissent les déclarations d'espaces de noms.

Évidemment, avec les espaces de noms, on peut combiner plusieurs vocabulaires. 
Par exemple, si nous voulons décrire une commande en utilisant les vocabulaires « facture » et « expedition », 
on peut très bien le faire comme le montre l'exemple suivant :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<fact:facture xmlns:fact="http://www.domaine.com/facture">
<fact:montant>10$</fact:montant>
<fact:nom>Jean</fact:nom>
<exp:expedition xmlns:exp="http://www.domaine.com/expedition">
<exp:nom>
<exp:prenom>Jean</exp:prenom>
<exp:nomfamille>Bertrand</exp:nomfamille>
<exp:adresse>1040, rue Jean</exp:adresse>
</exp:nom>
</exp:expedition> 
</fact:facture>
```

En outre, on pourrait même combiner les espaces de noms de façon arbitraire 
comme le montre le prochain exemple :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<fact:facture xmlns:fact="http://www.domaine.com/facture">
<fact:montant>10$</fact:montant>
<fact:nom>Jean</fact:nom>
<exp:nom xmlns:exp="http://www.domaine.com/expedition">
<exp:prenom>Jean</exp:prenom>
<exp:nomfamille>Bertrand</exp:nomfamille>
<exp:adresse>1040, rue Jean</exp:adresse>
</exp:nom>
</fact:facture>
```

### Les déclarations croisées

La déclaration d'espace de noms n'est valable qu'au sein de l'élément. Pour
déterminer l'espace de nom auquel appartient un élément, il ne suffit donc pas
de remonter et de s'arrêter à la première déclaration que l'on trouve. Voyez
si vous pouvez voir pourquoi l'espace de nom de l'élément « fact:montant » dans 
l'exemple suivant est « http://www.domaine.com/facture » et non « http://www.domaine.com/facture2 ».

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<fact:facture xmlns:fact="http://www.domaine.com/facture">
<fact:facture xmlns:fact="http://www.domaine.com/facture2">
</fact:facture>
<fact:montant />
</fact:facture>
```
### Le préfixe par défaut

On peut utiliser le préfixe par défaut, c'est-à-dire ne pas mettre de préfixe du tout. 
L'utilisation du préfixe par défaut est optionnelle dans un document XML. Comme tout autre préfixe, 
le préfixe par défaut peut être réutilisé, redéfini plusieurs fois dans un même document. 
Voici un exemple de préfixe par défaut :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<fact:facture xmlns:fact="http://www.domaine.com/facture">
<fact:montant>10$</fact:montant>
<nom xmlns="http://www.domaine.com/expedition">
<prenom>Jean</prenom>
<nomfamille>Bertrand</nomfamille>
<adresse>1040, rue Jean</adresse>
</nom>
</fact:facture>
```

Notons cependant que le préfixe par défaut ne s'utilise que pour les éléments :
**les attributs sans préfixe 
ne sont dans aucun espace de noms, et cela sans exception.**

### Rappel des notions formelles

La définition d'un préfixe d'espace de noms inclut l'élément où le préfixe 
est défini et tout son contenu, et rien d'autre. 
Le document qui suit fait une utilisation incorrecte des espaces de noms :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<expedition>
<fact:facture xmlns:fact="http://www.domaine.com/facture">
</fact:facture>
<fact:nom></fact:nom>
</expedition>
```

parce que le préfixe « fact » n'est défini qu'au sein de l'élément « facture ».

Bien que cela ne soit pas recommandable, il est possible de redéfinir les préfixes d'espace de noms. 
C'est simple si l'on se rappelle que la définition d'un préfixe inclut l'élément où 
la définition est faite. Ainsi, dans l'exemple :

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<expedition>
<fact:facture xmlns:fact="http://www.domaine.com/facture">
<fact:nom xmlns:fact="http://www.domaine.com/nom"></fact:nom>
</fact:facture>
```

l'élément « nom » appartient à l'espace de noms « http://www.domaine.com/nom » et 
non à l'espace de noms « http://www.domaine.com/facture ».

Par convention, on doit toujours accorder à un préfixe d'espace de noms un URI 
et il serait incorrect d'écrire <fact:facture /> 
au lieu de <fact:facture xmlns:fact="http://www.domaine.com/facture"> 
dans l'exemple précédent.

### Les espaces de noms et Relax NG

Alors que les DTD ne permettent pas de traiter les espaces
de noms, les spécifications Relax NG et XML Schema le permettent.
L'utilisation des espaces de noms en Relax NG est particulièrement
simple comme le montre cet exemple.

```xml
namespace fact = "http://www.domaine.com/facture"
namespace fact2 = "http://www.domaine.com/facture2"

element fact:facture {
    element fact:nom {text},
    element fact:montant {text},
    element fact2:id {text}
  }*
}
```

Le document XML suivant sera alors valable.

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<f:facture xmlns:f="http://www.domaine.com/facture">
  <f:nom>Daniel</f:nom>
  <f:montant>10,80$</f:montant>
  <f2:id xmlns:f2="http://www.domaine.com/facture2">10,80$</f2:id>
</f:facture>
```

Par défaut, il n'y a pas d'espace de noms lorsqu'un préfixe
n'est pas utilisé, mais on peut définir l'espace de noms par défaut
comme ceci :

```xml
namespace fact = "http://www.domaine.com/facture"
default namespace = "http://www.domaine.com/facture2"

element fact:facture {
    element fact:nom {text},
    element fact:montant {text},
    element id {text}
  }*
}
```

Les deux exemples précédents de Relax NG sont d'ailleurs équivalents.

### Le préfixe « xml »

Par convention, le préfixe « xml » est réservé à des
applications telles que la déclaration de la langue utilisée (« xml:lang »)
ou le traitement des espaces (« xml:space »). Il n'est pas nécessaire d'y associer
explicitement un 
URI : l'URI « http://www.w3.org/XML/1998/namespace » y est automatiquement associé.

### Rappel : des espaces de noms pour les attributs?

Les choses se corsent un peu quand on considère les attributs. 
Alors qu'un élément sans préfixe tombe dans l'espace de noms par défaut si 
celui-ci a été défini par un attribut « xmlns="..." », ce n'est pas le cas 
pour les attributs. Un attribut sans préfixe n'est dans 
aucun espace de noms; pour y être, un attribut doit être muni d'un préfixe.

### En résumé, qu'est-ce que les espaces de noms?

Une DTD définit un ensemble fixe d'éléments, ensemble qui ne peut être recombiné avec d'autres DTD; 
c'est un instrument rigide. Par contre, les espaces de noms permettent de recombiner 
des éléments provenant de différentes applications; ils permettent donc une grande flexibilité.

Alors que la DTD définit des éléments et comment les utiliser ensemble, 
les espaces de noms ne permettent d'établir qu'un lien entre un élément et un URI, 
mais sans indiquer les contraintes d'utilisation.

---


