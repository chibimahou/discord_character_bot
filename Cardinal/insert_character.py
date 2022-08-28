#Insert Data into Table

import sqlite3

try:
    sqliteConnection = sqlite3.connect('characterSheet.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO charactersheets
                          (firstName, lastName, nickname, height, size, age, birthday, playerStatus, guild, class, skillList, uniqueSkills, currentWeaponEquipped, playerColor, inventory, bio, col, experience, level, str, def, spd)
                           VALUES 
                          ('JJ','Test','JJ', '6.2', 'average', 22, '03/28/22', 'normal', 'Moonlit Black Cats', 'Berserker', 'Rage', 'duelWield', 'BlackSword of moonlight', 'red', 'poop stick', 'An angry player upset at kaiyaba and felt immense rage causing him to unlock berserker', 1050, 550, 2)"""

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
