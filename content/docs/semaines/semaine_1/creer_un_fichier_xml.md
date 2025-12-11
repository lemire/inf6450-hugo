---
title: "Créer un fichier XML"
weight: 30
---
<h1>
 Créer un fichier XML
</h1>
<p>
 Tous les systèmes d’exploitation fournissent un éditeur de texte. Windows a son Bloc-notes, macOS son TextEdit, et Linux propose de nombreux choix (vim, nano, gedit, etc.).
</p>
<p>
 Je vous recommande fortement d’utiliser
 <strong>
  <a href="https://code.visualstudio.com">
   Visual Studio Code
  </a>
 </strong>
 : il est gratuit, multiplateforme (Windows, macOS, Linux), très léger, et il offre une excellente coloration syntaxique pour le XML, le HTML, etc.
</p>
<h2>
 Assistance par intelligence artificielle
</h2>
<p>
 Pour bénéficier d’une assistance par intelligence artificielle directement dans l’éditeur, il est possible d’ajouter GitHub Copilot, un outil d’autocomplétion alimenté par l’intelligence artificielle. Voici comment procéder.
</p>
<ol>
 <li>
  Créez-vous un compte sur
  <a href="https://github.com">
   le site GitHub
  </a>
  .
  <a href="https://github.com/lemire">
   Vous pouvez en profiter vous consulter la page du professeur
  </a>
  .
 </li>
 <li>
  Installez Visual Studio Code depuis le site officiel (code.visualstudio.com) si ce n’est pas déjà fait.
 </li>
 <li>
  Ouvrez l’éditeur, puis accédez à la vue des extensions en cliquant sur l’icône carrée divisée en quatre dans la barre latérale gauche.
 </li>
 <li>
  Dans la barre de recherche des extensions, tapez GitHub Copilot et sélectionnez l’extension officielle publiée par GitHub.
 </li>
 <li>
  Cliquez sur Installer ou Install. Une fois l’installation terminée, une invite vous demandera de vous connecter avec votre compte GitHub. Suivez les instructions pour autoriser l’extension.
 </li>
 <li>
  Copilot est désormais actif. Il proposera des suggestions de code en temps réel pendant que vous tapez. Acceptez-les avec la touche Tab.
 </li>
</ol>
<p>
 Notez que GitHub Copilot nécessite un abonnement payant après une période d’essai gratuite.
</p>
<h2>
 Votre premier fichier XML
</h2>
<p>
 Comme premier exercice, créez un nouveau fichier et tapez le code suivant :
</p>
<pre><span style="color:#e06c75;">&lt;premier&gt;</span>
    Ceci est mon premier document XML.
<span style="color:#e06c75;">&lt;/premier&gt;</span></pre>
<p>
 Enregistrez-le sous le nom
 <code>
  premier.xml
 </code>
 .
</p>
<p>
 Attention sous Windows : le Bloc-notes ajoute automatiquement l’extension
 <code>
  .txt
 </code>
 .  
Pour éviter cela :  
→ dans la boîte d’enregistrement, choisissez
 <strong>
  Tous les fichiers (*.*)
 </strong>
 dans le menu déroulant « Type » et tapez le nom
 <code>
  premier.xml
 </code>
 entre guillemets si nécessaire.
</p>
<p>
 Vous pouvez aussi choisir l’encodage : sous Windows XP et plus récents, sélectionnez
 <strong>
  UTF-8
 </strong>
 (recommandé) ou
 <strong>
  ANSI
 </strong>
 (équivalent à ISO-8859-1 pour ce cours).
</p>
<p>
 Ouvrez maintenant
 <code>
  premier.xml
 </code>
 dans votre navigateur (Firefox, Chrome, Edge…).  
Si tout est correct, vous verrez le texte s’afficher. En cas d’erreur de syntaxe, le navigateur vous indiquera précisément le problème.
</p>
<h2>
 Un exemple de HTML bien formé (donc aussi du XML valide)
</h2>
<pre><span style="color:#e06c75;">&lt;html&gt;</span>
    <span style="color:#e06c75;">&lt;body&gt;</span>
        Bonjour le monde !
    <span style="color:#e06c75;">&lt;/body&gt;</span>
<span style="color:#e06c75;">&lt;/html&gt;</span></pre>
<p>
 Exercice facultatif :  
recopiez ce code dans un fichier nommé
 <code>
  test.html
 </code>
 , ouvrez-le avec votre navigateur → vous devez voir « Bonjour le monde ! » s’afficher.
</p>
<p>
 Vous savez maintenant créer, enregistrer et visualiser des fichiers XML.  
C’est la première étape essentielle avant de passer à des structures plus complexes !
</p>
