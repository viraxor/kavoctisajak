from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
import os

import asyncio
import aiohttp
import importlib

import commandlib
import base64

load_dotenv("./.env")
token = os.getenv("TOKEN")

bot = AsyncTeleBot(token)
commands = commandlib.Commands(bot)

owners = [6632670569, 6786212935] # change the ids with yours if you're making your bot

@bot.message_handler(regexp="^k!")
async def command_handler(msg):
    await commands.process(msg)
    
@bot.message_handler(commands=["reload"])
async def reload(msg):
    global commands
    
    if msg.from_user.id in owners:
        session = aiohttp.ClientSession()
        r1 = await session.get(f"https://api.github.com/repos/viraxor/kavoctisajak/contents/commandlib.py")
        resp = eval(await r1.content.read())
        content = base64.b64decode(resp["content"])
        await session.close()
        
        await bot.send_message(msg.chat.id, "saving commands")
        with open(f"./commandlib.py", "wb") as f:
            f.write(content)

        old_commands = commands
        try:
            importlib.reload(commandlib)
            commands = commandlib.Commands(bot)
        except Exception as exc:
            commands = old_commands
            await self.bot.reply_to(msg, f"{type(exc)}: {exc}")
        else:
            await bot.send_message(msg.chat.id, "success")

@bot.message_handler(commands=["help", "start"])
async def welcome(msg):
    await bot.reply_to(msg, "The prefix of the bot is ``k!``")
    
asyncio.run(bot.polling())
