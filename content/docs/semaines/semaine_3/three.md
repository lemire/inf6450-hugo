
---
title: "X3D"
weight: 55
---

# X3D

X3D, ou Extensible 3D, est un standard international ISO/IEC ouvert pour la représentation et la communication de graphiques 3D interactifs sur le web.
Ce format XML facilite la création de contenus 3D portables, visualisables dans des navigateurs, sans plugins supplémentaires. Maintenu par le Web3D Consortium, X3D évolue continuellement pour répondre aux besoins en visualisation scientifique, en éducation, et en réalité virtuelle/augmentée sur le web.

Prenons un exemple classique d'une scène X3D simple affichant un cône rouge tournant sur lui-même.

```xml
<X3D profile='Immersive' version='4.0' xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation='http://www.web3d.org/specifications/x3d-4.0.xsd'>
<head>
    <meta name='title' content='Simple Cone'/>
</head>
<Scene>
    <WorldInfo title='Simple rotating cone'/>
    <Background skyColor='0 0.5 1'/>
    <Viewpoint position='0 0 5'/>
    <DirectionalLight/>
    <TimeSensor DEF='Clock' cycleInterval='4' loop='true'/>
    <Transform DEF='Spinner'>
    <Shape>
    <Cone bottomRadius='1' height='2'/>
    <Appearance>
    <Material diffuseColor='1 0 0'/>
    </Appearance>
    </Shape>
    </Transform>
    <OrientationInterpolator DEF='SpinPath' key='0 0.5 1' keyValue='0 1 0 0, 0 1 0 3.14159, 0 1 0 6.28318'/>
    <ROUTE fromNode='Clock' fromField='fraction_changed' toNode='SpinPath' toField='set_fraction'/>
    <ROUTE fromNode='SpinPath' fromField='value_changed' toNode='Spinner' toField='rotation'/>
</Scene>
</X3D>
```

Ce code définit une scène basique dans le profil Immersive de X3D version 4.0. La balise &lt;Background&gt; crée un ciel bleu clair, &lt;Viewpoint&gt; positionne la caméra à 5 unités sur l'axe Z pour voir l'origine, et &lt;DirectionalLight&gt; ajoute un éclairage directionnel par défaut. Le cône est créé via &lt;Cone&gt; avec un rayon de base de 1 et une hauteur de 2, coloré en rouge (&lt;Material diffuseColor='1 0 0'&gt;). Un &lt;TimeSensor&gt; nommé Clock génère un cycle de 4 secondes en boucle, envoyant une fraction (de 0 à 1) via une ROUTE à l'&lt;OrientationInterpolator&gt; SpinPath, qui interpole une rotation autour de l'axe Y de 0 à deux tours complets (en radians). Cette valeur est routée vers la rotation du &lt;Transform&gt; Spinner contenant le cône, produisant une animation de rotation continue. L'ensemble forme un exemple pédagogique démontrant géométrie primitive, apparence, éclairage et animation par interpolation temporelle.


<script defer src="https://cdn.jsdelivr.net/npm/x_ite@latest/dist/x_ite.min.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/x_ite@latest/dist/x_ite.css">

