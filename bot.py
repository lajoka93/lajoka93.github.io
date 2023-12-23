import discord
import os
import requests
import json
from server import stay_alive
import urllib.request

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(command_prefix='<', intents=intents)

#@bot.command(pass_context = True)
#async def join(ctx):
#  if (ctx.author.voice):
 #   channel = ctx.mesage.author.voice.channel
  #  await channel.connect()
 # else:
  #  await ctx.send("You are not in a voice channel.")

#@bot.command(pass_context = True)
#async def leave(ctx):
 # if (ctx.voice_client):
  #  await ctx.guild.voice_client.disconnect()
   # await ctx.send("The bot left the voice channel")
  #else:
   # await ctx.send("The bot not in a voice channel.")

@bot.event
async def on_message(msg):
    if msg.content == "Hallo":
        a = str(msg.author)
        print(a)
        b = "Hallo " + a
        await msg.channel.send(b)

#    if msg.content == "Was waren die Hausaufgaben ?":
#       print(msg.content)
#      datei = open('homework.txt','r')
#     h = datei.read()
#    print(h)
#   await msg.channel.send(h)
#  datei.close

    if msg.content == "Was waren die Hausaufgaben ?":
        url = "https://raw.githubusercontent.com/lajoka93/lajoka93.github.io/main/homework.txt"
        response = urllib.request.urlopen(url)  # Öffnet die URL
        g = response.read().decode('utf-8')
        await msg.channel.send(g)

stay_alive()
bot.run(os.environ['DISCORD_TOKEN'])
