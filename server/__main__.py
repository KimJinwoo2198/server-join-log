import discord
from urllib import request
from discord.ext import commands

from server import TOKEN, commandInt

class serverjoinbot(commands.AutoShardedBot) :
    def __init__ (self) :
        super().__init__ (
            command_prefix=commandInt,
            intents=intents
        )
        self.remove_command("help")
    async def on_guild_join(self, guild):
        await bot.get_channel(int(938656148423344178)).send(f'새로운 서버에 추가됨 (현재 **{len(bot.guilds)}**개의 서버)')

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
bot = serverjoinbot()
bot.run(TOKEN)