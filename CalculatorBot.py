import discord
import asyncio
import time
import aiohttp
import json
import os
from discord import Game
from discord.ext import commands

client = commands.Bot(command_prefix='c')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Calculating by + | - | x | ÷ || c'))
    print('Connected on ' + client.user.name)

@client.command()
async def add(left: int, right: int):
    await client.say(left + right)

@client.command()
async def subtract(left: int, right: int):
    await client.say(left - right)

@client.command()
async def multiply(left: int, right: int):
    await client.say(left * right)

@client.command()
async def divide(left: int, right: int):
    try:
        await client.say(left // right)
    except ZeroDivisionError:
        await client.say("Can't be divided by ZERO")

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    channel = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.darkbrown()
    )
    embed.set_author(name='Help')
    embed.add_field(name='add', value='Adds a number to a number', inline=False)
    embed.add_field(name='subtract', value='Subtracts a number from another number', inline=False)
    embed.add_field(name='multiply', value='Multiplys a number', inline=False)
    embed.add_field(name='divide', value='Divides a number', inline=False)

    await client.send_message(channel, embed=embed)

client.run(str(os.environ.get('BOT_TOKEN')))
