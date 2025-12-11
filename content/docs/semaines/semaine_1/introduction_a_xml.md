---
title: "Introduction à XML"
weight: 40
---
<h1>
 Introduction à XML
</h1>
<p>
 Le XML est un « métalangage » permettant d'échanger de l'information, principalement sur le web. Il a été conçu par Tim Bray, Jon Bosak et de nombreux autres collaborateurs, entre 1996 et 1999. On dit que c'est un « métalangage » parce qu'il est une façon pratique de créer de nouveaux
 <i>
  langages
 </i>
 pour échanger des informations, mais qu'il ne constitue pas un langage en soi. On dit que le XML est « extensible » (peut être étendu) et que c'est un métalangage : les deux affirmations vont dans le même sens et notent la capacité du XML à s'adapter à des besoins différents.
</p>
<p>
 Un document XML est essentiellement du texte contenant des balises. Une balise est un segment de texte commençant par &lt; et se terminant par &gt;, comme &lt;personne&gt;. Voici un exemple simple de document XML :
</p>
<pre>        &lt;personne&gt;
        &lt;nom&gt;Jean&lt;/nom&gt;
        &lt;age&gt;42&lt;/age&gt;
        &lt;/personne&gt;
</pre>
<p>
 Le XML est très présent sur le web et les documents XML peuvent être affichés par la plupart des navigateurs récents. On échange aussi le XML entre des logiciels et des serveurs sur le web, et le XML est de plus en plus utilisé en bureautique, comme format pour les traitements de texte par exemple. Comme un document XML est avant tout du texte, il n'est pas avantageux d'utiliser le XML pour stocker des informations de type multimédia (vidéo, musique); le champ d'application du XML demeure toutefois très vaste.
</p>
<p>
 Le XML définit une grammaire stricte et relativement simple de manière que les outils XML génériques puissent traiter tous les documents XML, peu importe leur domaine d'application. On dit d'un document qui respecte cette grammaire qu'il est
 <b>
  bien formé
 </b>
 . Ainsi, il n'est pas nécessaire d'utiliser des outils coûteux et propriétaires pour faire du XML.
</p>
<p>
 Une application possible du XML correspond au scénario suivant. Un groupe de personnes travaillant dans un domaine particulier, disons l'industrie de la construction, ont besoin d'échanger des informations, par exemple le prix et la description des matériaux. Elles doivent s'entendre sur un format informatique commun de manière que tous les logiciels, écrits ou utilisés par les différents participants, puissent communiquer entre eux, sans problème. L'information pourra ainsi être transmise sans intervention humaine.
</p>
<p>
 Concrètement, on utilise le XML dans le contexte d'une
 <b>
  application XML
 </b>
 . Une application XML est un jeu de balises et son utilisation dans un domaine particulier, par exemple la musique ou la cuisine. On peut définir un jeu de balises et, dans une certaine mesure, son utilisation en se servant d'un document DTD, Relax NG ou XML Schema (sujets que nous étudierons plus tard dans le cours). Dans un sens, une application XML forme un langage. On dit d'un document XML qui respecte les normes d'une application XML donnée qu'il est
 <b>
  valide
 </b>. Un document
 <b>
  valide
 </b>
 doit toujours être bien formé en plus de respecter les contraintes de l'application.
</p>
<p>
 En théorie, on pourrait penser que l'importance du XML est mineure. En effet, n'est-il pas facile de s'entendre sur des formats communs? L'expérience montre que ce n'est pas si facile. D'abord, définir avec rigueur un format de données est complexe. D'autre part, le développement de logiciels particuliers à chaque format est coûteux : avec un métalangage comme XML, on peut réutiliser souvent les mêmes librairies logicielles. Finalement, il est plus facile de trouver des experts en XML que des experts dans un format de données, format particulier à un domaine pointu.
</p>
<p>
 Le XML n'est pas un langage de programmation bien qu'on puisse l'utiliser avec des langages comme Java. On se sert par contre du XML pour les fichiers de configuration des logiciels. Par exemple, il est possible que, si vous utilisez un serveur web dans votre entreprise, ce serveur ait des fichiers de configuration en XML. Un document XML ne fait rien : ce n'est qu'une source passive d'informations, comme n'importe quel document, comme des pages web. On peut bien sûr programmer en utilisant une syntaxe XML cependant : nous verrons plus tard dans le cours comment programmer en XSLT. Mais, encore une fois, le fichier XML ne fait rien en lui-même si ce n'est que représenter le programme.
