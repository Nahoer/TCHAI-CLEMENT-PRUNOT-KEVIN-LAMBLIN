
# TCHAI-CLEMENT-PRUNOT-KEVIN-LAMBLIN

L'objectif de ce projet est de concevoir un système de transactions électroniques avec une intégrité garantie, accessible par le protocole HTTP.

Il faut créer une API qui sera appelé à l'aide de requête HTTP.

## Choix techniques

Pour ce projet, nous n'avons pas effectué de choix techniques particuliers.  
Nous avons utilisé le technologie recommandé afin de rester au plus proche des choix fais par l'enseignant.  
Pour le SGBD (Système de Gestion de Base de Données), nous avons choisis SQL Lite 3 car nous le connaissons et qu'il permet de créer facilement notre base de données.  
De plus, il est simple à utiliser avec Python.

# Requêtes de Tchaî

Dans cette partie, nous allons détailler les différentes fonctionnalités de notre application et qu'elles sont les requêtes pour les utiliser.  
Pour simplifier la compréhension, l'URL du serveur sera simplement appelé "url".

## Méthodes utilitaires

### url/Connexion

Méthode qui renvoi un message permettant d'assurer que le serveur est bien démarré.  
Cette méthode ne nécessite aucun paramètre.  
Disponible en version v1.

## Méthode GET

### url/Persons

Méthode qui permet de récupérer la liste des personnes.  
Cette méthode ne nécessite aucun paramètre.  
Disponible en version v1.

### url/Transactions

Méthode qui permet de récupérer la liste des transactions.  
Cette méthode ne nécessite aucun paramètre.  
Disponible en version v1.

### url/TransactionsOrderedByDate

Méthode qui permet de récupérer la liste des transactions par ordre chronologique.  
Cette méthode ne nécessite aucun paramètre.  
Disponible en version v1.

### url/TransactionsFor

Méthode qui permet de récupérer la liste des transactions par ordre chronologique pour une personne donnée.  
Cette méthode nécessite l'identifiant de la personne nommé *id*.  
Disponible en version v1.

### url/getSolde

Méthode qui permet de récupérer le solde de la personne donnée en la calculant depuis la liste des transactions.  
Cette méthode nécessite l'identifiant de la personne nommé *idPerson*.  
Disponible en version v1.

## Méthode POST

### url/addTransaction

Méthode qui permet d'ajouter/créer une nouvelle transaction.  
Cette méthode nécessite l'identifiant de l'envoyeur et du receveur, respectivement nommé *idSender* et *idReceiver* et le montant nommé *amount*.  
Disponible en version v1.

### url/addPerson

Méthode qui permet d'ajouter/créer une nouvelle personne.  
Cette méthode nécessite le prénom de la personne nommé *firstName* et du nom nommé *lastName*.  
Disponible en version v1.


# Auteurs
Clément PRUNOT  
Kévin Lamblin
