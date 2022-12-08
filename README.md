
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

Méthode qui renvoie un message permettant d'assurer que le serveur est bien démarré.  
Cette méthode ne nécessite aucun paramètre.  
Disponible en version v1.

## Méthode GET

### url/persons

Méthode qui permet de récupérer la liste des personnes.  
Cette méthode ne nécessite aucun paramètre.  
Disponible en version v1.

### url/persons/<id de la personne>

Méthode qui permet de récupérer une pesonne.  
Cette méthode nécessie l'id de la personne.  
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

## Méthode POST

### url/transactions/add

Méthode qui permet d'ajouter/créer une nouvelle transaction.  
Cette méthode nécessite l'identifiant de l'envoyeur et du receveur, respectivement nommé *idSender* et *idReceiver* et le montant nommé *amount*.  
Exemple : url/transactions/add?idSender=1&idReceiver=2&amount=200
Disponible en version v1.

### url/persons/add

Méthode qui permet d'ajouter/créer une nouvelle personne.  
Cette méthode nécessite le prénom de la personne nommé *firstName* et du nom nommé *lastName*.  
Exemple : url/persons/add?lastName="Dupont&firstName=Jean
Disponible en version v1.

## Tests

Pour l'ensemble des tests, il est possible d'utiliser une base de données de test.  
Afin d'utiliser cette dernière, il suffit de changer le *path* de notre application.  
En saisissant *test.db* nous utilisons la base de test et en saisissant *transactions.db*, on utilise la base courante.  
Il exite également une base vide et une sauvegarde de la base de test.

### Version 1

Pour la version 1, nous avons réalisé un script de test qui nommé *testv1.py* qui permet de faire l'ensemble des appels à l'API qui permet de visualiser le fonctionnement des différentes fonctionnalités. 

# Auteurs
Clément PRUNOT  
Kévin Lamblin
