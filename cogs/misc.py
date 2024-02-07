from discord.ext import commands
import discord

async def setup(bot):
    await bot.add_cog(Misc(bot))

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="say")
    async def say(self, ctx, *, arg):
        await ctx.send(arg)
