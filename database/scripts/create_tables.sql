Create table Personne
(
  id integer PRIMARY KEY,
  last_name varchar NOT NULL,
  first_name varchar NOT NULL
  public_key varchar NOT NULL
);

CREATE TABLE Transactions
(
  id integer PRIMARY KEY,
  montant float NOT NULL,
  date date NOT NULL,
  id_envoyeur integer NOT NULL,
  id_receveur integer NOT NULL,
  hash varchar NOT NULL
);
