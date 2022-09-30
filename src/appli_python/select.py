#!/usr/bin/python3

import psycopg2

def quote(s):
    if s:
        return '\'%s\'' % s
    else:
        return 'NULL'



def sousMenuSelect(conn):
    saisie = '0'
    while (saisie != 'q'):
            print("Selectionner l'action que vous voulez faire :")
            print("1 : le nombre de prescriptions d'un médicament")
            print("2 : le nombre de rendez-vous par client")
            print("3 : la moyenne des rendez-vous par client")
            print("4 : le nombre de rendez-vous par animal")
            print("5 : la moyenne des rendez-vous par animal")
            print("6 : l'âge moyen des animaux soignée avec un médicament")
            print("7 : le montant moyen des factures")
            print("8 : le nombre de produits prescrits par vétérinaire")
            print("9 : Afficher les nom et id des vétérinaires")
            print("10 : Afficher les nom et nums des tel des clients")
            print("11 : Afficher les noms et les id des animaux")
            print("12 : Afficher les nums et les nom des medicamaux")
            print("'q' pour quitter")
            saisie = input()

            if (saisie == '1'):
                nomMedicament  = quote(input("Saisissez le nom du medicament : "))
                NbrePrescriptionParMedicament(conn, nomMedicament)
            if(saisie =='2'):
                client = quote(input("Saisissez le numéro de téléphone du client : "))
                NbreRdvParClient(conn,client)
            if(saisie =='3'):
                client = quote(input("Saisissez le numéro de téléphone du client : "))
                NbreRdvMoyenneParClient(conn,client)
            if(saisie =='4'):
                animal = quote(input("Saisissez l'id de l'animal : "))
                NbreRdvParAnimal(conn,animal)
            if(saisie =='5'):
                animal = quote(input("Saisissez l'id de l'animal  : "))
                NbreRdvMoyenneParAnimal(conn,animal)
            if(saisie =='6'):
                medicament = quote(input("Saisissez le nom du médicament : "))
                ageMoyenParAnimauxParMedicament(conn,medicament)
            if(saisie =='7'):
                prixMoyenFacture(conn)
            if(saisie =='8'):
                veterinaire = quote(input("Saisissez l'id du veterinaire : "))
                NbreProduitParVeterinaire(conn,veterinaire)
            if(saisie=='9'):
                AffichageNomVeterinaire(conn)
            if(saisie=='10'):
                AffichageTelClient(conn)
            if(saisie=='11'):
                AffichageAnimalID(conn)
            if(saisie=='12'):
                AffichageMedicament(conn)


def AffichageMedicament(conn):
   cur = conn.cursor()
   sql = "SELECT p.nom,p.num from produit p where p.type ='medicament' "
   cur.execute(sql)
   raw = cur.fetchone()
   while raw:
        name = raw[0]
        id = raw[1]
        print("%s (%s)" % (name,id))
        raw = cur.fetchone()

def AffichageTelClient(conn):
   cur = conn.cursor()
   sql = "SELECT nom,tel from client "
   cur.execute(sql)
   raw = cur.fetchone()
   while raw:
        name = raw[0]
        id = raw[1]
        print("%s (%s)" % (name,id))
        raw = cur.fetchone()

def AffichageAnimalID(conn):
   cur = conn.cursor()
   sql = "SELECT nom,id from animal "
   cur.execute(sql)
   raw = cur.fetchone()
   while raw:
        name = raw[0]
        id = raw[1]
        print("%s (%s)" % (name,id))
        raw = cur.fetchone()

def AffichageNomVeterinaire(conn):
   cur = conn.cursor()
   sql = "SELECT nom,id from veterinaire "
   cur.execute(sql)
   raw = cur.fetchone()
   while raw:
        name = raw[0]
        id = raw[1]
        print("%s (%s)" % (name,id))
        raw = cur.fetchone()


def NbrePrescriptionParMedicament(conn, medicament):

  cur = conn.cursor()
  sql = "SELECT P.num, COUNT(F.num_produit) FROM produit P JOIN facture F ON F.num_produit = P.num WHERE P.type = 'medicament' and P.nom = %s GROUP BY P.num" % medicament
  cur.execute(sql)
  raw = cur.fetchone()
  if (raw):
    nbreMedicament = raw[1]
    print ("Nombre de prescription du médicament %s : %s " % (medicament, nbreMedicament))
  else:
    print("Médicament inconnu")
    return(0)


def NbreRdvParClient(conn,client):
      cur = conn.cursor()
      sql = "select c.tel,c.nom,count(*) FROM animal a JOIN rendez_vous rdv ON rdv.id_animal = a.id JOIN client c ON a.proprio = c.tel and c.tel=%s group by c.tel,c.nom" % (client)
      cur.execute(sql)
      raw = cur.fetchone()
      if (raw):
           tel = raw[0]
           nom_client = raw[1]
           nbre_rdv = raw[2]
           print ("Le nombre de RDV du client  %s (%s) est %s" % (nom_client,tel,nbre_rdv))
      else:
         print("Numéro de téléphone Inconnu")
         return(0)

