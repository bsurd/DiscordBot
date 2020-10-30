from settings import *
from discord.ext import commands
from utils import load_cogs, get_prefix

client = commands.Bot(command_prefix=get_prefix,
                      # help_command=None,
                      case_insensitive=True)

load_cogs(client)
client.run(TOKEN)
