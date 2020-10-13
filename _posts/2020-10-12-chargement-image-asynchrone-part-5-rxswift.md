---
layout: post
title: "Comment charger une image de manière asynchrone ? avec RxSwift"
date: 2020-10-12
---

Résumé: Cette version permet de charger une image de manière asynchrone depuis une URL avec RxSwift

# Description

On utilise pour cela les helpers définis dans mon post précédent: [A RxSwift helper for network calls, JSON decoding and image decoding]({% post_url 2020-09-23-rxswift-helper-for-network-image-and-json-decoding %})

L'operation de chargement des données depuis le réseau et celle de décodage en tâche de fond sont combinées à l'aide de l'opérateur `flatMap`.

L'implementation repose sur `URLSession` pour le téléchargement et sur `NSCache` pour cacher les images. De plus, un niveau de cache supplémentaire `URLCache` sert à cacher les réponses du réseau.

# AsyncImageLoader.swift

L'interface publique est plutôt simple:

- `fetchObservable`: Cette methode retourne un observable de type `Single<UIImage>` à partir de l'url fournie

{% gist c7bf9e0cc5531538a262fc0694b4158c %}

# CameraRollCell.swift

Un exemple d'utilisation ce chargement d'image dans une `UICollectionViewCell`.

Note: ici, l'utilisation du `DisposeBag` permet d'annuler un chargement déjà en cours lors d'un défilement par exemple.

{% gist 67231f4a8140a877475527f76f24ebb7 %}

