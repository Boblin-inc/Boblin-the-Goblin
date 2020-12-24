import discord
from discord.ext import commands
from discord.utils import get
import arrow
import asyncio

bot = commands.Bot(command_prefix='!k ')
class uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.g = arrow.utcnow()

    @commands.command(name="uptime", aliases=['up'])
    async def get_uptime(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(1)
            p = arrow.utcnow()
            diff = (p - self.g)
            days = diff.days
            hours = int(diff.seconds / 3600)
            minutes = int(diff.seconds / 60) % 60
            if days == 1:
                dd = "day"
            else:
                dd = "days"
            if hours == 1:
                hh = "hour"
            else:
                hh = "hours"
            if minutes == 1:
                mm = "minute"
            else:
                mm = "minutes"
            embed = discord.Embed(color=discord.Color.green(),
                                               description="Boblin has been online for " + str(days) + " " + dd + ", " + str(
                                                   hours) + " " + hh + ", and " + str(minutes) + " " + mm + ".")
            embed.set_author(name="Uptime")
            embed.set_footer(text="Boblin the Goblin#4756")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(uptime(bot))
