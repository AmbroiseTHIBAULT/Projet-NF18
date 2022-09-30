-- Creation des tables --
DROP TABLE IF EXISTS veterinaire CASCADE;
DROP TABLE IF EXISTS employe CASCADE;
DROP TABLE IF EXISTS client CASCADE;
DROP TABLE IF EXISTS espece CASCADE;
DROP TABLE IF EXISTS race CASCADE;
DROP TABLE IF EXISTS animal CASCADE;
DROP TABLE IF EXISTS prestation CASCADE;
DROP TABLE IF EXISTS rendez_vous CASCADE;
DROP TABLE IF EXISTS produit CASCADE;
DROP TABLE IF EXISTS facture CASCADE;

DROP VIEW IF EXISTS Espece_Race;
DROP VIEW IF EXISTS Veterinaire_Employe;
DROP VIEW IF EXISTS Veterinaire_Client;
DROP VIEW IF EXISTS Employe_Client;


CREATE TABLE veterinaire (
	id INTEGER PRIMARY KEY,
	nom VARCHAR(20) NOT NULL,
	prenom VARCHAR(20) NOT NULL
);


CREATE TABLE employe (
	id INTEGER PRIMARY KEY,
	nom VARCHAR(20) NOT NULL,
	prenom VARCHAR(20) NOT NULL
);


CREATE TABLE client (
	tel VARCHAR(20) PRIMARY KEY,
	nom VARCHAR(20) NOT NULL,
	prenom VARCHAR(20) NOT NULL
);


CREATE TABLE espece (
	nom VARCHAR(20) PRIMARY KEY
);


CREATE TABLE race (
	nom VARCHAR(20) PRIMARY KEY,
	nom_espece VARCHAR(20) NOT NULL 
		REFERENCES espece(nom) ON DELETE CASCADE
);


CREATE TABLE animal (
	id INTEGER PRIMARY KEY,
	nom_race VARCHAR(20) NOT NULL 
		REFERENCES race(nom) ON DELETE CASCADE,
	nom_espece VARCHAR(20) NOT NULL 
		REFERENCES espece(nom) ON DELETE CASCADE,
	proprio VARCHAR(20) NOT NULL 
		REFERENCES client(tel) ON DELETE CASCADE,
	poids INTEGER,
	nom VARCHAR(20) NOT NULL,
	genre VARCHAR(20),
	naissance DATE NOT NULL,
	taille INTEGER,
CHECK (genre ='male' OR genre ='female')
);


CREATE TABLE prestation (
	id INTEGER UNIQUE,
	id_facture INTEGER UNIQUE,
	type VARCHAR(20) NOT NULL,
	PRIMARY KEY (id, id_facture),
	CHECK (type = 'consultation' OR type = 'intervention')
);


CREATE TABLE rendez_vous (
	date_rdv TIMESTAMP PRIMARY KEY,
	id_veto INTEGER NOT NULL
		REFERENCES veterinaire(id) ON DELETE CASCADE,
	id_animal INTEGER NOT NULL
		REFERENCES animal(id) ON DELETE CASCADE,
	id_prestation INTEGER 
		REFERENCES prestation(id) 
	ON DELETE CASCADE,
	id_facture INTEGER 
		REFERENCES prestation(id_facture) 
	ON DELETE CASCADE
);


CREATE TABLE produit (
	num INTEGER PRIMARY KEY,
	nom VARCHAR(20),
	date_fabric DATE NOT NULL,
	type VARCHAR(20) NOT NULL,
	CHECK (type ='medicament' OR type ='produit_entretien')
);


CREATE TABLE facture (
	id INTEGER PRIMARY KEY,
	vendeur INT 
		REFERENCES employe(id) 
	ON DELETE CASCADE NOT NULL,
	num_produit INTEGER 
		REFERENCES produit(num) 
	ON DELETE CASCADE,
	montant INTEGER,
	date_paiement DATE,
	reglement VARCHAR(20),
	quantite INTEGER,
	CHECK(quantite>0)
);





-- Creation des vues associees aux contraintes --

CREATE VIEW Espece_Race AS
SELECT nom_espece FROM Race
EXCEPT
SELECT nom FROM Espece;

CREATE VIEW Veterinaire_Employe AS
SELECT nom,prenom FROM Veterinaire
INTERSECT
SELECT nom,prenom FROM Employe;

CREATE VIEW Veterinaire_Client AS
SELECT nom,prenom FROM Veterinaire
INTERSECT
SELECT nom,prenom FROM Client;

CREATE VIEW Employe_Client AS
SELECT nom,prenom FROM Employe
INTERSECT
SELECT nom,prenom FROM Client;
