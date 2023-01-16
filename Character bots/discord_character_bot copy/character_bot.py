import discord
import sqlite3
import os
import re
import function_calls.inventory as inv
import function_calls.invites as invi
import function_calls.skills as ski
import function_calls.experience as exp
import function_calls.col as col
import function_calls.help as help
import function_calls.stats as sta
import function_calls.calc as mat
import function_calls.combat as com
import function_calls.trade as tra
from discord.ext import commands
from discord import app_commands
from discord.utils import get

print("Hello")
client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@commands.command()
async def sync(self, ctx) -> None:
   fmt = await ctx.bot.tree.sync()
   await ctx.send(
      f"Synced {len(fmt)} command to the current guild."
   )
   return

@client.command()
async def addrole(ctx, member : discord.Member, role : discord.Role):
    await member.add_roles(role)


@client.tree.command(name="hello", description="Hello!")
async def hello(interaction: discord.Interaction):
        await client.tree.sync()
        print(f'Command tree synced.')

@client.tree.command(name="test")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!" )

@client.tree.command(name="character")
@app_commands.describe(character_name = "kirito!")
async def character(interaction: discord.Interaction, character_name: str):
        results = sta.check_character(character_name)
        await interaction.response.send_message(results)
#Display Character stat screen.
@client.tree.command(name="stat_screen")
@app_commands.describe(character_name = "Hello!")
async def stat_screen(interaction: discord.Interaction, character_name: str):
            results = sta.stat_screen(character_name)
            await interaction.response.send_message(results)


#Display Character stat screen.
@client.tree.command(name="add_character")
@app_commands.describe(first_name="kirigaya", last_name="kazuto", ingame_name="Kirito", height="5'2\"", physique="muscular",  age="12", birthday="1/2/22", bio="A young boy who loves vrmmos.", level="1")
async def add_Character(interaction: discord.Interaction, first_name:str, last_name:str, ingame_name:str, height:str, physique:str,  age:str, birthday:str, bio:str, level: str):
            results = sta.add_character(first_name, last_name, ingame_name, height, physique,  age, birthday, bio, level)
            await interaction.response.send_message(results)

#Display Character stat screen.
@client.tree.command(name="inventory")
@app_commands.describe(character_name = "Hello!")
async def inventory(interaction: discord.Interaction, character_name: str):
            results = inv.inventory(character_name)
            await interaction.response.send_message(results)

#Display Character stat screen.
@client.tree.command(name="change_weapon")
@app_commands.describe(character_name = "Hello!")
async def change_weapon(interaction: discord.Interaction, character_name: str):
        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        character_information = cursor.execute("SELECT currentWeaponEquipped FROM charactersheets WHERE nickname = '" + character_name + "'").fetchall()
        cursor.close()
        await interaction.response.send_message('```' + character_name + ' currently equipped weapon: ' + character_information[0][0] + '```')

#Display Character stat screen.
@client.tree.command(name="add_inventory")
@app_commands.describe(character_name = "Kirito", items_to_add = "1,2")
async def add_inventory(interaction: discord.Interaction, character_name: str, items_to_add: str):
            results = inv.add_inventory(character_name, items_to_add)
            if results == True:
                await interaction.response.send_message('```' + items_to_add + ' has been successfully added to your inventory. ' + '```')
            else:    
                await interaction.response.send_message('``` Sorry, ' + items_to_add + ' is not in your inventory. ' + '```')

#Display Character stat screen.
@client.tree.command(name="remove_inventory")
@app_commands.describe(character_name = "Hello!", items_to_remove = "1,2")
async def remove_inventory(interaction: discord.Interaction, character_name: str, items_to_remove: str):
            results = inv.remove_inventory(character_name, items_to_remove)
            if results == True:
                await interaction.response.send_message('```' + items_to_remove + ' has been successfully removed from your inventory. ' + '```')
            else:    
                await interaction.response.send_message('``` Sorry, ' + items_to_remove + ' is not in your inventory. ' + '```')

