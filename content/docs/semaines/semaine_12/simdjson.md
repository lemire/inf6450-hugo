---
title: "Méthode On-Demand avec simdjson (C++)"
weight: 105
---

# Traitement on-demand du JSON en C++ avec simdjson (activité optionnelle)

simdjson est la bibliothèque JSON la plus rapide au monde (2025).   Elle est conçue dès le départ pour le parsing **on-demand** (aussi appelé **zero-copy** ou **lazy parsing**) : elle ne construit les objets C++ que pour les parties du JSON que vous consultez réellement. Si vous maîtriser le C++, il s'agit d'une librairie à connaître.

Site officiel : https://github.com/simdjson/simdjson  


### Principes du parsing on-demand

Au lieu de matérialiser le document comme avec DOM, un index est construit rapidement qui permet de naviguer
avec aisance vers les parties importantes du document JSON. L'index est porté pour une instance du type `parser`
(`simdjson::ondemand::parser`). Une vue paresseuse sur le document est obtenue avec `ondemand::document`. Seuls
les éléments nécessaires sont analysés, lors de l'appel `.get_string()`, `.get_uint64()`, etc. 


### Exemples complets

#### 1. Parcourir un tableau géant sans jamais tout charger en mémoire

```cpp
#include <iostream>
#include <simdjson.h>

int main() {
    simdjson::ondemand::parser parser;
    
    // Fichier de 3 Go contenant [ {obj1}, {obj2}, ... ]
    auto json = simdjson::padded_string::load("huge_array.json");
    
    simdjson::ondemand::document doc = parser.iterate(json);
    simdjson::ondemand::array items = doc.get_array(); // ne coûte presque rien

    uint64_t count = 0;
    for (auto item : items) {              // itération on-demand
        uint64_t id = item["id"];          // conversion uniquement ici
        std::string_view name = item["name"].get_string();

        std::cout << id << ": " << name << '\n';

        if (++count % 1'000'000 == 0)
            std::cout << "Traités : " << count << " objets\n";
    }

    std::cout << "Total : " << count << " objets\n";
}
```


#### 2. Accès à des chemins imbriqués profonds sans tout matérialiser

```cpp
for (auto user : doc["results"]["users"]) {
    std::string_view email = user["profile"]["contact"]["email"];
    double score = user["metrics"]["engagement_score"];

    process_user(email, score);
}
```

Chaque accès (`user["profile"]`, etc.) ne déclenche le parsing que de cette branche.


## Références

- John Keiser, Daniel Lemire, [On-Demand JSON: A Better Way to Parse Documents?](http://arxiv.org/abs/2312.17149), Software: Practice and Experience 54 (6), 2024.
- Geoff Langdale, Daniel Lemire, [Parsing Gigabytes of JSON per Second](https://arxiv.org/abs/1902.08318), VLDB Journal 28 (6), 2019.


## Vidéos

{{< youtube id="wlvKAT7SZIQ" >}}

{{< youtube id="9tWvDFhBlNU" >}}

