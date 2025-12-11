---
title: "Laboratoire sur la structure en arbre des documents XML"
weight: 90
---
<h1>
 Laboratoire sur la structure en arbre des documents XML
</h1>
<p>
 Il est important de bien comprendre la structure en arbre des documents XML. Comme nous l’avons vu, un document XML
    est arbre dont la racine est toujours le noeud-racine suivi normalement d’autres noeuds, comme des noeuds d’éléments.
    Les différents noeuds sont ordonnés (si on interverti deux éléments, on crée de facto un nouveau document). Il faut
    comprendre que les bouts de texte apparaissant dans un document XML sont noeuds à part entière.
</p>
<p>
 Nous vous invitons donc à utiliser l’application suivant pour bien vous familiariser avec la structure des documents
    XML. Vous pouvez saisir un document XML et le décomposer. Essayez de créer vos propres documents (bien formés) pour
    tester votre compréhension.
</p>
<p>
 Bien sûr, si vous saisissez un document XML qui n’est pas valable, vous n’obtiendrez pas une décomposition, mais un
    message d’erreur.
</p>
<p>
 Faites des expérience jusqu’à ce que vous soyez certain d’avoir bien compris.
</p>
<div style="max-width: 800px; margin: 0 auto; background-color: #ffffff; padding: 24px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
 <h1 style="font-size: 24px; font-weight: bold; margin-bottom: 16px; color: #1f2937;">
  Application d'arborescence XML
 </h1>
 <p style="margin-bottom: 16px; color: #4b5563;">
  Entrez un contenu XML dans le champ ci-dessous, puis cliquez sur "Dessine" pour afficher l'arborescence sous forme de liste hiérarchique, incluant les attributs des nœuds. Exemple :
 </p>
 <pre style="background-color: #e6f4ea; padding: 12px; border: 1px solid #15803d; border-radius: 4px; font-family: monospace; font-size: 14px; color: #374151; margin-bottom: 16px;">&lt;library&gt;
    &lt;book id="1" genre="fiction"&gt;
        &lt;title&gt;The Hobbit&lt;/title&gt;
        &lt;author&gt;J.R.R. Tolkien&lt;/author&gt;
    &lt;/book&gt;
    &lt;book id="2" genre="non-fiction"&gt;
        &lt;title&gt;Sapiens&lt;/title&gt;
        &lt;author&gt;Yuval Noah Harari&lt;/author&gt;
    &lt;/book&gt;
&lt;/library&gt;
        </pre>
 <div style="background-color: #f9fafb; padding: 16px; border: 1px solid #e5e7eb; border-radius: 8px;">
  <div style="margin-bottom: 16px;">
   <label for="xmlInput" style="display: block; font-size: 14px; font-weight: medium; color: #374151;">
    Contenu XML :
   </label>
   <textarea id="xmlInput" style="width: 100%; padding: 8px; border: 1px solid #d1d5db; border-radius: 4px; min-height: 100px;">&lt;library&gt;
    &lt;book id="1" genre="fiction"&gt;
        The Hobbit
        &lt;author&gt;J.R.R. Tolkien&lt;/author&gt;
    &lt;/book&gt;
    &lt;book id="2" genre="non-fiction"&gt;
        Sapiens
        &lt;author&gt;Yuval Noah Harari&lt;/author&gt;
    &lt;/book&gt;
&lt;/library&gt;
                </textarea>
  </div>
  <button onclick="drawTree()" style="width: 100%; background-color: #2563eb; color: #ffffff; padding: 8px; border: none; border-radius: 4px; cursor: pointer; transition: background-color 0.2s;">
   Dessine
  </button>
  <div id="error" style="margin-top: 16px; color: #dc2626; font-size: 14px;">
  </div>
  <div id="tree" style="margin-top: 16px; padding: 12px; border: 1px solid #d1d5db; border-radius: 4px;">
  </div>
 </div>
