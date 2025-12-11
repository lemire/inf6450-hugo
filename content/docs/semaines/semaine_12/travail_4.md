---
title: "Travail 4"
weight: 110
---

# Travail 4


<h2>
 Consignes générales
</h2>
<ol>
 <li>
  Utilisez les noms des fichiers spécifiés dans chaque exercice.
 </li>
 <li>
  Vous n'avez droit qu'à un seul fichier « .java » par exercice
        et
        il ne doit pas contenir plus de 500 lignes de code. Tous les problèmes
        peuvent être résolus en moins de 100 lignes!
        Rappelons qu'une « ligne » de code comprend un maximum de 80
        caractères.
 </li>
 <li>
  Chaque fichier Java doit débuter par un commentaire donnant le sigle du
        cours et votre nom comme ceci :
  <pre>
  /**
   * INF 6450 - Travail noté 4 - Votre nom, fait avec JDK 26
   */</pre>
 </li>
 <li>
  Vous devriez pouvoir accéder à la version de votre SDK, en tapant
        « javac -version » ou « java -version »
        dans une ligne de commande.
 </li>
 <li>
  Ne traitez pas les cas d'exception, comme les fichiers qui n'existent
        pas ou ne peuvent être ouverts.
        Par contre, votre code doit produire un résultat correct dans des
        conditions normales.
        Par exemple, si on vous demande de produire du XML, il doit s'agir de
        XML bien formé.
        Si on vous demande de lire du XML, vous devez pouvoir lire tout XML qui
        se conforme aux spécifications décrites dans l'exercice.
        Vous devez utiliser l'API DOM.
 </li>
 <li>
  Il est impératif que vos fichiers compilent avec le SDK (le plus
        récent), sans utiliser de librairies particulières.
  <strong>
   Un fichier Java qui ne compile pas ne sera pas noté.
  </strong>
 </li>
 <li>
  Lorsque vous aurez terminé les exercices, vous devez transmettre à votre
        personne tutrice,
        en utilisant l'outil de dépôt de l'Université, l'ensemble des fichiers
        avec l'extension Java comme fichiers attachés. Vous devez aussi remettre
        un fichier XML ainsi qu'un document (Word 97/2000/XP,
  <a href="https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=office">
   ODF
  </a>
  ,
        PDF, RTF ou en format texte) clairement identifié à votre nom contenant
        l'analyse demandée à la première question du travail.
        Il s'agit d'un travail personnel et vous ne devez pas partager vos
        solutions.
 </li>
</ol>
<p>
 Cette activité notée compte pour 15 % de la note globale.
</p>
<br/>
<h2>
 Exercice 1
</h2>
<p>
 Supposons une liste de transactions avec un attribut « montant »
    pour chaque client,
    comme dans le document XML suivant :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">liste</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">client</span> <span style="color:#274796; ">nom</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">Jean
        Charles</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">transaction</span> <span style="color:#274796; ">montant</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">500</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">question</span><span style="color:#a65700; ">&gt;</span>Quelle est la dernière marque?<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">question</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">transaction</span> <span style="color:#274796; ">montant</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">1200</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">client</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">client</span> <span style="color:#274796; ">nom</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">Pierre
        Élisabeth</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">transaction</span> <span style="color:#274796; ">montant</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">600</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">transaction</span> <span style="color:#274796; ">montant</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">800</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">question</span><span style="color:#a65700; ">&gt;</span>Où puis-je trouver le modèle
    2002?<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">question</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">transaction</span> <span style="color:#274796; ">montant</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">2000</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">client</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">liste</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Supposons que le fichier se nomme «
 <b>
  transactions.xml
 </b>
 ».
