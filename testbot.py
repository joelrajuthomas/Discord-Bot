import discord
from discord.ext import commands
import asyncio
import urllib.request

'''

    cd C:\Python\Discord
    py testbot.py

'''

prefixlist = ["/","!","$"]
bot = commands.Bot(command_prefix = prefixlist)
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Ready")

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Help Info", description="Here's what you can do.", color=0x00ff00)
    embed.add_field(name="/help", value="Gives list of commands", inline=False)
    embed.add_field(name="/convert", value="crypto and country currency converter. Example: '/convert 1 BTC USD' ", inline=False)
    embed.add_field(name="/lectro", value="Contact and social media info", inline=False)
    embed.add_field(name="/info", value="User info", inline=False)
    await bot.say(embed=embed)

@bot.command(pass_context=True) ##https://www.cryptocompare.com/api/#private-api-invocation
async def convert (ctx, q, curr1, curr2):
    u1 = curr1.upper()
    u2 = curr2.upper()
    link = "https://min-api.cryptocompare.com/data/price?fsym=" + u1 + "&tsyms=" + u2
    f = urllib.request.urlopen(link)
    myfile = f.read()
    mystr = myfile.decode("utf8")
    f.close()

    x = 0
    for c in mystr:
        mystr = mystr.replace("{", "" )
        mystr = mystr.replace("}", "" )
        mystr = mystr.replace('\"', "" )
    for c in mystr:
        if c != ":":
            x+=1
        else:
            mystr = mystr[x:]
            mystr = mystr.replace(":", "")
    newq = float(q)
    myflt = float(mystr)
    converted = myflt * newq
    await bot.say(q + " " + u1 + " = " + str(converted) + " " + u2)

@bot.command(pass_context=True)
async def lectro(ctx):
    embed = discord.Embed(title="Lectro LLC", description="Here's what we got.", color=0x00ff00)
    embed.set_thumbnail(url="https://lectro.io/wp-content/uploads/2018/04/Lectro-Coin-logo-293x300.png")
    embed.add_field(name="Website", value="https://lectrio.io", inline=False)
    embed.add_field(name="Twitter", value="https://twitter.com/LectroProject", inline=False)
    embed.add_field(name="Telegram", value="https://t.me/lectroproject", inline=False)
    embed.add_field(name="Facebook", value="https://www.facebook.com/LectroProject/", inline=False)
    embed.add_field(name="Email", value="info@electro.io", inline=False)
    await bot.say(embed=embed)

#Copy and paste bot token within the quotes
bot.run("<INSERT BOT TOKEN HERE>")
