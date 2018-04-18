import discord
from discord.ext import commands
import discord
from   discord import errors

bot = commands.Bot(command_prefix="ik", description="Discripto")
@bot.command()
###
import functools, youtube_dl
url = 'youtube url'
opts = {"format": 'webm[abr>0]/bestaudio/best',"ignoreerrors": True,"default_search": "auto","source_address": "0.0.0.0",'quiet': True}
ydl = youtube_dl.YoutubeDL(opts)
func = functools.partial(ydl.extract_info, url, download=False)
info = func()
player = discord.FFmpegPCMAudio(info['url'])
###
async def yeet(ctx):
    """Sends a simple Hello Message"""
    await ctx.send("Sup!!")
@bot.command()
async def mime(ctx, *, something):
	"""Repeats What you Say!"""
    await ctx.send(something)
#bot.remove_command('help')
#@bot.command()
#async def help(ctx):
	#await ctx.send("Figure it out Yourself!")
@bot.command()
async def cult(ctx, member: discord.User):
	"""Didnt fix that one"""
    await member.send("Wanna Join the Illuminati?")
@bot.command()
async def shout(ctx):
	"""Mentions"""
	await ctx.send(ctx.author.mention)
@bot.command()
async def mention(ctx):
	"""Mention"""
    await ctx.author.send(ctx.author.mention)
@bot.event
async def on_member_join(member):
    guild = member.guild
    await member.send("Welcome to {}!".format(guild.name))
@bot.command()
async def add(ctx,a,b):
	"""Simple Addition"""
	c=int(a)+int(b)
	await ctx.send(c)

@bot.event
async def on_command_error(ctx, exception):
	if type(exception) is commands.errors.CommandNotFound:
		await ctx.send("Cant do that mate")
	
bot.run("NDM0MDE5OTc4Nzg2ODk3OTMw.DbJaAg.ZMYTYDeGStoTJwsBpLBa8LD8cow") 


