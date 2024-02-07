from discord.ext import commands
import discord
import random

async def setup(bot):
    await bot.add_cog(Misc(bot))

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="say")
    async def say(self, ctx, *, arg):
        await ctx.send(arg)

    @commands.command(name="ask")
    async def ask(self, ctx):
        ask = ["Yes","Yep","I think so","Probably","Maybe","I don't know","Probably Not","I don't think so","Nope","No"]
        await ctx.send(f"{random.choice(ask)}")