#Display Character stat screen.
@client.tree.command(name="add_skill")
@app_commands.describe(character_name = "Kirito", skill_to_add = "Fishing", skill_level = "1")
async def add_skill(interaction: discord.Interaction, character_name: str, skill_to_add: str, skill_level: str):
            results = inv.add_inventory(character_name, skill_to_add)
            if results == True:
                await interaction.response.send_message('```' + skill_to_add + ' has been successfully added to your inventory. ' + '```')
            else:    
                await interaction.response.send_message('``` Sorry, ' + skill_to_add + ' is not in your inventory. ' + '```')

#Display Character stat screen.
@client.tree.command(name="remove_skill")
@app_commands.describe(character_name = "Hello!", skill_to_remove = "Fishing", levels_to_remove = "1")
async def remove_skill(interaction: discord.Interaction, character_name: str, skill_to_remove: str, levels_to_remove: str):
            results = ski.remove_skills(character_name, skill_to_remove)
            if results == True:
                await interaction.response.send_message('```' + skill_to_remove + ' has been successfully removed from your inventory. ' + '```')
            else:    
                await interaction.response.send_message('``` Sorry, ' + skill_to_remove + ' is not in your inventory. ' + '```')

#Display Character stat screen.
@client.tree.command(name="experience")
@app_commands.describe(character_name = "Kirito", experience_to_add = "10")
async def experience(interaction: discord.Interaction, character_name: str, experience_to_add: str):
            results = exp.experience(character_name, experience_to_add)
            await interaction.response.send_message(results)

#Display Character stat screen. 
@client.tree.command(name="add_experience")
@app_commands.describe(character_name = "Hello!", experience_to_add = "20")
async def add_experience(interaction: discord.Interaction, character_name: str, experience_to_add: str):
            results = exp.add_experience(character_name, experience_to_add)
            await interaction.response.send_message(results)

#Display Character stat screen.
@client.tree.command(name="remove_experience")
@app_commands.describe(character_name = "Hello!", experience_to_remove = "20")
async def remove_experience(interaction: discord.Interaction, character_name: str, experience_to_remove: str):
            results = exp.remove_experience(character_name, experience_to_remove)
            await interaction.response.send_message(results)

#Display Character stat screen.
@client.tree.command(name="combat")
@app_commands.describe(character_name = "Hello!")
async def combat(interaction: discord.Interaction, character_name: str):
            results = com.combat(character_name)
            await interaction.response.send_message(results)

#Display Character stat screen.
@client.tree.command(name="add_stat")
@app_commands.describe(character_name = "Hello!", stat = "str", points_to_add = "2")
async def add_stat(interaction: discord.Interaction, character_name: str, stat: str, points_to_add: str):
            results = sta.add_stats(character_name, stat, points_to_add)
            await interaction.response.send_message(results)

#Display Character stat screen.
@client.tree.command(name="remove_stat")
@app_commands.describe(character_name = "Hello!", stat = "str", points_to_remove = "2")
async def remove_stat(interaction: discord.Interaction, character_name: str, stat: str, points_to_remove: str):
            results = sta.remove_stats(character_name, stat, points_to_remove)
            await interaction.response.send_message(results)

#Display Character stat screen.
@client.tree.command(name="add_col")
@app_commands.describe(character_name = "Kirito", col_to_add = "20")
async def add_col(interaction: discord.Interaction, character_name: str, col_to_add: str):
            results = col.add_col(character_name, col_to_add)
            await interaction.response.send_message(results)


#Display Character stat screen.
@client.tree.command(name="remove_col")
@app_commands.describe(character_name = "Kirito",  col_to_remove = "20")
async def remove_col(interaction: discord.Interaction, character_name: str, col_to_remove: str):
            results = col.remove_col(character_name, col_to_remove)
            await interaction.response.send_message(results)

