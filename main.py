from settings import *
from utils import load_cogs, get_prefix

from discord.ext import commands

client = commands.Bot(command_prefix='.')

load_cogs(client)
client.run(TOKEN)
