########################################
#| Eternity Bot // created by: adieux |#
########################################

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print("  _____ _____ ___________ _   _ _____ _______   __")
    print(" |  ___|_   _|  ___| ___ \ \ | |_   _|_   _\ \ / /")
    print(" | |__   | | | |__ | |_/ /  \| | | |   | |  \ V / ")
    print(" |  __|  | | |  __||    /| . ` | | |   | |   \ /  ")
    print(" | |___  | | | |___| |\ \| |\  |_| |_  | |   | |  ")
    print(" \____/  \_/ \____/\_| \_\_| \_/\___/  \_/   \_/  ")
    print("")
    print(" -------------------------------------------------")
    print("")
    print(" # Eternity Bot // [currently ready for use] #")
    print(' # Running on ID: ["'  + bot.user.id + '"]     #')
    print("")
    print(" -------------------------------------------------")
    print("")

@bot.command(pass_context=True)
async def sv_rules(ctx):
    embed=discord.Embed(title="__𝙇𝙄𝙎𝙏 𝙊𝙁 𝙎𝙀𝙍𝙑𝙀𝙍 𝙍𝙐𝙇𝙀𝙎:__ -------------------------------------------------------------------", color=0xefefef)
    embed.set_author(name="𝗮𝗱𝗶𝗲𝘂𝘅#2718", icon_url="https://cdn.discordapp.com/avatars/239646694860521472/bd26bff6c993f58aacc0c4d6d2a5b172.png?size=256")
    embed.add_field(name="\u200b", value="[𝟭]: idc if you want to be racist, just don't constantly harass people.", inline=False)
    embed.add_field(name="\u200b", value="[𝟰]: if you come in here and start spamming or advertising, i'll ban you.", inline=False)
    embed.add_field(name="\u200b", value="[𝟮]: no leaking people's ip's or addresses. this includes ddosing and doxxing.", inline=False)
    embed.add_field(name="\u200b", value="[𝟱]: disrespecting or impersonating staff will lead to you being banned.", inline=False)
    embed.add_field(name="\u200b", value="[𝟯]: don't repeatedly tag people, including staff, with or without reason.", inline=False)
    embed.add_field(name="\u200b", value="[𝟲]: evading a ban with another account will lead to you being rebanned.", inline=False)
    embed.add_field(name="\u200b", value="__𝙁𝘼𝙄𝙇𝙐𝙍𝙀 𝙏𝙊 𝙁𝙊𝙇𝙇𝙊𝙒 𝙏𝙃𝙀𝙎𝙀 𝙍𝙐𝙇𝙀𝙎 𝙒𝙄𝙇𝙇 𝙍𝙀𝙎𝙐𝙇𝙏 𝙄𝙉 𝙔𝙊𝙐 𝘽𝙀𝙄𝙉𝙂 𝘽𝘼𝙉𝙉𝙀𝘿.__", inline=False)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def sv_information(ctx):
    embed=discord.Embed(title="__𝙏𝙊 𝘽𝙀 𝘼𝙉𝙉𝙊𝙐𝙉𝘾𝙀𝘿__", color=0xefefef)
    embed.set_author(name="𝗮𝗱𝗶𝗲𝘂𝘅#2718", icon_url="https://cdn.discordapp.com/avatars/239646694860521472/bd26bff6c993f58aacc0c4d6d2a5b172.png?size=256")
    await bot.say(embed=embed)
    
bot.run("Mzk3MjA4NTMyNTYwMzc5OTA0.DSspNA.buD1Dka75VFUM362cppcGACYB64")