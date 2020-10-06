---
layout: post
title: "Comment charger une image de manière asynchrone ? - UIKit + Swift + closures"
date: 2017-01-06
---

Résumé: Cette version permet de charger une image de manière asynchrone depuis une URL avec Swift et des closures.

# Description

L'implementation repose sur `URLSession` pour le téléchargement et sur `NSCache` pour cacher les images caching decoded images. De plus, un niveau de cache supplémentaire `NSURLCache` sert à cacher les réponses du réseau.


# Closure

On utilise différents type de closure pour retourner des resultats de manière asynchrone. La closure `CancelBlock` sert à annuler le chargement en cas de besoin.

```swift
    typealias DataBlock = (Data) -> Void
    typealias ImageBlock = (UIImage) -> Void
    typealias ErrorBlock = (Error) -> Void
    typealias CancelBlock = () -> Void
```

# SimpleImageManager.swift

L'interface publique est plutôt simple:

- `shared`: Cette propriété retourne une instance partagé de ce singleton
- `fetch`: Cette methode permet de charger une image à partir de l'url fournie

{% gist 2fecac2ecf066b6c620ea7b7f2965005 %}
