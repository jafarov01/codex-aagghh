import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
from discord.utils import get

#----------------------------------

intentStr = discord.Intents.all()
intentStr.members = True

#----------------------------------


#-----------------------------------
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
#-----------------------------------

client = commands.Bot(command_prefix = '!', intents=intentStr)

@client.event
async def on_ready():
    print("The bot is ready!")
    print("--------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am the AAGGHH Bot.")

@client.command()
async def goodbye(ctx):
    await ctx.send("Goodbye!")

@client.event
async def on_member_join(member):
    channel = client.get_channel(987651346079576117)
    await channel.send("Welcome to the channel!")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(987651346079576117)
    await channel.send("GoodBye!")

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = discord.FFmpegPCMAudio("aagghh.mp3")
        player = voice.play(source)
    else:
        await ctx.send("Not in a voice chat!")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Leaving...")
    else:
        await ctx.send("Not in a voice chat!")
    
#======================================================


#=========================================================

client.run(DISCORD_TOKEN)

