import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='d!')

class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='load')
    @commands.is_owner()
    async def load_cog(self, ctx, cog = 'all'):
        cog = cog.lower()
        if cog == "all":
            await ctx.send(embed=discord.Embed(color=discord.Color.green(), description='Loaded all cogs'))
            self.bot.load_extension('Cogs.owner')
            self.bot.load_extension('Cogs.main')
            self.bot.load_extension('Cogs.Events')
        elif cog == "owner" or cog == "events" or "main":
            self.bot.load_extension('Cogs.' + cog)
            await ctx.send(embed=discord.Embed(color=discord.Color.green(), description=f'Loaded "Cogs.{cog}"'))


    @commands.command(name='unload')
    @commands.is_owner()
    async def unload_cog(self, ctx, cog = 'all'):
        cog = cog.lower()
        if cog == "all":
            await ctx.send(embed=discord.Embed(color=discord.Color.green(), description='Unloaded all cogs'))
            self.bot.unload_extension('Cogs.owner')
            self.bot.unload_extension('Cogs.main')
            self.bot.unload_extension('Cogs.Events')
        elif cog == "owner" or cog == "events" or "main":
            self.bot.unload_extension('Cogs.' + cog)
            await ctx.send(embed=discord.Embed(color=discord.Color.green(), description=f'Unloaded "Cogs.{cog}"'))


    @commands.command(name='reload')
    @commands.is_owner()
    async def reload_cog(self, ctx, cog = 'all'):
        cog = cog.lower()
        if cog == "all":
            await ctx.send(embed=discord.Embed(color=discord.Color.green(), description='Reloaded all cogs'))
            self.bot.reload_extension('Cogs.owner')
            self.bot.reload_extension('Cogs.main')
            self.bot.reload_extension('Cogs.Events')
        elif cog == "owner" or cog == "events" or "main":
            self.bot.reload_extension('Cogs.' + cog)
            await ctx.send(embed=discord.Embed(color=discord.Color.green(), description=f'Reloaded "Cogs.{cog}"'))

    @commands.command(name='gitpull')
    @commands.is_owner()
    async def git_pull(self, ctx):
        os.system('git pull > git_pull_log 2>&1')

        with open('git_pull_log', 'r') as log_file:
            await ctx.send(embed=discord.Embed(color=discord.Color.green(), description=f'```{log_file.read()}```'))

        os.remove('git_pull_log')







def setup(bot):
    bot.add_cog(owner(bot))
