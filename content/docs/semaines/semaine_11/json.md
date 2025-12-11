---
title: "JSON"
weight: 25
---

# JSON

<p>
 Malheureusement, le traitement d’un document XML est parfois    inutilement lourd. Pour cette raison, on remplace souvent le XML par du
 <a href="https://fr.wikipedia.org/wiki/JavaScript_Object_Notation" rel="noopener noreferrer external" target="_blank">
  JSON
 </a>
 (JavaScript Object Notation).
</p>
<p>
 JSON a supplanté le XML dans plusieurs applications quant il s’agit de
    transmettre des informations simples, surtout lors que le récipiendaire
    utilise le JavaScript.
</p>
<p>
 On peut voir le JSON comme une forme très limitée de JavaScript où on peut
    utiliser que des « objets » et des tableaux. Un
    « objets » en JavaScript est une structure de clés-valeurs avec la
    syntaxe «
 <i>
  clef1 : valeur1, clef2:valeur2
 </i>
 » alors
    qu’un tableau est une simple liste de valeurs avec la syntaxe [ valeur1,
    valeur2 ] . Les clés doivent être des chaînes de caractères, mais les
    valeurs peuvent être d’autres objets, des tableaux, des chaînes de
    caractères, des nombres, des valeurs Booléennes ou la valeur spéciale
    « null ».
</p>
<p>
 Parce qu’un objet ou un tableau peuvent, eux-mêmes, comprendre des objets et
    des tableaux, la syntaxe JSON permet des structures en arbre ressemblant au
    XML.
</p>
<p>
 Voici, par exemple, les mêmes données présentées à la fois en JSON et en
    XML :
