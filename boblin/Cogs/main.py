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
import asyncio
conn = sqlite3.connect(r'C:\Users\trey\Documents\atom projects\Bots\Boblin-the-Goblin\boblin\data\boblindata.db')
c = conn.cursor()
bot = commands.Bot(command_prefix="d!")




class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='race')
    async def race(self, ctx, *, race = 'All'):
        race = race.lower()
        embs = self.bot.get_cog('embeds')
        if race == 'all':

            embeds = embs.races

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
        embs = self.bot.get_cog('embeds')
        classes = classes.lower()
        if classes == 'all':

            embeds = embs.classes

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

    @commands.command(name='spells')
    async def spells(self, ctx, *, spells='All'):
        spells = spells.lower()
        embs = self.bot.get_cog('embeds')
        paginator = BotEmbedPaginator(ctx, embs.allspells)
        await paginator.run()
        #finish later




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

        embed.set_footer(text='Boblin the Goblin#4756')

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

    @commands.command(name='info')
    async def info(self, ctx):
        embed=discord.Embed(color=discord.Color.green())
        embed.set_author(name='Bot Info')
        embed.set_footer(text='Created by Emerald#8617 | Boblin the Goblin#4756')

        embed.add_field(name='Command Prefix', value='d!')
        embed.add_field(name='Total Guilds', value=f'{len(self.bot.guilds)}')
        embed.add_field(name='Total Users', value=f'{len(self.bot.users)}')
        embed.add_field(name='GitHub Repository', value='[**Click Here**](https://github.com/Boblin-inc/Boblin-the-Goblin)')
        embed.add_field(name='top.gg page', value='[**Click Here**](https://top.gg/bot/778773013352546354)')

        await ctx.send(embed=embed)

    @commands.command(name='vote')
    async def vote(self, ctx):
        vote = discord.Embed(color=discord.Color.green())

        vote.set_author(name='Vote for Boblin!')
        vote.add_field(name='Vote for Boblin on top.gg to support the bot!', value='[**Click Here!**](https://top.gg/bot/778773013352546354/vote)')
        vote.set_footer(text='Created by Emerald#8617 | Boblin the Goblin#4756')

        await ctx.send(embed=vote)






def setup(bot):
    bot.add_cog(main(bot))
