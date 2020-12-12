from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
from discord.ext import commands
from discord.utils import get
from sqlite3 import Error
import classyjson as cj
import discord
import sqlite3

conn = sqlite3.connect(r'C:\Users\trey\Documents\atom projects\Bots\Boblin-the-Goblin\boblin\data\boblindata.db')
c = conn.cursor()
bot = commands.Bot(command_prefix="d!")

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='help')
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            help = discord.Embed(color=discord.Color.green())

            help.set_author(name='Boblin the Goblin - Help')

            help.add_field(name='D&D', value=f'D&D related commands\n`{ctx.prefix}help d&d`')
            help.add_field(name='Other Stuff', value=f'Non-D&D related commands\n`{ctx.prefix}help other`')
            help.add_field(name='More Coming Soon!', value='Boblin is still in development, so more commands will be added in the future!')

            help.set_footer(text='Boblin the Goblin#4756')

            await ctx.send(embed=help)


    @help.command(name='d&d', aliases=['dnd'])
    async def help_dnd(self, ctx):
        dndhelp = discord.Embed(color=discord.Color.green())

        dndhelp.set_author(name='Boblin the Goblin - D&D commands')

        dndhelp.add_field(name='race', value=f'Get info on a specified race\n`{ctx.prefix}race <race name (optional)>`')
        dndhelp.add_field(name='roll', value=f'roll the amount and type of dice specifiedn\n`{ctx.prefix}roll <3d20 (example)>`')
        dndhelp.add_field(name='More Coming Soon!', value='Boblin is still in development, so more commands will be added in the future!')

        dndhelp.set_footer(text='Boblin the Goblin#4756')

        await ctx.send(embed=dndhelp)


    @help.command(name='other')
    async def help_other(self, ctx):
        otherhelp = discord.Embed(color=discord.Color.green())

        otherhelp.set_author(name='Boblin the Goblin - Other commands')

        otherhelp.add_field(name='invite', value=f'Invite Boblin to your server\n`{ctx.prefix}invite`')
        otherhelp.add_field(name='ping', value=f'Show the latency of the bot (ms)\n`{ctx.prefix}ping`')
        otherhelp.add_field(name='uptime', value=f'Check how long the bot has been online for\n`{ctx.prefix}uptime`')
        otherhelp.add_field(name='More Coming Soon!', value='Boblin is still in development, so more commands will be added in the future!')

        otherhelp.set_footer(text='Boblin the Goblin#4756')

        await ctx.send(embed=otherhelp)


    @commands.command(name='ownerhelp')
    @commands.is_owner()
    async def ownerhelp(self, ctx):
        owner = discord.Embed(color=discord.Color.green())

        owner.set_author(name='Boblin the Goblin - Owner commands')

        owner.add_field(name='load', value=f'Load specified cog\n`{ctx.prefix}load <cog (optional>)`')
        owner.add_field(name='unload', value=f'Unload specified cog\n`{ctx.prefix}unload <cog (optional)>.`')
        owner.add_field(name='\uFEFF', value='\uFEFF')
        owner.add_field(name='reload', value=f'Reload specified cog\n`{ctx.prefix}reload <cog (optional)>`')
        owner.add_field(name='gitpull', value=f'Pulls most recent version from GitHub\n`{ctx.prefix}gitpull`')
        owner.add_field(name='\uFEFF', value='\uFEFF')
        owner.add_field(name='eval', value=f'Executes the inputted code\n`{ctx.prefix}eval <code>`')

        owner.set_footer(text='Boblin the Goblin#4756')

        await ctx.send(embed=owner)


def setup(bot):
    bot.add_cog(help(bot))
