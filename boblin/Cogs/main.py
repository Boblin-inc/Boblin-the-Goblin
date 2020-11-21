import discord
from discord.ext import commands
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
import classyjson as cj

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


    @commands.command(name='invite')
    async def invite(self, ctx):
        invembed = discord.Embed(color=discord.Color.green(), description='[Click Here!](https://discord.com/api/oauth2/authorize?client_id=778773013352546354&permissions=1544027201&scope=bot)')

        invembed.set_author(name='Invite Boblin to your server!')

        invembed.set_footer(text='Boblin the Goblin#4746')

        await ctx.send(embed=invembed)




def setup(bot):
    bot.add_cog(main(bot))
