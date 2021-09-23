import discord
import os
import spotipy
from discord.ext import commands
import requests
import json
from keep_alive import keep_alive
from Functions import reverse, get_alot_quotes, get_quote, get_quote_today, yturl, make_a_word, _search
from discord.utils import get 
from discord import FFmpegPCMAudio, PCMVolumeTransformer
import pafy
import youtube_dl
import random
import time
import math
import asyncio
import yt_search
from collections import defaultdict



global allow
allow = ["JuggernautRhino#0421"]

global Naughty
Naughty = os.environ['Naughty']

global condition
condition = True

client = commands.Bot(command_prefix="*")
client.remove_command('help')
player = {}
ydl_opts = {
    'format':
    'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }],
}

global queues
queues={}
queuetitles = {}
queue = []
queuenames = {}
loop = False
FFMPEG_OPTIONS = {
    'before_options':
    '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

def play_next(ctx, source):
    serverid = ctx.message.guild.id 
    if len(queues[serverid][0]) >= 1:
        del queues[serverid][0]
        vc = get(client.voice_clients, guild=ctx.guild)
        vc.play(discord.FFmpegPCMAudio(after=lambda e: play_next(ctx,source)))
        asyncio.run_coroutine_threadsafe(ctx.send("No more songs in queue."))

@client.event
async def on_ready():
    os.system("clear")
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="*help"),
                                 status=discord.Status.online)
    queue.clear()
    print('We have logged in as {0.user}'.format(client))


@client.group(invoke_without_command=True)
async def help(ctx):
    cc = [0x440DA0, 0xa576e0, 0x6b3eba]
    em = discord.Embed(title="Help",
                       description="**Do *<Command> to use the command!**",
                       colour=random.choice(cc))

    em.add_field(name="Misc", value="pong, say, inspire, twiki, urban")
    em.add_field(name="Useful", value="user, ping, join, leave")
    em.add_field(name="Music", value="play, stop, pause, resume, queue, show queue(sq), skip, clear")
    await ctx.send(embed=em)


@client.command(aliases=["inf"])
async def infinite(ctx):
    await ctx.send("*inf")


@client.command(aliases=["tag"])
async def _tag(ctx):
    user = ctx.message.author
    await ctx.send(f'your username is {user}')


@client.command(aliases=["id"])
async def _id(ctx):
    idd = ctx.message.author.id
    await ctx.send(f'Your id is {idd}')


@client.command(aliases=['user', 'users', 'resu'])
async def myid(ctx):
    await ctx.send(ctx.guild.member_count)

@client.command(aliases=['talk', 'say'])
async def _print(ctx, *, words):
    await ctx.send(words)


@client.command(aliases=['klat', 'yas'])
async def _yas(ctx, *, words):
    words = reverse(words)
    await ctx.send(words)


@client.command(aliases=['inspire', 'Inspire'])
async def _inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)


@client.command()
async def eripsni(ctx):
    quote = get_quote()
    quote = reverse(quote)
    await ctx.send(quote)


@client.command(aliases=['Daily', 'daily'])
async def Daily_Quote(ctx):
    Daily = get_quote_today()
    await ctx.send(Daily)


@client.command(aliases=['50', 'A lot', 'Loads'])
async def A_Lot_Of_Quotes(ctx):
    ALot = get_alot_quotes()
    await ctx.send(ALot)


@client.command(aliases=["btc"])
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    value = value.replace(",", "")
    value = float(value) / 1.37
    value = round(value, 2)
    await ctx.send(f'Bitcoin price is: £{value}')


@client.command(aliases=["answer"])
async def question(ctx):
    stugg = ["42", "nope not doing it", "5.5"]
    await ctx.send(random.choice(stugg))


@client.command(aliases=['flip', 'coinflip'])
async def CoinFlip(ctx):
    flip = random.randint(0, 2)
    await ctx.send("flipping coin now!")
    time.sleep(2)
    if flip == 0:
        await ctx.send("Heads")
    elif flip == 1:
        await ctx.send("Tails")
    elif flip == 2:
        flipp = random.randint(0, 1000)
        if flipp == 42:
            flippp = random.randint(0, 1000)
            if flippp == 42:
                await ctx.send("It landed on its side!")
            else:
                print("")
        else:
            print("")


@client.command(aliases=['ping'])
async def _ping(ctx):
    await ctx.send(f'**Pong!** In {round(client.latency * 1000)}ms')


