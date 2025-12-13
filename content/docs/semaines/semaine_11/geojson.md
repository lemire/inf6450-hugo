---
title: "GeoJSON"
weight: 39
---

# GeoJSON

Le GeoJSON est un format ouvert conçu pour représenter des données géographiques simples à l'aide de la notation JSON (JavaScript Object Notation). Il permet de décrire des objets spatiaux tels que des points, des lignes, des polygones, ainsi que des collections de ces objets, en associant à chacun des propriétés descriptives. Ce format est largement utilisé dans les applications web cartographiques, les SIG (systèmes d'information géographique) et les échanges de données géospatiales, car il est lisible par les humains et facilement interprétable par les machines. GeoJSON repose sur la norme RFC 7946 et utilise des coordonnées en longitude et latitude selon le système de référence WGS 84.

La structure principale d'un fichier GeoJSON commence souvent par un objet de type "FeatureCollection", qui contient une liste de "features". Chaque "feature" représente un élément géographique individuel et se compose de trois parties essentielles : un type "Feature", un objet "properties" pour stocker des métadonnées (comme un nom ou une description), et un objet "geometry" qui définit la forme spatiale. Cette organisation modulaire rend le format flexible et extensible, tout en restant simple à parser dans la plupart des langages de programmation.

L'objet "geometry" spécifie le type de forme géométrique, par exemple "Point" pour un point unique, "LineString" pour une ligne, ou "Polygon" pour une surface fermée. Dans le cas d'un polygone, les coordonnées sont fournies sous forme d'un tableau de tableaux de points, où chaque point est une paire [longitude, latitude]. Le premier et le dernier point doivent être identiques pour fermer le polygone, et les coordonnées sont ordonnées dans le sens antihoraire pour respecter les conventions (règle de la main droite). Les polygones peuvent également contenir des "trous" en ajoutant des anneaux intérieurs.

Prenons l'exemple fourni pour illustrer concrètement ces concepts. L'objet FeatureCollection ne contient qu'une seule feature, dont les propriétés indiquent le nom "Exemple de polygone à Québec". La géométrie est un Polygon dont les coordonnées forment un petit rectangle autour de la ville de Québec : les points vont de la longitude -71.215 à -71.200 et de la latitude 46.810 à 46.820. Ce rectangle fermé représente une zone simplifiée, avec le premier point répété à la fin pour clore la forme. En visualisant ces coordonnées sur une carte, on obtiendrait un polygone rectangulaire couvrant une petite portion du territoire québécois.


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<style>
    #container { width: 100%;  height: 100%; display: flex; flex-direction: column; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
    #editor { flex: 1; min-height: 300px; display: flex; flex-direction: column; background: white; }
    #textarea { flex: 1; font-family: monospace; font-size: 14px; padding: 10px; border: none; resize: none; }
    #status { padding: 5px 10px; background: #f0f0f0; font-size: 12px; }
    #map { flex: 1; min-height: 400px; }
</style>


<div id="container">
        <div id="editor">
            <textarea id="textarea">{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": { "name": "Exemple de polygone à Québec" },
      "geometry": {
        "type": "Polygon",
        "coordinates": [[
          [-71.215, 46.810],
          [-71.200, 46.810],
          [-71.200, 46.820],
          [-71.215, 46.820],
          [-71.215, 46.810]
        ]]
      }
    }
  ]
}</textarea>
            <div id="status">GeoJSON valide</div>
        </div>
        <div id="map"></div>
    </div>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
        const map = L.map('map').setView([46.8139, -71.2080], 13);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; Contributeurs OpenStreetMap'
        }).addTo(map);
        let geojsonLayer = null;
        const textarea = document.getElementById('textarea');
        const status = document.getElementById('status');
        function updateMap() {
            const text = textarea.value.trim();
            if (!text) {
                if (geojsonLayer) { map.removeLayer(geojsonLayer); geojsonLayer = null; }
                status.textContent = 'Vide';
                return;
            }
            try {
                const data = JSON.parse(text);
                if (geojsonLayer) { map.removeLayer(geojsonLayer); }
                geojsonLayer = L.geoJSON(data, {
                    onEachFeature: (feature, layer) => {
                        if (feature.properties) {
                            const props = Object.entries(feature.properties)
                                .map(([k, v]) => `<strong>${k} :</strong> ${v}`)
                                .join('<br>');
                            layer.bindPopup(props || 'Aucune propriété');
                        }
                    }
                }).addTo(map);
                if (geojsonLayer.getBounds().isValid()) {
                    map.fitBounds(geojsonLayer.getBounds(), { padding: [50, 50] });
                }
                status.textContent = 'GeoJSON valide';
                status.style.background = '#e0ffe0';
            } catch (e) {
                if (geojsonLayer) { map.removeLayer(geojsonLayer); geojsonLayer = null; }
                status.textContent = 'JSON invalide : ' + e.message;
                status.style.background = '#ffe0e0';
            }
        }
        textarea.addEventListener('input', updateMap);
        updateMap(); // Chargement initial
    </script>

Essayez de remplacer le GeoJSON dans l'application par l'un des exemples suivants.


## Position de Paris

```json
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [2.3522, 48.8566]
  },
  "properties": {
    "name": "Paris"
  }
}
```

## Un trajet de Paris à Lyon puis à Marseille


```json
{
  "type": "Feature",
  "geometry": {
    "type": "LineString",
    "coordinates": [
      [2.3522, 48.8566],
      [4.8357, 45.7640],
      [5.3698, 43.2965]
    ]
  },
  "properties": {
    "name": "Trajet Paris-Lyon-Marseille"
  }
}
```

## Zone rectangulaire simple autour de la Tour Eiffel

```json
{
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [2.28, 48.88],
        [2.40, 48.88],
        [2.40, 48.83],
        [2.28, 48.83],
        [2.28, 48.88]
      ]
    ]
  },
  "properties": {
    "name": "Zone autour de la Tour Eiffel"
  }
}
```

## Montréal (centre-ville)

```json
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [-73.5673, 45.5017]
  },
  "properties": {
    "name": "Centre-ville de Montréal"
  }
}
````


## Montréal (Vieux Port)

```json
{
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [-73.56, 45.50],
        [-73.54, 45.50],
        [-73.54, 45.52],
        [-73.56, 45.52],
        [-73.56, 45.50]
      ]
    ]
  },
  "properties": {
    "name": "Vieux-Port de Montréal"
  }
}
```