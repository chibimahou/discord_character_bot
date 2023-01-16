import discord
import sqlite3
import os
import re
from discord.ext import commands
from discord import app_commands
from discord.utils import get

def add_skills(character_name, skill_name):

        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        character_skills = cursor.execute("SELECT skilllist FROM characterSheets WHERE nickname = '" + character_name + "'").fetchall()
        skill_name_lower = skill_name.lower()
        old_skills = str(character_skills[0][0]).split(",")
        old_skills_length = len(old_skills)
        new_skills = ""
        temp = 0
        for temp in range(old_skills_length):
                if old_skills[temp] != skill_name_lower and temp < old_skills_length - 1:
                       new_skills = new_skills + old_skills[temp] + "," 
                elif old_skills[temp] != skill_name_lower and temp == old_skills_length - 1:
                       new_skills = new_skills + old_skills[temp] + "," 
                       new_skills = new_skills + skill_name_lower
                else:
                       return('```' + 'The skill: ' + skill_name_lower + ' is already in your skill list.' + '```')

        cursor.execute("UPDATE charactersheets SET skilllist = '" + new_skills + "' WHERE nickname = '" + character_name + "'").fetchall()
        sqliteConnection.commit()
        return('```' + 'The skill: ' + skill_name_lower + ' has been added. Your new skill list is: \n\n' + new_skills + '```')

def remove_skills(character_name, skill_name):
        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        character_skills = cursor.execute("SELECT skilllist FROM characterSheets WHERE nickname = '" + character_name + "'").fetchall()
        skill_name_lower = skill_name.lower()
        old_skills = str(character_skills[0][0]).split(",")
        old_skills_length = len(old_skills)
        new_skills = ""
        temp = 0
        for temp in range(old_skills_length):
                if old_skills[temp] != skill_name_lower and temp < old_skills_length - 1:
                       new_skills = new_skills + old_skills[temp] + "," 
                elif old_skills[temp] != skill_name_lower and temp == old_skills_length:
                        new_skills = new_skills + old_skills[temp]
                        return('```' + 'The skill: ' + skill_name_lower + ' does not exist.' + '```')
                elif old_skills[temp] == skill_name_lower and temp != old_skills_length - 1:
                        new_skills = new_skills + ""
                else:
                        new_skills = new_skills[:-1]
        cursor.execute("UPDATE charactersheets SET skilllist = '" + new_skills + "' WHERE nickname = '" + character_name + "'").fetchall()
        sqliteConnection.commit()
        return('```' + 'The skill: ' + skill_name_lower + ' has been removed. Your new skill list is: \n\n' + new_skills + '```')

def check_skill(skill_name):
        skill_name_lower = skill_name.lower()
        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        character_skills = cursor.execute("SELECT skill_description, skill_effects FROM proficiency_skills WHERE skill_name = '" + skill_name_lower + "'").fetchall()
        return('```' + skill_name_lower + '\n\n' + character_skills[0][0] + '\n\n' + character_skills[0][1] + '```')

#Adds a proficiency skill.
#Checks if skill exists in the database, if it does, get the callers character sheet.
#Remove commas and adds all skills to an array. After, check each value in a for loop
# and add them into a new array. If the skill names match, add it to the array and return True.  
#if not, return False. If the skill does not exist in the database, return False.
def add_proficiency_skills(character_name, skill_name):
        skill_name_lower = skill_name.lower()
        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        skill_exists = cursor.execute("SELECT skill_name FROM proficiency_skills WHERE skill_name = '" + skill_name_lower + "'").fetchall() 
        if len(skill_exists) != 0:
                character_skills = cursor.execute("SELECT skilllist FROM characterSheets WHERE nickname = '" + character_name + "'").fetchall()
                old_skills = str(character_skills[0][0]).split(",")
                old_skills_length = len(old_skills)
                new_skills = ""
                temp = 0
                for temp in range(old_skills_length):
                        old_skill_lower = old_skills[temp].lower()
                        if old_skill_lower != skill_name_lower and temp < old_skills_length - 1:
                                new_skills = new_skills + old_skill_lower + "," 
                        elif old_skill_lower != skill_name_lower and temp == old_skills_length - 1:
                                new_skills = new_skills + old_skill_lower + "," 
                                new_skills = new_skills + skill_name_lower
                        else:
                                return(False)

                cursor.execute("UPDATE charactersheets SET skilllist = '" + new_skills + "' WHERE nickname = '" + character_name + "'").fetchall()
                sqliteConnection.commit()
                return(True)
        else:
                return(False)

def remove_proficiency_skills(character_name, skill_name):
        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        character_skills = cursor.execute("SELECT proficiencySkills FROM characterSheets WHERE nickname = '" + character_name + "'").fetchall()
        skill_name_lower = skill_name.lower()
        old_skills = str(character_skills[0][0]).split(",")
        old_skills_length = len(old_skills)
        new_skills = ""
        temp = 0
        for temp in range(old_skills_length):
                old_skill_lower = old_skills[temp].lower()
                if old_skill_lower != skill_name_lower and temp < old_skills_length - 1:
                       new_skills = new_skills + old_skills[temp] + "," 
                elif old_skill_lower != skill_name_lower and temp == old_skills_length:
                        new_skills = new_skills + old_skills[temp]
                        return('```' + 'The skill: ' + skill_name_lower + ' does not exist.' + '```')
                elif old_skill_lower == skill_name_lower and temp != old_skills_length - 1:
                        new_skills = new_skills + ""
                else:
                        new_skills = new_skills[:-1]
        cursor.execute("UPDATE charactersheets SET skilllist = '" + new_skills + "' WHERE nickname = '" + character_name + "'").fetchall()
        sqliteConnection.commit()
        return('```' + 'The skill: ' + skill_name_lower + ' has been removed. Your new skill list is: \n\n' + new_skills + '```')
