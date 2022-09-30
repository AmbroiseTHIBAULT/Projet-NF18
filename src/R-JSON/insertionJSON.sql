INSERT INTO veterinaire VALUES (101,'Nourisson','Ernest');
INSERT INTO veterinaire VALUES (102,'Du',       'Sylvain');
INSERT INTO veterinaire VALUES (103,'Thibault', 'Ambroise');
INSERT INTO veterinaire VALUES (104,'Vandenbon','Pierre');


INSERT INTO employe VALUES (201,'Kahlaoui','Atef');
INSERT INTO employe VALUES (202,'Yaffa',   'Elie');
INSERT INTO employe VALUES (203,'Le Du',   'Valentin');
INSERT INTO employe VALUES (204,'Di Fiore','Clément');
INSERT INTO employe VALUES (205,'Di Fiore','Edouard');
INSERT INTO employe VALUES (206,'Outan',   'Laurent');
INSERT INTO employe VALUES (207,'Affeu',   'Pierre');
INSERT INTO employe VALUES (208,'Lip',     'Julie');
INSERT INTO employe VALUES (209,'Di Fiore','Patrice');
INSERT INTO employe VALUES (210,'Morto',   'Philippe');


INSERT INTO client VALUES ('06 78 79 80 81','Trinet',       'Pierre');
INSERT INTO client VALUES ('06 13 14 15 16','Kalubi Mwamba','William');
INSERT INTO client VALUES ('06 11 68 69 70','Nzengo',       'Jose');
INSERT INTO client VALUES ('05 12 13 45 15','Liaze',        'Valerie');
INSERT INTO client VALUES ('05 12 65 06 32','Pasdo',        'Guillaume');
INSERT INTO client VALUES ('06 51 52 53 54','Miman',        'Louise');
INSERT INTO client VALUES ('06 50 52 66 54','Jacos',        'Jean');
INSERT INTO client VALUES ('06 61 62 63 64','Michel',       'Polna');
INSERT INTO client VALUES ('06 82 83 84 85','Tintin',       'Milou');


INSERT INTO espece VALUES ('Chien');
INSERT INTO espece VALUES ('Chat');
INSERT INTO espece VALUES ('Cheval');
INSERT INTO espece VALUES ('Vache');



INSERT INTO race VALUES ('Pur Sang',         'Cheval');
INSERT INTO race VALUES ('Trotteur français','Cheval');
INSERT INTO race VALUES ('Arabe',            'Cheval');
INSERT INTO race VALUES ('Selle français',   'Cheval');
INSERT INTO race VALUES ('Aubrac',           'Vache');
INSERT INTO race VALUES ('Charolaise',       'Vache');
INSERT INTO race VALUES ('Limousine',        'Vache');
INSERT INTO race VALUES ('Salers',           'Vache');
INSERT INTO race VALUES ('Beagle',           'Chien');
INSERT INTO race VALUES ('Caniche',          'Chien');
INSERT INTO race VALUES ('Teckel',           'Chien');
INSERT INTO race VALUES ('Shiba',            'Chien');
INSERT INTO race VALUES ('Sphinx',           'Chat');
INSERT INTO race VALUES ('Persan',           'Chat');
INSERT INTO race VALUES ('Oriental',         'Chat');
INSERT INTO race VALUES ('Siamois',          'Chat');


