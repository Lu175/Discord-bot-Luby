import discord
from discord.ext import commands
import Luby_info
import time


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

        START = time.time()
        msg_1 = await ctx.author.send("ping")
        END = time.time()
        ping_1 = END-START
        START = time.time()
        msg_2 = await ctx.author.send("ping")
        END = time.time()
        ping_2 = END-START
        START = time.time()
        msg_3 = await ctx.author.send("ping")
        END = time.time()
        ping_3 = END-START

        embed_ping.add_field(name='API Latency',
                             value=f'{round(self.bot.latency * (10 ** 3))} ms',
                             inline=False)
        embed_ping.add_field(name='Latency',
                             value=f'1: {round(ping_1 * (10 ** 3))} ms\n'
                                   f'2: {round(ping_2 * (10 ** 3))} ms\n'
                                   f'3: {round(ping_3 * (10 ** 3))} ms',
                             inline=False)
        embed_ping.set_footer(text=self.Luby_footer)
        await ctx.send(embed=embed_ping)
        await msg_1.delete()
        await msg_2.delete()
        await msg_3.delete()
        await ctx.author.send("핑~ 핑~ 핑~")


def setup(bot):
    bot.add_cog(ShowPing(bot))
