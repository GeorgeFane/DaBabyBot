# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
client = discord.Client()

with open('suge.txt') as f:
    song = f.read()
verses = [verse for verse in song.split('\n\n')]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await message.channel.send(
        random.choice(verses)
    )

client.run(TOKEN)