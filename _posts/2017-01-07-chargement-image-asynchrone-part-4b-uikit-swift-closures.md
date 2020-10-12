---
layout: post
title: "Comment charger une image de manière asynchrone ? - avec des associated objects"
date: 2017-01-07
---

Résumé: On rajoute une extension sur `UIImageView` afin de charger de manière asynchrone une image. Pour cela, on va utiliser les associated objects.


# Description

Cette version permet de charger une image de manière asynchrone depuis une URL avec Swift et des closures.

Ici, on rajoute une extension sur `UIImageView` pour retenir le `CancelBlock` avec un associated object. Cela permet par exemple de pouvoir annuler le chargement de l'image en cas de défilement dans une table view.

# Associated Objects

Les "Associated Objects" - objets associés en français - sont une fonctionnalité du runtime Objective-C . 
Le terme fait référence aux trois fonctions C suivantes déclarées dans `<objc/runtime.h>`, qui permettent aux objets d'associer des valeurs arbitraires pour des clés au moment de l'exécution :

```
- objc_setAssociatedObject
- objc_getAssociatedObject
- objc_removeAssociatedObjects
```

Pourquoi est-ce utile ? Cela permet aux développeurs d'ajouter des propriétés personnalisées aux classes existantes depuis une catégorie, ce qui est par ailleurs un défaut notable de l'Objective-C.

Plus d'information sur le sujet ici: [NSHipster](https://nshipster.com/associated-objects/) .

# UIImageView+SimpleImageManager.swift

L'interface publique est plutôt simple, il y a une seule méthode dans cette extension de `UIImageView`:

- `setImageWithURL`: Cette méthode permet de charger de manière asynchrone une image dans une `UIImageView`

{% gist a09ca0abd424db0b01beeb88456c99ce %}
