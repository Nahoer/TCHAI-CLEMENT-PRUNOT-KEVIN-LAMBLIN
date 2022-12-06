
# TCHAI-CLEMENT-PRUNOT-KEVIN-LAMBLIN

L'objectif de ce projet est de concevoir un système de transactions électroniques avec une intégrité garantie, accessible par le protocole HTTP.

Il faut créer une API qui sera appelé à l'aide de requête HTTP.

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

## Méthode POST

### url/addTransaction

Méthode qui permet d'ajouter/créer une nouvelle transaction.
Cette méthode nécessite l'identifiant de l'envoyeur et du receveur, respectivement nommé *idEnvoyeur* et *idReceveur* et le montant nommé *montant*.
La transaction possède également une date // TODO voir si géré automatiquement
Disponible en version v1.

### url/addPerson

Méthode qui permet d'ajouter/créer une nouvelle personne.
Cette méthode nécessite le prénom de la personne nommé *first_name* et du nom nommé *last_name*.
Disponible en version v1.


# Auteurs
Clément PRUNOT
Kévin Lamblin
