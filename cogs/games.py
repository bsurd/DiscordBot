import random

from discord.ext.commands import *


class Games(Cog):
    def __init__(self, client):
        self.client = client
        print(f'{type(self).__name__} cog has been loaded.')

    @command(name='8ball', aliases=['eightball', 'eight_ball'], brief='Gives advice',
             description='To use the command you must use the prefix together with the command '
                         'name, then leave an empty space followed by your question.')
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes, definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most Likely.',
                     'Outlook Is Good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     "Don't count on it.",
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very Doubtful.']
        await ctx.send(f'{ctx.author.mention} asked, shaking vigorously: **{question}**\n'
                       f'The 8ball has found your answer: **{random.choice(responses)}**')

    @command(brief='Flips a coin')
    async def coin(self, ctx):
        await ctx.send(random.choice(["Heads", "Tails"]))

    @command(brief='Rolls a dice')
    async def dice(self, ctx):
        await ctx.send(random.randrange(1, 6))


def setup(client):
    client.add_cog(Games(client))
