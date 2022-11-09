Create table Personne
(
  id integer,
  last_name varchar,
  first_name varchar
);

CREATE TABLE Transactions
(
  id integer,
  montant float,
  date date,
  id_envoyeur integer,
  id_receveur integer,
  hash varchar
);