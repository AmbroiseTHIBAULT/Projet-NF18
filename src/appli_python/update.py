#!/usr/bin/python3

import psycopg2


def quote(s):
    if s:
        return '\'%s\'' % s
    else:
        return 'NULL'


def sousMenuUpdate(conn):
    saisie = '0'
    while (saisie != 'q'):
        print("\nSelectionner l'action que vous voulez faire :")
        print("1 : Ajouter un veterinaire")
        print("2 : Ajouter un employe")
        print("3 : Ajouter un client")
        print("4 : Ajouter une espece")
        print("5 : Ajouter une race")
        print("6 : Ajouter un animal")
        print("7 : Ajouter une prestation")
        print("8 : Ajouter un rendez_vous")
        print("9 : Ajouter un produit")
        print("10 : Ajouter une facture")
        print("'q' pour quitter")


        saisie = input("\nVotre choix : ")

        if (saisie == '1'):
            nomVeto = quote(input("Saisissez le nom du veterinaire à ajouter : "))
            prenomVeto = quote(input("Saisissez le prenom du veterinaire à ajouter : "))
            ajouteVeto(conn, nomVeto, prenomVeto)

        if (saisie == '2'):
            nomEmploye = quote(input("Saisissez le nom de l'employé a ajouter : "))
            prenomEmploye = quote(input("Saisissez le prenom de l'employé a ajouter : "))
            ajouteEmploye(conn, nomEmploye, prenomEmploye)

        if(saisie == '3'):
            telClient = quote(input("Saisissez le telephone du client à ajouter : "))
            nomClient = quote(input("Saisissez le nom du client a ajouter : "))
            prenomClient = quote(input("Saisissez le prenom du client a ajouter : "))
            ajouteCLient(conn, telClient, nomClient, prenomClient)

        if (saisie == '4'):
            nomEspece = quote(input("Saisissez le nom de l'espece à ajouter : "))
            ajouteEspece(conn, nomEspece)

        if (saisie == '5'):
            nomRace = quote(input("Saisissez le nom de la race à ajouter : "))
            nomE = quote(input("Saisissez le nom de l'espece à laquelle la race appartient : "))
            ajouteRace(conn, nomRace, nomE)

        if (saisie == '6'):
            nomRaceAnimal = quote(input("Saisissez le nom de la race à laquelle l'animal appartient : "))
            nomEspeceAnimal = quote(input("Saisissez le nom de l'espece à laquelle l'animal appartient : "))
            numProprio = quote(input("Saisissez le numero de telephone du proprietaire  de l'animal : "))
            poids = int(input("Saisissez le poids de l'animal"))
            nomAnimal = quote(input("Saisissez le nom de l'animal"))
            genre = quote(input("Saisissez le genre de l'animal"))
            dateNaissance = quote(input("Saisissez la date de naissance de l'animal en format YYYY-MM-JJ : "))
            taille = int(input("Saisissez la taille de l'animal en cm : "))
            ajouteAnimal(conn, nomRaceAnimal, nomEspeceAnimal, numProprio, poids, nomAnimal, genre, dateNaissance, taille)

        if (saisie == '7'):
            idFacture = int(input("Saisissez l'Id de la facture lié à la prestation : "))
            type = quote(input("Saisissez le type de facture, intervention ou consultation : "))
            ajoutePrestation(conn, idFacture, type)

        if (saisie == '8'):
            horaire = quote(input("Saisissez la date et horaire du rendez vous sous la forme YYYY-MM-DD HH24:MI:SS : "))
            idVeto = int(input("Saisissez l'id du veto qui s'occupe de rendez vous : "))
            idAnimal = int(input("Saisissez l'id de l'animal présent au rendez vous : "))
            idPresta = int(input("Saisissez l'id de la prestation : "))
            idFacture = int(input("Saisissez l'id de la prestation : "))
            ajouteRdv(conn, horaire, idVeto, idAnimal, idPresta, idFacture)

        if (saisie == '9'):
            nom = quote(input("Saissez le nom du produit : "))
            date = quote(input("Saisissez la date de fabrication au format YYYY-MM-DD : "))
            type = quote(input("Saisissez le type de produit, medicament ou produit_entretien : "))
            ajouteProduit(conn, nom, date, type)

        if (saisie == '10'):
            idVendeur = int(input("Saisissez l'id du vendeur à l'origine de la facture : "))
            numProduit = int(input("Saisissez le numéro du produit : "))
            montant = int(input("Saisissez le montant de la facture : "))
            date = quote(input("Saisissez la date du paiment sous la forme YYYY-MM-DD : "))
            reglement = quote(input("Saisissez le mode paiement : carte ou cheque : "))
            quantite = int(input("Saisissez la quantité de produit vendu : "))
            ajouteFacture(conn, idVendeur, numProduit, montant, date, reglement, quantite)