@client.command(aliases=['gnip'])
async def _gnip(ctx):
    ggnip = (round(client.latency * 1000))
    ggnip = str(ggnip)
    ggnop = reverse(ggnip)
    await ctx.send(f'sm {ggnop} nI **!gnoP**')


@client.command(aliases=['twiki'])
async def terrariawiki(ctx, ba="", baa="0", baaa="0", baaaa="0"):
    embed = discord.Embed()
    if baaaa == "0":
        if baaa == "0":
            if baa == "0":
                print("")
            else:
                ba = ba + "_" + baa
        else:
            ba = ba + "_" + baa + "_" + baaa
    else:
        ba = ba + "_" + baa + "_" + baaa + "_" + baaaa

    embed.description = "[Terraria wiki](" f'https://terraria.gamepedia.com/{str(ba)}' ")\nThe official terraria wiki!"
    embed.set_image(
        url=
        "https://static.wikia.nocookie.net/terraria_gamepedia/images/b/bc/Wiki.png/revision/latest/scale-to-width-down/196?cb=20181016001057"
    )
    await ctx.send(embed=embed)


@client.command(aliases=['urban', 'dict'])
async def urban_dict(ctx, ba="", baa="0", baaa="0", baaaa="0"):
    embed = discord.Embed()
    if baaaa == "0":
        if baaa == "0":
            if baa == "0":
                print("")
            else:
                ba = ba + "%20" + baa
        else:
            ba = ba + "%20" + baa + "%20" + baaa
    else:
        ba = ba + "%20" + baa + "%20" + baaa + "%20" + baaaa

    embed.description = "[The Urban Dictionary](" f'https://www.urbandictionary.com/define.php?term={str(ba)}' ")\nThe urban dictionary!"
    embed.set_image(
        url=
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/UD_logo-01.svg/768px-UD_logo-01.svg.png"
    )
    await ctx.send(embed=embed)


@client.command(aliases=['pong'])
async def _pong(ctx):
    await ctx.send('Ping!')


@client.command(aliases=['gnop'])
async def _gnop(ctx):
    await ctx.send('!gniP')


@client.command(pass_context=True)
async def join(ctx):

    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice is not None:
        await ctx.send("Moving Voice Chanels now")
        return await voice.move_to(channel)
    else:
        await channel.connect()

    await ctx.send(f'Joined {channel}')


@client.command(pass_context=True, aliases=['l', 'dc'])
async def leave(ctx):
    channel = ctx.message.guild.voice_client
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f'Left {channel}')
    else:
        await ctx.send('Im not connected to a call silly')


@client.command(aliases=["q", "queue"])
async def _queue(ctx, b1="0", b2="0", b3="0", b4="0", b5="0", b6="0"):
    url, title = _search(b1, b2, b3, b4, b5, b6)
    serverid = ctx.message.guild.id
    try:
        queues[serverid].append(url)
        await ctx.send("Added Song To Queue!")
        queuetitles[serverid].append(title)
    except KeyError:
        queues[serverid] = [url]
        await ctx.send("Added Song To Queue!")
        queuetitles[serverid] = [title]


@client.command(aliases=["aq", "asq"])
async def all_queues(ctx, queue=queue):
    await ctx.send(queuetitles)

@client.command(aliases=["sq", "show queue"])
async def show_queue(ctx):
    serverid = ctx.message.guild.id
    global queues
    if serverid in queues:
        cqueue = (', '.join(queue))
        embed = discord.Embed()
        embed.description = f"**Your Current Queue**\n {queuetitles[serverid]} "
        embed.color = 0x440DA0
        await ctx.send(embed=embed)
    else:
        queues[serverid] = []
        await ctx.send("Your queue is empty, maybe try adding a song to it!")


@client.command(aliases=["Skip", 'sk', 'next'])
async def skip(ctx, queue=queue):
    global loop
    serverid = ctx.message.guild.id
    song_there = os.path.isfile("song.mp3")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing() != None:
        voice.stop()
        video = pafy.new(queues[serverid][0])
        best = video.getbest()
        source = FFmpegPCMAudio(best.url, **FFMPEG_OPTIONS)
        await ctx.send(f'Now playing {queues[serverid][0]}')
        voice.play(source)
    await ctx.send(f'Now playing {queues[serverid][0]}')
    voice.play(source)


@client.command(aliases=["what?"])
async def what(ctx):
    global loop
    await ctx.send(f'loop is {loop}')


@client.command(aliases=["lo", "loop"])
async def _loop(ctx):
    global loop
    if loop == False:
        loop = True
        await ctx.send("Now Looping Queue")
    elif loop == True:
        loop = False
        await ctx.send("Stopped Looping Queue")


