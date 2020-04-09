# -*- coding: utf-8 -*-
import sqlite3

def createDB():
    with open('db.sqlite3.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.executescript(sql_script)
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
                        ON TRune.id_hu_moments = THuMoments.id_hu_moments
                    ORDER BY TRuneInfo.name"""
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

def delRune(idRune):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
        """DELETE FROM TRune WHERE id_rune = (? )""",
        (idRune, )
    )
    conn.commit()
    conn.close()