INSERT INTO animal VALUES(301,'Beagle',           'Chien', '06 51 52 53 54',20, 'Icar',            'male',  TO_DATE('2019-04-19','YYYY-MM-DD'),110);
INSERT INTO animal VALUES(302,'Persan',           'Chat',  '06 78 79 80 81',22, 'Bibi',            'female',TO_DATE('2008-01-28','YYYY-MM-DD'),80);
INSERT INTO animal VALUES(303,'Siamois',          'Chat',  '06 78 79 80 81',22, 'Paquerette',      'female',TO_DATE('2021-09-17','YYYY-MM-DD'),40);
INSERT INTO animal VALUES(304,'Caniche',          'Chien', '06 51 52 53 54',19, 'Trayton',         'male',  TO_DATE('2012-08-03','YYYY-MM-DD'),90);
INSERT INTO animal VALUES(305,'Caniche',          'Chien', '06 50 52 66 54',19, 'Nasus',           'male',  TO_DATE('2005-01-03','YYYY-MM-DD'),105);
INSERT INTO animal VALUES(306,'Persan',           'Chat',  '06 78 79 80 81',7,  'Chamine',         'female',TO_DATE('2013-10-31','YYYY-MM-DD'),67);
INSERT INTO animal VALUES(307,'Persan',           'Chat',  '06 78 79 80 81',5,  'Miniche',         'male',  TO_DATE('2014-11-30','YYYY-MM-DD'),69);
INSERT INTO animal VALUES(308,'Oriental',         'Chat',  '06 13 14 15 16',4,  'Grand Mère',      'female',TO_DATE('2018-03-09','YYYY-MM-DD'),53);
INSERT INTO animal VALUES(309,'Siamois',          'Chat',  '06 78 79 80 81',7,  'Caline',          'female',TO_DATE('2019-04-28','YYYY-MM-DD'),74);
INSERT INTO animal VALUES(310,'Siamois',          'Chat',  '06 78 79 80 81',3,  'Thierry',         'male',  TO_DATE('2020-05-26','YYYY-MM-DD'),71);
INSERT INTO animal VALUES(311,'Siamois',          'Chat',  '06 78 79 80 81',5,  'Miaomix',         'male',  TO_DATE('2021-06-25','YYYY-MM-DD'),70);
INSERT INTO animal VALUES(312,'Pur Sang',         'Cheval','06 13 14 15 16',470,'Petit Tonnerre',  'male',  TO_DATE('2017-08-28','YYYY-MM-DD'),157);
INSERT INTO animal VALUES(313,'Pur Sang',         'Cheval','06 82 83 84 85',465,'Éclair de Feu',   'female',TO_DATE('2018-12-29','YYYY-MM-DD'),153);
INSERT INTO animal VALUES(314,'Pur Sang',         'Cheval','06 82 83 84 85',485,'Tsunami',         'male',  TO_DATE('2016-04-12','YYYY-MM-DD'),169);
INSERT INTO animal VALUES(315,'Trotteur français','Cheval','06 13 14 15 16',579,'Rhum Rouge',      'male',  TO_DATE('2017-01-26','YYYY-MM-DD'),177);
INSERT INTO animal VALUES(316,'Trotteur français','Cheval','06 11 68 69 70',585,'Count Fleet',     'female',TO_DATE('2017-02-24','YYYY-MM-DD'),182);
INSERT INTO animal VALUES(317,'Trotteur français','Cheval','06 11 68 69 70',610,'Caviar Noir',     'female',TO_DATE('2015-03-22','YYYY-MM-DD'),185);
INSERT INTO animal VALUES(318,'Arabe',            'Cheval','06 11 68 69 70',430,'Eclipse',         'female',TO_DATE('2015-04-20','YYYY-MM-DD'),198);
INSERT INTO animal VALUES(319,'Arabe',            'Cheval','06 11 68 69 70',412,'Amiral de Guerre','male',  TO_DATE('2014-05-18','YYYY-MM-DD'),194);
INSERT INTO animal VALUES(320,'Arabe',            'Cheval','06 11 68 69 70',379,'Barbaro',         'male',  TO_DATE('2016-06-16','YYYY-MM-DD'),188);
INSERT INTO animal VALUES(321,'Selle français',   'Cheval','06 61 62 63 64',481,'Silence du Lundi','female',TO_DATE('2018-07-14','YYYY-MM-DD'),159);
INSERT INTO animal VALUES(322,'Selle français',   'Cheval','06 61 62 63 64',476,'Seattle Slew',    'female',TO_DATE('2014-08-12','YYYY-MM-DD'),162);
INSERT INTO animal VALUES(323,'Selle français',   'Cheval','06 61 62 63 64',458,'Alydar',          'male',  TO_DATE('2017-09-10','YYYY-MM-DD'),166);
INSERT INTO animal VALUES(324,'Aubrac',           'Vache', '05 12 13 45 15',602,'A27',             'female',TO_DATE('2017-04-12','YYYY-MM-DD'),234);
INSERT INTO animal VALUES(325,'Aubrac',           'Vache', '05 12 13 45 15',574,'A28',             'female',TO_DATE('2016-10-06','YYYY-MM-DD'),257);
INSERT INTO animal VALUES(326,'Aubrac',           'Vache', '05 12 13 45 15',642,'A29',             'female',TO_DATE('2016-08-20','YYYY-MM-DD'),248);
INSERT INTO animal VALUES(327,'Charolaise',       'Vache', '06 51 52 53 54',734,'C45',             'female',TO_DATE('2015-06-14','YYYY-MM-DD'),289);
INSERT INTO animal VALUES(328,'Charolaise',       'Vache', '05 12 65 06 32',708,'C46',             'female',TO_DATE('2015-12-27','YYYY-MM-DD'),304);
INSERT INTO animal VALUES(329,'Charolaise',       'Vache', '06 50 52 66 54',695,'C47',             'female',TO_DATE('2016-04-30','YYYY-MM-DD'),300);
INSERT INTO animal VALUES(330,'Limousine',        'Vache', '06 51 52 53 54',656,'L74',             'female',TO_DATE('2013-03-20','YYYY-MM-DD'),274);
INSERT INTO animal VALUES(331,'Limousine',        'Vache', '05 12 65 06 32',671,'L75',             'female',TO_DATE('2014-07-27','YYYY-MM-DD'),286);
INSERT INTO animal VALUES(332,'Limousine',        'Vache', '05 12 65 06 32',638,'L76',             'female',TO_DATE('2013-06-12','YYYY-MM-DD'),289);
INSERT INTO animal VALUES(333,'Salers',           'Vache', '06 51 52 53 54',771,'S62',             'female',TO_DATE('2017-04-17','YYYY-MM-DD'),335);
INSERT INTO animal VALUES(334,'Salers',           'Vache', '06 51 52 53 54',784,'S63',             'female',TO_DATE('2017-10-12','YYYY-MM-DD'),321);
INSERT INTO animal VALUES(335,'Salers',           'Vache', '06 50 52 66 54',756,'S64',             'female',TO_DATE('2017-08-28','YYYY-MM-DD'),309);
INSERT INTO animal VALUES(336,'Persan',           'Chat',  '06 50 52 66 54',4,  'Caramel',         'female',TO_DATE('2015-12-31','YYYY-MM-DD'),67);
INSERT INTO animal VALUES(337,'Oriental',         'Chat',  '06 78 79 80 81',5,  'Pastis',          'male',  TO_DATE('2016-01-02','YYYY-MM-DD'),57);
INSERT INTO animal VALUES(338,'Oriental',         'Chat',  '06 78 79 80 81',6,  'Voisin',          'male',  TO_DATE('2017-02-08','YYYY-MM-DD'),56);

