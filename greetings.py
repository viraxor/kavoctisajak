from discord.ext import commands
import discord

def setup(bot):
    bot.add_cog(Greetings(bot))
    
class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="hello")
    async def hello(self, ctx):
        await ctx.send(f"Hello, {ctx.author.mention}!")
        
    @commands.command(name="goodbye", aliases=["bye"])
    async def goodbye(self, ctx):
        await ctx.send(f"Goodbye, {ctx.author.mention}!")