</p>
<p>
 Nous ne savons pas combien de transactions il peut y avoir par client; nous
    ne savons pas combien de clients nous avons;
    de plus, nous ne connaissons pas les noms des clients d'avance. Nous
    supposons que l'élément-racine est toujours « liste »;
    que tous les éléments « transaction » ont un attribut
    « montant »;
    que tous les éléments « transaction » sont dans des éléments
    « client »; que les éléments
    « client » sont tous dans l'élément-racine et ont tous un attribut
    « nom ».
    Nous supposons également qu'il n'y aura pas deux attributs « nom »
    avec la même valeur (même nom).
    Enfin, nous supposons que toutes les valeurs d'attribut de
    « montant » sont des entiers (« int » en Java).
</p>
<p>
 Écrivez un programme qui calcule la somme des valeurs de l'attribut
    « montant » pour chaque
    client (seuls les attributs « montant » des éléments
    « transaction »).
    Nous supposons qu'il s'agit de nombres entiers, des dollars par exemple.
    Le code source de votre programme sera dans un fichier nommé
    «
 <b>
  Transactions.java
 </b>
 ».
</p>
<p>
 Ainsi, la commande « java Transactions transactions.xml » devra
    donner :
</p>
<pre> Nom du client: Jean Charles
    Somme: 1700
    Nom du client: Pierre Élisabeth
    Somme: 3400</pre>
<p>
 Comparez la solution que vous obtenez en utilisant DOM avec ce qui est
    possible de faire avec XSLT, en fonction du temps de développement.
    Donnez au moins un avantage de l'approche DOM sur l'approche XSLT et un
    avantage
    de l'approche XSLT sur DOM. Vous devez
    remettre une solution XSLT sous la forme d'un document XML. Vous pouvez
    mettre des commentaires dans votre code Java, mais la comparaison entre DOM
    et XSLT
    doit être faite dans un document à part.
</p>
<h2>
 Exercice 2
</h2>
<p>
 Avec XSLT, nous pouvons combiner plusieurs documents en utilisant la fonction
    « document » qui permet
    de charger plusieurs documents XML. Mais que se passe-t-il lorsque nous
    devons combiner plusieurs documents,
    dont certains ne sont pas en XML? À ce moment, l'utilisation d'un
    langage comme Java et de DOM peut être très avantageuse.
</p>
<p>
 Supposons qu'un serveur enregistre les achats effectués sur le site, dans un
    fichier texte, en plaçant
    chaque achat sur une ligne avec des informations séparées par des virgules.
    Le fichier se nomme «
 <b>
  achats.txt
 </b>
 » :
</p>
<pre> Jean Charles, 3214324565, 321, 2
    Yvan Richard, 5435435545, 321, 1
    Yvette Gagnon, 4324324243, 1, 12</pre>
<p>
 Sur chaque ligne, se trouvent le nom du client, son numéro de carte de
    crédit, le code du produit acheté et la quantité achetée.
    Nous supposons que le serveur est un logiciel commercial et qu'il n'est pas
    possible de le modifier
    pour obtenir le format des données en XML.
</p>
<p>
 Par ailleurs, nous avons un document XML contenant notre inventaire; le
    fichier se nomme «
 <b>
  inventaire.xml
 </b>
 ».
    Le voici :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">inventaire</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">produit</span> <span style="color:#274796; ">code</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">1</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">prix</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">432.00</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">quantité</span><span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">43</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">produit</span> <span style="color:#274796; ">code</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">32</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">prix</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">32.00</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">quantité</span><span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">100</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">produit</span> <span style="color:#274796; ">code</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">321</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">prix</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">31.00</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">quantité</span><span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">200</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">inventaire</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Écrivez un programme qui met à jour l'inventaire en tenant compte des achats
    de la journée,
    contenus dans le fichier «
 <b>
  achats.txt
 </b>
 ».
    Votre code source devra se trouver dans le fichier
    «
 <b>
  Inventaire.java
 </b>
 » et
    la commande « java Inventaire achats.txt inventaire.xml» va modifier le
    fichier
    « inventaire » pour y soustraire les produits achetés ce qui, dans
    le cas qui nous concerne,
    donnera un fichier « inventaire.xml » ayant le contenu
    suivant :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">inventaire</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">produit</span> <span style="color:#274796; ">code</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">1</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">prix</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">432.00</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">quantité</span><span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">31</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">produit</span> <span style="color:#274796; ">code</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">32</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">prix</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">32.00</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">quantité</span><span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">100</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">produit</span> <span style="color:#274796; ">code</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">321</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">prix</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">31.00</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">quantité</span><span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">197</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">inventaire</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Nous pouvons supposer que le fichier « inventaire.xml » ne contient
    qu'un seul élément
    « produit » pour chaque valeur d'attribut « code ». Nous
    pouvons aussi supposer
    qu'aucun code invalide n'apparaît dans le fichier « achats.txt ».
    Par contre, nous ne savons pas combien
    de produits nous avons et combien d'achats il y aura. Évidemment, il est
    possible d'avoir un nombre négatif de produits
    dans notre inventaire.
