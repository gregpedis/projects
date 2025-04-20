import discord
from discord.ext import commands
from base.config import PREFIX

intents = discord.Intents.default()

intents.members = True
intents.message_content = True

intents.typing = False
intents.presences = False

help_command = commands.DefaultHelpCommand()
help_command.no_category = ""
help_command.default_argument_description = ""

BOT = commands.Bot(
    command_prefix=PREFIX, 
    intents=intents,
    help_command=help_command
    )
