---
layout: post
title: "[Bitcoin] Installer le logiciel Bitcoin sur macOS"
date: 2020-09-24
---

Résumé: Comment installer le logiciel Bitcoin sur macOS, et synchroniser la blockchain .

# Coinbase

Donc vous avez, comme moi, décidé de découvrir le monde merveilleux du Bitcoin. Pour commencer, par exemple, vous ouvrez un compte chez [Coinbase](https://www.coinbase.com) et convertissez quelques euros en BTC. 

# Bitcoin Core

Ensuite, pour on installe le logiciel fondateur du système, [Bitcoin Core](https://bitcoin.org/fr/telecharger), codé à la base par l'enigmatique [M. Satoshi](https://fr.wikipedia.org/wiki/Satoshi_Nakamoto) ...

Je l'installe `brew cask install bitcoin-core`. Le logiciel se lance, je choisi de stocker la blockchain sur un disque externe (et oui, il y en a pour plus de 300 Go..) et j'attend... il y en a pour plus d'une semaine. Et cerise sur le gateau l'UI de Bitcoin Core freeze dès qu'on navigue un peu dans l'application.

# bitcoind

C'est le genre de problème qui me fait installer directement la version en ligne de commande: `brew install bitcoin` . Je lance le démon `bitcoind`. 

Afin d'ameliorer la vitesse de synchronisation, j'effectue quelques réglage dans le fichier de configuration `bitcoin.conf` :
- plus de mémoire cache
- ajouts de nodes trouvés sur https://bitnodes.io

```
listen=0
dbcache=4096
banscore=10

# France
addnode=51.83.67.9:8333
addnode=51.210.34.62:8333
addnode=51.68.208.252:8333
addnode=5.196.73.52:8333

# Germany
addnode=116.203.187.251:8333
addnode=134.209.228.52:8333
addnode=207.154.210.209:8333
addnode=46.101.198.6:8333

# US
addnode=18.222.118.166:8333
addnode=159.89.42.205:8333
addnode=136.52.114.123:8333
addnode=72.178.123.6:8333
```

Et c'est reparti, la blockchain se télécharge à bonne vitesse, mais il reste encore quelques jours à attendre. Bien sûr, j'aurai pu attendre quelques jours de plus. D'un autre coté, j'ai envie de jouer avec mes Bitcoins ;-) .

# Electrum

Une autre application me tente: [Electrum](https://electrum.org). Son avantage, c'est qu'Electrum est rapide, car il utilise des serveurs qui indexent la blockchain. 

Je l'installe: `brew cask install electrum` et je crée un nouveau wallet. Maintenant il ne reste plus qu'a effectuer une transaction pour transferer mes fonds depuis Bitcoin Core vers Electrum...
