import discord

from utils import mods_or_owner, notify_user
from discord.ext.commands import *


class Mod(Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None
        print(f'{type(self).__name__} cog has been loaded.')

    @mods_or_owner()
    @command(brief='Kicks a user from the server.')
    @guild_only()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None,
                   reason: str = 'You need a timeout.'):
        if member is not None:
            await notify_user(member, None, reason)
            await ctx.guild.kick(member, reason=reason)
            await ctx.send(f'{member} has been kicked.')
        else:
            await ctx.send('Please specify user to kick.')

    @mods_or_owner()
    @command(brief='Bans a user from the server.')
    @guild_only()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None,
                  reason: str = 'You are no longer allowed access to this server.'):
        if member is not None:
            await notify_user(member, None, reason)
            await ctx.guild.ban(member, reason=reason)
            await ctx.send(f'{member} has been banned.')
        else:
            await ctx.send('Please specify user to kick.')

    @mods_or_owner()
    @command(brief='Unbans a user from the server.')
    @guild_only()
    @has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
            else:
                await ctx.send(f'User {user} was not found in ban list.')

    @mods_or_owner()
    @command(brief='Mutes everyone in voice channel.')
    async def mute(self, ctx):
        voice_channel = ctx.author.voice.channel
        for member in voice_channel.members:
            await member.edit(mute=True)

    @mods_or_owner()
    @command(brief='Mutes everyone in voice channel.')
    async def unmute(self, ctx):
        voice_channel = ctx.author.voice.channel
        for member in voice_channel.members:
            await member.edit(mute=False)


def setup(client):
    client.add_cog(Mod(client))