</p>
<p>
 <b>
  Indice.-
 </b>
 Il est parfaitement possible d'écrire un tel programme en
    moins de 50 lignes.
</p>
<h2>
 Exercice 3
</h2>
<p>
 Il est parfois pénible d'utiliser l'interface DOM
    quand on cherche une seule information précise.
    Écrivez un programme Java qui permet d'extraire
    le prix correspondant à l'item ayant le code
    de produit 321 dans un fichier XML ayant la
    forme suivante en utilisant
 <strong>
  une expression XPath
 </strong>
 .
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">inventaire</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">produit</span> <span style="color:#274796; ">code</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">1</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">prix</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">432.00</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">quantité</span><span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">43</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">produit</span> <span style="color:#274796; ">code</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">32</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">prix</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">32.00</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">quantité</span><span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">100</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">produit</span> <span style="color:#274796; ">code</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">321</span><span style="color:#0000e6; ">"</span>
    <span style="color:#274796; ">prix</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">31.00</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">quantité</span><span style="color:#808030; ">=</span> <span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">200</span><span style="color:#0000e6; ">"</span>
    <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">inventaire</span><span style="color:#a65700; ">&gt;</span>
</pre>
<h2>
 Exercice 4
</h2>
<p>
 En utilisant AJAX, on peut rendre une page
    web dynamique. Malheureusement, pour des raisons de sécurité,
    un script dans une page
    web ne peut charger un fichier qui se trouve dans
    un domaine autre que celui d'origine. On vous demande
    donc de déposer le fichier RSS
 <a href="https://www.ledevoir.com/rss/edition_complete.xml">
  https://www.ledevoir.com/rss/edition_complete.xml
 </a>
 (il faut enregister le contenu sur votre disque) sur votre machine et de
    créer
    une page web AJAX capable de charger le fichier XML en question
    et d'afficher tant le titre des nouvelles que leur description
    complète. Attention, il ne faut récupérer que le contenu des
    éléments au sein des éléments item.
    Vous pouvez supposer que les titres et descriptions ne contiennent
    que du texte, sans éléments HTML.
</p>
<p>
 Certains étudiants trouvent utile d'utiliser la syntaxe
    « try { } catch(e) {} » de l'JavaScript (qui fonctionne
    comme en Java) pour traiter les erreurs. Cependant, cette
    syntaxe n'est pas nécessaire.
