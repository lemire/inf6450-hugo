---
title: "Introduction au XSLT"
weight: 20
---
# Introduction au XSLT
## Qu'est-ce que le XSLT
 La première version du langage XSLT (_Extensible Stylesheet Language Transformation_) a été publiée en 1997 et elle est devenue une recommandation W3C en 1999. Elle fait partie du XSL (_Extensible Stylesheet Language_) qui comprend une seconde composante, les XSL-FO (_Extensible Stylesheet Language Formatting Objects_). La technologie XSL tire son origine du besoin d'un langage simple, mais suffisamment puissant pour pouvoir contrôler finement l'affichage du XML. On utilise beaucoup le XSLT sur le web et au sein des systèmes d'information, alors que le XSL-FO est davantage utile pour les applications de mise en page spécialisées. Dans ce cours, nous nous soucierons seulement du XSLT, dont l'utilité dépasse de loin les problèmes de présentation.

 L'objectif poursuivi par le XSLT est de transformer les documents XML en d'autres documents. Par exemple, supposons que vous ayez le document suivant :

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<facture>
   <montant>10.10</montant>
   <personne>Jean Rochond</personne>
   <raison>Achat d'ordinateur</raison>
</facture>
```

 et que vous vouliez transformer ce type de document XML en document HTML qui aurait la forme suivante :

```html
<html>
<head>
   <title>Facture de Jean Rochond</title>
</head>
   <body><p>Ceci est une facture pour Jean Rochond de 10.10$
   pour: Achat d'ordinateur.</p></body>
</html>
```

Si votre entreprise utilise du XML et que vous désirez envoyer des factures
    par courriel, vous pourriez envoyer le document HTML au lieu du document XML. De cette
    manière, le client pourrait consulter sa facture sans avoir à comprendre le XML.

On pourrait bien sûr écrire un programme en Java qui effectuerait cette opération, mais
    la conception d'un programme Java prend du temps et on cherche parfois une solution
    plus économique, plus rapide. Avec l'exemple que nous venons de voir,
    on pourrait automatiser la transformation de XML en HTML en moins d'une quinzaine de minutes.
    Pour obtenir le résultat désiré, il faut utiliser un petit fichier XSLT. À la fin de cette semaine, vous devriez être capable de faire ce travail.

### Les documents XSLT

Le document XSLT contient des règles qu'un « processeur XSLT » applique aux documents XML
    pour les transformer. Heureusement, si vous utilisez un navigateur récent, vous avez déjà un
    processeur XSLT moderne à même votre navigateur. Lors de l'ouverture d'un document XML,
    votre navigateur tente automatiquement de trouver et d'exécuter un document XSLT
    pour transformer le document XML.

Un processeur XSLT va parcourir les noeuds de votre document en
    commençant par l'élément-racine et, à chaque fois, il va tenter d'appliquer une règle. Certaines règles peuvent lui dire de continuer l'application des règles au sein des noeuds contenus dans un élément (avec l'instruction apply-template) alors que d'autres peuvent simplement extraire une information particulière.

Commençons par créer le fichier XSLT suivant qu'on enregistrera
    sur le disque comme étant « xslt.xml » :


```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
</xsl:stylesheet>
```

Ce document ne contient aucune « règle » et constitue le document XSLT de base.  
Nous vous suggérons de faire l’exercice de création de ce document avec *Bloc-notes*, par exemple.

Un document XSLT est un document XML bien formé, utilisant l’espace de noms « http://www.w3.org/1999/XSL/Transform » et ayant pour élément-racine *stylesheet* (ou *transform*), lequel a lui-même un attribut « version ».  
On ne discute ici que de la première version de XSLT (1.0) ; on utilise donc 1.0 comme valeur d’attribut pour version.

Prenons maintenant le fichier XML que nous avions auparavant ; modifions-le un peu en le faisant pointer vers le fichier XSLT nouvellement créé :

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<?xml-stylesheet href="xslt.xml" type="application/xml"?>
<facture>
  <montant>10.10</montant>
  <personne>Jean Rochond</personne>
  <raison>Achat d'ordinateur</raison>
</facture>
```

On ajoute donc la ligne : `<?xml-stylesheet href="xslt.xml" type="application/xml"?>`.  
Cette ligne indique au navigateur, ou à un autre logiciel, que le document XML peut être transformé par le fichier XSLT nommé « xslt.xml ». Le chemin peut être relatif ou absolu : on pourrait donc aussi avoir une ligne comme :

```xml
<?xml-stylesheet href="http://www.mondomaine.com/xslt.xml"
                 type="application/xml"?>
```

si l’URL « http://www.mondomaine.com/xslt.xml » pointe vers un fichier XSLT.

Dans un navigateur, on peut enregistrer ce nouveau document XML dans le même répertoire que le fichier « xslt.xml », disons avec le nom « test.xml », puis ouvrir le fichier « test.xml » dans votre navigateur ; il est malheureusement nécessaire de déposer les fichiers sur un serveur web pour que cela fonctionne, les développeurs craignant les failles de sécurité associées aux fichiers locaux. Heureusement, vous n’avez pas à faire ce travail : nous fournissons un outil en ligne qui vous permet de saisir vos fichiers XSLT et XML dans votre navigateur sans devoir créer de fichiers. Nous vous présenterons cet outil dans le prochain article. Ceux qui souhaitent travailler avec des fichiers directement peuvent utiliser un serveur web.

Une fois le fichier XML chargé et la transformation XSLT appliquée, normalement, on ne devrait rien voir à l’écran (une page vide), car le document XSLT utilisé est vide de toute instruction et le résultat ne sera donc pas du HTML. Le résultat peut cependant varier selon le navigateur utilisé, car votre navigateur pourrait afficher le texte, même s’il ne s’agit pas de HTML : dans ce cas, vous ne verriez que le texte contenu dans le document XML, les balises en moins. Nous expliquerons bientôt pourquoi cela est le cas.

## application de bureau java (optionnelle)

Nous avons préparé une application conviviale en Java qui vous permet d’appliquer une transformation XSLT à un document XML.  
[Nous vous invitons à la mettre à l’essai en suivant nos consignes](https://github.com/lemire/javaxslt).