import sqlite3

def createDB():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS "THuMoments" (
            "id_hu_moments"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "hu_1"	REAL NOT NULL,
            "hu_2"	REAL NOT NULL,
            "hu_3"	REAL NOT NULL,
            "hu_4"	REAL NOT NULL,
            "hu_5"	REAL NOT NULL,
            "hu_6"	REAL NOT NULL,
            "hu_7"	REAL NOT NULL
        );"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS "TRune" (
            "id_rune"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "name"	TEXT NOT NULL,
            "id_hu_moments"	INTEGER NOT NULL,
            "description"	TEXT
        );"""
    )
    conn.commit()
    conn.close()

def saveImg(name, description, huMoments):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO THuMoments (hu_1, hu_2, hu_3, hu_4, hu_5, hu_6, hu_7)
           VALUES (?,?,?,?,?,?,?)""",
        (float(huMoments[0]), float(huMoments[1]), float(huMoments[2]), float(huMoments[3]), float(huMoments[4]), float(huMoments[5]), float(huMoments[6]))
    )
    id_hu_moments = cursor.lastrowid
    cursor.execute(
        """INSERT INTO TRune (name, id_hu_moments, description)
           VALUES (?,?,?)""",
        (name, id_hu_moments, description)
    )
    conn.commit()
    conn.close()

def searchRunes():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
        """SELECT name, hu_1, hu_2, hu_3, hu_4, hu_5, hu_6, hu_7 from TRune
           INNER JOIN THuMoments
           ON TRune.id_hu_moments = THuMoments.id_hu_moments"""
    )
    return cursor.fetchall()