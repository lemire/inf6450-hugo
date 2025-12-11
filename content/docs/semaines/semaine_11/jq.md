---
title: "Activité avec jq (optionnel)"
weight: 38
---

# Laboratoire pratique avec jq (optionnel)

jq est un petit programme qui permet de lire, filtrer, modifier et formater des fichiers JSON directement dans le terminal. Il peut servir d'équivalent JSON
aux approches de traitement XML comme XSLT, XQuery et XPath.


Il faut d'abord installer jq sur votre machine.


## Installation sur Windows

Il y a plusieurs méthodes. Voici les deux plus simples pour un débutant.

### Méthode 1 – La plus simple : télécharger l’exécutable officiel

1. Ouvrez votre navigateur et allez ici : https://github.com/jqlang/jq/releases
2. Descendez à la dernière version.
3. Sous “Assets”, cliquez sur le fichier `jq-win64.exe`. Il est possible que vous deviez chercher un peu, le fichier est bel est bien présent.
4. Le fichier se télécharge (environ 3-4 Mo).

5. **Renommez-le pour plus de simplicité** : cliquez droit sur le fichier → Renommer → appelez-le simplement `jq.exe`

6. **Déplacez-le dans un dossier facile d’accès**  
   Créez un dossier par exemple `C:\jq` et mettez-y le fichier `jq.exe`.

7. **Ajoutez ce dossier au PATH** (c’est ce qui permet de taper `jq` depuis n’importe où)  
   a. Cliquez droit sur “Ce PC” (ou “Ordinateur”) → Propriétés  
   b. Cliquez sur “Paramètres système avancés” (à droite)  
   c. Cliquez sur “Variables d’environnement”  
   d. Dans la partie “Variables système” (en bas), trouvez la ligne “Path” → cliquez sur Modifier  
   e. Cliquez sur “Nouveau” → tapez `C:\jq` → OK → OK → OK

8. **Fermez et rouvrez votre terminal** (Invite de commandes ou PowerShell).

9. Tapez :
   ```cmd
   jq --version
   ```
   Si vous voyez la version s’afficher → c’est bon !

### Méthode 2 – Avec Winget

Si vous avez Windows 10 ou 11 ou mieux :

1. Ouvrez PowerShell ou l’Invite de commandes **en tant qu’administrateur** (clic droit → Exécuter en tant qu’administrateur).
2. Tapez cette commande :
   ```powershell
   winget install jqlang.jq
   ```
3. Appuyez sur Entrée, acceptez si on vous demande.
4. Une fois terminé, ouvrez un **nouveau** terminal (normal, pas admin) et tapez :
   ```powershell
   jq --version
   ```

### Méthode 3 – Avec Chocolatey

1. Ouvrez PowerShell en administrateur.
2. Installez Chocolatey (une seule fois) :
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```
3. Puis installez jq :
   ```powershell
   choco install jq
   ```

## Installation sur macOS


### Méthode recommandée et la plus simple : Homebrew

1. **Ouvrir le Terminal**  
   Appuyez sur `Cmd + Espace`, tapez `Terminal` et appuyez sur Entrée.

2. **Installez Homebrew** (c’est un gestionnaire de paquets, comme un “App Store” en ligne de commande)  
   Copiez-collez cette ligne dans le Terminal et appuyez sur Entrée :
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   - Il va vous demander votre mot de passe (vous ne verrez pas les étoiles quand vous tapez, c’est normal).
   - Appuyez sur Entrée quand il vous le demande pour continuer.
   - Ça prend 2 à 5 minutes selon votre connexion.

3. **Une fois Homebrew installé, installez jq en une seule commande**  
   ```bash
   brew install jq
   ```

4. **Vérifiez que ça fonctionne**  
   Tapez cette commande et appuyez sur Entrée :
   ```bash
   jq --version
   ```
   Vous devriez voir quelque chose comme `jq-1.7` ou `jq-1.7.1`.

C’est fini ! Vous avez jq sur votre Mac.

### Méthode sans Homebrew

Vous pouvez télécharger la version pré-compilée directement :

1. Allez sur cette page : https://github.com/jqlang/jq/releases
2. Descendez jusqu’à la dernière version (en haut).
3. Sous “Assets”, cliquez sur le fichier qui s’appelle `jq-macos-arm64` (si vous avez un Mac M1/M2/M3/...) ou `jq-macos-amd64` (si vous avez un Mac Intel plus ancien).
4. Le fichier se télécharge (il fait ~3 Mo).
5. Ouvrez le Terminal, allez dans votre dossier Téléchargements :
   ```bash
   cd ~/Downloads
   ```
6. Rendez-le exécutable et déplacez-le au bon endroit :
   ```bash
   chmod +x jq-macos-arm64
   sudo mv jq-macos-arm64 /usr/local/bin/jq
   ```
   (Il vous demandera votre mot de passe pour `sudo`).
7. Vérifiez avec `jq --version`.

## Premier test rapide

Copiez-collez ceci dans votre terminal :

```bash
echo '{"utilisateur": "Alice", "age": 30, "ville": "Paris"}' | jq '.utilisateur'
```

Vous devriez voir s’afficher :
```
"Alice"
```

Si vous voyez ça → bravo, jq est parfaitement installé !




### Jeu de données utilisé

Créez un fichier `bibliotheque.json` :

```json
{
  "bibliotheque": {
    "nom": "Médiathèque centrale",
    "livres": [
      {
        "id": "b001",
        "titre": "1984",
        "auteur": "George Orwell",
        "année": 1949,
        "genres": ["dystopie", "politique"],
        "empruntable": true,
        "emprunts": [
          {"date": "2024-01-15", "lecteur": "Alice"},
          {"date": "2025-03-20", "lecteur": "Bob"}
        ]
      },
      {
        "id": "b002",
        "titre": "Le Petit Prince",
        "auteur": "Antoine de Saint-Exupéry",
        "année": 1943,
        "genres": ["conte"],
        "empruntable": false
      },
      {
        "id": "b003",
        "titre": "Fondation",
        "auteur": "Isaac Asimov",
        "année": 1951,
        "genres": ["science-fiction", "cycle"],
        "empruntable": true,
        "prix": 18.90
      }
    ]
  }
}
```

### Correspondance rapide XML ↔ JSON → jq

| Concept XML / XPath / XQuery           | Équivalent jq                                           |
|---------------------------------------|----------------------------------------------------------|
| `/bibliotheque/livres/livre[3]`       | `.bibliotheque.livres[2]` (indices commencent à 0)       |
| `//livre[titre="1984"]`               | `.bibliotheque.livres[] \| select(.titre=="1984")`       |
| `livre/@id`                           | `.id`                                                    |
| `count(//livre)`                      | `[.bibliotheque.livres[]] \| length`                     |
| `livre/genres/genre`                  | `.genres[]`                                              |
| Construction nouvelle structure (XSLT)| `{titre: .titre, auteur: .auteur}`                        |

