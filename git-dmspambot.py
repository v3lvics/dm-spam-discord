import discord
from discord.ext import commands
from discord import app_commands
import time
bot = commands.Bot(command_prefix=("$"),intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("DMSTRIKEBOT2.0 - LOGGED")

@bot.command()
async def ts(ctx):
     await ctx.send("Zobry den. <:white_check_mark:1093487994847117313>")

@bot.command()
async def msg(ctx, user: discord.User, message):
    while True:
     print("SPAMMED")
     await user.send(message)
     time.sleep(1)
     await user.send(message)
     time.sleep(1)
     await user.send(message)
     time.sleep(1)
     await user.send(message)
     time.sleep(1)
     await user.send(message)
     time.sleep(1)
     await user.send(message)
     time.sleep(1)
     await user.send(message)
     time.sleep(1)
     await user.send(message)
     time.sleep(1)
     await user.send(message)
     time.sleep(1)
     await user.send(message)
     time.sleep(1)
     await user.send(message)
     time.sleep(1)
     await user.send(message)
     time.sleep(1)

# DISCORD NEW UPDATE FOR SCRIPTING EMBEDS USE THIS WHEN SENDING:
# await ctx.send(embed = your_embed)
# role grant = await.user.add_roles(role) / include *role* in ctx
# BOT TOKEN DO NOT SHARE / BOT ABUSE RISK AND EXPLOIT
bot.run('YourShit')