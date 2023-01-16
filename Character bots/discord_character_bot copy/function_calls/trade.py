import discord
import sqlite3
import os
import re
import function_calls.inventory as inventory
from discord.ext import commands
from discord import app_commands
from discord.utils import get

def trade(character_name_a, item_to_trade_a, character_name_b, item_to_trade_b):
        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        character_a_inventory = inventory.check_inventory_for_item(character_name_a, item_to_trade_a)
        character_b_inventory = inventory.check_inventory_for_item(character_name_b, item_to_trade_b)
        print(str(character_a_inventory) + " " + str(character_b_inventory))
        if(character_a_inventory == True and character_b_inventory == True):
                return True
        else:
                return False

def accept_trade(character_name_a, item_to_trade_a, character_name_b, item_to_trade_b):
        check_item_exist_a = inventory.check_inventory_for_item(character_name_a, item_to_trade_a)
        check_item_exist_b = inventory.check_inventory_for_item(character_name_b, item_to_trade_b)
        if(check_item_exist_a == True and check_item_exist_b == True):
                remove_a = inventory.remove_inventory(character_name_a, item_to_trade_a)
                print("Remove: " + item_to_trade_a)
                if(remove_a == True):
                        add_a = inventory.add_inventory(character_name_a, item_to_trade_b)
                        print("add: " + item_to_trade_b)
                        if(add_a == True):
                                print("Remove: " + item_to_trade_b)
                                remove_b = inventory.remove_inventory(character_name_b, item_to_trade_b)                                                  
                                if(remove_b == True):
                                        print("add: " + item_to_trade_a)

                                        add_b = inventory.add_inventory(character_name_b, item_to_trade_a)                             
                                        if(add_b == True):
                                                return True
                                        else:
                                                add_b = inventory.remove_inventory(character_name_b, item_to_trade_b)
                                                remove_a = inventory.add_inventory(character_name_a, item_to_trade_b)
                                                add_a = inventory.remove_inventory(character_name_a, item_to_trade_a)
                                                return False          

                                else:
                                        add_b = inventory.remove_inventory(character_name_b, item_to_trade_b)
                                        remove_a = inventory.add_inventory(character_name_a, item_to_trade_b)  
                                        return False          
                        
                        else:
                                remove_a = inventory.add_inventory(character_name_a, item_to_trade_b)
                                return False          
                else:
                        return False
        else:
                return False