import discord
from discord import FFmpegPCMAudio
from discord.ext import commands
import os
import urllib.request

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='c!', intents=intents)


queues = {}

def check_queues(ctx, id):
    if queues[id] != []:
        voice = ctx.guild.voice_client
        source = queues[id].pop(0)
        player = voice.play(source)

@bot.command(pass_context = True)
async def play(ctx, arg):
    if (ctx.author.voice):
        if(ctx.voice_client):
           print("Test")

        else:

            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio(arg)
            player = voice.play(source, after=lambda x=None: check_queues(ctx, ctx.message.guild.id))
    else:
        await ctx.send("Du bist in keinem Voice Channel")


@bot.command(pass_context = True)
async def queue(ctx, arg):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio(arg)

    guild_id = ctx.message.guild.id

    if guild_id in queues:
        queues[guild_id].append(source)

    else:
        queues[guild_id] = [source]


        await ctx.send("Das Lied wurde der Warteschlange hinzugefügt.")


@bot.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        if(ctx.voice_client):
            await ctx.send("Der Bot ist bereits im Voice Channel")

        else:
            channel = ctx.message.author.voice.channel
            await channel.connect()
    else:
        await ctx.send("Du bist in keinem Voice Channel")

@bot.command(pass_context = True)
async def list(ctx):
    url_list = "https://raw.githubusercontent.com/lajoka93/lajoka93.github.io/main/list.txt"
    response = urllib.request.urlopen(url_list)  # Öffnet die URL
    l = response.read().decode('utf-8')
    await ctx.send(l)



@bot.command(name='skip')
async def skip(ctx):
    # Überprüfen, ob der Bot gerade einen Song spielt
    if not bot.voice_clients:
        await ctx.send("Ich spiele gerade keinen Song.")
        return

    # Zugriff auf den Voice-Client des Bots
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    # Überprüfen, ob es Songs in der Warteschlange gibt
    if not queue:
        await ctx.send("Es gibt keine Songs in der Warteschlange.")
        return

    # Den aktuellen Song stoppen
    voice_client.stop()

    # Den nächsten Song in der Warteschlange abspielen
    next_song = queue.pop(0)
    await ctx.send("Das Lied wurde übersprungen.")
    voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=next_song))



@bot.command(pass_context = True)
async def leave(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("Der Bot hat den Voice Channel verlassen.")
  else:
    await ctx.send("Der Bot ist in keinem Voice Channel.")


@bot.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients,guild=ctx.guild)

    if voice.is_playing():
        voice.pause()

    else:
        await ctx.send("Es wird momentan kein Lied abgespielt")


@bot.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Es wird momentan kein Lied abgespielt")

@bot.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients,guild=ctx.guild)
    voice.stop()
    await ctx.guild.voice_client.disconnect()
#@bot.event
#async def on_message(msg):
  #  if msg.content == "Hallo":
 #       a = str(msg.author)
        #print(a)
       # b = "Hallo " + a
      #  await msg.channel.send(b)

#    if msg.content == "Was waren die Hausaufgaben ?":
#       print(msg.content)
#      datei = open('homework.txt','r')
#     h = datei.read()
#    print(h)
#   await msg.channel.send(h)
#  datei.close


@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return

    if msg.content == "Hallo":
        a = str(msg.author)
        print(a)
        b = "Hallo " + a
        await msg.channel.send(b)

    if msg.content == "Was waren die Hausaufgaben ?" and any(role.name in ["Schüler", "Lehrer"] for role in msg.author.roles):
        url = "https://raw.githubusercontent.com/lajoka93/lajoka93.github.io/main/homework.txt"
        response = urllib.request.urlopen(url)  # Öffnet die URL
        g = response.read().decode('utf-8')
        await msg.channel.send(g)
        
    await bot.process_commands(msg)

#@bot.event
#async def on_message(msg):
 #       if msg.content == "Hallo":
  #          a = str(msg.author)
   #         print(a)
    #        b = "Hallo " + a
     #       await msg.channel.send(b)
      #      await bot.process_commands(msg)


stay_alive()
bot.run(os.environ['DISCORD_TOKEN'])
