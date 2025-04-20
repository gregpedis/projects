import os
import json
import discord
import random
import configparser as cp
import commands as cmd

cfg = cp.ConfigParser()
cfg.read("config.ini")

TOKEN = cfg["client"]["token"]
FILES_DIRECTORY = cfg["DEFAULT"]["files_directory"]

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print("Indeed, a wise choice.")


@client.event
async def on_message(message):
    if message.author != client.user:
        result = cmd.execute_command(message.content)
        if isinstance(result, str):
            await message.channel.send(result)
        elif isinstance(result, list):
            for r in result:
                    await message.channel.send(r)

client.run(TOKEN)
