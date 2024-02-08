import discord
from discord.ext import commands
import random

async def setup(bot):
    await bot.add_cog(Text(bot))

class Text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="reverse")
    async def reverse(self, ctx, *, text):
        await ctx.send(text[::-1])
