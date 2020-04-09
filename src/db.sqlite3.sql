CREATE TABLE IF NOT EXISTS "TRune" (
	"id_rune"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"id_runeinfo"	INTEGER NOT NULL,
	"id_hu_moments"	INTEGER NOT NULL,
	FOREIGN KEY("id_runeinfo") REFERENCES "TRuneInfo"("id_runeinfo"),
	FOREIGN KEY("id_hu_moments") REFERENCES "THuMoments"("id_hu_moments") ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "TRuneInfo" (
	"id_runeinfo"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT,
	"description"	TEXT
);

CREATE TABLE IF NOT EXISTS "THuMoments" (
	"id_hu_moments"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"hu_1"	REAL NOT NULL,
	"hu_2"	REAL NOT NULL,
	"hu_3"	REAL NOT NULL,
	"hu_4"	REAL NOT NULL,
	"hu_5"	REAL NOT NULL,
	"hu_6"	REAL NOT NULL,
	"hu_7"	REAL NOT NULL
);

INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 1,'Fehu','Simboliza riquezas materiais, sucesso e vitória.'WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 1);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 2,'Uruz','Sorte, crescimento, perseverança e progresso.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 2);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 3,'Thurisaz','Proteção divina e entusiasmo.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 3);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 4,'Ansuz','Sabedoria, inspiração e ouvir bons conselhos.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 4);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 5,'Raidho','Viagem, progresso em direção às metas.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 5);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 6,'Kenaz','Renovação, novos começos e iluminação.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 6);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 7,'Gebo','União, equilíbrio e bons negócios.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 7);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 8,'Wunjo','Bem-estar e evolução positiva.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 8);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 9,'Hagalaz','Simboliza precauções, obstáculos e adiamento de planos.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 9);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 10,'Naudhiz','Limitações e cautela com planos.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 10);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 11,'Isa','Concentração, paciência e equilíbrio.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 11);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 12,'Jera','Recompensas, alegria e satisfação.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 12);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 13,'Eihwaz','Proteção, final de um ciclo e recomeço.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 13);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 14,'Perdhro','Ganhos inesperados, conhecimentos ocultos e espirituais.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 14);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 15,'Sowelo','Autoconhecimento, regeneração, sucesso e vitória.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 15);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 16,'Algiz','Viagem, novos caminhos, alegria e progresso.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 16);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 17,'Tiwaz','Simboliza vitórias, honra e justiça.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 17);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 18,'Berkana','Renovação.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 18);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 19,'Ehwaz','Mudanças, progresso e lealdade.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 19);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 20,'Mannaz','Integridade, fé e clareza espiritual.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 20);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 21,'Laguz','Intuição e poderes psíquicos.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 21);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 22,'Inguz','Realizações, nascimentos, amor e sexualidade.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 22);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 23,'Dagaz','Prosperidade, transformações positivas.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 23);
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") SELECT 24,'Othila','Sabedoria ancestral, domínio, notícias distantes.' WHERE NOT EXISTS (SELECT 1 FROM TRuneInfo WHERE id_runeinfo = 24);

INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 1,1,1 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 1);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 2,1,2 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 2);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 3,1,3 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 3);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 4,1,4 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 4);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 5,1,5 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 5);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 6,4,6 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 6);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 7,4,7 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 7);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 8,4,8 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 8);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 9,4,9 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 9);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 10,7,10 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 10);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 11,7,11 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 11);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 12,7,12 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 12);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 13,7,13 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 13);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 14,4,14 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 14);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 15,7,15 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 15);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 16,6,16 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 16);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 17,6,17 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 17);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 18,6,18 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 18);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 19,6,19 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 19);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 20,6,20 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 20);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 21,5,21 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 21);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 22,5,22 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 22);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 23,5,23 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 23);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 24,5,24 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 24);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 25,5,25 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 25);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 26,3,26 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 26);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 27,3,27 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 27);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 28,3,28 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 28);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 29,3,29 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 29);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 30,3,30 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 30);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 31,2,31 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 31);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 32,2,32 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 32);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 33,2,33 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 33);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 34,2,34 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 34);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 35,2,35 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 35);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 36,8,36 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 36);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 37,8,37 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 37);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 38,8,38 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 38);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 39,8,39 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 39);
INSERT INTO "TRune" ("id_rune","id_runeinfo","id_hu_moments") SELECT 40,8,40 WHERE NOT EXISTS (SELECT 1 FROM TRune WHERE id_rune = 40);


INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 1,3.05535116431433,8.66791110281768,13.0057239112835,11.6317943351568,-23.9997574091389,-16.363429553292,-24.2970682505024 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 1);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 2,3.10980295036628,9.20547316689379,14.592485630937,12.5635891071675,-28.1338737103485,-17.1665280575283,-26.1416489813926 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 2);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 3,3.07298116582935,7.27174296028503,13.011432841515,11.5053634629972,-24.1776233072875,16.0716375265263,23.7987172984438 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 3);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 4,3.11563072497685,9.40461572853175,12.6440499901669,12.0981733383906,-25.0535716017193,17.5972937303697,-24.4845376230655 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 4);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 5,3.10392955350237,7.32082890101705,13.8935826732492,12.2899954271093,-25.4090127145474,-16.4615195437264,25.8461237522885 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 5);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 6,3.12068745770109,7.77112497656102,13.709677975487,12.8971954291582,-26.2237810174112,17.0262768212097,26.6982158705264 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 6);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 7,3.11962513564826,7.35503758195361,13.8175785487856,12.6214110316801,-26.3582729994295,-17.132660505776,25.8619379055422 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 7);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 8,3.10733395802344,9.53306628650318,12.2913109636837,11.8611641081543,-24.5321092800312,17.4246151589717,-23.9519151286155 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 8);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 9,3.09108239950858,7.3889749072931,12.7182818353661,11.8921331732711,-24.2013306093815,15.8526918823302,25.0672270109049 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 9);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 10,3.09404403861732,9.08620427029732,19.2404704618337,18.4998944039507,-37.468657189704,-23.0430165080884,-37.5889874524492 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 10);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 11,3.06965131237254,7.35343722361298,15.0386265849302,14.1805478177331,-28.8452248135964,17.8792486491686,-29.1149394697084 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 11);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 12,3.06457359385014,7.3209456672629,14.5985519216678,14.0927795153312,-29.1336328140416,-18.3690174494094,-28.4474686571501 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 12);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 13,2.93780890434289,8.17879627166927,13.5950523467955,15.4528079744701,30.0659654911095,-20.1932312813971,30.212954429308 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 13);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 14,3.06895828122951,7.3890106999837,12.4190336317943,12.1897998217534,25.1127266131498,16.3682134498263,-24.5071773089709 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 14);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 15,3.11450020941533,9.88987184168493,15.4758458920044,15.1150671551257,30.698587727172,20.7070002313879,30.4774929754928 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 15);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 16,3.0566913578366,6.58262048153208,13.2197201337035,12.7340800168756,25.710982692319,16.0254021206396,-28.1718590246305 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 16);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 17,3.11003804041843,7.4852724411756,13.1759945461105,13.933966446594,27.5145525540951,17.686453412901,27.9658335409669 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 17);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 18,3.08216572472141,9.43818237550959,11.6677384255741,14.053962311987,-26.9148543545471,18.7730711999977,28.7732792305931 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 18);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 19,3.11001766096872,7.48524885322595,13.1824631220474,13.9682356660569,27.5560681961003,17.7150521966768,28.1700120351411 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 19);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 20,3.11513115364344,7.35087320729558,13.0989206960796,12.9237004713874,-25.9383813405747,-16.6009711268413,-26.8412378331319 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 20);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 21,3.06865590628677,7.34944820328218,12.8770770542859,12.3062442824178,25.0962789102739,-16.035478112808,-25.009227599675 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 21);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 22,3.06812105945928,7.34793541535467,12.6158076069609,12.0876639768731,24.5075874367641,15.8179439655846,-24.7241264067453 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 22);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 23,3.06651347622544,7.298448292549,13.1747560800947,11.6719265810522,24.5580368330477,-15.3337805251503,-24.1227067968668 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 23);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 24,3.11138711888881,7.28655299986214,12.3576139157187,12.0979463380248,24.5028629095659,16.0129655017946,-24.452530176053 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 24);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 25,2.9168768832557,6.11034354151706,10.8367414203424,10.9502474416489,21.8700653619907,14.0131832358751,22.3149761026788 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 25);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 26,3.11296090825643,9.61508505714887,12.638563275171,12.4108429185083,24.9757441195327,17.2378813598292,-25.3216094681408 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 26);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 27,3.0878211262792,7.45268203739848,12.5059211818772,12.1098934937549,24.4180665954052,15.8363942160915,25.8740629172266 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 27);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 28,3.12943166761887,8.59698796965556,13.5508093233573,12.626992104111,25.7660767141378,16.9482321889965,-26.058596709831 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 28);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 29,3.11439017568338,7.33805585590626,14.0929913888035,12.7527742993887,-26.2181949224965,-16.6049136516192,26.5505686929386 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 29);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 30,2.85426772115719,5.89362404768321,11.465246028501,12.0384886720846,23.9737633408797,15.2650437662277,23.9123118750282 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 30);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 31,3.11197896341745,8.04833555463133,13.6905763379266,12.5322059407458,-25.7851148321609,16.5901182696294,25.8034982885378 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 31);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 32,3.07595570459096,7.22643838023277,12.1932704007462,12.3407136005326,24.9504686903718,16.0102104558427,24.6578741093047 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 32);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 33,3.10109372949895,7.29530116203334,14.5482782106507,13.0276800895592,-28.027038517789,16.8898699300232,26.8164811366679 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 33);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 34,3.08194108399705,7.37659006701064,13.102886512252,13.0849209500809,26.3075587883771,16.9264576930734,-26.353551381784 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 34);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 35,3.04764302120047,8.81148970088502,12.2662216331509,12.3445198769711,25.0006421255841,-18.2722559084007,-24.6980301665049 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 35);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 36,3.1134730522999,9.3999965580252,12.5385216606245,12.0236610655623,-24.7542163719414,17.518475344021,-24.3340473298195 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 36);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 37,3.1164451229797,9.47757045143344,12.6339640049131,12.0697312472082,-24.8339900763162,17.6721380760118,-24.45678889257 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 37);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 38,3.06085652094327,8.976303252605,11.8780158668683,11.2187933332483,-23.0713214593313,-16.5360614206223,-22.8286458415045 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 38);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 39,3.11317050557479,9.39639799044374,12.5237152713924,12.01454992892,-24.75158772943,17.4809767116218,-24.3104387934289 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 39);
INSERT INTO "THuMoments" ("id_hu_moments","hu_1","hu_2","hu_3","hu_4","hu_5","hu_6","hu_7") SELECT 40,3.1132679365211,7.37588955117303,13.6697454349327,12.2962140755796,-25.9779127501479,16.2643393655882,25.2880686824951 WHERE NOT EXISTS (SELECT 1 FROM THuMoments WHERE id_hu_moments = 40);