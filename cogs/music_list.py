import discord
from discord.ext import commands
import Luby_info


class MusicList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Luby_color = Luby_info.Luby_color
        self.Luby_footer = Luby_info.Luby_footer

    @commands.command(name='LM')
    async def lu175_music(self, ctx):
        embed_Lu175_Music = discord.Embed(title='Lu175의 음악리스트입니다!',
                                          colour=self.Luby_color,
                                          description='복붙 ㄱㄱ')
        embed_Lu175_Music.set_footer(text=self.Luby_footer)
        embed_Lu175_Music.add_field(name='어과음', value='?p https://youtube.com/playlist?list=PLVW_htI5V49iz9Z38iaKOoS8JByghA0cb', inline=False)
        embed_Lu175_Music.add_field(name='Araha', value='?!p https://youtube.com/playlist?list=PLVW_htI5V49iz9Z38iaKOoS8JByghA0cb', inline=False)
        await ctx.reply(embed=embed_Lu175_Music, mention_author=True)


def setup(bot):
    bot.add_cog(MusicList(bot))
