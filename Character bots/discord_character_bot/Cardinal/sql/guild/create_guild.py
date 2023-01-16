        #Create Table

import sqlite3

try:
    sqliteConnection = sqlite3.connect('characterSheet.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """CREATE TABLE guilds(guild_name VARCHAR(50) PRIMARY KEY, guild_description VARCHAR(200), guild_approvers VARCHAR(200), guild_member_count int);"""

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