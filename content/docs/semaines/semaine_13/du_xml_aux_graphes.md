---
title: "Du XML aux graphes"
weight: 20
---
# Du XML aux graphes

Le cours porte sur le XML en tant qu'outil pour la gestion de l'information. Nous avons vu, dans les modules précédents, le rôle que peut jouer le XML comme outil dans la gestion des données, qui sont une forme de connaissances de premier niveau : le XML rend plus facile l'échange et la transformation des données. De plus, nous avons vu que le XML permet le marquage « sémantique » des informations; le XML s'impose donc naturellement comme outil de gestion des connaissances. En effet, prenons cet exemple de marquage sémantique :

```xml
<personne>
    <nomdefamille>Jean</nomdefamille>
    <datedenaissance>3 février 1971</datedenaissance>
</personne>
```

Ce document XML contient non seulement l'information souhaitée, mais en plus, à un niveau élémentaire, il nous permet de comprendre le sens de cette information, grâce aux noms des balises.

Cependant, utiliser le nom des balises pour représenter les connaissances n'est pas toujours très pratique. Supposons que nous ayons deux documents XML semblables à celui de l'exemple précédent. Comment pouvons-nous représenter le fait que les deux personnes sont amies?

Une façon plus naturelle de représenter les connaissances est d'utiliser des graphes. Un graphe est un ensemble de nœuds liés par des relations d'un nœud à un autre. Par exemple, l'ensemble des pages web forme un graphe avec la relation « contient un lien vers ». On dit que le graphe est « dirigé » si les relations sont à sens unique.

Le web est un exemple de graphe dirigé : une page web peut avoir un lien vers une autre page web, qui elle-même ne contient pas un lien de retour vers la page d'origine. On dit qu'un graphe est « annoté » si les relations entre deux nœuds peuvent être de différentes natures. Par exemple, une communauté d'humains forme un graphe dirigé avec les relations « est ami avec » et « est parent avec ». Supposons que les relations « est ami avec » et « est parent avec » soient réflexives, alors le graphe d'humains est annoté, mais pas dirigé. Par contre, si nous acceptons qu'une personne puisse être l'ami de quelqu'un sans que cette personne soit son ami, alors le graphe d'humains sera annoté et dirigé.

Nous invitons à lire l'article de Wikipedia sur la [théorie des graphes](https://fr.wikipedia.org/wiki/Th%C3%A9orie_des_graphes) afin de vous familiariser davantage avec la notion de graphe.
