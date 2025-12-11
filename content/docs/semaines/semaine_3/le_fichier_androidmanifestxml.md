---
title: "Le fichier AndroidManifest.xml"
weight: 60
---

# Le fichier AndroidManifest.xml

Le fichier AndroidManifest.xml est le cœur de toute application Android. Il s'agit d'un fichier XML obligatoire situé à la racine du projet qui décrit les composants essentiels de l'application au système Android. Il déclare notamment le package de l'application, les activités (Activity), services, récepteurs de diffusion (Broadcast Receiver) et fournisseurs de contenu (Content Provider). Sans ce fichier correctement configuré, l'application ne peut pas être installée ni exécutée sur un appareil ou un émulateur.
Ce manifeste sert également à déclarer les permissions nécessaires (par exemple l'accès à Internet, à la caméra, au stockage), les fonctionnalités matérielles requises (comme la présence d'un capteur GPS ou d'une caméra), la version minimale et cible de l'API Android, ainsi que des métadonnées comme l'icône de l'application, le label affiché dans le launcher, le thème, ou encore si l'application supporte le mode portrait/seulement paysage. Depuis Android 12 et plus, certaines déclarations comme les activités exportées doivent être explicites pour des raisons de sécurité.
Voici un exemple simple d'un AndroidManifest.xml pour une application basique contenant une seule activité :
```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.monapplication">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/Theme.MonApplication">

        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

    </application>

</manifest>
```
Dans cet exemple, l'activité MainActivity est déclarée comme point d'entrée principal grâce au filtre d'intention MAIN et LAUNCHER, et android:exported="true" est obligatoire lorsqu'il y a un intent-filter (règle de sécurité à partir d'Android 12).