@client.command(aliases=["c"])
async def clear(ctx):
    serverid = ctx.message.guild.id
    queue = queues[serverid]
    queue.clear()
    await ctx.send("Cleared Queue")


@client.command()
async def test(ctx):
    serverid = ctx.message.guild.id
    print(queues[serverid[0]])


@client.command(aliases=["p"])
async def play(ctx,
               b1="0",
               b2="0",
               b3="0",
               b4="0",
               b5="0",
               b6="0",
               ydl_opts=ydl_opts,
               queue=queue,
               FFMPEG_OPTIONS=FFMPEG_OPTIONS):
    serverid = ctx.message.guild.id
    try:
        url, title = _search(b1, b2, b3, b4, b5, b6,ctx,queues)
    
        #if they're trying to specify a song to play
        channel = ctx.message.author.voice.channel
        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

        if voice is None:
            if channel is None:
                await voiceChannel.connect()
            else:
                await channel.connect()
            voice = discord.utils.get(client.voice_clients, guild=ctx.guild)


        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            await ctx.send("Song is playing already so i've added it to queue")
            queues[serverid].append(url)
        else:
            video = pafy.new(queues[serverid][0])
            best = video.getbest()
            source = FFmpegPCMAudio(best.url, **FFMPEG_OPTIONS)
            #voice.play(discord.FFmpegPCMAudio(after=lambda e: play_next(ctx,source)))
            voice.play(source)
            await ctx.send(f'Now playing {title}')
    except KeyError:
            queues[serverid] = [url]
            queuetitles[serverid] = [title]
            await play(ctx,
               b1="0",
               b2="0",
               b3="0",
               b4="0",
               b5="0",
               b6="0",
               ydl_opts=ydl_opts,
               queue=queue,
               FFMPEG_OPTIONS=FFMPEG_OPTIONS)



@client.command(aliases=["api"])
async def apii(ctx, searchterm):
    yt = yt_search.build("AIzaSyBNsZ6TUJVBP61YAUtvoOwh28mtSxWlC3I")
    search_result = yt.search(searchterm, sMax=1, sType=["video"])
    await ctx.send(search_result.title)
    time.sleep(1)
    await ctx.send(search_result.videoId)
    time.sleep(1)
    await ctx.send(search_result.channelTitle)


@client.command(aliases=["search"])
async def testie(ctx, b1, b2="0", b3="0", b4="0", b5="0", b6="0"):
    st = _search(b1, b2, b3, b4, b5, b6)  #st stands for search term
    await ctx.send(st)


@client.command(aliases=['pa'])
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('there is no audio silly')


@client.command(aliases=['r'])
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Audio is not paused")


@client.command(aliases=['s'])
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.stop()


snipe_message_author = {}
snipe_message_content = {}


@client.event
async def on_message_delete(message):
    if snipe_message_author == None:
        snipe_message_author[message.channel.id] = message.author
        snipe_message_content[message.channel.id] = message.content
    else:
        snipe_message_author[message.channel.id] = 0
        snipe_message_content[message.channel.id] = 0
        del snipe_message_author[message.channel.id]
        del snipe_message_content[message.channel.id]
        snipe_message_author[message.channel.id] = message.author
        snipe_message_content[message.channel.id] = message.content


@client.command(name='snipe', aliases=["reverse", "Reverse"])
async def snipe(ctx):
    user = str(ctx.message.author)
    if user in allow:
        channel = ctx.channel
        try:  #This piece of code is run if the bot finds anything in the dictionary
            em = discord.Embed(name=f"Last deleted message in #{channel.name}",
                               description=snipe_message_content[channel.id])
            em.set_footer(
                text=
                f"This message was sent by {snipe_message_author[channel.id]}")
            await ctx.send(embed=em)
        except:  #This piece of code is run if the bot doesn't find anything in the dictionary
            await ctx.send(
                f"There are no recently deleted messages in #{channel.name}")
    else:
        await ctx.send("woah dude, no")


@client.command(aliases=["list"])
async def allowed(ctx):
    global allow
    await ctx.send(allow)


#If the bot sends the embed, but it's empty, it simply means that the deleted message was either a media file or another embed.


@client.command(aliases=["sfw"])
async def SFW(ctx):
    global condition
    if condition == False:
        condition = True
        await ctx.send("SFW mode activated")
    elif condition == True:
        condition = False
        await ctx.send("Get ready for hell to break loose")


keep_alive()
client.run(os.getenv('TOKEN'))
