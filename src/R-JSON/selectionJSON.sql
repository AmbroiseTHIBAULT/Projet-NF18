
CREATE VIEW Facture_Prestation AS
SELECT f.id, f.vendeur, f.num_produit, f.quantite, f.montant, f.date_paiement, f.reglement, CAST(p->>'id' AS integer) AS id_prestation, p->>'type' AS type_prestation
FROM facture f, JSON_ARRAY_ELEMENTS(f.prestations) p;


-- le nombre de prescriptions d'un médicament --
CREATE VIEW nb_prescriptions_medicament AS
SELECT P.num_produit, COUNT(FP.num_produit)
FROM produit P JOIN Facture_Prestation FP ON FP.num_produit = P.num_produit
WHERE P.type = 'medicament'
GROUP BY P.num_produit;


-- le prix moyen d'une facture --
CREATE VIEW prix_moyen_facture AS
SELECT ROUND(AVG(F.montant) :: numeric,2) FROM Facture_Prestation F WHERE F.date_paiement IS NOT NULL

--nombre de RDV par client--
CREATE VIEW rdvParClient AS
select c.tel,c.nom,count(*) FROM animal a JOIN rendez_vous rdv ON rdv.id_animal = a.id JOIN client c ON a.proprio = c.tel group by c.tel,c.nom


--nombre de RDV par moyenne par client--
CREATE VIEW rdvMoyenneParClient AS
select rdv.tel,rdv.nom,rdv.rdv_moyenne FROM ( select c.tel,c.nom,count(*),ROUND(COUNT(*)/SUM(COUNT(*)) OVER(),2) AS rdv_moyenne FROM animal a JOIN rendez_vous rdv ON rdv.id_animal = a.id JOIN client c ON a.proprio = c.tel  group by c.tel,c.nom) AS rdv


--nombre de RDV par animal--
CREATE VIEW rdvParAnimal AS
select a.id,a.nom,count(*)  FROM animal a JOIN rendez_vous rdv ON rdv.id_animal = a.id group by a.id,a.nom


--nombre de RDV par moyenne par animal--
CREATE VIEW rdvMoyenneParAnimal AS
select rdv.id,rdv.nom,rdv.rdv_moyenne FROM (select a.id,a.nom,ROUND(COUNT(*)/SUM(COUNT(*)) OVER(),2) AS rdv_moyenne FROM animal a JOIN rendez_vous rdv ON rdv.id_animal = a.id group by a.id) AS rdv



--nombre de produit prescrit par vétérinaire PAS FAIT--
CREATE VIEW nombreProduitParVeterinaire AS
SELECT v.id,v.nom,count(*)
FROM veterinaire v JOIN rendez_vous rdv
            ON rdv.id_veto = v.id
        JOIN Facture_Prestation FP
            ON fp.id_prestation = rdv.id_prestation
        JOIN produit p
            ON fp.num_produit = p.num_produit
GROUP BY v.id,v.nom


--age moyen soignée par animaux PAS FAIT--
CREATE VIEW ageMoyenSoigneeParAnimaux AS
SELECT p.nom,ROUND(AVG(date_part('year',age(a.naissance))) :: numeric,2) AS AGE
FROM Facture_Prestation f JOIN produit p ON f.num_produit = p.num_produit
JOIN rendez_vous rdv ON rdv.id_prestation = f.id_prestation
JOIN animal a ON rdv.id_animal = a.id  WHERE p.type = 'medicament'  group by p.nom
