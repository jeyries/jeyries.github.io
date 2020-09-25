---
layout: post
title: "[Bitcoin] Comment récupérer des fonds à partir d'un fichier wallet.dat de Bitcoin Core sans avoir à télécharger toute la blockchain ?"
date: 2019-09-02
---

Résumé: Vous avez envoyé des fonds à une adresse de réception de Bitcoin Core. Malheureusement il vous reste encore plus d'une semaine pour synchroniser la blockchain. Et vous ne voulez pas attendre une synchronisation complète de la blockchain avant de transférer vos fonds ..

# Le problème

Vous avez envoyé des fonds à une adresse de réception de Bitcoin Core. Malheureusement il vous reste encore plus d'une semaine pour synchroniser la blockchain. Et vous ne voulez pas attendre une synchronisation complète de la blockchain avant de transférer vos fonds ..

# La procédure en bref

- Installer un nouveau porte-monnaie électronique 
- Utiliser la ligne de commande `bitcoin-cli` pour communiquer avec le démon `bitcoind` 
- Rassembler des informations
- Créer une transaction
- Signer la transaction
- Broadcaster la transaction

# Étapes :

## Installez un nouveau portefeuille

- installer un nouveau portefeuille, par exemple Electrum
- récupérer une adresse de réception de votre nouveau portefeuille

## Recupérez les infos de la précédente transaction

- récupérer l'adresse sur laquelle se trouvent les fonds dans l'ancien portefeuille

Dans mon cas: `bc1q0f0elkl5q7njxp67maja63jpmgds6s67u3zg0w`

- récupérer la transaction qui a amené les fonds - par exemple en faisant une recherche sur le site [blockchain.com](https://www.blockchain.com/)

Dans mon cas, voici l'adresse de départ: [https://www.blockchain.com/fr/btc/address/bc1q0f0elkl5q7njxp67maja63jpmgds6s67u3zg0w](https://www.blockchain.com/fr/btc/address/bc1q0f0elkl5q7njxp67maja63jpmgds6s67u3zg0w)

et la transaction:
[https://www.blockchain.com/btc/tx/03a9b2ff64f52b298927ed0d7ad6aa21fc4952a0954177f3eb5a6fa953df78d6](https://www.blockchain.com/btc/tx/03a9b2ff64f52b298927ed0d7ad6aa21fc4952a0954177f3eb5a6fa953df78d6)

- notez le montant de bitcoin que vous voulez transférer
- examinez la transaction
- récuperez "vout", c'est l'indice de la sortie qui concerne votre adresse
- récuperez le "scriptPubKey", c'est le "Pkscript" en hexa

## Estimez les frais de transaction

Choisissez le "fee", qui correspondent aux frais de transaction. Veuillez consulter ce site pour connaître un tarif correct : [https://bitcoinfees.earn.com/](https://bitcoinfees.earn.com/). Un exemple de ce que vous indique ce site:

```
Which fee should I use?

For the median transaction size of 224 bytes, this results in a fee of 0.00013888 BTC.

``` 
## Créez la nouvelle transaction . 

Ici, on utilise `bitcoin-cli` pour communiquer avec `bitcoind`.

```
createrawtransaction [{"txid":"hex","vout":n,"sequence":n},...] [{"address":amount},{"data":"hex"},...] ( locktime replaceable )
```

remplissez les paramètres suivants:

```
txid: votre transaction id
vout: vout
adresse: l'adresse de réception
amount: le montant final = le montant initial - les frais de transaction
``` 

par exemple dans mon cas:

```
createrawtransaction "[{\"txid\":\"03a9b2ff64f52b298927ed0d7ad6aa21fc4952a0954177f3eb5a6fa953df78d6\",\"vout\":31}]" "{\"bc1q86dhxl3xfuy4ag2zcz7wercud9lp63t5crhp8m\":0.00210026}"
```

vous obtenez la transaction en hexa:

```
0200000001d678df53a96f5aebf3774195a05249fc21aad67a0ded2789292bf564ffb2a9031f00000000ffffffff016a340300000000001600143e9b737e264f095ea142c0bcec8f1c697e1d457400000000
```

Si vous obtenez une erreur, vous avez probablement supprimé accidentellement un guillemet ou une barre oblique inversée. Vérifiez soigneusement votre chaîne et réessayez.

Ensuite, nous allons signer la transaction en vue de sa diffusion. Pour cela il vous faut la clé privée correspondant à l'adresse de départ.

## Recupérez la clé privée

Toujours avec `bitcoin-cli`:

```
dumpprivkey "address"
```

address: adresse de départ

```
dumpprivkey bc1q0f0elkl5q7njxp67maja63jpmgds6s67u3zg0w
```

On obtient:

```
L4752xBnTYrmhqa24ZWB8oKEENJD9FosEN1Z1jDtcF7gemvgj6fR
```

## Signez la transaction

Dans `bitcoin-cli`:

```
signrawtransactionwithkey "hexstring" ["privatekey",...] ( [{"txid":"hex","vout":n,"scriptPubKey":"hex","redeemScript":"hex","witnessScript":"hex","amount":amount},...] "sighashtype" )
```

amount: le montant total = montant final + les frais

par exemple dans mon cas:

```
signrawtransactionwithkey "0200000001d678df53a96f5aebf3774195a05249fc21aad67a0ded2789292bf564ffb2a9031f00000000ffffffff016a340300000000001600143e9b737e264f095ea142c0bcec8f1c697e1d457400000000" "[\"L4752xBnTYrmhqa24ZWB8oKEENJD9FosEN1Z1jDtcF7gemvgj6fR\"]" "[{\"txid\":\"03a9b2ff64f52b298927ed0d7ad6aa21fc4952a0954177f3eb5a6fa953df78d6\",\"vout\":31,\"amount\":0.00224362,\"scriptPubKey\":\"00147a5f9fdbf407a723075edf65dd4641da1b0d435e\"}]"
```

S'il n'y a pas d'erreurs, vous devriez avoir une transaction signée ! C'était la partie difficile. Vous avez simplement créé à la main une transaction bitcoin et utilisé votre clé privée pour la signer. Le résultat ressemble à cela: 

```
{
  "hex": "02000000000101d678df53a96f5aebf3774195a05249fc21aad67a0ded2789292bf564ffb2a9031f00000000ffffffff016a340300000000001600143e9b737e264f095ea142c0bcec8f1c697e1d45740247304402207d425a5273fcf65f8b43ffbd7554fa057785d7ef2449278a05a95aa37a8db0db022011ea799d6e13f07feb9fc4a02929b0fc9a101d974502be2c6d3abf33419d55f50121031a2e7e647c2cc33f03ecfc4092e93ec6220edce69e961fc7bc525522a4d0d8e300000000",
  "complete": true
}
```

## Diffusez la transaction

Cette valeur hexadécimale peut être envoyée directement au réseau Bitcoin pour être incluse dans la blockchain. 

Enfin, allez à : [https://www.blockchain.com/btc/pushtx](https://www.blockchain.com/btc/pushtx)
Collez la chaîne hexadécimale et cliquez sur "Envoyer la transaction"

Vous devriez alors voir une nouvelle transaction entrante dans votre nouveau portefeuille.




