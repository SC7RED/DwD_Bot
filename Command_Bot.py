# command bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='membercount')
async def membercount(ctx):
    await ctx.send(len(guild.member_count)

member_count = len([m for m in ctx.guild.members if not m.bot]) # doesn't include bots

bot.run('YOUR TOKEN HERE')