</div>
<script>
 function drawTree() {
            const xmlInput = document.getElementById('xmlInput').value.trim();
            const errorDiv = document.getElementById('error');
            const treeDiv = document.getElementById('tree');
            // Réinitialiser
            errorDiv.innerHTML = '';
            treeDiv.innerHTML = '';
            if (!xmlInput) {
                errorDiv.innerHTML = 'Erreur : Veuillez entrer un contenu XML.';
                return;
            }
            try {
                const parser = new DOMParser();
                const xmlDoc = parser.parseFromString(xmlInput, 'text/xml');
                // Vérifier les erreurs de parsing
                if (xmlDoc.getElementsByTagName('parsererror').length > 0) {
                    throw new Error('XML mal formé');
                }
                const root = xmlDoc.documentElement;
                if (!root) {
                    throw new Error('Aucun nœud racine trouvé.');
                }
                // Fonction pour formater les attributs
                function formatAttributes(node) {
                    const attributes = Array.from(node.attributes);
                    if (attributes.length === 0) return '';
                    return ' (' + attributes.map(attr => `${attr.name}="${attr.value}"`).join(', ') + ')';
                }
                // Fonction récursive pour construire la liste
                function buildTree(node) {
                    const ul = document.createElement('ul');
                    ul.style.listStyleType = 'none';
                    ul.style.paddingLeft = '20px';
                    ul.style.borderLeft = '2px solid #15803d';
                    ul.style.margin = '0';
                    const li = document.createElement('li');
                    li.style.margin = '8px 0';
                    li.style.position = 'relative';
                    const nodeSpan = document.createElement('span');
                    nodeSpan.textContent = node.nodeName + formatAttributes(node);
                    nodeSpan.style.display = 'inline-block';
                    nodeSpan.style.padding = '4px 8px';
                    nodeSpan.style.backgroundColor = '#e6f4ea';
                    nodeSpan.style.border = '1px solid #15803d';
                    nodeSpan.style.borderRadius = '4px';
                    nodeSpan.style.color = '#374151';
                    nodeSpan.style.fontSize = '14px';
                    li.appendChild(nodeSpan);
                    // Ajouter les enfants
                    if (node.children.length > 0) {
                        const childUl = buildTreeChildren(node);
                        li.appendChild(childUl);
                    }
                    ul.appendChild(li);
                    return ul;
                    function buildTreeChildren(parent) {
                        const childUl = document.createElement('ul');
                        childUl.style.listStyleType = 'none';
                        childUl.style.paddingLeft = '20px';
                        childUl.style.borderLeft = '2px solid #15803d';
                        childUl.style.margin = '0';
                        for (let child of parent.children) {
                            const childLi = document.createElement('li');
                            childLi.style.margin = '8px 0';
                            childLi.style.position = 'relative';
                            const childSpan = document.createElement('span');
                            childSpan.textContent = child.nodeName + formatAttributes(child);
                            childSpan.style.display = 'inline-block';
                            childSpan.style.padding = '4px 8px';
                            childSpan.style.backgroundColor = '#e6f4ea';
                            childSpan.style.border = '1px solid #15803d';
                            childSpan.style.borderRadius = '4px';
                            childSpan.style.color = '#374151';
                            childSpan.style.fontSize = '14px';
                            childLi.appendChild(childSpan);
                            if (child.children.length > 0) {
                                const grandChildUl = buildTreeChildren(child);
                                childLi.appendChild(grandChildUl);
                            }
                            childUl.appendChild(childLi);
                        }
                        return childUl;
                    }
                }
                // Construire et afficher l'arborescence
                const treeUl = buildTree(root);
                treeDiv.appendChild(treeUl);
            } catch (e) {
                errorDiv.innerHTML = `Erreur : ${e.message || 'Impossible de traiter le XML.'}`;
            }
        }
</script>
<p>
 <br/>
</p>