def NbreRdvMoyenneParClient(conn,animal):
      cur = conn.cursor()
      sql = "select rdv.tel,rdv.nom,rdv.rdv_moyenne FROM ( select c.tel,c.nom,count(*),ROUND(COUNT(*)/SUM(COUNT(*)) OVER(),2) AS rdv_moyenne FROM animal a JOIN rendez_vous rdv ON rdv.id_animal = a.id JOIN client c ON a.proprio = c.tel  group by c.tel,c.nom) AS rdv where tel = %s " % animal
      cur.execute(sql)
      raw = cur.fetchone()
      if (raw):
           id = raw[0]
           nom_animal = raw[1]
           nbre_rdv = raw[2]
           print ("Le nombre de RDV en moyenne d'un client %s (%s) est %s" % (nom_animal,id,nbre_rdv))
      else:
         print("Numéro idclient Inconnu")
         return(0)




def NbreRdvParAnimal(conn,animal):
      cur = conn.cursor()
      sql = "select a.id,a.nom,count(*)  FROM animal a JOIN rendez_vous rdv ON rdv.id_animal = a.id and a.id = %s group by a.id,a.nom" % animal
      cur.execute(sql)
      raw = cur.fetchone()
      if (raw):
           id = raw[0]
           nom_animal = raw[1]
           nbre_rdv = raw[2]
           print ("Le nombre de RDV de l'animal  %s (%s) est %s" % (nom_animal,id,nbre_rdv))
      else:
         print("Numéro id animal Inconnu")
         return(0)

def NbreRdvMoyenneParAnimal(conn,animal):
      cur = conn.cursor()
      sql = "select rdv.id,rdv.nom,rdv.rdv_moyenne FROM (select a.id,a.nom,ROUND(COUNT(*)/SUM(COUNT(*)) OVER(),2) AS rdv_moyenne FROM animal a JOIN rendez_vous rdv ON rdv.id_animal = a.id group by a.id) AS rdv where id = %s" % animal
      cur.execute(sql)
      raw = cur.fetchone()
      if (raw):
           id = raw[0]
           nom_animal = raw[1]
           nbre_rdv = raw[2]
           print ("Le nombre de RDV en moyenne de l'animal  %s (%s) est %s" % (nom_animal,id,nbre_rdv))
      else:
         print("Numéro id animal Inconnu")
         return(0)



def ageMoyenParAnimauxParMedicament(conn,medicament):
  cur = conn.cursor()
  sql = "SELECT p.nom,ROUND(AVG(date_part('year',age(a.naissance))) :: numeric,2) AS AGE FROM facture f JOIN produit p ON f.num_produit = p.num JOIN prestation pr ON pr.id_facture = f.id JOIN rendez_vous rdv ON rdv.id_prestation = pr.id JOIN animal a ON rdv.id_animal = a.id  WHERE p.type = 'medicament'  and p.nom = %s group by p.nom " % medicament
  cur.execute(sql)
  raw = cur.fetchone()
  if (raw):
    agemoyen = raw[1]
    print ("Age moyen des animaux soigné soigné par le médicament %s : %s " % (medicament, agemoyen))
  else:
    print("Médicament inconnu")
    return(0)

def prixMoyenFacture(conn):
      cur = conn.cursor()
      sql = "SELECT ROUND(AVG(F.montant) :: numeric,2) FROM facture F WHERE F.date_paiement IS NOT NULL"
      cur.execute(sql)
      raw = cur.fetchone()
      if (raw):
        prix_moyen = raw[0]
        print ("Le prix moyen des facture est %s" % (prix_moyen))
      else:
        print("NULL")
        return(0)


def NbreProduitParVeterinaire(conn,veterinaire):
      cur = conn.cursor()
      sql = "SELECT v.id,v.nom,count(*) FROM veterinaire v JOIN rendez_vous rdv ON rdv.id_veto = v.id JOIN prestation pr ON  rdv.id_prestation = pr.id JOIN facture f ON pr.id_facture = f.id JOIN produit p ON f.num_produit = p.num and v.id=(%s) group by v.id,v.nom" % (veterinaire)
      cur.execute(sql)
      raw = cur.fetchone()
      if (raw):
          idveto = raw[0]
          nomveto = raw[1]
          nbre_produit = raw[2]
          print ("Le nombre de medicament prescrit par le véterinaire %s (%s) est %s" % (nomveto,idveto,nbre_produit))
      else:
         print("VéterinaireID Inconnu")
         return(0)
