INSERT INTO facture VALUES(
    501, 201, 601, 2, TO_DATE('2022-02-16','YYYY-MM-DD'), 'carte', 2,
    '{"id" : 401, "type" : "intervention"}'
);

-- le nombre de prescriptions d'un médicament --
CREATE VIEW nb_prescriptions_medicament AS 
SELECT P.num, COUNT(F.num_produit)
FROM produit P JOIN facture F ON F.num_produit = P.num
WHERE P.type = 'medicament'
GROUP BY P.num; 

-- le prix moyen d'une facture --
CREATE VIEW prix_moyen_facture AS 
SELECT ROUND(AVG(F.montant) :: numeric,2) FROM facture F WHERE F.date_paiement IS NOT NULL


-- age moyen animaux par médicament--
CREATE VIEW ageMoyenAnimaux AS
SELECT p.nom,AVG(EXTRACT(YEAR FROM NOW()) - EXTRACT(YEAR FROM a.naissance)) AS AGE
FROM facture f JOIN produit p ON f.num_produit = p.num JOIN prestation pr ON pr.id_facture = f.id JOIN rendez_vous rdv ON rdv.id_prestation = pr.id JOIN animal a ON rdv.id_animal = a.id 
WHERE p.type = 'medicament'
group by p.nom



sql = "SELECT a.age FROM ageMoyenAnimaux WHERE p.nom='%s'" % medicament
