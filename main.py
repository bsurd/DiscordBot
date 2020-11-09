import discord

from settings import *
from discord.ext import commands
from utils import load_cogs, get_prefix

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=get_prefix,
                      # help_command=None,
                      case_insensitive=True,
                      intents=intents)

load_cogs(client)
client.run(TOKEN)
