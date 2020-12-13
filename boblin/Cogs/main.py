import discord
from discord.ext import commands
from discord.utils import get
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
import classyjson as cj
import arrow
import random
from random import randint
import sqlite3
from sqlite3 import Error
conn = sqlite3.connect(r'C:\Users\trey\Documents\atom projects\Bots\Boblin-the-Goblin\boblin\data\boblindata.db')
c = conn.cursor()
bot = commands.Bot(command_prefix="d!")

class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='race')
    async def race(self, ctx, *, race = 'All'):
        race = race.lower()
        if race == 'all':

            embeds = [discord.Embed(title="Dragonborn", color=discord.Color.green(), description="d!race dragonborn"),
            discord.Embed(title="Dwarf", color=discord.Color.green(), description="d!race dwarf"),
            discord.Embed(title='Elf', color=discord.Color.green(), description="d!race elf"),
            discord.Embed(title='Gnome', color=discord.Color.green(), description="d!race gnome"),
            discord.Embed(title='Half-Elf', color=discord.Color.green(), description="d!race half-elf"),
            discord.Embed(title='Halfling', color=discord.Color.green(), description="d!race halfling"),
            discord.Embed(title='Half-Orc', color=discord.Color.green(), description="d!race half-orc"),
            discord.Embed(title='Human', color=discord.Color.green(), description="d!race human"),
            discord.Embed(title='Tiefling', color=discord.Color.green(), description="d!race tiefling"),
            discord.Embed(title='Leonin', color=discord.Color.green(), description="d!race leonin"),
            discord.Embed(title='Satyr', color=discord.Color.green(), description="d!race satyr"),
            discord.Embed(title='Aarakocra', color=discord.Color.green(), description="d!race aarakocra"),
            discord.Embed(title='Genasi', color=discord.Color.green(), description="d!race genasi"),
            discord.Embed(title='Goliath', color=discord.Color.green(), description="d!race goliath"),
            discord.Embed(title='Aasimar', color=discord.Color.green(), description="d!race aasimar"),
            discord.Embed(title='Bugbear', color=discord.Color.green(), description="d!race bugbear"),
            discord.Embed(title='Firbolg', color=discord.Color.green(), description="d!race firbolg"),
            discord.Embed(title='Goblin', color=discord.Color.green(), description="d!race goblin"),
            discord.Embed(title='Hobgoblin', color=discord.Color.green(), description="d!race hobgoblin"),
            discord.Embed(title='Kenku', color=discord.Color.green(), description="d!race kenku"),
            discord.Embed(title='Kobold', color=discord.Color.green(), description="d!race kobold"),
            discord.Embed(title='Lizardfolk', color=discord.Color.green(), description="d!race lizardfolk"),
            discord.Embed(title='Orc', color=discord.Color.green(), description="d!race orc"),
            discord.Embed(title='Tabaxi', color=discord.Color.green(), description="d!race tabaxi"),
            discord.Embed(title='Triton', color=discord.Color.green(), description="d!race triton"),
            discord.Embed(title='Yuan-ti Pureblood', color=discord.Color.green(), description="d!race yuan-ti pureblood"),
            discord.Embed(title='Changeling', color=discord.Color.green(), description="d!race changeling"),
            discord.Embed(title='Kalashtar', color=discord.Color.green(), description="d!race kalashtar"),
            discord.Embed(title='Shifter', color=discord.Color.green(), description="d!race shifter"),
            discord.Embed(title='Warforged', color=discord.Color.green(), description="d!race warforged"),
            discord.Embed(title='Gith', color=discord.Color.green(), description="d!race gith"),
            discord.Embed(title='Centaur', color=discord.Color.green(), description="d!race centaur"),
            discord.Embed(title='Loxodon', color=discord.Color.green(), description="d!race loxodon"),
            discord.Embed(title='Minotaur', color=discord.Color.green(), description="d!race minotaur"),
            discord.Embed(title='Simic Hybrid', color=discord.Color.green(), description="d!race simic hybrid"),
            discord.Embed(title='Vedalken', color=discord.Color.green(), description="d!race vedalken"),
            discord.Embed(title='Verdan', color=discord.Color.green(), description="d!race verdan")]

            paginator = BotEmbedPaginator(ctx, embeds)
            await paginator.run()

        elif race == "dragonborn" or race == "dwarf" or race == "elf" or race == "gnome" or race == "half-elf" or race == "halfling" or race == "half-orc" or race == "human" or race == "tiefling" or race == "leonin" or race == "satyr" or race == "aarakocra" or race == "genasi" or race == "goliath" or race == "aasimar" or race == "bugbear" or race == "firbolg" or race == "goblin" or race == "hobgoblin" or race == "kenku" or race == "kobold" or race == "lizardfolk" or race == "orc" or race == "tabaxi" or race == "triton" or race == "yuan-ti pureblood" or race == "changeling" or race == "kalashtar" or race == "shifter" or race == "warforged" or race == "gith" or race == "centaur" or race == "loxodon" or race == "minotaur" or race == "simic hybrid" or race == "vedalken" or race == "verdan" or race == "locathath" or race == "grung":
            with open("data/races.json") as racez:
                races = cj.load(racez)

                embed=discord.Embed(color=discord.Color.green())

                temp = []
                for k, v in races[race].items():
                    temp.append(str(k + ': ' + v))

                val = '\n'.join(temp)

                for key in races.items():
                    embed.add_field(name=race, value=val)
                    break

                await ctx.send(embed=embed)

        elif race == 'game':
            await ctx.send(embed=discord.Embed(color=discord.Color.green(), description='YOU JUST LOST THE GAME'))


    @commands.command(name='class')
    async def classes(self, ctx, *, classes = 'All'):
        classes = classes.lower()
        if classes == 'all':
            embeds = [
            discord.Embed(title='Barbarian', color=discord.Color.green(), description='d!class barbarian'),
            discord.Embed(title='Bard', color=discord.Color.green(), description='d!class bard'),
            discord.Embed(title='Cleric', color=discord.Color.green(), description='d!class cleric'),
            discord.Embed(title='Druid', color=discord.Color.green(), description='d!class druid'),
            discord.Embed(title='Fighter', color=discord.Color.green(), description='d!class fighter'),
            discord.Embed(title='Monk', color=discord.Color.green(), description='d!class monk'),
            discord.Embed(title='Paladin', color=discord.Color.green(), description='d!class paladin'),
            discord.Embed(title='Ranger', color=discord.Color.green(), description='d!class ranger'),
            discord.Embed(title='Rogue', color=discord.Color.green(), description='d!class rogue'),
            discord.Embed(title='Sorcerer', color=discord.Color.green(), description='d!class sorcerer'),
            discord.Embed(title='Warlock', color=discord.Color.green(), description='d!class warlock'),
            discord.Embed(title='Wizard', color=discord.Color.green(), description='d!class wizard'),
            discord.Embed(title='Artificer', color=discord.Color.green(), description='d!class artificer'),]

            paginator = BotEmbedPaginator(ctx, embeds)
            await paginator.run()

        elif classes == 'barbarian' or classes == 'bard' or classes == 'cleric' or classes == 'druid' or classes == 'fighter' or classes == 'monk' or classes == 'paladin' or classes == 'ranger' or classes == 'rogue' or classes == 'sorcerer' or classes == 'warlock' or classes == 'wizard' or classes == 'artificer':
            with open('data/classes.json') as classez:
                classess = cj.load(classez)

                embed=discord.Embed(color=discord.Color.green())

                temp = []
                for k, v in classess[classes].items():
                    temp.append(str(k + ': ' + v))

                val = '\n'.join(temp)

                for key in classess.items():
                    embed.add_field(name=classes, value=val)
                    break

                await ctx.send(embed=embed)


    @commands.command(name='invite')
    async def invite(self, ctx):
        invembed = discord.Embed(color=discord.Color.green(), description='[Click Here!](https://discord.com/api/oauth2/authorize?client_id=778773013352546354&permissions=1544027201&scope=bot)')

        invembed.set_author(name='Invite Boblin to your server!')

        invembed.set_footer(text='Boblin the Goblin#4756')

        await ctx.send(embed=invembed)

    @commands.command(name='ping', aliases=["latency", "pong"])
    async def ping(self, ctx):

        pong = round(self.bot.latency * 1000, 2)

        embed = discord.Embed(color=discord.Color.green(), description=f'`Current ping: {pong} ms`')

        embed.set_author(name="Pong!")

        embed.set_footer(text='Boblin the Goblin#4746')

        await ctx.send(embed=embed)


    @commands.command(name='roll',help='Rolls dice',pass_context = True)
    async def roll(self,ctx,numofdice_d_numofsides=None):
        if numofdice_d_numofsides is None:
            await ctx.send(embed=discord.Embed(color=discord.Color.green(), description='You are missing arguments: `number of dice`, `number of sides`!'))
        else:
            rolling = []

            try:
                for x in range(int(numofdice_d_numofsides.split('d')[0])):
                    rolling.append(randint(1,int(numofdice_d_numofsides.split('d')[1])))
                await  ctx.send(embed=discord.Embed(color=discord.Color.green(), description=f'You rolled {", ".join(str(x) for x in rolling)} which has a total'f' of {sum(rolling)}'))
            except IndexError as err:
                await ctx.send(embed=discord.Embed(color=discord.Color.green(), description=f'Your argument must be put together (for example: `3d20` as opposed to `3 d20`)'))


    @commands.command(name='say')
    async def say(selfsay, ctx, *,something,pass_context=True):
        if something is None:
            await ctx.send(embed=discord.Embed(color=discord.Color.green(), description="You need to enter something for me to say!"))
            return

        await ctx.send(f"{something}")
        await discord.Message.delete(ctx.message)


def setup(bot):
    bot.add_cog(main(bot))
