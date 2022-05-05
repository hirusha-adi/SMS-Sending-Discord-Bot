import platform

import discord
from discord.ext import commands

from bot.database.manager.blacklisted import addGuild, addUser, addChannel
from bot.database.manager.blacklisted import blacklisted_channels_all_lines, blacklisted_guilds_all_lines, blacklisted_users_all_lines
from bot.database.manager.main import admins


class Base(commands.Cog, description="Main stuff related to the bot"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'[*] Python Version: {platform.python_version()}')
        print(f'[*] Discord.py API Version: {discord.__version__}')
        print(f'[*] Logged in as {self.client.user} | {self.client.user.id}')

        await self.client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=f'{len(self.client.guilds)} servers!'
            )
        )
        print(f'[*] Bot is ready to be used!')

    @commands.command()
    async def blacklist(self, ctx, sub_cat, id):
        if ctx.author.id in admins:
            user_list = ("user", "u")
            channel_list = ("channel", "ch", "c")
            guild_list = ("guild", "g", "server", "s")

            if sub_cat in user_list:
                addUser(str(id))
                await ctx.send(f'Added {id} to the blacklisted users list')
                await ctx.send(f'New length of blacklisted users list: {len(blacklisted_users_all_lines)}')

            elif sub_cat in channel_list:
                addChannel(str(id))
                await ctx.send(f'Added {id} to the blacklisted channels list')
                await ctx.send(f'New length of blacklisted channels list: {len(blacklisted_channels_all_lines)}')

            elif sub_cat in guild_list:
                addGuild(str(id))
                await ctx.send(f'Added {id} to the blacklisted guild list')
                await ctx.send(f'New length of blacklisted guild list: {len(blacklisted_guilds_all_lines)}')

            else:
                await ctx.send('Please mention a category: ( user, channel, guild )')
        else:
            await ctx.send("You do not have permission to use this command!")


def setup(client: commands.Bot):
    client.add_cog(Base(client))