#Display Character stat screen.
@client.tree.command(name="check_items")
@app_commands.describe(item_name = "Healing potion")
async def check_items(interaction: discord.Interaction, item_name: str):
        sqliteConnection = sqlite3.connect('characterSheet.db')
        cursor = sqliteConnection.cursor()
        character_information = cursor.execute("SELECT * FROM items WHERE item = '" + item_name + "'").fetchall()
        await interaction.response.send_message('```' + 'The item you selected is: ' + character_information[0][1] + ' ' + character_information[0][2] + ' ' + character_information[0][3] + character_information[0][4] + '```')

#Display Character stat screen.
@client.tree.command(name="add_skills")
@app_commands.describe(character_name = "Kirito", skill_name = "Vorpal Slash")
async def add_skills(interaction: discord.Interaction,character_name: str, skill_name: str):
            results = ski.add_skills(character_name, skill_name)
            await interaction.response.send_message(results)

#Display Character stat screen.
@client.tree.command(name="remove_skills")
@app_commands.describe(character_name = "Kirito", skill_name = "Vorpal Strike")
async def remove_skills(interaction: discord.Interaction, character_name: str, skill_name: str):
            results = ski.remove_skills(character_name, skill_name)
            await interaction.response.send_message(results)

#Display Character stat screen.
@client.tree.command(name="send_guild_request")
@app_commands.describe(inviters_name = "Kirito", invitees_name = "Asuna", guild_name = "Moonlit black cats")
async def remove_skills(interaction: discord.Interaction, inviters_name: str, invitees_name: str, guild_name: str):
           results = invi.request_guild_invite(inviters_name, invitees_name, guild_name)
           await interaction.response.send_message(results)

#Display Character stat screen.
@client.tree.command(name="accept_or_decline_guild_request")
@app_commands.describe(inviters_name = "Kirito", invitees_name = "Asuna", guild_name = "moonlit black cats", accept_or_decline = "accept")
async def accept_or_decline_guild_request(interaction: discord.Interaction, inviters_name: str, invitees_name: str, guild_name: str, accept_or_decline: str):
            results = invi.accept_or_decline_guild_invite(inviters_name, invitees_name, guild_name, accept_or_decline)
            await interaction.response.send_message(results)

#Display Character stat screen.
@client.tree.command(name="send_party_invite")
@app_commands.describe(inviters_name = "Kirito", invitees_name = "Asuna")
async def send_party_invite(interaction: discord.Interaction, inviters_name: str, invitees_name: str):
            results = invi.request_party_invite(inviters_name, invitees_name)
            await interaction.response.send_message(results)

#Display Character stat screen.
@client.tree.command(name="accept_or_decline_party_invite")
@app_commands.describe(inviters_name = "Kirito", invitees_name = "Asuna", accept_or_decline = "Accept")
async def accept_or_decline_party_invite(interaction: discord.Interaction, inviters_name: str, invitees_name: str, accept_or_decline: str):
            results = invi.accept_or_decline_party_invite(inviters_name, invitees_name, accept_or_decline)
            await interaction.response.send_message(results)

#Display Character stat screen.
@client.tree.command(name="request_trade")
@app_commands.describe(character_name_a="Kirito", item_to_trade_a="herb", character_name_b="Asuna", item_to_trade_b="Bronze Ingot")
async def request_trade(interaction: discord.Interaction, character_name_a: str, item_to_trade_a: str, character_name_b: str, item_to_trade_b: str):
    valid_trade = tra.trade(character_name_a, item_to_trade_a, character_name_b, item_to_trade_b)
    moderator_roles = [role for role in interaction.guild.roles if role.permissions.manage_messages]

    moderator_mentions = ' '.join([role.mention for role in moderator_roles])
    if valid_trade:
        await interaction.response.send_message(f"```{moderator_mentions}: {character_name_a} would like to trade: \n\n{item_to_trade_a} \n\n{character_name_b} would like to trade: \n\n{item_to_trade_b}. \n\nIf both players respond to this with an emote, that will confirm the trade: \n\nPlease ping a moderator to come and innitiate the trade.```"
        )
    else:
        await interaction.response.send_message("```Trade invalid: One player does not have the required item(s). Please verify your inventories.```")

