import discord

from utils import notify_user
from discord.ext.commands import *


class Basic(Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None
        print(f'{type(self).__name__} cog has been loaded.')

    @command(brief='Greets you.')
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}!')
        else:
            await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member

    @command(brief='Pokes user.')
    async def poke(self, ctx, member: discord.Member = None):
        if member is not None:
            message = f'{ctx.author.name} poked you!!!'
            await notify_user(member, ctx.author.name, message)
        else:
            await ctx.send('Please use @mention to poke someone.')

    # @command(brief='Creates a channel invite.')
    # async def invite(self, ctx):
    #     link = ctx.channel.create_invite(max_age=30)
    #     await ctx.send(f'Invite link: {link}')


def setup(client):
    client.add_cog(Basic(client))
