class Commands():
    def __init__(self, bot):
        self.bot = bot
        
        self.command_dict = {
        "hello": self.hello,
        "reload": self.nothing,
        "say": self.say
        }
        
    async def nothing(self, msg):
        pass
        
    async def hello(self, msg):
        await self.bot.reply_to(msg, f"Hello, {msg.from_user.first_name}!")

    async def say(self, msg):
        args = msg.text[2:].split(" ")
        output = ' '.join(args[1:])
        await self.bot.reply_to(msg, msg.text)
        
    async def process(self, msg):
        args = msg.text[2:].split(" ")
        await self.bot.reply_to(msg, f"{args}")
        
        try:
            function = self.command_dict[args[0]]
        except KeyError:
            await self.bot.reply_to(msg, "Invalid command.")
        else:
            await function(msg)
