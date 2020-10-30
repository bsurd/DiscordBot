import random
import discord

from discord.ext.commands import *


class Help(Cog):
    def __init__(self, client):
        self.client = client
        print(f'{type(self).__name__} cog has been loaded.')

    # @command(name='help', aliases=['h', 'commands'], description='The help command!')
    @command()
    async def help2(self, ctx):
        help_embed = discord.Embed(title='Help Section', colour=random.choice([discord.Color.blue(),
                                                                               discord.Color.dark_blue(),
                                                                               discord.Color.purple(),
                                                                               discord.Color.dark_purple(),
                                                                               discord.Color.magenta(),
                                                                               discord.Color.dark_magenta(),
                                                                               discord.Color.gold(),
                                                                               discord.Color.dark_gold(),
                                                                               discord.Color.orange(),
                                                                               discord.Color.dark_orange(),
                                                                               discord.Color.red(),
                                                                               discord.Color.dark_red(),
                                                                               discord.Color.lighter_grey(),
                                                                               discord.Color.dark_grey(),
                                                                               discord.Color.light_grey(),
                                                                               discord.Color.darker_grey(),
                                                                               discord.Color.greyple()]))
        help_embed.set_thumbnail(url=ctx.author.avatar_url)

        # cogs = [c for c in self.client.cogs.keys()]
        # cogs.remove('listeners')

        await ctx.author.send(embed=help_embed)


def setup(client):
    client.add_cog(Help(client))
