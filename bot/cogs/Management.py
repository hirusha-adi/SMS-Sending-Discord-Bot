import discord
import telnyx
from discord.ext import commands

from bot.database.manager import main
from bot.database.manager import telnyx_data
from bot.database.manager import telnyx_manager


class Management(commands.Cog, description="Manage Discord Bot. Only admins can run these commands"):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def change_number(self, ctx, number):
        if int(ctx.author.id) in main.admins:
            telnyx_manager.update(from_number=str(number))
            await ctx.send(f"Updated")
        
        else:
            await ctx.send(f"You do not have permission to change the number")

def setup(client: commands.Bot):
    client.add_cog(Management(client))
