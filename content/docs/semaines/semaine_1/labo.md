---
title: "Vérificateur de XML bien formé"
weight: 90
---

# Vérificateur de XML bien formé  

<p>Collez votre document XML ci-dessous et cliquez sur le bouton pour vérifier s’il est bien formé.
Vérifiez votre compréhension de la syntaxe XML en testant différents documents.</p>

<textarea id="xmlInput" placeholder="Collez ici votre XML..." style="width: 100%; height: 300px; font-family: Consolas, Monaco, monospace; font-size: 14px; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;"><?xml version="1.0" encoding="UTF-8"?>
<catalogue>&#10;    <livre id="1">&#10;        <titre>Le Petit Prince</titre>&#10;        <auteur>Antoine de Saint-Exupéry</auteur>&#10;        <année>1943</année>&#10;    </livre>&#10;</catalogue></textarea>

<button onclick="verifierXML()" style="margin-top: 15px; padding: 10px 20px; font-size: 16px; background: #3498db; color: white; border: none; border-radius: 4px; cursor: pointer;">Vérifier le XML</button>

<div id="resultat" style="margin-top: 20px; padding: 15px; font-size: 18px; font-weight: bold; border-radius: 4px;"></div>

<script>
    function appliquerStyleValide(element) {
        element.style.background = '#d5efda';
        element.style.color = '#27ae60';
        element.style.border = '1px solid #27ae60';
    }

    function appliquerStyleInvalide(element) {
        element.style.background = '#fadbd8';
        element.style.color = '#c0392b';
        element.style.border = '1px solid #c0392b';
    }

    function verifierXML() {
        const texte = document.getElementById('xmlInput').value.trim();
        const resultatDiv = document.getElementById('resultat');
        
        // Si le champ est vide
        if (texte === '') {
            resultatDiv.textContent = 'Veuillez entrer un document XML.';
            appliquerStyleInvalide(resultatDiv);
            return;
        }

        try {
            // Création d’un parser XML
            const parser = new DOMParser();
            const doc = parser.parseFromString(texte, 'application/xml');

            // parseError existe dans Firefox, errorCode dans certains cas
            const erreurs = doc.getElementsByTagName('parsererror');

            if (erreurs.length > 0) {
                // Il y a une erreur de parsing
                const messageErreur = erreurs[0].textContent || erreurs[0].innerText || 'Erreur inconnue';
                resultatDiv.textContent = 'XML non valide : ' + extraireMessage(messageErreur);
                appliquerStyleInvalide(resultatDiv);
            } else {
                resultatDiv.textContent = 'Bravo ! Le XML est bien formé.';
                appliquerStyleValide(resultatDiv);
            }
        } catch (e) {
            resultatDiv.textContent = 'XML non valide : ' + e.message;
            appliquerStyleInvalide(resultatDiv);
        }
    }

    // Fonction pour nettoyer le message d’erreur (différent selon les navigateurs)
    function extraireMessage(texteComplet) {
        const lignes = texteComplet.split('\n');
        for (let ligne of lignes) {
            ligne = ligne.trim();
            if (ligne && !ligne.startsWith('<?xml') && !ligne.includes('parsererror')) {
                return ligne;
            }
        }
        return 'Erreur de syntaxe XML détectée.';
    }

    // Vérification automatique au chargement pour l’exemple
    window.onload = function() {
        verifierXML();
    };
</script>