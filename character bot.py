import discord
import os

print("Hello")
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('!Character'):
        await message.channel.send('Character!')
client.run("MTAwNjM4NTMzNDEwOTYyMjMzNA.GCL0zu.BQZnjK71yc6QpzXYGRWj1NzdQLAuvO1c_67OVg")