import json
import discord

from utils import get_prefix, greeter
from discord.ext.commands import *
from settings import DEFAULT_USER_ROLE_NAME


class Activities(Cog):
    def __init__(self, client):
        self.client = client
        print(f'{type(self).__name__} cog has been loaded.')

    @Cog.listener()
    async def on_ready(self):
        print(f'Bot has started and logged in as {self.client.user.name}')
        activity = discord.Activity(name=f'type .help', type=discord.ActivityType.playing)
        await self.client.change_presence(activity=activity)

    @Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name='general')
        await channel.send(greeter(member.mention))
        print(member.display_name)

    @Cog.listener()
    async def on_guild_join(self, guild):
        with open('prefixes.json', 'r') as json_file:
            prefixes = json.load(json_file)
        prefixes[str(guild.id)] = '.'

        with open('prefixes.json', 'w') as json_file:
            json.dump(prefixes, json_file, indent=4)

    @Cog.listener()
    async def on_guild_remove(self, guild):
        with open('prefixes.json', 'r') as json_file:
            prefixes = json.load(json_file)
        prefixes.pop(str(guild.id))

        with open('prefixes.json', 'w') as json_file:
            json.dump(prefixes, json_file, indent=4)

    @Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server')


def setup(client):
    client.add_cog(Activities(client))
