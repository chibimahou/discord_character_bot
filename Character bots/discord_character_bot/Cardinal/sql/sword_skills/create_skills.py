        #Create Table

import sqlite3

try:
    sqliteConnection = sqlite3.connect('characterSheet.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """CREATE TABLE sword_skills(ID int AUTOINCRIMEN PRIMARY KEY, skill_name VARCHAR(20), skill_description VARCHAR(200), skill_hits(3), skill_effects VARCHAR(200), skill_type VARCHAR(20), skill_power int);"""

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