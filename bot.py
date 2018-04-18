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

bot = commands.Bot(command_prefix="ik", description="Discripto")
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
	
bot.run("NDM0MDE5OTc4Nzg2ODk3OTMw.DbJaAg.ZMYTYDeGStoTJwsBpLBa8LD8cow") 



