#!/usr/bin/python3

import sys
import psycopg2

import create as C
import read as R
import update as U
import delete as D
import select as S
sys.path.append("./create")
sys.path.append("./read")
sys.path.append("./update")
sys.path.append("./delete")
sys.path.append("./select")

# psql -h tuxa.sme.utc -U nf18p081 -d dbnf18p081


def main():
    HOST = "tuxa.sme.utc"
    USER = "nf18p081"
    PASSWORD = "oDAkbH7R"
    DATABASE = "dbnf18p081"


    # Connexion a la BDD
    try:
        conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (
            HOST, DATABASE, USER, PASSWORD))
    except psycopg2.OperationalError as e:
        print("connexion à la BDD impossible")
        raise(e)


    # creation des tables
    C.createTables(conn)
    # insertion de valeurs de tests
    print("\n\n---------------- Bienvenue sur l'application de gestion de la clinique vétérinaire ---------------- \n")
    insere = input("Voulez vous insérer des données prédéfinis dans la base de donnée ? Taper y si oui : ")
    if (insere == 'y'):
        C.insertDonnees(conn)

    # boucle du menu
    saisie = '0'
    while (saisie != 'q'):

        print("\nSelectionner l'action que vous voulez faire : ")
        print("\n1 : Visualiser les informations d'un élément en particulier : ")
        print("2 : Insérer des valeurs dans une table")
        print("3 : Supprimer des valeurs")
        print("4 : Visualiser des informations particulières")
        print("'q' pour quitter")

        saisie = input("Votre réponse : ")
        if(saisie == '1'):
            R.sousMenuRead(conn)
        if(saisie == '2'):
            U.sousMenuUpdate(conn)
        if (saisie == '3'):
            D.sousMenuDelete(conn)
        if(saisie == '4'):
            S.sousMenuSelect(conn)

    # fermeture de la connexion lorsque le menu est ferme
    conn.close()


if __name__ == "__main__":
    main()
