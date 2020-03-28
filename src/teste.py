import sqlite3


with open('db.sqlite3.sql', 'r') as sql_file:
    sql_script = sql_file.read()

conn = sqlite3.connect('dbTESTE.sqlite3')
cursor = conn.cursor()
cursor.executescript(sql_script)
conn.commit()
conn.close()