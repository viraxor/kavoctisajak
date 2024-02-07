import discord
from discord.ext import commands, tasks

from dotenv import load_dotenv
from os import getenv

import aiohttp

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="k!", intents=intents)

owners = [1172378388212760587, 523887995850326017]

@bot.command(name="reload", hidden=True)
async def reload(ctx, name: str):
    if ctx.author.id in owners:
        session = aiohttp.ClientSession()
        r1 = await session.get(f"https://github.com/viraxor/kavoctisajak/raw/main/cogs/{name}.py")
        content = await r1.content.read()
        await session.close()
        await ctx.send("saving cog")
        with open(f"./cogs/{name}.py", "wb") as f:
            f.write(content)
        
        try:
            await bot.reload_extension(f"cogs.{name}")
        except commands.errors.ExtensionNotLoaded:
            await bot.load_extension(f"cogs.{name}")
        await ctx.send("reloaded")

load_dotenv("./.env")
token = getenv("TOKEN")

@bot.event
async def on_ready():
    await bot.load_extension("cogs.greetings")
    await bot.load_extension("cogs.misc")
    
bot.run(token)
