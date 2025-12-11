---
title: "Problèmes résolus"
weight: 40
---
<h1>
 Problèmes résolus
</h1>
<h2>
 Deux problèmes avec solution
</h2>
<p>
 Pour vous aider à maîtriser le modèle DOM, nous vous proposons deux problèmes
    et une solution possible pour chacun.
</p>
<h3>
 Problème 1
</h3>
<p>
 Créez une classe « Arbre » (fichier « Arbre.java ») qui
    donne
    l'arbre DOM d'un document XML. Pour chaque nœud, donnez son nom et sa valeur
    (indices : « getNodeName », « get NodeValue »).
    Enfin, indentez les nœuds
    selon le nombre de parents qu'ils ont.
</p>
<p>
 Ainsi, étant donné le fichier « test.xml » suivant :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">joueur</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">nom</span> <span style="color:#274796; ">surnom</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">jojo</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>Jean<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">buts</span><span style="color:#a65700; ">&gt;</span>32<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">buts</span><span style="color:#a65700; ">&gt;</span><span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">joueur</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 La commande « java Arbre test.xml » devrait afficher à l'écran le
    résultat
    suivant :
</p>
<pre> Nom: #document Valeur: null
    Nom: joueur Valeur: null
    Nom: nom Valeur: null
    Nom: #text Valeur: Jean
    Nom: buts Valeur: null
    Nom: #text Valeur: 32
</pre>
<h3>
 Problème 2
</h3>
<p>
 Nous pouvons utiliser un fichier XML comme archive d'une base de données
    primitive.
    Cette fois-ci, nous vous demandons d'écrire un programme qui permet de
    chercher,
    d'effacer et d'ajouter des noms dans un bottin téléphonique.
</p>
<p>
 Stockez les numéros dans un fichier XML nommé « bottin.xml » et
    ayant le contenu qui suit :
</p>
<pre><span style="color:#004a43; ">&lt;?</span><span style="color:#800000; font-weight:bold; ">xml</span><span style="color:#004a43; "> </span><span style="color:#074726; ">version</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#7d0045; ">1.0</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">
    </span><span style="color:#074726; ">encoding</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">ISO-8859-1</span><span style="color:#0000e6; ">"</span><span style="color:#004a43; ">?&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">bottin</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">personne</span> <span style="color:#274796; ">nom</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">Jean
        Réjean</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">téléphone</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">432-4421</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">personne</span> <span style="color:#274796; ">nom</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">Jules
        Desche</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">téléphone</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">432-4332</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">bottin</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Concevez un programme dont le code source sera contenu dans un fichier nommé
    « Bottin.java ».
    Votre programme doit posséder les trois fonctions suivantes :
</p>
<ul>
 <li>
  « java Bottin efface "Jean Réjean" » : élimine du fichier
        « bottin.xml »
        tout élément « personne » ayant comme attribut
        « nom="Jean Réjean" ».
 </li>
 <li>
  « java Bottin cherche "Jean Réjean" » : donne le numéro
        de téléphone correspondant
        au nom donné à partir du contenu du fichier « bottin.xml », et
        ne retourne rien si le nom donné n'est pas trouvé.
 </li>
 <li>
  « java Bottin ajoute "Jean Réjean" 432-4421 » : fait en
        sorte que le nom « Jean Réjean »
        soit associé au seul numéro de téléphone « 432-4421 ».
 </li>
</ul>
<p>
 Vous pouvez supposer que le fichier « bottin.xml » existe et se
    trouve dans le même répertoire
    que le fichier « Bottin.java ». Vous pouvez également supposer que
    l'élément-racine est « bottin ».
</p>
