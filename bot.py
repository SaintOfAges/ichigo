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

@bot.event
async def on_command_error(ctx, exception):
	if type(exception) is commands.errors.MissingRequiredArgument:
		await ctx.send("You are missing Arguments there buddy!")
"""
@bot.event
async def on_message(msg):
    if msg.author.id != "434019978786897930":
        chat = msg.server.get_member_named("Abhi#3482")
        await bot.send_message(chat, "({}) | **{}** sent: *{}* | From: *{}* server".format(msg.timestamp, msg.author, msg.content, msg.server))
    await bot.process_commands(msg)
"""


bot.run("BOT_TOKEN") 



