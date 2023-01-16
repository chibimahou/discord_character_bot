import discord
import sqlite3
import os
import re
import math
import function_calls.calc as calc
from discord.ext import commands
from discord import app_commands
from discord.utils import get

def combat(skill_use, offense_a, weapon_value_a, skill_a, ailment, material_modifier_a, defense_b, armor_value_b, dex_b, skill_reduction_b, material_modifier_b):
    skill_use_lower = skill_use.lower()
    ailment_lower = ailment.lower()
    check_graze = calc.check_for_bleed()
    if(ailment_lower == "poison"):
        check_poison = calc.check_for_bleed()
    elif(ailment_lower == "bleed"):
        check_bleed = calc.check_for_bleed()
    graze_dex = math.ceil(int(dex_b) * 5)
    if graze_dex > 40 and skill_use_lower == 'yes':
        graze_dex = 40
    elif graze_dex > 15 and skill_use_lower == 'no':
        graze_dex = 15
    graze_reduction = 90 - graze_dex
    print("check: " + str(check_graze) + " " + str(graze_reduction))
    if check_graze >= graze_reduction:
        print("check: " + str(check_graze) + " " + str(graze_reduction))
        graze_reduction = 100 - check_graze
        print("check: " + str(check_graze) + " " + str(graze_reduction))
    else:
        graze_reduction = 1
    print(graze_reduction)
    if skill_use_lower == 'yes':
        damage_dealt = calc.skill_damage_calculation(offense_a, weapon_value_a, skill_a, graze_reduction, material_modifier_a, defense_b, armor_value_b, skill_reduction_b, material_modifier_b)
        return('```You dealt: ' + str(damage_dealt) + ' skill damage.```')
    else:
        damage_dealt = calc.slash_damage_calculation(offense_a, weapon_value_a, graze_reduction, material_modifier_a, defense_b, armor_value_b, material_modifier_b)
        return('```You dealt: ' + str(damage_dealt) + ' slash damage.```')

