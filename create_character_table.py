        #Create Table

import sqlite3

try:
    sqliteConnection = sqlite3.connect('characterSheet.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """CREATE TABLE charactersheets(firstName varchar(30), lastName varchar(30), height varchar(30), size varchar(30), age varchar(2), skillList varchar(100), inventory varchar(100), bio varchar(1000), guild varchar(20), class varchar(20), playerColor varchar(6), birthday varchar(20), nickname varchar(20), uniqueSkills varchar(20), playerStatus varchar (20), currentWeaponEquipped varchar(20), col int, experience int, level int, str int, def int, spd int);"""

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")