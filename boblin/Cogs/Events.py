import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix="d!")

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Game(name="D&D 5e", type=3)
        await self.bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = get(member.guild.channels, name='join-leave')
        await channel.send(f'Sup {member.mention}, welcome to BoblinTown!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = get(member.guild.channels, name='join-leave')
        await channel.send(f'Thanks for visiting BoblinTown, {member.mention} ({member}), come again soon!')

def setup(bot):
    bot.add_cog(Events(bot))
