import random
import asyncio
from functools import partial

class Commands():
    def __init__(self, bot):
        self.bot = bot
        
        self.command_dict = {
        "hello": self.hello,
        "say": self.say,
        "roll": self.roll,
        "github": self.github,
        "cock": self.cock,
        "ip": self.ip,
        "help": self.help,
        "reverse": self.reverse,
        "capslock": self.capslock,
        "lowercase": self.lowercase,
        "repeat": self.repeat,
        "shuffle": self.shuffle
        }

        self.construct_help()
        loop = asyncio.get_event_loop()

    def construct_help(self):
        self.help_msg = ""
        for key in self.command_dict:
            if not key[0] == "_":
                self.help_msg += f"k!{key}: {self.command_dict[key].__doc__}\n"
        self.help_msg = self.help_msg[:-1]
        
    async def nothing(self, msg, args=None):
        pass

    async def help(self, msg, args=None):
        """Sends this message."""
        if args == []:
            await self.bot.reply_to(msg, self.help_msg)
        else:
            try:
                await self.bot.reply_to(msg, self.command_dict[args[0]].__doc__)
            except KeyError:
                await self.bot.reply_to(msg, "Invalid command.")
        
    async def hello(self, msg, args=None):
        """Says hello."""
        await self.bot.reply_to(msg, f"Hello, {msg.from_user.first_name}!")

    async def say(self, msg, args=None):
        """Usage: k!say <sentence> | Repeats what you say."""
        output = ' '.join(args)
        await self.bot.send_message(msg.chat.id, output)

    async def roll(self, msg, args=None):
        """Usage: k!roll <number|defaults to 6> | Rolls a dice from 1 to <number>."""
        try:
            number = random.randint(1, int(args[0]))
        except:
            number = random.randint(1, 6)
        await self.bot.send_message(msg.chat.id, f"{msg.from_user.first_name} rolls {number}!")

    async def cock(self, msg, args=None):
        """8=========D"""
        await self.bot.reply_to(msg, "8" + random.randint(0,15)*"=" + "D")

    async def github(self, msg, args=None):
        """Sends the bot's GitHub repository. Join us in the development!"""
        await self.bot.reply_to(msg, "https://github.com/viraxor/kavoctisajak")

    async def ip(self, msg, args=None):
        """Sends a random IP address."""
        await self.bot.reply_to(msg, f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}")

    async def reverse(self, msg, args=None):
        """Usage: k!reverse <sentence> | Reverses the text."""
        if args != []:
            await self.bot.reply_to(msg, ' '.join(args)[::-1])
        elif msg.reply_to_message:
            await self.bot.reply_to(msg, msg.reply_to_message.text[::-1])
        else:
            await self.bot.reply_to(msg, "You need to pass an argument/reply to a message.")

    async def capslock(self, msg, args=None):
        """Usage: k!capslock <sentence> | Swaps the case of the text."""
        if args != []:
            await self.bot.reply_to(msg, ' '.join(args).swapcase())
        elif msg.reply_to_message:
            await self.bot.reply_to(msg, msg.reply_to_message.text.swapcase())
        else:
            await self.bot.reply_to(msg, "You need to pass an argument/reply to a message.")

    async def lowercase(self, msg, args=None):
        """Usage: k!lowercase <sentence> | Turns the sentence into lowercase."""
        if args != []:
            await self.bot.reply_to(msg, ' '.join(args).lower())
        elif msg.reply_to_message:
            await self.bot.reply_to(msg, msg.reply_to_message.text.lower())
        else:
            await self.bot.reply_to(msg, "You need to pass an argument/reply to a message.")

    async def repeat(self, msg, args=None):
        """Usage: k!repeat <number> <sentence> | Repeats a sentence <number> times."""
        if len(args) >= 1:
            await self.bot.reply_to(msg, ' '.join(args[1:]) * int(args[0]))
        elif msg.reply_to_message:
            await self.bot.reply_to(msg, msg.reply_to_message.text * int(args[0]))
        else:
            await self.bot.reply_to(msg, "You need to pass an argument/reply to a message.")

    def shuffle_r(self, text):
        text = list(text)
        random.shuffle(text)
        return ''.join(text)

    async def shuffle(self, msg, args=None):
        """Usage: k!shuffle <sentence> | Shuffles text."""
        if args != []:
            text = ' '.join(args)
            fn = partial(self.shuffle_r, text)
            output = await self.loop.run_in_executor(None, fn)
            await self.bot.reply_to(msg, output)
        elif msg.reply_to_message:
            text = msg.reply_to_message.text
            fn = partial(self.shuffle_r, text)
            output = await self.loop.run_in_executor(None, fn)
            await self.bot.reply_to(msg, output)
        else:
            await self.bot.reply_to(msg, "You need to pass an argument/reply to a message.")
            
    async def process(self, msg):
        args = msg.text[2:].split(" ")
        
        try:
            function = self.command_dict[args[0]]
        except KeyError:
            await self.bot.reply_to(msg, "Invalid command.")
        else:
            try:
                await function(msg, args[1:])
            except Exception as exc:
                await self.bot.reply_to(msg, f"{type(exc)}: {exc}")
