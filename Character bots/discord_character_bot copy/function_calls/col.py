import discord
import sqlite3
import os
import re
from discord.ext import commands
from discord import app_commands
from discord.utils import get

def add_col(character_name, col_to_add):

        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        character_current_stat = cursor.execute("SELECT col FROM charactersheets WHERE nickname = '" + character_name + "'").fetchall()
        previous_col = character_current_stat[0][0]
        new_col_ammount = str(previous_col + int(col_to_add))
        cursor.execute("UPDATE charactersheets SET col = '" + new_col_ammount + "' WHERE nickname = '" + character_name + "'").fetchall()
        sqliteConnection.commit()
        return('```' + 'Your new col ammount is: ' + new_col_ammount + '.```')

def remove_col(character_name, col_to_remove):
        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        character_current_stat = cursor.execute("SELECT col FROM charactersheets WHERE nickname = '" + character_name + "'").fetchall()
        previous_col = character_current_stat[0][0]
        new_col_ammount = str(previous_col - int(col_to_remove))
        cursor.execute("UPDATE charactersheets SET col = '" + new_col_ammount + "' WHERE nickname   = '" + character_name + "'").fetchall()
        sqliteConnection.commit()
        return('```' + 'Your new col ammount is: ' + new_col_ammount + '.```')