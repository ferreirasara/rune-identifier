import sqlite3

def createDB():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS "TRune" (
            "id_rune"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "id_runeinfo"	INTEGER NOT NULL,
            "id_hu_moments"	INTEGER NOT NULL,
            FOREIGN KEY("id_runeinfo") REFERENCES "TRuneInfo"("id_runeinfo"),
            FOREIGN KEY("id_hu_moments") REFERENCES "THuMoments"("id_hu_moments")
        );"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS "TRuneInfo" (
            "id_runeinfo"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "name"	TEXT,
            "description"	TEXT
        );"""
    )
    # cursor.execute(
    #     """INSERT INTO "TRuneInfo" ("id_runeinfo","name","description") VALUES (1,'Fehu','Simboliza riquezas materiais, sucesso e vitória.'),
    #     (2,'Uruz','Sorte, crescimento, perseverança e progresso.'),
    #     (3,'Thurisaz','Proteção divina e entusiasmo.'),
    #     (4,'Ansuz','Sabedoria, inspiração e ouvir bons conselhos.'),
    #     (5,'Raidho','Viagem, progresso em direção às metas.'),
    #     (6,'Kenaz','Renovação, novos começos e iluminação.'),
    #     (7,'Gebo','União, equilíbrio e bons negócios.'),
    #     (8,'Wunjo','Bem-estar e evolução positiva.'),
    #     (9,'Hagalaz ','Simboliza precauções, obstáculos e adiamento de planos.'),
    #     (10,'Naudhiz','Limitações e cautela com planos.'),
    #     (11,'Isa ','Concentração, paciência e equilíbrio.'),
    #     (12,'Jera ','Recompensas, alegria e satisfação.'),
    #     (13,'Eihwaz ','Proteção, final de um ciclo e recomeço.'),
    #     (14,'Perdhro ','Ganhos inesperados, conhecimentos ocultos e espirituais.'),
    #     (15,'Sowelo ','Autoconhecimento, regeneração, sucesso e vitória.'),
    #     (16,'Algiz ','Viagem, novos caminhos, alegria e progresso.'),
    #     (17,'Tiwaz ','Simboliza vitórias, honra e justiça.'),
    #     (18,'Berkana ','Renovação.'),
    #     (19,'Ehwaz ','Mudanças, progresso e lealdade.'),
    #     (20,'Mannaz ','Integridade, fé e clareza espiritual.'),
    #     (21,'Laguz ','Intuição e poderes psíquicos. '),
    #     (22,'Inguz ','Realizações, nascimentos, amor e sexualidade.'),
    #     (23,'Dagaz ','Prosperidade, transformações positivas.'),
    #     (24,'Othila ','Sabedoria ancestral, domínio, notícias distantes.');"""
    # )
    conn.commit()
    conn.close()

def saveImg(idRuneInfo, huMoments):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO THuMoments (hu_1, hu_2, hu_3, hu_4, hu_5, hu_6, hu_7)
           VALUES (?,?,?,?,?,?,?)""",
        (huMoments[0], huMoments[1], huMoments[2], huMoments[3], huMoments[4], huMoments[5], huMoments[6])
    )
    id_hu_moments = cursor.lastrowid
    cursor.execute(
        """INSERT INTO TRune (id_runeinfo, id_hu_moments)
           VALUES (?,?)""",
        (idRuneInfo, id_hu_moments)
    )
    conn.commit()
    conn.close()

def searchAvgRunes():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
        """SELECT   TRune.id_rune,
                    TRuneInfo.name,
                    avg(THuMoments.hu_1) as hu_1,
                    avg(THuMoments.hu_2) as hu_2,
                    avg(THuMoments.hu_3) as hu_3,
                    avg(THuMoments.hu_4) as hu_4,
                    avg(THuMoments.hu_5) as hu_5,
                    avg(THuMoments.hu_6) as hu_6,
                    avg(THuMoments.hu_7) as hu_7
                    FROM TRune
                    INNER JOIN TRuneInfo
                        ON TRune.id_runeinfo = TRuneInfo.id_runeinfo
                    INNER JOIN THuMoments
                        ON TRune.id_hu_moments = THuMoments.id_hu_moments
                    GROUP BY TRuneInfo.name"""
    )
    return cursor.fetchall()

def searchAllRunes():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
        """SELECT   TRune.id_rune,
                    TRuneInfo.name,
                    THuMoments.hu_1,
                    THuMoments.hu_2,
                    THuMoments.hu_3,
                    THuMoments.hu_4,
                    THuMoments.hu_5,
                    THuMoments.hu_6,
                    THuMoments.hu_7
                    FROM TRune
                    INNER JOIN TRuneInfo
                        ON TRune.id_runeinfo = TRuneInfo.id_runeinfo
                    INNER JOIN THuMoments
                        ON TRune.id_hu_moments = THuMoments.id_hu_moments"""
    )
    return cursor.fetchall()

def getRune(idRune):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
        """SELECT name, description, hu_1, hu_2, hu_3, hu_4, hu_5, hu_6, hu_7 from TRune
                INNER JOIN THuMoments
                    ON TRune.id_hu_moments = THuMoments.id_hu_moments
                INNER JOIN TRuneInfo
                    ON TRune.id_runeinfo = TRuneInfo.id_runeinfo
                WHERE id_rune = (?)""",
        (idRune, )
    )
    return cursor.fetchall()

def getRuneNames():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
        """SELECT name
	        FROM TRuneInfo"""
    )
    return cursor.fetchall()

def getIdRuneInfo(name):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
        """SELECT id_runeinfo
                FROM TRuneInfo
                WHERE name = (?)""",
        (name, )
    )
    idRuneInfo = cursor.fetchall()[0][0]
    return idRuneInfo