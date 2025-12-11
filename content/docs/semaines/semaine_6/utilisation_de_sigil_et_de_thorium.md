---
title: "Utilisation de Sigil et de Thorium"
weight: 30
---
<h1>
 Utilisation de Sigil et de Thorium
</h1>
<h2>
 Sigil
</h2>
<p>
 Créer un fichier EPUB manuellement est un peu lourd. Ce n’est pas une
    opération particulièrement difficile, mais il faut créer quelques fichiers
    et les placer au bon endroit. Il est facile de faire des erreurs.
</p>
<p>
 Au lieu de cela, nous allons utiliser un éditeur dédié nommé Sigil. Vous
    devez donc commencer par installer Sigil sur votre ordinateur :
</p>
<p>
 <a class="spip_url spip_out auto" href="https://github.com/user-none/Sigil/releases" rel="noopener noreferrer nofollow external" target="_blank">
  https://github.com/user-none/Sigil/releases
 </a>
</p>
<p>
 Il suffit de télécharger et d’exécuter le fichier setup.exe correspondant à
    votre version de Windows. Choisissez une version "release" et non une
    version beta ou "pre-release".
</p>
<p>
 Pour nous amuser un peu, nous allons créer un livre électronique digne de ce
    nom. Commencer par écrire un paragraph que vous ajouterez au fichier XHTML
    déjà ouvert. Quelque chose comme ceci :
</p>
<pre style=" white-space: pre-wrap;       /* CSS 3 */
        white-space: -moz-pre-wrap;  /* Mozilla, since 1999 */
        white-space: -pre-wrap;      /* Opera 4-6 */
        white-space: -o-pre-wrap;    /* Opera 7 */
        word-wrap: break-word;       /* Internet Explorer 5.5+ */"><span style="color:#a65700; ">&lt;</span><span style="color:#800000; font-weight:bold; ">p</span><span style="color:#a65700; ">&gt;</span>Mon premier livre<span style="color:#008c00; ">.</span><span style="color:#a65700; ">&lt;/</span><span style="color:#800000; font-weight:bold; ">p</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Trouvez le fichier content.opf qui se trouve à la racine de tout EPUB et
    modifiez-le afin de donner un titre et un auteur à votre livre. Quelque
    chose comme ceci au sein de l’élément metadata fera l’affaire :
</p>
<pre><span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>Mon premier livre<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">title</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">creator</span> <span style="color:#274796; ">opf:role</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">aut</span><span style="color:#0000e6; ">"</span><span style="color:#a65700; ">&gt;</span>Daniel Lemire<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">creator</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">language</span><span style="color:#a65700; ">&gt;</span>fr-CA<span style="color:#a65700; ">&lt;/</span><span style="color:#666616; ">dc</span><span style="color:#800080; ">:</span><span style="color:#5f5035; ">language</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Notez bien l’espace de noms utilisé ("
 <a href="http://purl.org/dc/elements/1.1/" rel="noopener noreferrer nofollow external" target="_blank">
  http://purl.org/dc/elements/1.1/
 </a>
 "). Il s’agit de
    l’espace de noms de Dublin Core. Nous y reviendrons plus tard dans le cours.
</p>
<p>
 Un lien vers un document HTML se trouve sans doute déjà dans le fichier
    content.opf. Vous trouverez ailleurs dans l’interface de Sigil un éditeur
    vous permettant de modifier le fichier HTML en question. Vous pourriez ainsi
    rédiger tout un livre dans un seul fichier HTML. Mais il peut être plus
    pratique de diviser votre livre en plusieurs fichiers HTML. En cliquant sur
    le bouton droit de la souris sur le dossier Text, ajoutez un nouveau fichier
    HTML (par exemple Section0002.xhtml). Vous pouvez remplir ce nouveau fichier
    de texte. Notez qu’il est permis d’utiliser des hyperliens offrant la
    possibilité au lecteur de passer directement d’un fichier à l’autre.
</p>
<p>
 Consultez à nouveau le fichier content.opf. Vous trouverez alors des liens
    vers vos deux fichiers HTML. Vous devriez voir quelque chose comme
    ceci :
