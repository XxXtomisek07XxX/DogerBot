import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

import asyncio
import platform
import colorsys
import random
import os 
import time





bot=commands.Bot(command_prefix='l!')



@bot.event
async def on_ready():
     await bot.change_presence(game=discord.Game(name= "none"))
     print('The bot is ready!')
     print(bot.user.name)
     print(bot.user.id)
     
@bot.command
async def bacha():
     await bot.say('dávejte si bacha kam dáváte token!')


bot.run(os.getenv("BOT_TOKEN"))
