BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "TRune" (
	"id_rune"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"id_runeinfo"	INTEGER NOT NULL,
	"id_hu_moments"	INTEGER NOT NULL,
	FOREIGN KEY("id_runeinfo") REFERENCES "TRuneInfo"("id_runeinfo"),
	FOREIGN KEY("id_hu_moments") REFERENCES "THuMoments"("id_hu_moments")
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
INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") VALUES (1,'Fehu','Simboliza riquezas materiais, sucesso e vitória.'),
 (2,'Uruz','Sorte, crescimento, perseverança e progresso.'),
 (3,'Thurisaz','Proteção divina e entusiasmo.'),
 (4,'Ansuz','Sabedoria, inspiração e ouvir bons conselhos.'),
 (5,'Raidho','Viagem, progresso em direção às metas.'),
 (6,'Kenaz','Renovação, novos começos e iluminação.'),
 (7,'Gebo','União, equilíbrio e bons negócios.'),
 (8,'Wunjo','Bem-estar e evolução positiva.'),
 (9,'Hagalaz ','Simboliza precauções, obstáculos e adiamento de planos.'),
 (10,'Naudhiz','Limitações e cautela com planos.'),
 (11,'Isa ','Concentração, paciência e equilíbrio.'),
 (12,'Jera ','Recompensas, alegria e satisfação.'),
 (13,'Eihwaz ','Proteção, final de um ciclo e recomeço.'),
 (14,'Perdhro ','Ganhos inesperados, conhecimentos ocultos e espirituais.'),
 (15,'Sowelo ','Autoconhecimento, regeneração, sucesso e vitória.'),
 (16,'Algiz ','Viagem, novos caminhos, alegria e progresso.'),
 (17,'Tiwaz ','Simboliza vitórias, honra e justiça.'),
 (18,'Berkana ','Renovação.'),
 (19,'Ehwaz ','Mudanças, progresso e lealdade.'),
 (20,'Mannaz ','Integridade, fé e clareza espiritual.'),
 (21,'Laguz ','Intuição e poderes psíquicos. '),
 (22,'Inguz ','Realizações, nascimentos, amor e sexualidade.'),
 (23,'Dagaz ','Prosperidade, transformações positivas.'),
 (24,'Othila ','Sabedoria ancestral, domínio, notícias distantes.');
COMMIT;