</p>
<pre><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">itemref</span> <span style="color:#274796; ">idref</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">Section0001.xhtml</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">itemref</span> <span style="color:#274796; ">idref</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">Section0002.xhtml</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
</pre>
<p>
 C’est de cette manière qu’une liseuse sait quels fichiers HTML offrir au
    lecteur.
</p>
<p>
 Enregistrez ensuite le résultat sur votre disque sous la forme d’un fichier
    avec l’extension .epub.
</p>
<h2>
 Thorium
</h2>
<p>
 Il n’est pas très drôle de créer un livre sans pouvoir le consulter.
    Heureusement, il existe une application qui s’installe partout et qui fait bien l’affaire :
 <a href="https://thorium.edrlab.org/" rel="noopener noreferrer external" target="_blank">
  Thorium
 </a>
 . Prenez la peine de l’installer et de la
    lancer.
</p>
<p>
 <br/>
</p>
<p>
 Vous pouvez ensuite charger un livre. Vérifiez que le livre correspond bien à ce que vous avez créé. Si ça ne
    fonctionne pas comme vous le pensez, pour une raison ou une autre, consultez
    de nouveau le document dans Sigil. Est-ce que vous voyez bien le contenu que
    vous y avez mis ? Si ça ne va toujours pas, vérifiez que vous utilisez
    bien une version de Sigil de qualité « release ». Essayez une
    autre version de Sigil au besoin. Vous pouvez aussi expérimenter avec
    d’autres lecteurs de EPUB.
</p>
<p>
 Dans tous les cas, nous vous invitons bien sûr à expérimenter avec d’autres
    lecteurs de livres électroniques. Si vous avez une tablette, vous trouverez
    sans doute une application pertinente. Votre PC a peut-être déjà des
    logiciels compatibles avec la norme EPUB.
</p>
<h2 class="spip">
 Le projet Gutenberg
</h2>
<p>
 Le projet Gutenberg est une collection de livres électroniques gratuits,
    disponibles au format EPUB. Commencez par télécharger la version
 <a class="spip_out" href="http://www.gutenberg.org/ebooks/11049" rel="noopener noreferrer external" target="_blank">
  EPUB d’Eugénie
        Grandet
 </a>
 (de Balzac). Ouvrez-le dans Sigil.
</p>
<p>
 Vous constaterez que le texte est composé de trois fichiers XHTML indiqué par
    le fichier content.opf :
</p>
<pre style=" white-space: pre-wrap;       /* CSS 3 */
        white-space: -moz-pre-wrap;  /* Mozilla, since 1999 */
        white-space: -pre-wrap;      /* Opera 4-6 */
        white-space: -o-pre-wrap;    /* Opera 7 */
        word-wrap: break-word;       /* Internet Explorer 5.5+ */"><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">item</span> <span style="color:#274796; ">href</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">Styles/pgepub.css</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">id</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">item1</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">media-type</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">text/css</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">item</span> <span style="color:#274796; ">href</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">Text/www.gutenberg.org%40files%4011049%4011049-8-0.html</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">id</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">id00000</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">media-type</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">application/xhtml+xml</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">item</span> <span style="color:#274796; ">href</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">Text/www.gutenberg.org%40files%4011049%4011049-8-1.html</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">id</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">id00639</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">media-type</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">application/xhtml+xml</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">item</span> <span style="color:#274796; ">href</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">Text/www.gutenberg.org%40files%4011049%4011049-8-2.html</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">id</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">id01301</span><span style="color:#0000e6; ">"</span> <span style="color:#274796; ">media-type</span><span style="color:#808030; ">=</span><span style="color:#0000e6; ">"</span><span style="color:#0000e6; ">application/xhtml+xml</span><span style="color:#0000e6; ">"</span> <span style="color:#a65700; ">/&gt;</span>
</pre>
<p>
 Si le coeur vous en dit, vous pouvez modifier les mots de Balzac, enregistrer
    le nouveau document EPUB et le lire en famille.
</p>
<p>
 Notez que l’on peut spécifier une feuille de style CSS associées avec les
    différents fichiers HTML. Nous reviendrons sur ce point plus tard dans le
    cours.
</p>
