import nextcord
from nextcord import interactions
from nextcord import Member
from nextcord import FFmpegPCMAudio
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions, MissingPermissions
import os
import urllib.request
from nextcord import Interaction

intents = (nextcord.Intents.default())
intents.message_content = True
bot = commands.Bot(command_prefix='c!', intents=intents)
testServerId = 1125508167716048977


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
async def qotd(ctx):
    if (ctx.author.voice):
        if(ctx.voice_client):
           print("Test qotd")

        else:

            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio("qotd.mp3")
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
    response_list = urllib.request.urlopen(url_list)  # Öffnet die URL
    l = response_list.read().decode('utf-8')
    await ctx.send(l)

@bot.command(pass_context = True)
async def wlist(ctx):
    url_w_list = "https://raw.githubusercontent.com/lajoka93/lajoka93.github.io/main/w_list.txt"
    response_w_list = urllib.request.urlopen(url_w_list)  # Öffnet die URL
    w_l = response_w_list.read().decode('utf-8')
    await ctx.send(w_l)

@bot.command(pass_context = True)
async def chelp(ctx):
    url_help = "https://raw.githubusercontent.com/lajoka93/lajoka93.github.io/main/help.txt"
    response_help = urllib.request.urlopen(url_help)  # Öffnet die URL
    l_help = response_help.read().decode('utf-8')
    await ctx.send(l_help)



@bot.command(name='skip')
async def skip(ctx):
    # Überprüfen, ob der Bot gerade einen Song spielt
    if not bot.voice_clients:
        await ctx.send("Ich spiele gerade keinen Song.")
        return

    # Zugriff auf den Voice-Client des Bots
    voice_client = nextcord.utils.get(bot.voice_clients, guild=ctx.guild)

    # Überprüfen, ob es Songs in der Warteschlange gibt
    if not queue:
        await ctx.send("Es gibt keine Songs in der Warteschlange.")
        return

    # Den aktuellen Song stoppen
    voice_client.stop()

    # Den nächsten Song in der Warteschlange abspielen
    next_song = queue.pop(0)
    await ctx.send("Das Lied wurde übersprungen.")
    voice_client.play(nextcord.FFmpegPCMAudio(executable="ffmpeg", source=next_song))



@bot.command(pass_context = True)
async def leave(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("Der Bot hat den Voice Channel verlassen.")
  else:
    await ctx.send("Der Bot ist in keinem Voice Channel.")


@bot.command(pass_context = True)
async def pause(ctx):
    voice = nextcord.utils.get(bot.voice_clients,guild=ctx.guild)

    if voice.is_playing():
        voice.pause()

    else:
        await ctx.send("Es wird momentan kein Lied abgespielt")


@bot.command(pass_context = True)
async def resume(ctx):
    voice = nextcord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Es wird momentan kein Lied abgespielt")


@bot.command(pass_context = True)
async def stop(ctx):
    voice = nextcord.utils.get(bot.voice_clients,guild=ctx.guild)
    voice.stop()
    await ctx.guild.voice_client.disconnect()


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Du hast nicht die Rechte dazu.')

@bot.command(name='ban')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: nextcord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} wurde gebannt.')

@bot.command(name='kick')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: nextcord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} wurde gekickt.')

@bot.slash_command(name = "report", description = "Kickt User, die nicht gewhitelisted sind.", guild_ids=[testServerId])
async def report(interaction: Interaction, member: nextcord.Member, reason: str = 'Du bist nicht für diesen Server gewhitelistet worden.'):


    url_w = "https://raw.githubusercontent.com/lajoka93/lajoka93.github.io/main/whitelist.txt"
    response_w = urllib.request.urlopen(url_w)  # Öffnet die URL
    g_w = response_w.read().decode('utf-8')
    whitelist = g_w.split(",", -1)
    #whitelist = ['_lajoka_', '.lajoka', 'altay2', 'ChatBot#4790', 'Maki#4920', 'MEE6#4876', 'OcelotBOT#7126', 'Pancake#3691', '_pineapple_1', 'berke13.', 'carlo11120', 'emre357', 'yunghenri', 'laurachristiansen', 'lifee5870', 'lynnmh', 'minqq_', 'mmo5882', 'tjay4228', 'shawtykimy', 'tony.trng']
    print(member)
    print("Benutzer_w: " + whitelist[0])
    print(whitelist)
    member_str = str(member)
    if member_str not in whitelist and ".lajoka" in whitelist:
        #await member.kick(reason=reason)
        await interaction.response.send_message(f'{member} wurde wegen eines Reports gekickt.')
    else:
        await interaction.response.send_message(f'{member} ist gewhitelisted oder die Whitelist ist nicht erreichbar.')

@bot.slash_command(name="schüler", description="Macht user zu Schülern.", guild_ids=[testServerId])
async def schüler(interaction: Interaction, member: nextcord.Member):
    guild = interaction.guild
    role = nextcord.utils.get(guild.roles, name='Schüler')
    lehrer_role = nextcord.utils.get(guild.roles, name='Lehrer')
    author = interaction.user.id

    if any(role.name in ["Schüler", "Lehrer"] for role in interaction.user.roles):
        await member.add_roles(role)
        await interaction.response.send_message(f'{member} wurde erfolgreich als Schüler markiert!')
    else:
        await interaction.response.send_message("Du hast nicht die nötigen Rechte dazu.")


@bot.event
async def on_message(msg):

    if msg.author == bot.user:
        return

    if msg.content == "Hallo":
        a = str(msg.author)
        print(a)
        b = "Hallo " + a
        await msg.channel.send(b)

    url_h_d = "https://raw.githubusercontent.com/lajoka93/lajoka93.github.io/main/h_deny.txt"
    response_h_d = urllib.request.urlopen(url_h_d)  # Öffnet die URL
    g_h_d = response_h_d.read().decode('utf-8')
    h_deny = g_h_d.split(",", -1)
    print(h_deny)
    if msg.content == "Was waren die Hausaufgaben ?" and any(role.name in ["Schüler", "Lehrer"] for role in msg.author.roles):
        if msg.author.name not in h_deny:
            url = "https://raw.githubusercontent.com/lajoka93/lajoka93.github.io/main/homework.txt"
            response = urllib.request.urlopen(url)  # Öffnet die URL
            g = response.read().decode('utf-8')
            await msg.channel.send(g)
        else:
            await msg.channel.send("Du wurdest gesperrt.")

    allowed_users = ['altay2', '.lajoka']
    if 'qotd' in msg.content and msg.author.name in allowed_users:
        for attachment in msg.attachments:
            await attachment.save(attachment.filename)
            await os.system("ffmpeg -i " + attachment.filename + " qotd.mp3 -y")
            await msg.channel.send("Das neue Quote of the Day wurde hochgeladen")

    if msg.content == "Ich will gebannt werden":
        reason = "Wunsch"
        await msg.author.ban(reason=reason)


    await bot.process_commands(msg)

bot.run(os.environ['DISCORD_TOKEN'])
