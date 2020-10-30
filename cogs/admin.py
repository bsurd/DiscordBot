from utils import mods_or_owner
from discord.ext.commands import *


class Admin(Cog):
    def __init__(self, client):
        self.client = client
        print(f'{type(self).__name__} cog has been loaded.')

    @mods_or_owner()
    @command(brief='Unloads cogs')
    async def unload(self, ctx, cog: str):
        try:
            self.client.unload_extension(cog)
        except Exception as e:
            await ctx.send('Could not unload {cog}')
        await ctx.send(f'{cog}  unloaded')

    @mods_or_owner()
    @command(brief='Loads cogs')
    async def load(self, ctx, cog: str):
        try:
            self.client.load_extension(cog)
        except Exception as e:
            await ctx.send(f'Could not load {cog}')
        await ctx.send(f'{cog} loaded')

    @mods_or_owner()
    @command(brief='Reloads cogs')
    async def reload(self, ctx, cog: str):
        try:
            self.client.unload_extension(cog)
            self.client.load_extension(cog)
        except Exception as e:
            await ctx.send(f'Could not reload {cog}')
        await ctx.send(f'{cog} reloaded')


def setup(client):
    client.add_cog(Admin(client))
