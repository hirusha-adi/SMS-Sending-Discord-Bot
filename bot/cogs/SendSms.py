import discord
import telnyx
from discord.ext import commands
from datetime import datetime

from bot.database.manager import main
from bot.database.manager import telnyx_data


class SendSMS(commands.Cog, description="Send messages"):

    def __init__(self, client: commands.Bot):
        self.client = client

        telnyx.api_key = telnyx_data.api_key

    @commands.command()
    async def sms(self, ctx, number, *text):
        """
        Usage -->
            >sms <to_number> *[text]

        Example -->
            >sms +12345678910 any text that comes after the phone number to be sent will be the content of the message

        Telynx API Documentation -->
            https://developers.telnyx.com/docs/v2/messaging/quickstarts/sending-sms-and-mms?lang=python
        """

        text = " ".join(text)

        try:
            telnyx.Message.create(
                from_=telnyx_data.from_number,
                to=str(number),
                text=text
            )
        except Exception as _err:
            embed = discord.Embed(title="Send SMS",
                                  timestamp=datetime.utcnow(),
                                  description=f"```{_err}```",
                                  color=0x00ffff)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
            return

        embed = discord.Embed(title="Send SMS",
                              timestamp=datetime.utcnow(),
                              color=0x00ffff)
        embed.set_author(
            name=str(self.client.user.name),
            icon_url=str(self.client.user.avatar_url)
        )
        embed.add_field(
            name="From",
            value=f"{telnyx_data.from_number}",
            inline=False
        )
        embed.add_field(
            name="To",
            value=f"{number}",
            inline=False
        )
        embed.add_field(
            name="By",
            value=f"{ctx.author.name}",
            inline=False
        )
        embed.add_field(
            name="Content",
            value=f"{text}",
            inline=False
        )
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(SendSMS(client))
