import discord
from discord.ext import commands
import sys
import discord
import time
import sys
import os
import random
import subprocess
import traceback
from   discord import errors
import json
import random
bot = commands.Bot(command_prefix="ik", description="Discripto")
try:
	bot.load_extension("REPL")
except:
	print("Hmm")
###NSFW ALERT
a= ["i fuck my teddy bear and cum in it",
"reaxt im going to shove a football down your nosetril",
"hows it hangin? from a string probably","*ping* while u were slurping pussy from a bendy straw i studied the blade",
"i was in a good mood laughing at stupid as fuck deaths then 11 year old cancer child's last moments happend","why does it look like electricity is coming out of their dick","horsecock tho :heart:","*ping* THAT DOES IT FAGGOT! IM NOT A FURRY OR CLOSET FURRY! SHUT THE FUCK UP! EAT ASS AND DIE!","Hey faggots you can buy yourself dragon dildos 40% off tomorrow",
"Oh no I need my underage boobies !!!",
"Paul Blart: Mall Cop is my favorite movie",
"Does anyone here know how to download club penguin?",
"shes gonna find your dirty mageziens","bedroom? if you insist. i mean you are pretty cute. he took my hand, i blush deeply. as we walk to the bedroom. i pull out my bad dick. wow i thought you were a lady. well, whatever works!! narrator it didnt work. its ok my surgeon is the best my surgeon did a good job on me. i was once a dog. conveniently, he identifies as a dogkin. wow thats quite a surprise you know what else is surprising? he had a 13 inch dog penis it was red and everything, but like as a joke anyways i fucked it. my parents are really proud of him for that massive honk they were also happy with my ability to take such a massive dog... to think i was gay before( now im mega gay!)",
" named the image of the citadel nigger.jpg","```make a website like real people``` this server is to use the bots, you cant do that on websites",
"im wating the security cams in a chinese nursing home lobby","node.js more like nude.js","If Im going to blow a man, Id like to have his dick wrapped in a hot dog bun",
"should be called baka",
"ASIANBOI",
"if ma girl ever cheats on me ill stick her to a chair and make her watch me have sex with the guy who cheated on me with",
"Your midget spunnerr spun for 3 minutes 12 seconds. Congratulations, you now have asshole cancer",
"Pls stop i have miniophobia"]
###NFSW END
@bot.command()
async def nsfw(ctx):
    """Its NSFW ;-)"""
    await ctx.send(random.choice(a))
###NSFW END

@bot.command()
async def yeet(ctx):
    """Sends a simple Hello Message"""
    await ctx.send("Sup!!")
@bot.command()
async def mime(ctx, *, something):
    await ctx.send(something)
#bot.remove_command('help')
#@bot.command()
#async def help(ctx):
	#await ctx.send("Figure it out Yourself!")
@bot.command()
async def cult(ctx, member: discord.User):
    await member.send("Wanna Join the Illuminati?")
@bot.command()
async def shout(ctx):
	await ctx.send(ctx.author.mention)
@bot.command()
async def mention(ctx):
    await ctx.author.send(ctx.author.mention)
@bot.event
async def on_member_join(member):
    guild = member.guild
    await member.send("Welcome to {}!".format(guild.name))

@bot.command()
async def add(ctx,a,b):
	c=int(a)+int(b)
	await ctx.send(c)

@bot.event
async def on_command_error(ctx, exception):
	if type(exception) is commands.errors.CommandNotFound:
		await ctx.send("Cant do that mate")
	if type(exception) is commands.errors.MissingRequiredArgument:
		await ctx.send("You are missing Arguments there buddy!")
def check(ctx):
    return ctx.message.author.id == 199129403458977792

@bot.command()
@commands.check(check)
async def owner(ctx):
    await ctx.send('Thanks for making me!')

@bot.command()
@commands.has_any_role('Sigurd', 'Jacques', 'DR', 'beebee', 'chokkers delight', 'Alexa', 'Lava', 'Norway', 'jacob', 'couch', 'Brutally', 'Hunt', 'Cops', 'bob', 'DJ V/SA', 'Alena', 'new role', 'Shrew', 'Tequila', 'Xam', 'Karlie', 'Monday Meme', 'musik', 'Usagirl', 'Batman', 'Random', 'Octavia', 'Pikachu', 'Jacq', 'Perolina', 'soul', 'Riddle Honor', 'Mallu', 'Bots', 'Dark Kun', 'Labeeb', 'Pain', 'Pop', 'DJ','Members')
async def cool(ctx):
    await ctx.send('You are cool indeed')
@bot.command()
async def embed(ctx,title,text):
	await ctx.send(embed=discord.Embed(title=title,description=text,colour=discord.Colour(0xFF000)))

emo=":regional_indicator_"
ji=":" 
cat=""
@bot.command()
async def emote(ctx,word):
	cat=""
	for i in word:
		i=emo+i+ji
		cat=cat+i
	await ctx.send(cat)
	
bot.run("NDM0MDE5OTc4Nzg2ODk3OTMw.DbJaAg.ZMYTYDeGStoTJwsBpLBa8LD8cow") 



