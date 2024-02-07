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
        response = await session.get(f"https://raw.githubusercontent.com/viraxor/kavoctisajak/main/cogs/{name}.py?token=GHSAT0AAAAAACN54HLO672SEOBSP5VVDJTUZOD7EFQ")
        content = await response.content.read()
        with open(f"./cogs/{name.py}", "w") as f:
            f.write(content)
            
        await bot.reload_extension(f"cogs.{name}")
        await ctx.send("reloaded")

load_dotenv("./.env")
token = getenv("TOKEN")

@bot.event
async def on_ready():
    await bot.load_extension("cogs.greetings")
    await bot.load_extension("cogs.misc")
    
bot.run(token)
