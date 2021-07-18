import os
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio, PCMVolumeTransformer
import time 
import random
import pafy
import asyncio
import urllib3
import re

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
client = commands.Bot(command_prefix = "nica!")
frases = "frases.txt"
token = os.environ.get('NicaBotKey') # To run bot (command at the bottom)

print(token)

@client.command()
async def getNumber(ctx):
    num_lines = sum(1 for line in open('woop.txt'))
    await ctx.send(num_lines)

@client.command()
async def todo(ctx):
    if ctx.author.id == 194152947808993280:
        phraseList = open(frases, "r")
        readPhraseList = phraseList.readlines()
        await ctx.send(readPhraseList)

@client.command() # add phrase to element.txt
async def agregar(ctx, *arg1):
    addSpace = [word + ' ' for word in arg1]
    stringPhrase = ''.join(addSpace)
    openAppendTXT = open(frases, "a") # if not in directory it will create file 
    openAppendTXT.write(stringPhrase + "\n")
    await ctx.send('" '+stringPhrase+'" ha sido agregado!') # "phrase" has been added!

@client.command()
async def frase(ctx):
    try:
        randomPhrases = open(frases, "r")
        listFile = randomPhrases.readlines()

        rPhrase = random.choice(listFile) # chooses random element from element.txt
        await ctx.send(rPhrase)
    except IndexError:
        await ctx.send("No hay frases disponibles...")

@client.command() 
async def ping(ctx): 
    ctx.send("Pong!")
    

@client.command()
async def logout(ctx):
    print("Desconectado >:O")
    if ctx.author.id == 194152947808993280:
            await ctx.send("¡Desconectad@!")
            await ctx.bot.logout()
    elif ctx.author.id == 671180188301656075:
        await ctx.send("Esa onda Nica... :pensive:") 
    else:    
        await ctx.send("No. :(")

client.run(token)

