import discord
from discord.ext import commands
from discord.utils import get
import sqlite3
from sqlite3 import Error
conn = sqlite3.connect(r'C:\Users\trey\Documents\atom projects\Bots\Boblin-the-Goblin\boblin\data\boblindata.db')
c = conn.cursor()


bot = commands.Bot(command_prefix="d!")

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        guildcount = len(self.bot.guilds)
        activity = discord.Game(name=f"D&D 5e in {guildcount} servers", type=3)
        await self.bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user.mentioned_in(message):
            embed = discord.Embed(color=discord.Color.green(), description="My prefix is `d!`, and you can get started by using`d!help`!")
            embed.set_author(name="Hey there, I'm Boblin!")
            embed.set_footer(text='Boblin the Goblin#4756')
            await message.channel.send(embed=embed)
            await bot.process_commands(message)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
         for channel in guild.text_channels:
            if 'general' in channel.name:
                embed = discord.Embed(color=discord.Color.green(), description='Use `d!help` to see a list of my commands!')

                embed.set_author(name="Hey there, I'm Boblin!")
                embed.set_footer(text='Boblin the Goblin#4756')

                await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(events(bot))
