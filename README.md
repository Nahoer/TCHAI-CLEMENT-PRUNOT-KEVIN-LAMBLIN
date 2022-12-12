# TCHAI-CLEMENT-PRUNOT-KEVIN-LAMBLIN

L'objectif de ce projet est de concevoir un système de transactions électroniques avec une intégrité garantie,
accessible par le protocole HTTP.

Il faut créer une API qui sera appelé à l'aide de requête HTTP.

## Choix techniques

Pour ce projet, nous n'avons pas effectué de choix techniques particuliers.  
Nous avons utilisé les technologies recommandées afin de rester au plus proche des choix fais par l'enseignant.  
Pour le SGBD (Système de Gestion de Base de Données), nous avons choisi SQLite3 car nous le connaissons et qu'il permet
de créer facilement notre base de données.  
De plus, il est simple à utiliser avec Python.

Pour le choix de la fonction de hachage, nous avons choisi sha224. Cette fonction de hachage fait partie de la famille
SHA2, cette famille de fonction de hachage est très fiable, car elle a été développée par la NSA.  
Ces fonctions sont à ce jour toujours considérées comme très fiable.

# Requêtes de Tchaî

Dans cette partie, nous allons détailler les différentes fonctionnalités de notre application et qu'elles sont les
requêtes pour les utiliser.  
Pour simplifier la compréhension, l'URL du serveur sera simplement appelé "url".

## Méthodes utilitaires

### url/connexion

Méthode qui renvoie un message permettant d'assurer que le serveur est bien démarré.  
Cette méthode ne nécessite aucun paramètre.  
Disponible en version v1.

## Méthode GET

### url/persons

Méthode qui permet de récupérer la liste des personnes.  
Cette méthode ne nécessite aucun paramètre.  
Disponible en version v1.

### url/persons/<id de la personne>

Méthode qui permet de récupérer une personne.  
Cette méthode nécessite l'id de la personne.  
Disponible en version v1.

### url/transactions

Méthode qui permet de récupérer la liste des transactions.  
Cette méthode ne nécessite aucun paramètre.  
Disponible en version v1.

### url/transactions/date

Méthode qui permet de récupérer la liste des transactions par ordre chronologique.  
Cette méthode ne nécessite aucun paramètre.  
Disponible en version v1.

### url/transactions/person/<id de la personne>

Méthode qui permet de récupérer la liste des transactions par ordre chronologique pour une personne donnée.  
Cette méthode nécessite l'identifiant de la personne nommé.  
Disponible en version v1.

### url/transactions/<id de la transaction>

Méthode qui permet de récupérer la transaction correspondant à l'id fournit.  
Disponible en version v1.

### url/getSolde

Méthode qui permet de récupérer le solde de toutes les personnes en calculant depuis la liste des transactions.  
Disponible en version v1.

### url/getSolde/<id de la personne>

Méthode qui permet de récupérer le solde de la personne donnée en la calculant depuis la liste des transactions.  
Cette méthode nécessite l'identifiant de la personne nommé.  
Disponible en version v1.

### url/verifyIntegrity

Méthode qui permet de vérifier l'intégrité des données dans la base. Cette méthode nous renvoi la liste des transactions
dont le hash ne correspond pas aux données  
Cette méthode ne nécessite aucun paramètre.  
Disponible en version v2.  
Améliorer en version v3 afin de calculer le hash en mode *blockchain*.

## Méthode POST

### url/transactions/add

Méthode qui permet d'ajouter/créer une nouvelle transaction.  
Cette méthode nécessite l'identifiant de l'envoyeur et du receveur, respectivement nommé *idSender* et *idReceiver* et
le montant nommé *amount*.  
Exemple : url/transactions/add?idSender=1&idReceiver=2&amount=200
Disponible en version v1.

### url/persons/add

Méthode qui permet d'ajouter/créer une nouvelle personne.  
Cette méthode nécessite le prénom de la personne nommé *firstName* et du nom nommé *lastName*.  
Exemple : url/persons/add?lastName=Dupont&firstName=Jean
Disponible en version v1.

## Tests

Pour l'ensemble des tests, il est possible d'utiliser une base de données de test. Cette dernière est choisie par
défaut.  
Afin de lancer les scripts de test, il est nécessaire d'avoir un serveur flask sur l'adresse *http://127.0.0.1:5000*.  
Il existe également une base vide et une sauvegarde de la base de test.

### Version 1

Pour la version 1, nous avons réalisé un script de test qui nommé *testv1.py* qui permet de faire l'ensemble des appels
à l'API qui permet de visualiser le fonctionnement des différentes fonctionnalités.

### Version 2

Pour la version 2, nous avons réalisé un script de test qui nommé *testv2.py* qui appel le script de la première
version.  
Ensuite nous appelons l'attaque de la version 1 et verifions l'intégrité. Nous remarquons que cette fois,
l'erreur est détectée.

### Version 2

Pour la version 2, nous avons réalisé un script de test qui nommé *testv3.py* qui appel le script de la première
version.  
Ensuite nous appelons l'attaque de la version 2 et verifions l'intégrité. Nous remarquons que cette fois,
l'erreur est détectée.

## Attaques

Pour l'ensemble des versions, nous avons réalisé des attaques. La démarche de chaque attaque sera détaillée ci-dessous.

### Version 1

Pour la première version, nous devions réaliser une attaque qui modifie les données dans la base de données. Vous
trouverez le script nommé *attackv1.py*.  
Ce dernier va afficher la liste des transactions, modifier le montant de l'une d'entre elle et afficher à nouveau les
transactions.  
Nous remarquerons alors que les données ont bien été modifiées.

### Version 2

Pour la seconde version, nous devions réaliser une attaque qui supprime une transaction dans la base de données. Vous
trouverez le script nommé *attackv2.py*.  
Ce dernier va afficher la liste des transactions et des integrités, supprimer l'une d'entre elle et afficher à nouveau
les
transactions et des integrités.  
Nous remarquerons alors que les données ont bien été modifiées.

### Version 3

Pour la troisième version, nous devions réaliser une attaque ou le pirate crée une transaction vers son compte. Vous
trouverez le script nommé *attackv3.py*.  
Ce dernier va afficher la liste des transactions, ajoute une transaction et afficher à nouveau les
transactions et des integrités.  
Nous remarquerons alors que la transaction a été ajoutée.

# Auteurs

Clément PRUNOT  
Kévin Lamblin
