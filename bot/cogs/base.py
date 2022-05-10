import platform

import discord
from discord.ext import commands
from datetime import datetime

from database.manager.main import prefix, admins


class Base(commands.Cog, description="Main stuff related to the bot"):

    def __init__(self, client: commands.Bot):
        self.client = client
        self.client.remove_command('help')

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
    async def help(self, ctx):
        final_help = f"{prefix}sms <to_number> *[text]\n"
        if ctx.author.id in admins:
            final_help += f"{prefix}change_number <number>\n"
            final_help += f"{prefix}change_api_key <api_key>\n"

        embed = discord.Embed(title=f"Help for {self.client.user.name}",
                              description="All commands usage",
                              timestamp=datetime.utcnow(),
                              color=0x00ffff)
        embed.set_author(
            name=str(self.client.user.name),
            icon_url=str(self.client.user.avatar_url)
        )
        embed.add_field(
            name="Commands",
            value=final_help,
            inline=False
        )
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Base(client))
