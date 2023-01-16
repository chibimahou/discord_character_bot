import discord
import sqlite3
import os
import re
import math as mat
from discord.ext import commands
from discord import app_commands
from discord.utils import get

def add_stats(character_name, stat, points_to_add):
        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        character_current_stat = cursor.execute("SELECT " + stat + " FROM charactersheets WHERE nickname = '" + character_name + "';").fetchall()
        print('prev stat: ' + str(character_current_stat[0][0]) + ' points_to_add: ' + str(points_to_add))
        new_stat = str(character_current_stat[0][0] + int(points_to_add))
        cursor.execute("UPDATE charactersheets SET " + stat + " = '" + new_stat + "' WHERE nickname = '" + character_name + "';").fetchall()
        sqliteConnection.commit()
        cursor.close()      
        return('```' + 'Your new ' + stat + ' is: ' + new_stat + '.```')

def remove_stats(character_name, stat, points_to_remove):
        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        character_current_stat = cursor.execute("SELECT " + stat + " FROM charactersheets WHERE nickname = '" + character_name + "'").fetchall()
        previous_stat = character_current_stat[0][0]
        print('prev stat: ' + str(previous_stat) + ' points_to_remove: ' + str(points_to_remove))

        new_stat = str(previous_stat - int(points_to_remove))
        cursor.execute("UPDATE charactersheets SET " + stat + " = '" + new_stat + "' WHERE nickname = '" + character_name + "'").fetchall()
        sqliteConnection.commit()
        cursor.close()

        return('```' + 'Your new ' + stat + ' is: ' + new_stat + '.```')

def check_character(character_name):
        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        character_information = cursor.execute("SELECT firstName, lastName, height, size, age, skillList, inventory, bio, guild, class, playerColor, birthday, nickname, uniqueSkills, proficiencySkills, currentWeaponEquipped, col, experience, level, str, def, spd, playerStatus, dex FROM charactersheets WHERE nickname = '" + character_name + "'").fetchall()
        first_name = str(character_information[0][0])
        last_name = str(character_information[0][1])
        height = str(character_information[0][2])
        size = str(character_information[0][3])
        age = str(character_information[0][4])
        skill_list = str(character_information[0][5])
        inventory = str(character_information[0][6])
        bio = str(character_information[0][7])
        guild = str(character_information[0][8])
        player_class = str(character_information[0][9])
        player_color = str(character_information[0][10])
        birthday = str(character_information[0][11])
        nickname = str(character_information[0][12])
        unique_skills = str(character_information[0][13])
        proficiency_skills = str(character_information[0][14])
        current_weapon = str(character_information[0][15])
        col = str(character_information[0][16])
        exp = str(character_information[0][17])
        level = str(character_information[0][18])
        strength = str(character_information[0][19])
        defense = str(character_information[0][20])
        speed = str(character_information[0][21])
        player_status = str(character_information[0][22])
        dex = str(character_information[0][23])

        cursor.close()
        return("""```real name:                    ** """ + first_name + """ """ + last_name + """ **\nheight:                       ** """ + height + """
        **\nsize:                         ** """ + size  + """ **\nage:                          ** """ + age + """ **\nbirthday:                     ** """ + birthday + """ **\nbio:                          ** """ + bio + """ **
        \nusername:                     ** """ + nickname + """ **                            cursor color: ** """ + player_color + """ **
        \nlevel:                        ** """ + level + """ **\nexperience:                   ** """ +  exp + """ **\nstr: ** """ + strength + """ ** def: ** """ + defense + """ **spd: ** """ + speed + """ **  dex: ** """ + dex + """ **                   col: ** """ + col +  """ **
        \nclass:                        ** """ + player_class + """ **
        \ncurrently equipped weapon:    ** """ + current_weapon + """ **\nstatus:                       ** """ + player_status + """ **
        \nguild:                        ** """ + guild + """ **\nsword arts:\n\n** """ + skill_list + """ **\n\nunique skills:\n\n** """ +  unique_skills + """**
        \nProficiency Skills:\n\n** """ + proficiency_skills + """ **\n\ninventory:\n\n** """ + inventory + """ **```""")

def add_character(first_name, last_name, ingame_name, height, physique,  age, birthday, bio, level):
        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        ingame_name_lower = ingame_name.lower()
        height_escape_characters = height.replace('\'', '.')
        height_escape_characters = height.replace('\"', '..')
        character_information = cursor.execute("INSERT INTO charactersheets(firstName, lastName, nickname, height, size, age, birthday, playerStatus, guild, class, skillList, uniqueSkills, currentWeaponEquipped, proficiencySkills, playerColor, inventory, bio, col, experience, level, str, def, spd, dex) VALUES ('" + first_name + "','" + last_name + "','" + ingame_name_lower + "','" + height_escape_characters + "','" + physique + "','" + age + "','" + birthday + "','normal','guild','class','','unique skills','weapon equipped', 'one-handed sword mastery', 'green', 'herb, training bronze sword','" + bio + "','100','0','" + level + "','5','5','5','5'" + ")")
        sqliteConnection.commit()
        cursor.close()

        return('``` Character: ' + ingame_name_lower + ' was created. Welcome to Sword Art Online!```')

def stat_screen(character_name):
        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        character_information = cursor.execute("SELECT str, def, spd, dex FROM charactersheets WHERE nickname = '" + character_name + "'").fetchall()
        cursor.close()
        return('```str: ' + str(character_information[0][0]) + '\ndef: ' + str(character_information[0][1]) + '\nspd: ' + str(character_information[0][2]) + '\ndex: ' + str(character_information[0][3]) + '```')
