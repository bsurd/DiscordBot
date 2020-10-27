import discord

from utils import get_prefix, greeter
from discord.ext.commands import *
from settings import USER_ROLE_NAME


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
    async def on_command_error(self, ctx, err):
        print(err)
        await ctx.send('Please check help section to verify command usage.')

    @Cog.listener()
    async def on_missing_permissions_error(self, ctx, err):
        print(err)
        await ctx.send('You do not have enough permissions to perform this action.')

    @Cog.listener()
    async def on_member_join(self, member):
        # channel = member.Guild.system_channel
        print(member.Guild.get_role(USER_ROLE_NAME))
        role = discord.utils.get(member.Guild.roles, name=USER_ROLE_NAME)
        await member.add_roles(role, reason='Automatic role assignment', automatic=True)
        print(f'{member} joined and was given the role {role}')
        # if channel is not None:
        #     await channel.send(greeter(member.mention))


def setup(client):
    client.add_cog(Activities(client))
