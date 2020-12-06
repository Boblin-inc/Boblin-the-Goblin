import discord
from discord.ext import commands
import classyjson as cj
import sqlite3
from sqlite3 import Error

conn = sqlite3.connect(r'C:\Users\trey\Documents\atom projects\Bots\Boblin-the-Goblin\boblin\data\boblindata.db')
c = conn.cursor()

def get_prefix(client, message):

    prefixes = ['d!']

    if not message.guild:
        prefixes = ['d!']
    return commands.when_mentioned_or(*prefixes)(client, message)

bot = commands.Bot(command_prefix=get_prefix)

with open('data/keys.json', 'r') as keys_file:
    bot.key = cj.load(keys_file)


bot.load_extension("Cogs.Events")
bot.load_extension("Cogs.main")
bot.load_extension("Cogs.owner")
bot.load_extension("Cogs.uptime")
bot.run(bot.key.discord_token)
