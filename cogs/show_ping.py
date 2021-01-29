import discord
from discord.ext import commands
import Luby_info


class ShowPing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Luby_color = Luby_info.Luby_color
        self.Luby_footer = Luby_info.Luby_footer

    @commands.command()
    async def ping(self, ctx):
        embed_ping = discord.Embed(title='Ping ~ :incoming_envelope:',
                                   colour=self.Luby_color,
                                   description='**:mailbox_with_mail: Pong !**')

        START = ctx.message.created_at.timestamp()
        PING_MSG = await ctx.send("ping")
        END = PING_MSG.created_at.timestamp()
        PING_TIME = (END-START) % 3600

        embed_ping.add_field(name='API Latency',
                             value=f'{round(self.bot.latency * (10 ** 3))} ms',
                             inline=False)
        embed_ping.add_field(name='Latency',
                             value=f'{round(PING_TIME * (10 ** 3))} ms',
                             inline=False)
        embed_ping.set_footer(text=self.Luby_footer)
        await ctx.send(embed=embed_ping)
        await PING_MSG.delete()


def setup(bot):
    bot.add_cog(ShowPing(bot))