<style>
    textarea { width: 100%; height: 300px; font-family: monospace; font-size: 14px; }
    x3d-canvas { width: 100%; height: 500px; display: block; border: 1px solid #ccc; margin-top: 20px; }
    button { padding: 10px; font-size: 16px; margin-top: 10px; }
</style>

<textarea id="x3dCode">
&lt;X3D profile='Immersive' version='4.0' xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation='http://www.web3d.org/specifications/x3d-4.0.xsd'&gt;
  &lt;head&gt;
    &lt;meta name='title' content='Simple Cone'/&gt;
  &lt;/head&gt;
  &lt;Scene&gt;
    &lt;WorldInfo title='Simple rotating cone'/&gt;
    &lt;Background skyColor='0 0.5 1'/&gt;
    &lt;Viewpoint position='0 0 5'/&gt;
    &lt;DirectionalLight/&gt;
    &lt;TimeSensor DEF='Clock' cycleInterval='4' loop='true'/&gt;
    &lt;Transform DEF='Spinner'&gt;
      &lt;Shape&gt;
        &lt;Cone bottomRadius='1' height='2'/&gt;
        &lt;Appearance&gt;
          &lt;Material diffuseColor='1 0 0'/&gt;
        &lt;/Appearance&gt;
      &lt;/Shape&gt;
    &lt;/Transform&gt;
    &lt;OrientationInterpolator DEF='SpinPath' key='0 0.5 1' keyValue='0 1 0 0, 0 1 0 3.14159, 0 1 0 6.28318'/&gt;
    &lt;ROUTE fromNode='Clock' fromField='fraction_changed' toNode='SpinPath' toField='set_fraction'/&gt;
    &lt;ROUTE fromNode='SpinPath' fromField='value_changed' toNode='Spinner' toField='rotation'/&gt;
  &lt;/Scene&gt;
&lt;/X3D&gt;
</textarea>
<button id="updateButton">Mise à jour du rendu 3D</button>
<x3d-canvas id="canvas"></x3d-canvas>

<script>
    const textarea = document.getElementById('x3dCode');
    const canvas = document.getElementById('canvas');
    const button = document.getElementById('updateButton');
    // The core function to parse the X3D text and load it into the canvas
    async function updateScene() {
        const code = textarea.value.trim();
        if (code) {
            // 1. Get the X3D scene object by parsing the string
            const scene = await canvas.browser.createX3DFromString(code);
            // 2. Replace the world
            await canvas.browser.replaceWorld(scene);
        }
    }
    // Since x_ite loads asynchronously, we must wait for the document to be ready 
    // AND for the X3D global object to be available. 
    // Using a simple timeout or a DOMContentLoaded listener often works if the script is deferred.
    // The safest way is to check for the X3D object.
    document.addEventListener('DOMContentLoaded', () => {
        // x_ite registers a custom element, so the 'canvas' variable should be an X3D component
        // which has a 'browser' property after it is initialized.
        // A short timeout can sometimes help ensure the component is fully ready.
        setTimeout(updateScene, 50); 
    });
    button.addEventListener('click', updateScene);
</script>

Essayez les exemples suivants.


## Sphère rouge avec un fond bleu ciel.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE X3D PUBLIC "ISO//Web3D//DTD X3D 4.0//EN" "https://www.web3d.org/specifications/x3d-4.0.dtd">
<X3D profile="Immersive" version="4.0">
  <head>
    <meta name="title" content="Sphère rouge"/>
  </head>
  <Scene>
    <Background skyColor="0.5 0.8 1"/>
    <Viewpoint position="0 0 5" description="Vue initiale"/>
    <Shape>
      <Sphere radius="1"/>
      <Appearance>
        <Material diffuseColor="1 0 0"/>
      </Appearance>
    </Shape>
  </Scene>
</X3D>
```

## Un cube bleu et une sphère rouge côte à côte

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE X3D PUBLIC "ISO//Web3D//DTD X3D 4.0//EN" "https://www.web3d.org/specifications/x3d-4.0.dtd">
<X3D profile="Immersive" version="4.0">
  <head>
    <meta name="title" content="Cube et sphère"/>
  </head>
  <Scene>
    <Background skyColor="1 1 1"/>
    <Viewpoint position="0 0 10"/>
    <Transform translation="-2 0 0">
      <Shape>
        <Box size="2 2 2"/>
        <Appearance>
          <Material diffuseColor="0 0 1"/>
        </Appearance>
      </Shape>
    </Transform>
    <Transform translation="2 0 0">
      <Shape>
        <Sphere radius="1"/>
        <Appearance>
          <Material diffuseColor="1 0 0"/>
        </Appearance>
      </Shape>
    </Transform>
  </Scene>
</X3D>
```

## un cylindre vert et texte en 3D

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE X3D PUBLIC "ISO//Web3D//DTD X3D 4.0//EN" "https://www.web3d.org/specifications/x3d-4.0.dtd">
<X3D profile="Immersive" version="4.0">
  <head>
    <meta name="title" content="Formes basiques avec texte"/>
  </head>
  <Scene>
    <Background skyColor="0 0 0"/>
    <Viewpoint position="0 5 15"/>
    <Transform translation="-3 0 0">
      <Shape>
        <Box size="3 3 3"/>
        <Appearance>
          <Material diffuseColor="0 0 1"/>
        </Appearance>
      </Shape>
    </Transform>
    <Transform translation="0 0 0">
      <Shape>
        <Cylinder radius="1.5" height="4"/>
        <Appearance>
          <Material diffuseColor="0 1 0"/>
        </Appearance>
      </Shape>
    </Transform>
    <Transform translation="3 0 0">
      <Shape>
        <Sphere radius="2"/>
        <Appearance>
          <Material diffuseColor="1 0 0"/>
        </Appearance>
      </Shape>
    </Transform>
    <Transform translation="0 -4 0" rotation="1 0 0 -1.57">
      <Shape>
        <Text string='"Exemple X3D"'>
          <FontStyle size="2" justify='"MIDDLE"'/>
        </Text>
        <Appearance>
          <Material emissiveColor="1 1 0"/>
        </Appearance>
      </Shape>
    </Transform>
  </Scene>
</X3D>
```
