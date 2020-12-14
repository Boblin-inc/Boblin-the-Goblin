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
        dndhelp.add_field(name='class', value=f'Get info on a specified class\n`{ctx.prefix}class <class name (optional)>`')
        dndhelp.add_field(name='roll', value=f'roll the amount and type of dice specified\n`{ctx.prefix}roll <3d20 (example)>`')
        dndhelp.add_field(name='More Coming Soon!', value='Boblin is still in development, so more commands will be added in the future!')

        dndhelp.set_footer(text='Boblin the Goblin#4756')

        await ctx.send(embed=dndhelp)


    @help.command(name='other')
    async def help_other(self, ctx):
        otherhelp = discord.Embed(color=discord.Color.green())

        otherhelp.set_author(name='Boblin the Goblin - Other commands')

        otherhelp.add_field(name='invite', value=f'Invite Boblin to your server\n`{ctx.prefix}invite`')
        otherhelp.add_field(name='ping', value=f'Show the latency (response time) of the bot (ms)\n`{ctx.prefix}ping`')
        otherhelp.add_field(name='uptime', value=f'Check how long Boblin has been online for\n`{ctx.prefix}uptime`')
        otherhelp.add_field(name='say', value=f'Make the bot say something\n`{ctx.prefix}say <message>`')
        otherhelp.add_field(name='More Coming Soon!', value='Boblin is still in development, so more commands will be added in the future!')

        otherhelp.set_footer(text='Boblin the Goblin#4756')

        await ctx.send(embed=otherhelp)


    @help.command(name='all')
    async def help_all(self, ctx):

        embeds = [discord.Embed(title='Race', color=discord.Color.green(), description='Get info on a specified race'),
        discord.Embed(title='Class', color=discord.Color.green(), description='Get info on a specified class'),
        discord.Embed(title='Roll', color=discord.Color.green(), description='roll the amount and type of dice specified'),
        discord.Embed(title='Invite', color=discord.Color.green(), description='Invite Boblin to your server'),
        discord.Embed(title='Ping', color=discord.Color.green(), description='Show the latency (response time) of the bot (ms)'),
        discord.Embed(title='Uptime', color=discord.Color.green(), description='Check how long Boblin has been online for'),
        discord.Embed(title='Say', color=discord.Color.green(), description='Make the bot say something'),
        discord.Embed(title='More Coming Soon!', color=discord.Color.green(), description='Boblin is still in development, so more commands will be added in the future!')]

        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()


    @commands.command(name='ownerhelp')
    @commands.is_owner()
    async def ownerhelp(self, ctx):
        owner = discord.Embed(color=discord.Color.green())

        owner.set_author(name='Boblin the Goblin - Owner commands')

        owner.add_field(name='load', value=f'Load specified cog\n`{ctx.prefix}load <cog (optional>)`')
        owner.add_field(name='unload', value=f'Unload specified cog\n`{ctx.prefix}unload <cog (optional)>.`')
        owner.add_field(name='reload', value=f'Reload specified cog\n`{ctx.prefix}reload <cog (optional)>`')
        owner.add_field(name='gitpull', value=f'Pulls most recent version from GitHub\n`{ctx.prefix}gitpull`')
        owner.add_field(name='eval', value=f'Executes the inputted code\n`{ctx.prefix}eval <code>`')
        owner.add_field(name='aeval', value=f'Awaits and executes inputted code\n`{ctx.prefix}aeval <code>`')

        owner.set_footer(text='Boblin the Goblin#4756')

        await ctx.send(embed=owner)





def setup(bot):
    bot.add_cog(help(bot))
