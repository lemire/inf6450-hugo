---
title: "MarkDown"
weight: 80
---
<h1 class="">
 MarkDown
</h1>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js">
</script>
<div class="">
 <p>
  Composer un document en XML afin de créer un document n’est pas toujours une chose facile. Les balises occupent beaucoup d’espace et la structure du document n’est pas toujours apparente. Une solution de rechange viable est le MarkDown qui est un format de texte simple permettant un formattage basique des différents éléments.
 </p>
 <p>
  Pour utiliser le Markdown, il suffit de maîtriser quelques règles de base. Par exemple, pour créer un titre, on place un ou plusieurs # avant le texte (comme # Titre pour un titre principal), pour mettre du texte en gras, on entoure le mot avec deux étoiles **gras**, et pour une liste, on commence chaque ligne par un tiret -. Ces conventions permettent de structurer un document sans quitter le clavier pour des outils complexes comme Word. Le texte reste lisible même sans conversion, ce qui est parfait pour les gens qui veulent se concentrer sur le contenu plutôt que sur le formatage.
 </p>
 <div style="max-width: 1000px; margin: 0 auto; background-color: #ffffff; padding: 24px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
  <h1 style="font-size: 24px; font-weight: bold; margin-bottom: 16px; color: #1f2937;">
   Laboratoire Markdown : Rendu de Liste d'étudiants
  </h1>
  <p style="margin-bottom: 16px; color: #4b5563;">
   Modifiez ou utilisez le contenu Markdown ci-dessous, puis cliquez sur "Rendre" pour afficher le résultat formaté. Exemple :
  </p>
  <div style="margin-bottom: 24px;">
   <h2 style="font-size: 18px; font-weight: bold; color: #374151; margin-bottom: 8px;">
    Exemple Markdown :
   </h2>
   <pre style="background-color: #e6f4ea; padding: 12px; border: 1px solid #15803d; border-radius: 4px; font-family: monospace; font-size: 14px; color: #374151;"># Liste d'étudiants

Voici une liste d'étudiants inscrits :

- **Jean Aaron**
- **Pierre Laroche**

*Fin du document.*
            </pre>
  </div>
  <div style="background-color: #f9fafb; padding: 16px; border: 1px solid #e5e7eb; border-radius: 8px;">
   <p style="font-size: 16px; font-weight: bold; color: #374151; margin-bottom: 8px;">
    Contenu Markdown :
   </p>
   <textarea cols="45" id="mdInput" rows="15" style="width: 100%; padding: 8px; border: 1px solid #d1d5db; border-radius: 4px; font-family: monospace; font-size: 14px; margin-bottom: 16px;"># Liste d'étudiants
Voici une liste d'étudiants inscrits :
- **Jean Aaron**
- **Pierre Laroche**
*Fin du document.*
            </textarea>
   <button id="renderButton" style="width: 100%; background-color: #2563eb; color: #ffffff; padding: 10px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; transition: background-color 0.2s; margin-bottom: 16px;">
    Rendre
   </button>
   <div id="error" style="margin-bottom: 16px; color: #dc2626; font-size: 14px;">
   </div>
   <div id="result" style="padding: 12px; border: 1px solid #d1d5db; border-radius: 4px;">
   </div>
  </div>
 </div>
 <script>
  document.getElementById('renderButton').addEventListener('click', function() {
            const mdInput = document.getElementById('mdInput').value.trim();
            const errorDiv = document.getElementById('error');
            const resultDiv = document.getElementById('result');
            // Réinitialiser
            errorDiv.textContent = '';
            resultDiv.innerHTML = '';
            if (!mdInput) {
                errorDiv.textContent = 'Erreur : Veuillez entrer un contenu Markdown.';
                return;
            }
            try {
                // Convertir le Markdown en HTML avec Marked
                const html = marked.parse(mdInput);
                resultDiv.innerHTML = html;
                // Appliquer des styles inline au contenu rendu
                resultDiv.querySelectorAll('*').forEach(element => {
                    element.style.margin = '0';
                    element.style.padding = '0';
                    element.style.fontFamily = 'Arial, sans-serif';
                    element.style.color = '#374151';
                });
                resultDiv.querySelectorAll('h1').forEach(h1 => {
                    h1.style.fontSize = '24px';
                    h1.style.fontWeight = 'bold';
                    h1.style.marginBottom = '16px';
                });
                resultDiv.querySelectorAll('p').forEach(p => {
                    p.style.fontSize = '14px';
                    p.style.marginBottom = '12px';
                });
                resultDiv.querySelectorAll('ul').forEach(ul => {
                    ul.style.listStyleType = 'disc';
                    ul.style.paddingLeft = '20px';
                    ul.style.marginBottom = '12px';
                });
                resultDiv.querySelectorAll('li').forEach(li => {
                    li.style.fontSize = '14px';
                    li.style.marginBottom = '8px';
                });
                resultDiv.querySelectorAll('strong').forEach(strong => {
                    strong.style.fontWeight = 'bold';
                });
                resultDiv.querySelectorAll('em').forEach(em => {
                    em.style.fontStyle = 'italic';
                });
            } catch (e) {
                errorDiv.textContent = `Erreur : Impossible de traiter le Markdown - ${e.message}`;
            }
        });
 </script>
</div>
<hr/>
