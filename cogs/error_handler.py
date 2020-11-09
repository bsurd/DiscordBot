from discord.ext.commands import *


class ErrorHandler(Cog):
    def __init__(self, client):
        self.client = client
        print(f'{type(self).__name__} cog has been loaded.')

    @Cog.listener()
    async def on_command_error(self, ctx, err):
        print(err)
        await ctx.send('Please check help section to verify command usage.')

    @Cog.listener()
    async def on_missing_permissions_error(self, ctx, err):
        print(err)
        await ctx.send('You do not have enough permissions to perform this action.')


def setup(client):
    client.add_cog(ErrorHandler(client))
