---
title: "Pense-bête DTD"
weight: 180
---
<h1>Pense-bête DTD</h1>

## Quelques symboles importants en DTD

**<!DOCTYPE nomXML_elementRacine SYSTEM "URL">**

: Déclaration de type de document.

**<!ELEMENT ... >**

: Déclaration d'un élément (instruction DTD).

**?** — Élément optionnel.

<strong>*</strong> — Élément pouvant être présent plusieurs fois (0..∞).

**+** — Élément présent au moins une fois (1..∞).

**|** — Alternative (ou).

**#PCDATA** — Contenu textuel (parsed character data).

**<!ATTLIST nomElementX nomAttributY ...>**

: Spécifie qu’un élément `nomElementX` possède l’attribut `nomAttributY`.

**CDATA** — Type d’attribut indiquant que l’attribut contient du texte.

**REQUIRED** — Attribut obligatoire.

**IMPLIED** — Attribut optionnel (pas de valeur par défaut).

**FIXED** — Attribut fixé à une valeur constante.

**<!ENTITY nomEntiteX "Yvaleur">**

: Définit une entité nommée `nomEntiteX` qui vaut `Yvaleur`.

> Note : j'ai remplacé `valeurY` par `Yvaleur` dans l'exemple pour éviter une répétition maladroite du mot "valeur".

**<!ENTITY % nomEntiteX "Yvaleur">**

: Entité paramètre pour la DTD (locale à la DTD) — `nomEntiteX` prend la valeur `Yvaleur`.

---

### Exemples rapides

```dtd
<!DOCTYPE livre SYSTEM "livre.dtd">
<!ELEMENT livre (titre, auteur+, chapitre*)>
<!ATTLIST chapitre numero CDATA #REQUIRED>
<!ENTITY entiteExemple "Valeur de l'entite">
```

Ces exemples montrent la syntaxe de base pour déclarer un DTD et des éléments/attributs.
