import discord
import sqlite3
import os
import re
import function_calls.calc as calc
from discord.ext import commands
from discord import app_commands
from discord.utils import get

def add_inventory(character_name, items_to_add):
        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        character_inventory = cursor.execute("SELECT inventory FROM charactersheets WHERE nickname = '" + character_name + "'").fetchall()       
        old_inventory = calc.remove_white_spaces_around_commas(character_inventory[0][0])
        old_inventory_length = len(old_inventory)
        new_items = calc.remove_white_spaces_around_commas(items_to_add)
        new_items_length = len(new_items)
        new_inventory = ""
        temp = 0
        for temp in range(old_inventory_length):
            new_inventory = new_inventory + old_inventory[temp] + ","

        temp2 = 0
        try:
            for temp2 in range(new_items_length):
                item_exists = cursor.execute("SELECT item FROM items WHERE item = '" + new_items[temp2] + "'").fetchall()
                item_exist_count = item_exists.__len__()
                if item_exist_count != 0:      
                        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
                        if regex.search(new_items[temp2]) == None:
                                if temp2 != new_items_length - 1:
                                        new_inventory = new_inventory + new_items[temp2] + ","
                                else:
                                        new_inventory = new_inventory + new_items[temp2]
                        else:
                                new_inventory = new_inventory[:-1]
                                return False
                else:
                        new_inventory = new_inventory[:-1]
            cursor.execute("UPDATE charactersheets SET inventory = '" + new_inventory + "' WHERE nickname = '" + character_name + "'").fetchall()
            sqliteConnection.commit()
            character_information = cursor.execute("SELECT inventory FROM charactersheets WHERE nickname = '" + character_name + "'").fetchall()       
            sqliteConnection.commit()
            cursor.close()

            return True
        except:
            return False

def remove_inventory(character_name, items_to_remove):
        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        character_inventory = cursor.execute("SELECT inventory FROM charactersheets WHERE nickname = '" + character_name + "'").fetchall()       
        old_inventory = str(character_inventory[0][0]).split(",")
        old_inventory_length = len(old_inventory)
        items_to_add_remove_spaces = items_to_remove.replace(", ", ",")
        items_to_add_remove_spaces = items_to_add_remove_spaces.replace(" ,", ",")
        new_items = items_to_add_remove_spaces.split(",")
        new_items_length = len(new_items)
        new_inventory = ""
        temp = 0
        temp2 = 0

        for temp in range(old_inventory_length):
            for temp2 in range(new_items_length):
                if old_inventory[temp] != new_items[temp2]:
                    if old_inventory_length != temp + 1:
                        new_inventory = new_inventory + old_inventory[temp] + ","
                    else:
                        new_inventory = new_inventory + old_inventory[temp]

                else:
                    old_inventory_length = old_inventory_length - 1
        try:

            cursor.execute("UPDATE charactersheets SET inventory = '" + new_inventory + "' WHERE nickname = '" + character_name + "'").fetchall()
            sqliteConnection.commit()
            character_information = cursor.execute("SELECT inventory FROM charactersheets WHERE nickname = '" + character_name + "'").fetchall()       
            sqliteConnection.commit()
            cursor.close()

            return True
        except:
            return False

def inventory(character_name):
        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        character_information = cursor.execute("SELECT inventory FROM charactersheets WHERE nickname = '" + character_name + "'").fetchall()
        cursor.close()
        character_inventory = character_information[0][0]
        print(character_inventory)

        return character_inventory

def check_inventory_for_item(character_name, item_to_check):
        character_inventory = inventory(character_name)
        item_to_check_lower = item_to_check.lower()
        current_inventory = calc.remove_white_spaces_around_commas(character_inventory)
        inventory_size = len(current_inventory)
        temp = 0
        for temp in range(inventory_size):
            print(character_inventory[temp] + " item to check: " + item_to_check_lower)
            if(current_inventory[temp] == item_to_check):
                return True
        return False
