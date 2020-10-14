---
layout: post
title: "Comment charger une image de manière asynchrone ? Une vue d'ensemble de quelques méthodes disponibles"
date: 2020-10-13
---

Résumé: Comment charger une image de manière asynchrone ? C'est une question que tout développeur iOS s'est un jour posé. 

# Description

En effet Apple n'a jamais jugé necessaire de publier une API officielle sur le sujet. 

Ce n'est pas vraiment un problème tant de nombreux framework sont venus apporter leur solution au chargement d'image asynchrone. 

Par exemple, j'utilise personnellement à cet effet le framework [KingFisher](https://github.com/onevcat/Kingfisher).

Cependant, certains éditeurs prefèrent éviter des dépendances vers des frameworks externes. Ce peut être une bonne raison pour mettre au point sa propre version du chargement d'image asynchrone. 

Par ailleurs, cela fait une bonne question pour un entretien en vue d'embaucher un développeur iOS . J'ai moi-même vu cette question sortir plus d'une fois depuis 10 ans que je fais du développement iOS :-)

A ce sujet, je tiens à féliciter les compagnies comme [Zenly](https://zen.ly) qui jouent fair-play en indemnisant les candidats pour passer du temps à coder les problèmes demandés en entretien. Chapeau !

# Vue d'ensemble 

Voici donc quelques méthodes disponibles pour charger une image de manière asynchrone:

- [UIKit in Objective-C using ReactiveCocoa]({% post_url 2016-04-01-asynchronous-image-loading-part-1a-objective-c %})
- [... adding associated objects.]({% post_url 2016-04-02-asynchronous-image-loading-part-1b-objective-c %})
- [avec Swift dans une UITableViewCell custom]({% post_url 2019-05-10-chargement-image-asynchrone-part-2-swift-uitableviewcell %})
- [Depuis un fichier avec Swift et une OperationQueue, vers une UICollectionViewCell]({% post_url 2019-01-25-chargement-image-asynchrone-part-3-swift-fichier-operation-queue-uicollectionviewcell %})
- [UIKit + Swift + closures]({% post_url 2017-01-06-chargement-image-asynchrone-part-4a-uikit-swift-closures %})
- [... avec des associated objects]({% post_url 2017-01-07-chargement-image-asynchrone-part-4b-uikit-swift-closures %})
- [avec RxSwift]({% post_url 2020-10-12-chargement-image-asynchrone-part-5-rxswift %})




