import json
import random

from settings import *
from discord.ext.commands import *


def load_cogs(client):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename != '__init__.py':
            client.load_extension(f'cogs.{filename[:-3]}')


async def notify_user(member, author, message):
    if member is not None:
        channel = member.dm_channel
        if channel is None:
            channel = await member.create_dm()
        await channel.send(message)


def mods_or_owner():
    def check(ctx):
        return check_any(is_owner(),
                         has_role(MODERATOR_ROLE_NAME),
                         has_role('Admin'))

    return check(check)


def get_prefix(client, message):
    with open('prefixes.json', 'r') as json_file:
        prefixes = json.load(json_file)
    try:
        return prefixes[str(message.guild.id)]
    except AttributeError as ae:
        return '.'


def greeter(member):
    greetings = [f'Welcome {member}',
                 f"Hey everyone it's {member}",
                 f"How you doin' {member}",
                 f'{member} has joined! Cool, cool, cool, cool, cool! No doubt, no doubt, no doubt.']
    return random.choice(greetings)
