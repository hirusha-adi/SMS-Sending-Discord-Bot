import discord
import telnyx
from discord.ext import commands
from datetime import datetime

from bot.database.manager import main
from bot.database.manager import telnyx_data
from bot.database.manager import telnyx_manager


class Management(commands.Cog, description="Manage Discord Bot. Only admins can run these commands"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def change_number(self, ctx, number):
        if int(ctx.author.id) in main.admins:
            embed = discord.Embed(title="Bot Management",
                                  description="Change Phone Number",
                                  color=0x00ffff)
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.add_field(
                name="Old Phone Number",
                value=str(telnyx_data.from_number),
                inline=False
            )

            telnyx_data.from_number = str(number)
            telnyx_manager.update(from_number=str(number))

            embed.add_field(
                name="New Phone Number",
                value=str(telnyx_data.from_number),
                inline=False
            )
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                title="An error has occured",
                color=0xff0000,
                timestamp=datetime.utcnow()
            )
            embed.set_author(
                name=str(self.client.user.name),
                icon_url=str(self.client.user.avatar_url)
            )
            embed.add_field(
                name="Error:",
                value="You do not have permission to use this command",
                inline=False
            )
            embed.set_footer(text=f"Reuqested by {ctx.author.name}")
            await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Management(client))
