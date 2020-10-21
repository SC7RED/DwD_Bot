#  bot.py
import os

import discord
from dotenv import load_doten

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'Welcome {client.user}. You are connected to the server:\n'
        f'{guild.name}\n'
    )
    
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hey {member.name}, welcome to the' + ('DISCORD_GUILD') + 'discord server!'
        'By joining this discord server you accept the rules of the server.'
    )

client.run('Token')
