import os
import discord

from discord.ext.commands import *


class Utility(Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None
        print(f'{type(self).__name__} cog has been loaded.')

    @command(brief='Deletes messages.')
    @has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'{amount} messages have been cleared.')

    @command(brief='Returns latency, bot and client version.')
    async def version(self, ctx):
        my_embed = discord.Embed(title='Bot Version', description=f'The bot version is {os.getenv("BOT_VERSION")}',
                                 color=discord.Color.dark_teal())
        my_embed.add_field(name='Release Date', value=os.getenv('RELEASE_DATE'))
        my_embed.add_field(name='Latency', value=f'{round(self.client.latency * 1000)}ms')
        my_embed.set_footer(text=f'Client Version: {discord.__version__}')
        await ctx.send(embed=my_embed)


def setup(client):
    client.add_cog(Utility(client))
