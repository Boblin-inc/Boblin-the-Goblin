import discord
from discord.ext import commands
import classyjson as cj
import sqlite3
from sqlite3 import Error

conn = sqlite3.connect(r'C:\Users\trey\Documents\atom projects\Bots\Boblin-the-Goblin\boblin\data\boblindata.db')
c = conn.cursor()

#todo
#campaign ideas
#classes




bot = commands.Bot(command_prefix='d!', help_command=None)



with open('data/keys.json', 'r') as keys_file:
    bot.key = cj.load(keys_file)


bot.load_extension("Cogs.events")
bot.load_extension("Cogs.main")
bot.load_extension("Cogs.owner")
bot.load_extension("Cogs.uptime")
bot.load_extension("Cogs.help")
bot.run(bot.key.discord_token)
