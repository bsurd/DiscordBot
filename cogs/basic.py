import discord

from utils import notify_user
from discord.ext.commands import *


class Basic(Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None
        print(f'{type(self).__name__} cog has been loaded.')

    @command(brief='Greets you')
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}!')
        else:
            await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member

    @command(brief='Pokes user')
    async def poke(self, ctx, member: discord.Member = None):
        if member is not None:
            message = f'{ctx.author.name} poked you!!!'
            await notify_user(member, ctx.author.name, message)
        else:
            await ctx.send('Please use @mention to poke someone.')

    @command(brief='Displays user avatar')
    async def avatar(self, ctx, member: discord.Member = None):
        if member is not None:
            show_avatar = discord.Embed(colour=discord.Color.dark_teal())
            show_avatar.set_image(url=member.avatar_url)
            await ctx.send(embed=show_avatar)
        else:
            await ctx.send('You need to mention someone!')

    @command(brief='Creates a channel invite')
    async def invite(self, ctx, member: discord.Member = None):
        link = await ctx.channel.create_invite(max_age=300, unique=True)
        if member is not None:
            await notify_user(member, ctx.author.name, f'Invite link {link}')
        else:
            await ctx.author.send(f'Invite link: {link}')


def setup(client):
    client.add_cog(Basic(client))
