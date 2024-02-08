from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
import os

import asyncio
import aiohttp
import importlib

import commandlib

load_dotenv("./.env")
token = os.getenv("TOKEN")

bot = AsyncTeleBot(token)
commands = commandlib.Commands(bot)

owners = [6632670569, 6786212935]

@bot.message_handler(regexp="^k!")
async def command_handler(msg):
    await commands.process(msg)
    
@bot.message_handler(regexp="^k!reload")
async def reload(msg):
    if msg.from_user.id in owners:
        session = aiohttp.ClientSession()
        r1 = await session.get(f"https://github.com/viraxor/kavoctisajak/raw/main/commandlib.py")
        content = await r1.content.read()
        await session.close()
        
        await bot.send_message(msg.chat.id, "saving commands")
        with open(f"./commandlib.py", "wb") as f:
            f.write(content)
        
        importlib.reload(commandlib)
        commands = commandlib.Commands(bot)
        await bot.send_message(msg.chat.id, "success")

@bot.message_handler(commands=["help", "start"])
async def welcome(msg):
    await bot.reply_to(msg, "The prefix of the bot is ``k!``")
    
asyncio.run(bot.polling())