INSERT INTO produit VALUES(601,'savon',    TO_DATE('2005-03-10','YYYY-MM-DD'),'produit_entretien');
INSERT INTO produit VALUES(602,'vaccin',   TO_DATE('2008-03-10','YYYY-MM-DD'),'medicament');
INSERT INTO produit VALUES(603,'smecta',   TO_DATE('2011-03-13','YYYY-MM-DD'),'medicament');
INSERT INTO produit VALUES(604,'dogoprane',TO_DATE('2008-03-14','YYYY-MM-DD'),'medicament');
INSERT INTO produit VALUES(605,'parfum',   TO_DATE('2003-03-08','YYYY-MM-DD'),'produit_entretien');

INSERT INTO quantite_numProduit VALUES (604,8,66);
INSERT INTO quantite_numProduit VALUES (601,2,2);
INSERT INTO quantite_numProduit VALUES (603,2,8);
INSERT INTO quantite_numProduit VALUES (604,1,42);
INSERT INTO quantite_numProduit VALUES (601,6,56);
INSERT INTO quantite_numProduit VALUES (604,7,112);
INSERT INTO quantite_numProduit VALUES (604,5,99);
INSERT INTO quantite_numProduit VALUES (604,6,13);

INSERT INTO facture VALUES(515, 210, 604,TO_DATE('2022-04-25','YYYY-MM-DD'),'cheque',8,'[{"id" : 412, "type" : "consultation"},{"id" : 413, "type" : "prestation"},{"id" : 414, "type" : "prestation"}]');
INSERT INTO facture VALUES(516, 210, 604,TO_DATE('2022-04-25','YYYY-MM-DD'),'cheque',8,'[{"id" : 414, "type" : "prestation"}]');
INSERT INTO facture VALUES(517, 210, 604,TO_DATE('2022-04-25','YYYY-MM-DD'),'cheque',8,'[{"id" : 415, "type" : "consultation"}]');
INSERT INTO facture VALUES(501, 201, 601,TO_DATE('2022-02-16','YYYY-MM-DD'), 'carte', 2,'[{"id" : 401, "type" : "intervention"}]');
INSERT INTO facture VALUES(502, 201, 603,TO_DATE('2022-02-16','YYYY-MM-DD'), 'carte', 2,'[{"id" : 402, "type" : "intervention"}]');
INSERT INTO facture VALUES(503, 201, 601,TO_DATE('2022-01-14','YYYY-MM-DD'),'carte',2,'[{"id" : 403, "type" : "consultation"}]');
INSERT INTO facture VALUES(504, 208, 604,TO_DATE('2022-04-25','YYYY-MM-DD'),'cheque',1,'[{"id" : 404, "type" : "consultation"}]');
INSERT INTO facture VALUES(505, 207, 601,TO_DATE('2022-04-25','YYYY-MM-DD'),'cheque',6,'[{"id" : 405, "type" : "intervention"}]');
INSERT INTO facture VALUES(506, 208, 604,TO_DATE('2022-04-25','YYYY-MM-DD'),'cheque',7,'[{"id" : 406, "type" : "consultation"}]');
INSERT INTO facture VALUES(507, 210, 604,TO_DATE('2022-04-25','YYYY-MM-DD'),'cheque',8,'[{"id" : 407, "type" : "consultation"}]');
INSERT INTO facture VALUES(508, 207, 604,TO_DATE('2022-04-25','YYYY-MM-DD'),'cheque',5,'[{"id" : 408, "type" : "intervention"}]');
INSERT INTO facture VALUES(509, 203, 604,TO_DATE('2022-04-25','YYYY-MM-DD'),'cheque',6,'[{"id" : 409, "type" : "consultation"}]');

