import discord
from discord.ext import commands, tasks

from dotenv import load_dotenv
from os import getenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="k!", intents=intents)

@bot.command(name="reload", hidden=True)
async def reload(ctx, name: str):
    await bot.reload_extension(f"cogs.{name}")
    await ctx.send("reloaded")

@bot.command(name="say")
async def say(ctx, *, arg):
    await ctx.send(arg)

load_dotenv("./.env")
token = getenv("TOKEN")

@bot.event
async def on_ready():
    await bot.load_extension("cogs.greetings")
    
bot.run(token)
