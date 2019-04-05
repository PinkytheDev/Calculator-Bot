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

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    channel = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.green()
    )
    embed.set_author(name='Help')
    embed.add_field(name='add', value='Adds a number to a number')
