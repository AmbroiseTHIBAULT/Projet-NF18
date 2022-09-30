import psycopg2


def sousMenuRead(conn):
    saisie = '0'
    while (saisie != 'q'):
        print("\nSelectionner le choix :")
        print("1 : Visualiser les données d'un veterinaire")
        print("2 : Visualiser les données d'un employe")
        print("3 : Visualiser les données d'un client")
        print("4 : Visualiser les données d'une espece")
        print("5 : Visualiser les données d'une race")
        print("6 : Visualiser les données d'un animal")
        print("7 : Visualiser les données d'une prestation")
        print("8 : Visualiser les données d'un rendez_vous")
        print("9 : Visualiser les données d'un produit")
        print("10 : Visualiser les données d'une facture")
        print("'q' pour quitter")

        saisie = input("Votre choix : ")

        if (saisie == '1'):  # veterinaire
            veterinaire = int(input("Rentrez un identifiant : "))
            readVeto(conn, veterinaire)

        elif (saisie == '2'):  # employe
            employe = int(input("Rentrez un identifiant : "))
            readEmploye(conn, employe)

        elif (saisie == '3'):  # client
            client = quote(input("Rentrez un numero de telephone : "))
            readClient(conn, client)

        elif (saisie == '4'):  # espece
            espece = quote(input("Rentrez un nom : "))
            readEspece(conn, espece)

        elif (saisie == '5'):  # race
            race = quote(input("Rentrez un nom : "))
            readRace(conn, race)

        elif (saisie == '6'):  # animal
            animal = int(input("Rentrez un identifiant : "))
            readAnimal(conn, animal)

        elif (saisie == '7'):  # prestation
            idPrestation = int(input("Rentrez un identifiant : "))
            idFacturePrestation = input("Rentrez un identifiant de facture : ")
            readPrestation(conn, idPrestation, idFacturePrestation)

        elif (saisie == '8'):  # rendez_vous
            dateRdv = quote(input("Rentrez une date et un horaire de rendez-vous (YYYY-MM-DD HH:MM:SS) : "))
            readRdv(conn, dateRdv)

        elif (saisie == '9'):  # produit
            produit = int(input("Rentrez un numero : "))
            readProduit(conn, produit)

        elif (saisie == '10'):  # facture
            facture = int(input("Rentrez un identifiant : "))
            readFacture(conn, facture)


def quote(s):
    if s:
        return '\'%s\'' % s
    else:
        return 'NULL'


def readVeto(conn, veterinaire):
    sql = "SELECT * FROM veterinaire WHERE id=%i" % veterinaire
    cur = conn.cursor()
    cur.execute(sql)
    raw = cur.fetchone()
    while raw:
        print("%i | %s | %s" % (raw[0], raw[1], raw[2]))
        raw = cur.fetchone()


def readEmploye(conn, employe):
    sql = "SELECT * FROM employe WHERE id=%i" % employe
    cur = conn.cursor()
    cur.execute(sql)
    raw = cur.fetchone()
    while raw:
        print("%i | %s | %s" % (raw[0], raw[1], raw[2]))
        raw = cur.fetchone()


def readClient(conn, client):
    sql = "SELECT * FROM client WHERE tel=%s" % client
    cur = conn.cursor()
    cur.execute(sql)
    raw = cur.fetchone()
    while raw:
        print("%s | %s | %s" % (raw[0], raw[1], raw[2]))
        raw = cur.fetchone()


def readEspece(conn, espece):
    sql = "SELECT * FROM espece WHERE nom=%s" % espece
    cur = conn.cursor()
    cur.execute(sql)
    raw = cur.fetchone()
    while raw:
        print(raw[0])
        raw = cur.fetchone()


def readRace(conn, race):
    sql = "SELECT * FROM race WHERE nom=%i" % race
    cur = conn.cursor()
    cur.execute(sql)
    raw = cur.fetchone()
    while raw:
        print("%s | %s" % (raw[0], raw[1]))
        raw = cur.fetchone()


def readAnimal(conn, animal):
    sql = "SELECT * FROM animal WHERE id=%i" % animal
    cur = conn.cursor()
    cur.execute(sql)
    raw = cur.fetchone()
    while raw:
        print("%i | %s | %s | %s | %i | %s | %s | %s | %i" % (
            raw[0], raw[1], raw[2], raw[3], raw[4], raw[5], raw[6], raw[7], raw[8]))
        raw = cur.fetchone()


def readPrestation(conn, idPrestation, idFacturePrestation):
    sql = "SELECT * FROM prestation WHERE id=%i and id_facture=%i" % (idPrestation, idFacturePrestation)
    cur = conn.cursor()
    cur.execute(sql)
    raw = cur.fetchone()
    while raw:
        print("%i | %i | %s" % (raw[0], raw[1], raw[2]))
        raw = cur.fetchone()


def readRdv(conn, dateRdv):
    sql = "SELECT * FROM rendez_vous WHERE date_rdv=%s" % dateRdv
    cur = conn.cursor()
    cur.execute(sql)
    raw = cur.fetchone()
    while raw:
        print("%s | %i | %i | %i | %i" % (raw[0], raw[1], raw[2], raw[3], raw[4]))
        raw = cur.fetchone()


def readProduit(conn, produit):
    sql = "SELECT * FROM produit WHERE num=%i" % produit
    cur = conn.cursor()
    cur.execute(sql)
    raw = cur.fetchone()
    while raw:
        print("%i | %s | %s | %s" % (raw[0], raw[1], raw[2], raw[3]))
        raw = cur.fetchone()


def readFacture(conn, facture):
    sql = "SELECT * FROM facture WHERE id=%i" % facture
    cur = conn.cursor()
    cur.execute(sql)
    raw = cur.fetchone()
    while raw:
        print("%i | %i | %i | %i | %s | %s | %i" % (raw[0], raw[1], raw[2], raw[3], raw[4], raw[5], raw[6]))
        raw = cur.fetchone()
