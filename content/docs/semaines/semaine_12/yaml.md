---
title: "YAML"
weight: 90
---
<h1>
 YAML
</h1>
<p>
 JSON (JavaScript Object Notation) est aujourd’hui le format le plus populaire pour échanger des données structurées, surtout dans les API web. Il est très strict : tout est basé sur des objets avec des tableaux, des chaînes entre guillemets doubles, des nombres, des booléens (true/false) et null. Sa syntaxe est rigide mais extrêmement prévisible pour les machines, ce qui explique son succès. Cependant, quand un humain doit lire ou écrire du JSON à la main (par exemple dans un fichier de configuration), cette rigueur devient vite pénible : les guillemets partout, les virgules obligatoires, l’absence de commentaires rendent le fichier verbeux et sujet aux erreurs de syntaxe.
</p>
<p>
 YAML (YAML Ain’t Markup Language) est né justement pour résoudre ce problème de lisibilité tout en restant compatible, dans une très large mesure, avec la structure de données de JSON. YAML est en réalité un sur-ensemble de JSON : tout fichier JSON valide est aussi un YAML valide. Cela signifie que vous pouvez prendre n’importe quel JSON et le parser avec un parseur YAML sans modification. Mais YAML va beaucoup plus loin en offrant une syntaxe beaucoup plus naturelle et agréable pour les humains.
</p>
<p>
 Contrairement à JSON qui n’autorise qu’une seule façon d’écrire les données (accolades et crochets), YAML propose deux syntaxes principales : la syntaxe indentée (la plus courante, proche du Python) et la syntaxe « en ligne » qui ressemble énormément à JSON. Grâce à l’indentation (généralement 2 espaces), on élimine presque totalement les accolades, les virgules de fin et les guillemets autour des clés. YAML autorise aussi nativement les commentaires avec #, les listes simples avec - et supporte des types supplémentaires comme les dates, les timestamps ou les valeurs null écrites ~ ou null ou simplement absentes.
</p>
<p>
 Si on compare avec XML, on voit que YAML et XML poursuivent des objectifs opposés bien qu’ils soient tous les deux plus lisibles que JSON brut. XML est un langage de balisage (markup language) avec des balises ouvrantes et fermantes, des attributs, des namespaces, conçu à l’origine pour structurer des documents. Il est extrêmement verbeux et exigeant en syntaxe. YAML, au contraire, n’est pas un langage de balisage mais un format de sérialisation de données. Il cherche la concision et la clarté maximale pour représenter des structures de données (objets, listes, valeurs scalaires) sans aucune balise. Là où XML répète le nom de la balise deux fois (&lt;person&gt;…&lt;/person&gt;), YAML écrit simplement person: suivi de ses propriétés indentées.