</p>
<p>
 Le XML met à profit un principe essentiel à l'architecture du web :
 <em>
  be conservative in what you do, be liberal in what you accept from others
 </em>
 (soyez strict dans ce que vous produisez, mais généreux dans ce que vous acceptez). En d'autres mots, le XML fonctionne parce que les gens tentent le plus possible de produire du XML de qualité (bien formé et valide), mais ils acceptent que les autres fassent des entorses aux règles. C'est, en partie, ce qu'on entend lorsqu'on dit que le XML est « extensible ». Cette règle est parfois
    appelée la loi de Postel parce qu'elle fut rédigée par Jon Postel dans la spécification
 <a href="http://tools.ietf.org/html/rfc793">
  RFC 793
 </a>
 .
</p>
<p>
 Par exemple, supposons que vous écriviez un logiciel qui s'attend à recevoir des commandes ayant la forme suivante.
</p>
<pre>    &lt;commande&gt;
    &lt;produit&gt;papier&lt;/produit&gt;
    &lt;quantite&gt;2&lt;/quantite&gt;
    &lt;/commande&gt;
</pre>
<p>
 Supposons maintenant que le logiciel qui émet les commandes est mis à jour et qu'il vous transmet dorénavant les commandes sous le format suivant.
</p>
<pre>    &lt;commande&gt;
    &lt;produit&gt;papier&lt;/produit&gt;
    &lt;quantite&gt;2&lt;/quantite&gt;
    &lt;emballage&gt;oui&lt;/emballage&gt;
    &lt;/commande&gt;
</pre>
<p>
 Selon les principes du XML, votre logiciel doit continuer à fonctionner, il
 <strong>
  doit ignorer
 </strong>
 le nouvel élément qu'il ne connaît pas. En d'autres mots, votre logiciel doit être généreux et ne pas exiger une conformité parfaite. Tant qu'il dispose des informations dont il a besoin, votre logiciel doit continuer à fonctionner. C'est ce principe fondateur qui permet à des millions de personnes d'utiliser le XML pour s'échanger des données sans le moindre arbitrage. Plus généralement, les technologies XML tentent de fonctionner le plus correctement possible même si les données ne correspondent pas à ce qu'on attendait.
</p>
<p>
 Plus généralement, le XML respecte plusieurs principes fondamentaux:
</p>
<ul>
 <li>
  Il est facile d'entretenir et modifier au fil du temps une application basée sur XML.
 </li>
 <li>
  Le XML est modulaire : on peut décomposer les applications en plusieurs fichiers, on peut traiter séparément différents morceaux d'un même document XML.
 </li>
 <li>
  Les spécifications XML minimisent la redondance sans la réduire à néant : il y a plusieurs façons de faire une même chose en XML, mais ce nombre est généralement limité. On a souvent le choix entre plusieurs stratégies, mais pas un trop grand nombre.
 </li>
 <li>
  Les technologies XML tiennent compte des personnes ayant des handicaps, notamment parce que plusieurs modes de présentation sont possibles.
 </li>
 <li>
  Le XML ne dépend pas d'une plate-forme particulière : que vous utilisiez Linux, Mac OS ou Windows, vous pouvez travailler avec le XML.
 </li>
 <li>
  Le XML est international : le XML supporte toutes les langues, pas seulement l'anglais.
 </li>
 <li>
  Le XML est extensible : on peut facilement faire évoluer les formats sans avoir à réécrire tous nos logiciels.
 </li>
 <li>
  Il est facile d'apprendre les fondements de base du XML.
 </li>
 <li>
  Il est facile pour un humain de lire du XML.
 </li>
 <li>
  Le XML est efficace : un ordinateur peu puissant peut traiter du XML rapidement.
 </li>
 <li>
  Le XML est un format textuel.
 </li>
 <li>
  Le XML est simple. La spécification technique de base tient sur quelques pages.
 </li>
 <li>
  Le XML assure la pérennité des informations.
 </li>
 <li>
  Le XML permet l'interopérabilité des systèmes.
 </li>
 <li>
  Un document XML peut être réutilisé facilement à plusieurs fins.
 </li>
 <li>
  Le XML est stable : les spécifications ne changent pas trop souvent.
 </li>
 <li>
  Le XML est universel : c'est un métalangage qui s'applique à un grand nombre de problèmes.
 </li>
</ul>
<p>
 Le XML n'est pas une nouveauté scientifique. Le XML représente, par contre, un pas en avant parce que c'est un des rares méta-langages universel. Le XML est aussi fondé sur des principes importants comme la pérennité, la simplicité, etc. qui ne sont pas toujours présents en technologie de l'information.
</p>
