---
layout: post
title: "Comment charger une image de manière asynchrone ? Depuis un fichier avec Swift et une OperationQueue, vers une UICollectionViewCell"
date: 2019-01-25
---

Résumé: Cette version permet de charger une image de manière asynchrone depuis un fichier avec Swift et une OperationQueue, vers une UICollectionViewCell.

# Description

On utilise `OperationQueue` pour charger depuis un fichier et decoder les données de l'image, tout cela en arrière plan. Si besoin on peut limiter le nombre des operations concurrentes avec `maxConcurrentOperationCount`.

De plus, un `NSCache` est utilisé pour cacher les images décodées.

Enfin on retient l'objet `Operation` dans la `UICollectionViewCell`, pour pouvoir annuler le chargement en cas de défilement.

# OperationQueue

Plus d'info sur `OperationQueue` ici: [https://developer.apple.com/documentation/foundation/operationqueue](https://developer.apple.com/documentation/foundation/operationqueue)

# ImageLoader.swift

{% gist 338264195b6d48a14b445f3d64764e49 %}

# GalleryCell.swift 

{% gist 4aca9a8cf544647d342f013293aaab6c %}