INSERT INTO rendez_vous VALUES(TO_TIMESTAMP('2022-04-26 10:00:00','YYYY-MM-DD HH24:MI:SS'),101,301,401,501);
INSERT INTO rendez_vous VALUES(TO_TIMESTAMP('2022-04-26 11:30:00','YYYY-MM-DD HH24:MI:SS'),103,305,402,502);
INSERT INTO rendez_vous VALUES(TO_TIMESTAMP('2021-05-13 14:00:00','YYYY-MM-DD HH24:MI:SS'),101,304,403,503);
INSERT INTO rendez_vous VALUES(TO_TIMESTAMP('2022-02-24 10:00:00','YYYY-MM-DD HH24:MI:SS'),102,321,404,504);
INSERT INTO rendez_vous VALUES(TO_TIMESTAMP('2022-05-23 08:30:00','YYYY-MM-DD HH24:MI:SS'),103,331,405,505);
INSERT INTO rendez_vous VALUES(TO_TIMESTAMP('2020-01-29 16:45:00','YYYY-MM-DD HH24:MI:SS'),102,312,406,506);
INSERT INTO rendez_vous VALUES(TO_TIMESTAMP('2019-02-16 13:30:00','YYYY-MM-DD HH24:MI:SS'),104,337,407,507);
INSERT INTO rendez_vous VALUES(TO_TIMESTAMP('2022-10-15 09:00:00','YYYY-MM-DD HH24:MI:SS'),101,327,408,508);
INSERT INTO rendez_vous VALUES(TO_TIMESTAMP('2012-04-24 11:30:00','YYYY-MM-DD HH24:MI:SS'),101,316,409,509);
