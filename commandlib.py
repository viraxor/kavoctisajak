import random

class Commands():
    def __init__(self, bot):
        self.bot = bot
        
        self.command_dict = {
        "hello": self.hello,
        "reload": self.nothing,
        "say": self.say,
        "roll": self.roll,
        "github": self.github,
        "cock": self.cock,
        "dividebyzero": self.divide_by_zero
        }
        
    async def nothing(self, msg):
        pass

    async def divide_by_zero(self, msg):
        await self.bot.reply_to(msg, f"{1/0}")
        
    async def hello(self, msg):
        await self.bot.reply_to(msg, f"Hello, {msg.from_user.first_name}!")

    async def say(self, msg):
        args = msg.text[2:].split(" ")
        output = ' '.join(args[1:])
        await self.bot.send_message(msg.chat.id, output)

    async def roll(self, msg):
        args = msg.text[2:].split(" ")
        try:
            number = random.randint(1, int(args[1]))
        except:
            number = random.randint(1, 6)
        await self.bot.send_message(msg.chat.id, f"{msg.from_user.first_name} rolls {number}!")

    async def cock(self, msg):
        await self.bot.reply_to(msg, "8" + random.randint(0,15)*"=" + "D")

    async def github(self, msg):
        await self.bot.reply_to(msg, "https://github.com/viraxor/kavoctisajak")
        
    async def process(self, msg):
        args = msg.text[2:].split(" ")
        
        try:
            function = self.command_dict[args[0]]
        except KeyError:
            await self.bot.reply_to(msg, "Invalid command.")
        except Exception as exc:
            await self.bot.reply_to(msg, f"{exc}")
        else:
            await function(msg)