### Exercices progressifs

#### Exercice 1 – Affichage brut et pretty-print
```bash
jq . bibliotheque.json                  # équivalent cat
jq '.' bibliotheque.json                # plus lisible
```

#### Exercice 2 – Sélection simple (équivalent XPath absolu)
```bash
# Tous les titres de livres
jq '.bibliotheque.livres[].titre' bibliotheque.json

# Le nom de la bibliothèque
jq '.bibliotheque.nom' bibliotheque.json
```

#### Exercice 3 – Parcours de tableau avec [] (comme // en XPath)
```bash
# Tous les auteurs
jq '.bibliotheque.livres[].auteur' bibliotheque.json

# Tous les genres (aplatissement automatique)
jq '.bibliotheque.livres[].genres[]' bibliotheque.json
```

#### Exercice 4 – Filtrage avec select() (comme [condition] en XPath)
```bash
# Livres publiés après 1950
jq '.bibliotheque.livres[] | select(.année > 1950)' bibliotheque.json

# Livres empruntables
jq '.bibliotheque.livres[] | select(.empruntable == true)' bibliotheque.json

# Livres contenant "fiction" dans les genres
jq '.bibliotheque.livres[] | select(.genres[] | contains("fiction"))' bibliotheque.json
```

#### Exercice 5 – Projection / construction de nouveaux objets (comme XSLT)
```bash
# Liste simplifiée : titre + année
jq '.bibliotheque.livres[] | {titre, année}' bibliotheque.json

# Créer un catalogue avec id comme clé
jq '.bibliotheque.livres | map({key: .id, value: {titre, auteur}}) | from_entries' bibliotheque.json
```

#### Exercice 6 – Agrégations (length, min, max, group_by…)
```bash
# Nombre total de livres
jq '[.bibliotheque.livres[]] | length' bibliotheque.json

# Année la plus ancienne
jq '[.bibliotheque.livres[].année] | min' bibliotheque.json

# Regrouper par première lettre du titre
jq '.bibliotheque.livres | group_by(.titre[0:1]) | map({lettre: .[0].titre[0:1], count: length})' bibliotheque.json
```

#### Exercice 7 – Gestion des valeurs optionnelles (comme if en XQuery)
```bash
# Afficher le prix, ou "non vendu" s'il n’existe pas
jq '.bibliotheque.livres[] | .titre as $t | .prix // "non vendu" | "\($t) : \(.)"' bibliotheque.json
```

#### Exercice 8 – Transformation complète (votre premier "XSLT JSON")
Créer un fichier `catalogue-court.json` contenant seulement :

```
[
  {"id": "...", "titre": "...", "auteur": "...", "disponible": true/false}
]
```

Solution en une ligne :

```bash
jq '[ .bibliotheque.livres[] | {id, titre, auteur, disponible: .empruntable}]' bibliotheque.json > catalogue-court.json
```

#### Exercice 9 – Bonus : jq comme greppel pour logs JSON
```bash
# Supposons un log d’accès au format JSON par ligne JSON
cat access.log | jq 'select(.status == 404) | .ip + " " + .url'
```

### Mini-projet

À partir de `bibliotheque.json`, produisez un fichier `rapport.md` en Markdown contenant :

- Le nom de la bibliothèque en titre
- Un tableau Markdown avec : Titre | Auteur | Année | Genres | Empruntable | Nombre d’emprunts (0 si absent)
- Le nombre total de livres et le nombre de livres empruntables

Exemple de solution (à adapter) :

```bash
echo "# Rapport $(jq -r '.bibliotheque.nom' bibliotheque.json)" > rapport.md
echo "" >> rapport.md
echo "| Titre | Auteur | Année | Genres | Empruntable | Nb emprunts |" >> rapport.md
echo "|-------|--------|------|--------|-------------|-------------|" >> rapport.md

jq -r '.bibliotheque.livres[] 
  | .emprunts // [] 
  | {
      titre: .titre,
      auteur,
      année,
      genres: (.genres | join(", ")),
      empruntable,
      nb: length
    }
  | "| \(titre) | \(auteur) | \(année) | \(genres) | \(empruntable) | \(nb) |"' bibliotheque.json >> rapport.md

echo -e "\nTotal livres : $(jq '[.bibliotheque.livres[]] | length' bibliotheque.json)" >> rapport.md
echo "Empruntables : $(jq '[.bibliotheque.livres[] | select(.empruntable)] | length' bibliotheque.json)" >> rapport.md
```
