import cmd
from gettext import install
import os
import hikari
import lightbulb

bot = lightbulb.BotApp
os.environ["Token"]
default_enabled_guilds=int(os.environ["Default_Guild_ID"]),
help_slash_command=True,
intents=hikari.Intents.ALL,


@bot.command()
@lightbulb.command('!Inspect', 'Player inspects item within range or posession.')
@lightbulb.implements(lightbulb.SlashCommand)
async def Inspect(ctx):
    await ctx.respond()

    bot.run()
    


           