def executeUpdate(conn, requete):
    try:
        cur = conn.cursor()
        cur.execute(requete)
        conn.commit()

    except psycopg2.IntegrityError as e:
        conn.rollback()
        print("Message systeme :", e)


def getMaxIdTable(conn, nomTable):
    requeteMaxId =  "SELECT MAX(id) FROM %s;" % (nomTable)
    cur = conn.cursor()
    cur.execute(requeteMaxId)
    max = cur.fetchone()
    return max[0]


def ajouteVeto(conn, nom, prenom):
    id = getMaxIdTable(conn, "veterinaire") + 1
    requete = "INSERT INTO veterinaire VALUES (%i, %s, %s);" % (id, nom, prenom)
    executeUpdate(conn, requete)

def ajouteEmploye(conn, nom, prenom):
    id = getMaxIdTable(conn, "employe") + 1
    requete = "INSERT INTO employe VALUES (%i, %s, %s);" % (id, nom, prenom)
    executeUpdate(conn, requete)

def ajouteCLient(conn, tel, nom, prenom):
    requete = "INSERT INTO client VALUES (%s, %s, %s);" % (tel, nom, prenom)
    executeUpdate(conn, requete)

def ajouteEspece(conn, nom):
    requete = "INSERT INTO espece VALUES (%s);" % (nom)
    executeUpdate(conn, requete)

def ajouteRace(conn, nomRace, nomEspece):
    requete = "INSERT INTO race VALUES (%s, %s);" % (nomRace, nomEspece)
    executeUpdate(conn, requete)

def ajouteAnimal(conn, nomRace, nomEspece, proprio, poids, nom, genre, dateN, taille):
    id = getMaxIdTable(conn, "animal") + 1
    requete = "INSERT INTO animal VALUES (%i, %s, %s, %s, %i, %s, %s, TO_DATE(%s,'YYYY-MM-DD'), %i);" % (id, nomRace, nomEspece, proprio, poids, nom, genre, dateN, taille)
    executeUpdate(conn, requete)

def ajoutePrestation(conn, idFacture, type):
    id = getMaxIdTable(conn, "prestation") + 1
    requete = "INSERT INTO prestation VALUES(%i, %i, %s);" % (id, idFacture, type)
    executeUpdate(conn, requete)

def ajouteRdv(conn, horaire, idVeto, idAnimal, idPresta, idFacture):
    requete = "INSERT INTO rendez_vous VALUES(TO_TIMESTAMP('2022-04-26 10:00:00', %s), %i, %i, %i, %i);" % (horaire, idVeto, idAnimal, idPresta, idFacture)
    executeUpdate(conn, requete)

def ajouteProduit(conn, nom, date, type):
    id = getMaxIdTable(conn, "produit") + 1
    requete = "INSERT INTO produit VALUES(%i, %s, TO_DATE(%s,'YYYY-MM-DD'),%s);" % (id, nom, date, type)
    executeUpdate(conn, requete)

def ajouteFacture(conn, idVendeur, numProduit, montant, date, reglement, quantite):
    id = getMaxIdTable(conn, "facture") + 1
    requete = "INSERT INTO facture VALUES(%i,%i,%i,%i,TO_DATE(%s,'YYYY-MM-DD'),%s,%i);" % (id, idVendeur, numProduit, montant, date, reglement, quantite)
    executeUpdate(conn, requete)