</p>
<pre><span style="color:#800080; ">{</span>
    <span style="color:#800000; ">"</span><span style="color:#0000e6; ">nom</span><span style="color:#800000; ">"</span><span style="color:#800080; ">:</span>
    <span style="color:#800000; ">"</span><span style="color:#0000e6; ">Daniel
        Lemire</span><span style="color:#800000; ">"</span><span style="color:#808030; ">,</span>
    <span style="color:#800000; ">"</span><span style="color:#0000e6; ">âge</span><span style="color:#800000; ">"</span><span style="color:#800080; ">:</span>
    <span style="color:#008c00; ">72</span><span style="color:#808030; ">,</span>
    <span style="color:#800000; ">"</span><span style="color:#0000e6; ">téléphone</span><span style="color:#800000; ">"</span><span style="color:#800080; ">:</span>
    <span style="color:#808030; ">[</span><span style="color:#800000; ">"</span><span style="color:#0000e6; ">442-4321</span><span style="color:#800000; ">"</span><span style="color:#808030; ">,</span><span style="color:#800000; ">"</span><span style="color:#0000e6; ">442-4323</span><span style="color:#800000; ">"</span><span style="color:#808030; ">]</span><span style="color:#808030; "></span>
    <span style="color:#800080; ">}</span>
</pre>
<pre><span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">personne</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>Daniel Lemire<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">nom</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">age</span><span style="color:#a65700; ">&gt;</span>72<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">age</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">telephone</span><span style="color:#a65700; ">&gt;</span>442-4321<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">telephone</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;</span><span style="color:#5f5035; ">telephone</span><span style="color:#a65700; ">&gt;</span>442-4323<span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">telephone</span><span style="color:#a65700; ">&gt;</span>
    <span style="color:#a65700; ">&lt;/</span><span style="color:#5f5035; ">personne</span><span style="color:#a65700; ">&gt;</span>
</pre>
<p>
 Le chargement d’une chaîne de caractères au format JSON en JavaScript est
    aisé, il suffit d’utiliser la fonction : « var monjson =
    JSON.parse(machaine) ; ». La fonction retourne l’objet JavaScript
    correspondant. Par exemple, je pourrait faire monjson["nom"] dans l’exemple
    précédent pour obtenir le résultat « Daniel Lemire ». Nul besoin
    d’une API DOM.
</p>
<p>
 Bien que JSON représente une excellente idée, il s’agit d’une idée plus
    simple que le XML... il n’y a pas, par exemple, d’équivalent du XSLT ou du
    CSS en JSON. Bien qu’on le pourrait en théorie, personne ne préconise
    d’utiliser JSON comme format de base pour les documents de bureautique (par
    ex., Microsoft Office).
</p>
<div style="max-width: 800px; margin: 0 auto; background-color: #ffffff; padding: 24px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
 <h1 style="font-size: 24px; font-weight: bold; margin-bottom: 16px; color: #1f2937;">
  Application d'Arborescence JSON
 </h1>
 <p style="margin-bottom: 16px; color: #4b5563;">
  Entrez un contenu JSON dans le champ ci-dessous, puis cliquez sur "Dessine" pour afficher l'arborescence sous forme de liste hiérarchique. Exemple :
 </p>
 <pre style="background-color: #e6f4ea; padding: 12px; border: 1px solid #15803d; border-radius: 4px; font-family: monospace; font-size: 14px; color: #374151; margin-bottom: 16px;">{
    "library": {
        "books": [
            {
                "id": 1,
                "genre": "fiction",
                "title": "The Hobbit",
                "author": "J.R.R. Tolkien"
            },
            {
                "id": 2,
                "genre": "non-fiction",
                "title": "Sapiens",
                "author": "Yuval Noah Harari"
            }
        ]
    }
}
        </pre>
 <div style="background-color: #f9fafb; padding: 16px; border: 1px solid #e5e7eb; border-radius: 8px;">
  <div style="margin-bottom: 16px;">
   <label for="jsonInput" style="display: block; font-size: 14px; font-weight: medium; color: #374151;">
    Contenu JSON :
   </label>
   <textarea id="jsonInput" style="width: 100%; padding: 8px; border: 1px solid #d1d5db; border-radius: 4px; min-height: 100px;">{
    "library": {
        "books": [
            {
                "id": 1,
                "genre": "fiction",
                "title": "The Hobbit",
                "author": "J.R.R. Tolkien"
            },
            {
                "id": 2,
                "genre": "non-fiction",
                "title": "Sapiens",
                "author": "Yuval Noah Harari"
            }
        ]
    }
}
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
            const jsonInput = document.getElementById('jsonInput').value.trim();
            const errorDiv = document.getElementById('error');
            const treeDiv = document.getElementById('tree');
            // Réinitialiser
            errorDiv.innerHTML = '';
            treeDiv.innerHTML = '';
            if (!jsonInput) {
                errorDiv.innerHTML = 'Erreur : Veuillez entrer un contenu JSON.';
                return;
            }
            try {
                const jsonObj = JSON.parse(jsonInput);
                // Fonction récursive pour construire la liste
                function buildTree(obj, key = 'root') {
                    const ul = document.createElement('ul');
                    ul.style.listStyleType = 'none';
                    ul.style.paddingLeft = '20px';
                    ul.style.borderLeft = '2px solid #15803d';
                    ul.style.margin = '0';
                    const li = document.createElement('li');
                    li.style.margin = '8px 0';
                    li.style.position = 'relative';
                    const nodeSpan = document.createElement('span');
                    let displayText = key;
                    // Afficher la valeur si c'est une feuille
                    if (typeof obj !== 'object' || obj === null) {
                        displayText += `: ${obj === null ? 'null' : obj}`;
                    }
                    nodeSpan.textContent = displayText;
                    nodeSpan.style.display = 'inline-block';
                    nodeSpan.style.padding = '4px 8px';
                    nodeSpan.style.backgroundColor = '#e6f4ea';
                    nodeSpan.style.border = '1px solid #15803d';
                    nodeSpan.style.borderRadius = '4px';
                    nodeSpan.style.color = '#374151';
                    nodeSpan.style.fontSize = '14px';
                    li.appendChild(nodeSpan);
                    // Ajouter les enfants si objet ou tableau
                    if (typeof obj === 'object' && obj !== null) {
                        const childUl = buildTreeChildren(obj);
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
                        if (Array.isArray(parent)) {
                            parent.forEach((item, index) => {
                                const childLi = document.createElement('li');
                                childLi.style.margin = '8px 0';
                                childLi.style.position = 'relative';
                                const childSpan = document.createElement('span');
                                childSpan.textContent = `[${index}]`;
                                childSpan.style.display = 'inline-block';
                                childSpan.style.padding = '4px 8px';
                                childSpan.style.backgroundColor = '#e6f4ea';
                                childSpan.style.border = '1px solid #15803d';
                                childSpan.style.borderRadius = '4px';
                                childSpan.style.color = '#374151';
                                childSpan.style.fontSize = '14px';
                                childLi.appendChild(childSpan);
                                if (typeof item === 'object' && item !== null) {
                                    const grandChildUl = buildTreeChildren(item);
                                    childLi.appendChild(grandChildUl);
                                } else {
                                    const valueSpan = document.createElement('span');
                                    valueSpan.textContent = `: ${item === null ? 'null' : item}`;
                                    valueSpan.style.color = '#374151';
                                    valueSpan.style.fontSize = '14px';
                                    childLi.appendChild(valueSpan);
                                }
                                childUl.appendChild(childLi);
                            });
                        } else {
                            for (let childKey in parent) {
                                const childLi = document.createElement('li');
                                childLi.style.margin = '8px 0';
                                childLi.style.position = 'relative';
                                const childSpan = document.createElement('span');
                                childSpan.textContent = childKey;
                                childSpan.style.display = 'inline-block';
                                childSpan.style.padding = '4px 8px';
                                childSpan.style.backgroundColor = '#e6f4ea';
                                childSpan.style.border = '1px solid #15803d';
                                childSpan.style.borderRadius = '4px';
                                childSpan.style.color = '#374151';
                                childSpan.style.fontSize = '14px';
                                childLi.appendChild(childSpan);
                                if (typeof parent[childKey] === 'object' && parent[childKey] !== null) {
                                    const grandChildUl = buildTreeChildren(parent[childKey]);
                                    childLi.appendChild(grandChildUl);
                                } else {
                                    const valueSpan = document.createElement('span');
                                    valueSpan.textContent = `: ${parent[childKey] === null ? 'null' : parent[childKey]}`;
                                    valueSpan.style.color = '#374151';
                                    valueSpan.style.fontSize = '14px';
                                    childLi.appendChild(valueSpan);
                                }
                                childUl.appendChild(childLi);
                            }
                        }
                        return childUl;
                    }
                }
                // Construire et afficher l'arborescence
                const treeUl = buildTree(jsonObj);
                treeDiv.appendChild(treeUl);
            } catch (e) {
                errorDiv.innerHTML = `Erreur : ${e.message || 'Impossible de traiter le JSON.'}`;
            }
        }
</script>


À lire :

- [présentation de JSON sur json.org](http://json.org/json-fr.html)
