import discord
from discord.ext import commands
import another
import ffmpeg

cogs = [another]

client = commands.Bot(command_prefix = "!!", intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

token = ":)"
client.run(token)