</p>
<p>
 On peut voir une évolution : XML (années 90-2000) → JSON (années 2010, priorité à la simplicité machine) → YAML (priorité à la lisibilité humaine tout en restant 100 % compatible avec JSON. C’est pourquoi YAML s’est imposé massivement dans les fichiers de configuration (Docker Compose, Kubernetes, GitHub Actions, Ansible, etc.) : il offre le offre un  compromis.
</p>
<h2>
 Syntaxe
</h2>
<h3>
 1. Les trois briques de base
</h3>
<p>
 Tout fichier YAML est construit avec seulement trois types de données :
</p>
<ul>
 <li>
  <strong>
   Scalaires
  </strong>
  : une valeur simple (chaîne, nombre, booléen, null, date)
 </li>
 <li>
  <strong>
   Séquences
  </strong>
  : des listes ordonnées (équivalent d’un tableau)
 </li>
 <li>
  <strong>
   Objets
  </strong>
  : des dictionnaires clé → valeur
 </li>
</ul>
<pre>
# Exemple réunissant les trois
prénom: Alice          # mapping (clé: valeur)
âge: 32                # mapping
développeuse: true     # mapping
hobbies:               # mapping
  - lecture            # séquence (liste)
  - escalade
  - photographie
</pre>
<h3>
 2. L’indentation
</h3>
<p>
 YAML utilise
 <strong>
  l’indentation avec des espaces
 </strong>
 pour indiquer la hiérarchie. Le nombre d’espaces par niveau est libre, mais doit être constant dans tout le fichier (la convention la plus courante est 2 espaces).
</p>
<h3>
 3. Les objets
</h3>
<pre>
nom: Alice Dupont
âge: 32
adresse:
  rue: 12 rue des Lilas
  ville: Paris
  pays: France
</pre>
<h3>
 4. Écrire des séquences (listes)
</h3>
<p>
 Deux syntaxes équivalentes :
</p>
<pre>
# Style bloc (le plus lisible)
fruits:
  - pomme
  - banane
  - orange

# Style « flow » (comme JSON)
fruits: [pomme, banane, orange]
</pre>
<h3>
 5. Les chaînes de caractères
</h3>
<pre>
# Sans guillemets (la plupart du temps)
nom: Alice

# Avec simples ou doubles guillemets si besoin
message: 'Elle a dit : "Salut !"'
description: "Texte sur\nplusieurs lignes\navec retours à la ligne"

# Bloc littéral (garde exactement le texte, retours à la ligne inclus)
poeme: |
  Roses are red
  Violets are blue
  YAML est génial
  Et toi aussi !

# Bloc replié (les retours à la ligne deviennent des espaces)
resume: &gt;
  Ceci est un long texte
  qui sera mis sur une seule
  ligne lors du parsing.
</pre>
<h3>
 6. Les booléens et null
</h3>
<pre>
actif: true          # ou True, TRUE, on, On, yes…
inactif: false       # ou off, no…
site_web: null       # ou ~ ou simplement rien → site_web:
</pre>
<h2>
 7. Les commentaires
</h2>
<pre>
# Ceci est un commentaire
nom: Alice    # commentaire en fin de ligne autorisé
# Les commentaires rendent les fichiers de config très lisibles
</pre>
<h3>
 8. Style flow (comme JSON) – à utiliser avec parcimonie
</h3>
<pre>
personne: { nom: Alice, âge: 32, hobbies: [lecture, escalade] }
</pre>
<h2>
 Exemples
</h2>
<p>
 Considérons les exemples suivants.
</p>
<h3>
 1. En XML
</h3>
<pre>
&lt;person&gt;
  &lt;name&gt;Alice Dupont&lt;/name&gt;
  &lt;age&gt;32&lt;/age&gt;
  &lt;isDeveloper&gt;true&lt;/isDeveloper&gt;
  &lt;address&gt;
    &lt;street&gt;12 rue des Lilas&lt;/street&gt;
    &lt;city&gt;Paris&lt;/city&gt;
    &lt;country&gt;France&lt;/country&gt;
  &lt;/address&gt;
  &lt;hobbies&gt;
    &lt;hobby&gt;lecture&lt;/hobby&gt;
    &lt;hobby&gt;escalade&lt;/hobby&gt;
    &lt;hobby&gt;photographie&lt;/hobby&gt;
  &lt;/hobbies&gt;
&lt;/person&gt;
</pre>
<h3>
 2. En JSON
</h3>
<pre>
{
  "name": "Alice Dupont",
  "age": 32,
  "isDeveloper": true,
  "address": {
    "street": "12 rue des Lilas",
    "city": "Paris",
    "country": "France"
  },
  "hobbies": ["lecture", "escalade", "photographie"]
}
</pre>
<h3>
 3. En YAML
</h3>
<pre>
# Exemple de personne en YAML
name: Alice Dupont
age: 32
isDeveloper: true                  # booléen
address:
  street: 12 rue des Lilas
  city: Paris
  country: France
hobbies:
  - lecture                        # liste avec des tirets
  - escalade
  - photographie
</pre>
<h2>
 Laboratoire YAML
</h2>
<p>
 Utilisez l'application suivante pour tester votre compréhension du YAML.
</p>
<div style="flex: 1; display: flex; flex-direction: column;">
 <label for="yaml" style="display: block; margin-bottom: 0.5rem; font-weight: 600;">
  YAML
 </label>
 <textarea id="yaml" placeholder="personne:
  nom: Dupont
  age: 32
  actif: true
  hobbies:
    - lecture
    - vélo" style="width: 100%; height: 10cm; padding: 1rem; font-family: 'Consolas', 'Monaco', monospace; font-size: 14px; border: 1px solid #ccc; border-radius: 8px; box-sizing: border-box; resize: none;"></textarea>
</div>
<div style="flex: 1; display: flex; flex-direction: column;">
 <label style="display: block; margin-bottom: 0.5rem; font-weight: 600;">
  JSON
  <span id="status" style="font-weight:normal; color:#666;">
   (valide)
  </span>
 </label>
 <pre id="json" style="width: 100%; height: 100%; padding: 1rem; font-family: 'Consolas', 'Monaco', monospace; font-size: 14px; border: 1px solid #ccc; border-radius: 8px; box-sizing: border-box; margin: 0;"></pre>
</div>
<!-- js-yaml depuis le CDN officiel -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/js-yaml/4.1.0/js-yaml.min.js">
</script>
<script>
 const yamlInput = document.getElementById('yaml');
    const jsonOutput = document.getElementById('json');
    const status = document.getElementById('status');
    function convert() {
      const text = yamlInput.value;
      // Réinitialiser le style
      yamlInput.style.backgroundColor = '';
      yamlInput.style.borderColor = '#ccc';
      status.textContent = '';
      jsonOutput.textContent = '';
      if (text.trim() === '') {
        jsonOutput.textContent = '// Entrez du YAML à gauche';
        return;
      }
      try {
        const parsed = jsyaml.load(text);               // parsing YAML
        const json = JSON.stringify(parsed, null, 2);    // pretty JSON
        jsonOutput.textContent = json;
        status.textContent = '(valide)';
        status.style.color = '#28a745';
      } catch (err) {
        jsonOutput.textContent = '';
        status.textContent = '(erreur : ' + err.message + ')';
        status.style.color = '#dc3545';
        yamlInput.style.backgroundColor = '#ffecec';
        yamlInput.style.borderColor = '#f5a5a5';
      }
    }
    // Conversion immédiate à chaque frappe
    yamlInput.addEventListener('input', convert);
    // Premier rendu avec l'exemple
    convert();
</script>
