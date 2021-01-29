import discord
from discord.ext import commands
import Luby_info


class ShowInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Luby_color = Luby_info.Luby_color
        self.Luby_footer = Luby_info.Luby_footer

    @commands.command(name='info')
    async def _info(self, ctx):
        embed_info = discord.Embed(title='lu175.com',
                                   colour=self.Luby_color,
                                   url='https://lu175.com',
                                   description="""As you can see,\nLuby lives in computer, Raspberry pi 4.""")
        embed_info.set_thumbnail(url='https://lu175.com/pic/HaNyang_PNG-08.png')
        embed_info.set_image(url='https://lu175.com/pic/Rpi4.jpg')
        embed_info.set_footer(text=self.Luby_footer)
        await ctx.send(embed=embed_info)


def setup(bot):
    bot.add_cog(ShowInfo(bot))