#Display Character stat screen.
@client.tree.command(name="help_commands")
@app_commands.describe()
async def help_commands(interaction: discord.Interaction):
    results = help.help_commands()
    await interaction.response.send_message(results, ephemeral=True)

#Display Character stat screen.
@client.tree.command(name="help_damage")
@app_commands.describe()
async def help_damage(interaction: discord.Interaction):
    results = help.help_damage()
    await interaction.response.send_message(results, ephemeral=True)

#Display Character stat screen.
@client.tree.command(name="help_roleplay")
@app_commands.describe()
async def help_roleplay(interaction: discord.Interaction):
    results = help.help_roleplay()
    await interaction.response.send_message(results, ephemeral=True)

@client.tree.command(name="calculate_combat_skill")
@app_commands.describe(offense_a = "50", weapon_value_a = "25", skill_a = "2.0", ailment = "poison, bleed", material_modifier_a = "1.0", defense_b = "15", armor_value_b = "25", dex_b = "10",  skill_reduction_b = "15", material_modifier_b = "1.0")
async def calculate_combat(interaction: discord.Interaction, skill_use: str, offense_a: str, weapon_value_a: str, ailment: str, skill_a: str, material_modifier_a: str, defense_b: str, armor_value_b: str, dex_b: str, skill_reduction_b: str, material_modifier_b: str):
       results = com.combat(skill_use, offense_a, weapon_value_a, skill_a, ailment, material_modifier_a, defense_b, armor_value_b, dex_b, skill_reduction_b, material_modifier_b)
       await interaction.response.send_message (results)

@client.tree.command(name="calculate_combat_slash")
@app_commands.describe(offense_a = "50", weapon_value_a = "25", ailment = "poison", material_modifier_a = "1.0", defense_b = "15", dex_b = "10", armor_value_b = "25", material_modifier_b = "1.0")
async def calculate_combat(interaction: discord.Interaction, offense_a: str, weapon_value_a: str, ailment: str, material_modifier_a: str, defense_b: str, dex_b: str, armor_value_b: str, material_modifier_b: str):
       skill_use = "no"
       skill_a = "0"
       skill_reduction_b = "0"
       results = com.combat(skill_use, offense_a, weapon_value_a, skill_a, ailment, material_modifier_a, defense_b, armor_value_b, dex_b, skill_reduction_b, material_modifier_b)
       await interaction.response.send_message (results)

@client.tree.command(name="confirm_trade")
@app_commands.describe(character_name_a = "Kirito", item_to_trade_a = "herb", character_name_b = "Asuna", item_to_trade_b = "Bronze Ingot" )
async def confirm_trade(interaction: discord.Interaction, character_name_a: str, item_to_trade_a: str, character_name_b: str, item_to_trade_b: str):
       trade_completed = tra.accept_trade(character_name_a, item_to_trade_a, character_name_b, item_to_trade_b)
       allowed_roles = ['executive', 'co-owner', 'owner', 'moderator']
       if mat.is_allowed(interaction.user.roles, allowed_roles):
         if trade_completed == True:
           await interaction.response.send_message ('```The trade has been completed!```')
         else:
           await interaction.response.send_message ('```There seems to have been an issue with the trade.```')
       else:
           await interaction.response.send_message ('```You do not have permission to confirm trades.```')       

@client.tree.command(name="at_command", description="test")
@app_commands.describe()
async def at_command(interaction: discord.Interaction):
    moderator_roles = [role for role in interaction.guild.roles if role.permissions.manage_messages]

    moderator_mentions = ','.join([role.mention for role in moderator_roles])
    allowed_roles = ['Moderator', 'Co-Owner']
    print(moderator_mentions)
    if not mat.is_allowed(interaction.user.roles, allowed_roles):
        await interaction.response.send_message(f'Invalid roles')
    else: 
        await interaction.response.send_message(f'{moderator_mentions} Please check the character stats')
  
#Run the client.
client.run("")