</p>
<!-- HTML generated using hilite.me -->
<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
 <pre style="margin: 0; line-height: 125%"><span style="color: #557799">&lt;?xml version="1.0" ?&gt;</span>
        <span style="color: #007700">&lt;html</span> <span style="color: #0000CC">xmlns=</span><span style="background-color: #fff0f0">"http://www.w3.org/1999/xhtml"</span><span style="color: #007700">&gt;</span>
        <span style="color: #007700">&lt;head&gt;</span>
        <span style="color: #007700">&lt;meta</span> <span style="color: #0000CC">charset=</span><span style="background-color: #fff0f0">"UTF-8"</span><span style="color: #007700">&gt;</span>
        <span style="color: #007700">&lt;title&gt;</span>Exemple AJAX<span style="color: #007700">&lt;/title&gt;</span>
        <span style="color: #007700">&lt;script </span><span style="color: #0000CC">language=</span><span style="background-color: #fff0f0">"JavaScript"</span><span style="color: #007700">&gt;</span>
        <span style="color: #008800; font-weight: bold">function</span>
        afficheTitres(doc) {
        titres <span style="color: #333333">=</span>
        doc.getElementsByTagName(<span style="background-color: #fff0f0">"title"</span>);
        elementol <span style="color: #333333">=</span> <span style="color: #007020">document</span>.createElement(<span style="background-color: #fff0f0">"ol"</span>);
        <span style="color: #008800; font-weight: bold">var</span> longueur
        <span style="color: #333333">=</span> titres.length;
        <span style="color: #008800; font-weight: bold">for</span> ( k <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">0</span>; k <span style="color: #333333">&lt;</span> longueur ; <span style="color: #333333">++</span>k) {
        elementli <span style="color: #333333">=</span> <span style="color: #007020">document</span>.createElement(<span style="background-color: #fff0f0">"li"</span>);
        elementli.appendChild(<span style="color: #007020">document</span>.createTextNode(titres[k].firstChild.nodeValue));
        elementol.appendChild(elementli);
        }
        body <span style="color: #333333">=</span> <span style="color: #007020">document</span>.getElementsByTagName(<span style="background-color: #fff0f0">"body"</span>).item(<span style="color: #0000DD; font-weight: bold">0</span>);
        body.appendChild(elementol);
        }
        <span style="color: #008800; font-weight: bold">function</span>
        chargeDocument(f) {
        <span style="color: #008800; font-weight: bold">var</span> fileReader
        <span style="color: #333333">=</span> <span style="color: #008800; font-weight: bold">new</span> FileReader();
        fileReader.onload <span style="color: #333333">=</span> <span style="color: #008800; font-weight: bold">function</span>(evt) {
        <span style="color: #008800; font-weight: bold">var</span> doc <span style="color: #333333">=</span> <span style="color: #008800; font-weight: bold">new</span>
        DOMParser().parseFromString(<span style="color: #008800; font-weight: bold">this</span>.result, <span style="background-color: #fff0f0">'application/xml'</span>);
        afficheTitres(doc);
        }
        fileReader.readAsText(f[<span style="color: #0000DD; font-weight: bold">0</span>]);
        }
        <span style="color: #007700">&lt;/script&gt;</span>
        <span style="color: #007700">&lt;/head&gt;</span>
        <span style="color: #007700">&lt;body&gt;</span>
        <span style="color: #007700">&lt;p&gt;</span>Récupére et affiche
        les nouvelles du devoir: <span style="color: #007700">&lt;/p&gt;</span>
        <span style="color: #007700">&lt;input</span> <span style="color: #0000CC">type=</span><span style="background-color: #fff0f0">"file"</span> <span style="color: #0000CC">onchange=</span><span style="background-color: #fff0f0">"chargeDocument(this.files)"</span>
        <span style="color: #007700">&gt;&lt;/input&gt;</span>
        <span style="color: #007700">&lt;/body&gt;</span>
        <span style="color: #007700">&lt;/html&gt;</span>
    </pre>
</div>
<h2>
 Exercice 5
</h2>
<p>
 Pour les cas simples, on peut convertir les documents XML en JSON, et vice
    versa avec une simple familiarité avec les formats. Convertissez le fichier
    suivant en fichier JSON.
 <a href="https://jsonlint.com/">
  Vérifiez que votre
        document JSON est un document JSON valable
 </a>
 .
</p>
<pre style="color:#000000;background:#ffffff;"><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#800000; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#800000; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#800000; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#800000; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">joueur</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>Pierrot Rouge<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">cote</span><span style="color:#a65700; ">&gt;</span>3 étoiles<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">cote</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">parent</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>Pierrette Rouge<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>Pierre Rouge<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">parent</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">joueur</span><span style="color:#a65700; ">&gt;</span>
</pre>
