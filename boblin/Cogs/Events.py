import discord
from discord.ext import commands
from discord.utils import get
import sqlite3
from sqlite3 import Error
conn = sqlite3.connect(r'C:\Users\trey\Documents\atom projects\Bots\Boblin-the-Goblin\boblin\data\boblindata.db')
c = conn.cursor()

bot = commands.Bot(command_prefix="d!")

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Game(name="D&D 5e", type=3)
        await self.bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)






def setup(bot):
    bot.add_cog(Events(bot))
