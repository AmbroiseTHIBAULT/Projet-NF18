#!/usr/bin/python3

import psycopg2


def sousMenuDelete(conn):
    saisie = '0'
    while (saisie != 'q'):
        print("\nSelectionner l'action que vous voulez faire :")
        print("1 : Supprimer un veterinaire")
        print("2 : Supprimer un employe")
        print("3 : Supprimer un client")
        print("4 : Supprimer une espece")
        print("5 : Supprimer une race")
        print("6 : Supprimer un animal")
        print("7 : Supprimer une prestation")
        print("8 : Supprimer un rendez_vous")
        print("9 : Supprimer un produit")
        print("10 : Supprimer une facture")
        print("'q' pour quitter")

        saisie = input()

        if (saisie == '1'):
            vetoDelete = input(
                "Saisissez l'id du veterinaire a supprimer : ")
            deleteVeto(conn, vetoDelete)

        elif(saisie == '2'):
            employeDelete = input(
                "Saisissez l'id de l'employe a supprimer : ")
            deleteEmploye(conn, employeDelete)

        elif(saisie == '3'):
            clientDelete = input(
                "Saisissez le numero du client a supprimer : ")
            deleteClient(conn, clientDelete)

        elif(saisie == '4'):
            especeDelete = input(
                "Saisissez le nom de l'espece a supprimer : ")
            deleteEspece(conn, especeDelete)

        elif(saisie == '5'):
            raceDelete = input(
                "Saisissez le nom de la race a supprimer : ")
            deleteRace(conn, raceDelete)

        elif(saisie == '6'):
            animalDelete = input(
                "Saisissez l'id de l'animal a supprimer : ")
            deleteAnimal(conn, animalDelete)

        elif(saisie == '7'):
            idPrestationDelete = input(
                "Saisissez l'id de la prestation a supprimer : ")
            idFactureDelete = input(
                "Saisissez l'id de la facture, associee a la prestation precedemment saisie, a supprimer : ")
            deletePrestation(conn, idPrestationDelete, idFactureDelete)

        elif(saisie == '8'):
            rdvDelete = input(
                "Saisissez l'horaire du rdv a supprimer (format : YYYY-MM-DD HH:MI:SS) : ")
            deleteRdv(conn, rdvDelete)

        elif(saisie == '9'):
            produitDelete = input(
                "Saisissez le numero du produit a supprimer : ")
            deleteProduit(conn, produitDelete)

        elif(saisie == '10'):
            factureDelete = input(
                "Saisissez l'id de la facture a supprimer : ")
            deleteFacture(conn, factureDelete)


def executeSuppression(conn, requete):
    try:
        cur = conn.cursor()
        cur.execute(requete)
        conn.commit()

    except psycopg2.IntegrityError as e:
        conn.rollback()
        print("Message systeme :", e)


def deleteVeto(conn, idVeto):
    requete = f"DELETE FROM veterinaire WHERE id = {idVeto};"
    executeSuppression(conn, requete)


def deleteEmploye(conn, idEmploye):
    requete = f"DELETE FROM employe WHERE id = {idEmploye};"
    executeSuppression(conn, requete)


def deleteClient(conn, telClient):
    requete = f"DELETE FROM client WHERE tel = '{telClient}';"
    executeSuppression(conn, requete)


def deleteEspece(conn, nomEspece):
    requete = f"DELETE FROM espece WHERE nom = '{nomEspece}';"
    executeSuppression(conn, requete)


def deleteRace(conn, nomRace):
    requete = f"DELETE FROM race WHERE nom = '{nomRace}';"
    executeSuppression(conn, requete)


def deleteAnimal(conn, idAnimal):
    requete = f"DELETE FROM animal WHERE id = {idAnimal};"
    executeSuppression(conn, requete)


def deletePrestation(conn, idPrestation, idFacture):
    requete = f"DELETE FROM prestation WHERE id = {idPrestation} AND id_facture = {idFacture} ;"
    executeSuppression(conn, requete)


def deleteRdv(conn, dateRdv):
    requete = f"DELETE FROM rendez_vous WHERE date_rdv = TO_TIMESTAMP('{dateRdv}','YYYY-MM-DD HH24:MI:SS'));"
    executeSuppression(conn, requete)


def deleteProduit(conn, idProduit):
    requete = f"DELETE FROM produit WHERE id = {idProduit};"
    executeSuppression(conn, requete)


def deleteFacture(conn, idFacture):
    requete = f"DELETE FROM facture WHERE id = {idFacture};"
    executeSuppression(conn, requete)
