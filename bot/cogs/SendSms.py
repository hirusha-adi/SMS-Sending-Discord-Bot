import discord
import telnyx
from discord.ext import commands

from bot.database.manager import main
from bot.database.manager import telnyx_data


class OnMessage(commands.Cog, description="Handle the messages sent"):

    def __init__(self, client: commands.Bot):
        self.client = client

        telnyx.api_key = telnyx_data.api_key

    
    @commands.command()
    async def sms(self, ctx, number, *text):

        text  = " ".join(text)

        telnyx.Message.create(
            _from=telnyx_data.from_number,
            to=str(number),
            text=text
        )

        await ctx.send(f"Send SMS:\nFrom: {telnyx_data.from_number}\nTo: {number}\nBy {ctx.author.name}\nContent: ``` {text} ```")



def setup(client: commands.Bot):
    client.add_cog(OnMessage(client))
