import discord
import os
from discord.ext import commands
import requests
import json
from keep_alive import keep_alive
from discord.utils import get
import youtube_dl
import random
import time
import math
import asyncio

#id = 786256912387407932
#welcomechannel id = 786277477286805524

client = commands.Bot(command_prefix = "*")
client.remove_command('help')
player = {}
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
queue=["https://www.youtube.com/watch?v=0lhhrUuw2N8"]
loop = False


def reverse(string):
    revstring = ''
    index = len(string)
    while index > 0:
        revstring += string[index -1]
        index = index -1
    return revstring 
    
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_quote_today():
  response = requests.get("https://zenquotes.io/api/today")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_alot_quotes():
  response = requests.get("https://zenquotes.io/api/quotes")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="*help"), status = discord.Status.online)
    print('We have logged in as {0.user}'.format(client))

@client.group(invoke_without_command = True)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "**Do *<Command> to use the command!**", colour = 0x440DA0)
    
    em.add_field(name = "Misc", value = "pong, say, inspire, twiki, urban")
    em.add_field(name = "Useful", value = "user, ping, join, leave")
    em.add_field(name = "Music", value = "play, stop, pause, resume, queue")
    await ctx.send(embed = em)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.command(aliases=["inf"])
async def infinite(ctx):
    await ctx.send("*inf")

@client.command(aliases=['user','users','resu'])
async def myid(ctx):
    await ctx.send(ctx.guild.member_count)

@client.command(aliases=['talk','say','print'])
async def _print(ctx, *, words):
    await ctx.send(words)

@client.command(aliases=['klat','yas','tnirp'])
async def _yas(ctx, *, words):
    words=reverse(words)
    await ctx.send(words)

@client.command(aliases=['inspire','Inspire','eripsni'])
async def _inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)

@client.command(aliases=['Daily','daily'])
async def Daily_Quote(ctx):
    Daily = get_quote_today()
    await ctx.send(Daily)

@client.command(aliases=['50','A lot','Loads'])
async def A_Lot_Of_Quotes(ctx):
    ALot = get_alot_quotes()
    await ctx.send(ALot)

@client.command(aliases=["btc"])
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    value = value.replace(",","")
    value = float(value) / 1.37
    value = round(value, 2)
    await ctx.send(f'Bitcoin price is: £{value}')

@client.command(aliases=['flip','coinflip'])
async def CoinFlip(ctx):
    flip = random.randint(0,2)
    await ctx.send("flipping coin now!")
    time.sleep(2)
    if flip == 0:
        await ctx.send("Heads")
    elif flip == 1:
        await ctx.send("Tails")
    elif flip == 2:
        flipp = random.randint(0,1000)
        if flipp == 42:
            flippp = random.randint(0,1000)
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
    ggnip=(round(client.latency * 1000))
    ggnip =str(ggnip)
    ggnop = reverse(ggnip)
    await ctx.send(f'sm {ggnop} nI **!gnoP**')
    

@client.command(aliases=['twiki'])
async def terrariawiki(ctx,ba = "",baa="0",baaa="0",baaaa="0"):
    embed = discord.Embed()
    if baaaa == "0":
        if baaa == "0":
            if baa == "0":
                print("")
            else:
                ba = ba + "_" + baa
        else:
            ba = ba + "_"+ baa + "_" + baaa
    else:
        ba = ba +"_"+baa+"_"+baaa+"_"+baaaa

    embed.description = "[Terrari wiki]("f'https://terraria.gamepedia.com/{str(ba)}'")\nThe official terraria wiki!"
    embed.set_image(url = "https://static.wikia.nocookie.net/terraria_gamepedia/images/b/bc/Wiki.png/revision/latest/scale-to-width-down/196?cb=20181016001057")
    await ctx.send(embed = embed)

@client.command(aliases=['urban','dict'])
async def urban_dict(ctx,ba = "",baa="0",baaa="0",baaaa="0"):
    embed = discord.Embed()
    if baaaa == "0":
        if baaa == "0":
            if baa == "0":
                print("")
            else:
                ba = ba + "%20" + baa
        else:
            ba = ba + "%20"+ baa + "%20" + baaa
    else:
        ba = ba +"%20"+baa+"%20"+baaa+"%20"+baaaa

    embed.description = "[The Urban Dictionary]("f'https://www.urbandictionary.com/define.php?term={str(ba)}'")\nThe urban dictionary!"
    embed.set_image(url = "https://commons.wikimedia.org/wiki/File:UD_logo-01.svg")
    await ctx.send(embed = embed)


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

@client.command(pass_context = True, aliases = ['l','dc'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f'Left {channel}')
    else:
        await ctx.send('Im not connected to a call silly')

@client.command(aliases=["q","queue"])
async def _queue(ctx,url):
    queue.append(url)
    await ctx.send("Added Song To Queue!")

@client.command(aliases=["sq","show queue"])
async def show_queue(ctx, queue = queue):
    cqueue = (', '.join(queue))
    embed = discord.Embed()
    embed.description="**Your Current Queue**\n("f'{cqueue}'")"
    embed.color = 0x440DA0
    await ctx.send(embed=embed)

@client.command(aliases=["Skip",'sk','next'])
async def skip(ctx, queue = queue):
    song_there = os.path.isfile("song.mp3")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.stop()
        os.remove("song.mp3")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([queue[0]])
                
        for file in os.listdir("./"):
            if file.endswith("mp3"):
                os.rename(file, "song.mp3")
    else:
        try:
            if song_there:
                os.remove("song.mp3")   
        except PermissionError:
            print("")
            return
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([queue[0]])
                queue.remove(queue[0]) 
        for file in os.listdir("./"):
            if file.endswith("mp3"):
                os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command(aliases=["what?"])
async def what(ctx, loop = loop):
    await ctx.send(f'loop is {loop}')

@client.command(aliases=["lo"])
async def loop(ctx, loop = loop):
    if loop == False:
        loop = True
        await ctx.send("Now Looping Queue")
    elif loop == True:
        loop == False
        await ctx.send("Stopped Looping Queue")
    else:
        await ctx.send("somehow you've fucked the code up. You shithead")
    return loop

@client.command(aliases=["c"])
async def clear(ctx):
    queue.clear()
    await ctx.send("Cleared Queue")

@client.command(aliases=["p"])
async def play(ctx, url = "0", ydl_opts = ydl_opts, queue = queue):
    
    if url == "0":
        print(" ")
    else:
        queue.insert(0, url)

    song_there = os.path.isfile("song.mp3")
    
    channel = ctx.message.author.voice.channel
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice is None:
        if channel is None:
            await voiceChannel.connect()
        else:
            await channel.connect()
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    
    if voice.is_playing():
        print("adding song to Queue")
    else:
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing music to end or use the 'stop' command")
            return
    
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        queue.append(url)
        await ctx.send("Song is playing already so i've added it to queue")
    else:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([queue[0]])
                queue.remove(queue[0])
        for file in os.listdir("./"):
            if file.endswith("mp3"):
                os.rename(file, "song.mp3")

        voice.play(discord.FFmpegPCMAudio("song.mp3"))



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





keep_alive()
client.run(os.getenv('TOKEN'))