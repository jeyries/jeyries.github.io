---
layout: post
title: "Comment charger une image de manière asynchrone ? avec Swift dans une UITableViewCell custom"
date: 2019-05-10
---


Résumé: C'est la version la plus minimaliste pour charger une image de manière asynchrone avec Swift dans une UITableViewCell custom.


# Description

On utilise `URLSession` pour charger les données de l'image. Le décodage se fait directement dans la queue en background de `URLSession`. On retourne le resultat dans la queue principale `DispatchQueue.main` et on l'affecte à `UIImageView`. Enfin 
on retient le `URLSessionDataTask` dans la `UITableViewCell`, pour pouvoir annuler le chargement en cas de défilement.

# BookCell.swift

{% gist c4c446e6c9798f188af9226b0a96ef1f %}
