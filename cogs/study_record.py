import discord
from discord.ext import commands
import func_Lu175 as FLU
import Luby_info
import asyncio
from time import time


def make_time_str(time_sec):
    return str(int(time_sec // 3600)) + '시간 ' + str(int((time_sec % 3600) // 60)) + '분'


class StudyRecord(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.eeLu175_id = Luby_info.eeLu175_id
        self.Luby_color = Luby_info.Luby_color
        self.Luby_footer = Luby_info.Luby_footer
        self.NOW_STUDY = False
        self.showTimerEmbed = None
        self.START_TIME = None
        self.LAP_COUNT = 0
        self.LAP_TIME = []
        self.LAP_TIME_str = []
        self.REF_TIME = None
        self.NT_Emoji_URL = FLU.def_get_emoji_url('1f914', mode=3)
        self.T_Emoji_URL = FLU.def_get_emoji_url('667750969592774676', mode=1)

    def make_timerEmbed(self, ctx):
        embed_timer = discord.Embed(colour=self.Luby_color)
        embed_timer.set_thumbnail(url=self.T_Emoji_URL)
        embed_timer.add_field(name='Timer', value=f'{make_time_str(time() - self.REF_TIME)}', inline=False)
        if len(self.LAP_TIME_str) != 0:
            LAP_TIME_STR = '\n'.join(self.LAP_TIME_str)
            embed_timer.add_field(name=f'Laps  | counting: {self.LAP_COUNT}', value=f"{LAP_TIME_STR}", inline=False)
        embed_timer.set_footer(text=self.Luby_footer)
        embed_timer.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        return embed_timer

    async def timer(self, ctx, LAP=False, RESET=False):
        if LAP:
            self.NOW_STUDY = False
            self.LAP_TIME.insert(0, time())
            self.LAP_COUNT += 1
            if len(self.LAP_TIME_str) == 5:
                self.LAP_TIME_str.pop()
            self.LAP_TIME_str.insert(0, str(self.LAP_COUNT) +'. '+ make_time_str(self.LAP_TIME[0] - self.REF_TIME))
            self.REF_TIME = self.LAP_TIME[-1]
            await asyncio.sleep(1)
            self.NOW_STUDY = True
        elif RESET:
            self.LAP_TIME = []

        embed_timer = self.make_timerEmbed(ctx)
        self.showTimerEmbed = await ctx.send(embed=embed_timer)

        while self.NOW_STUDY:
            await asyncio.sleep(0.5)
            if (((time() - self.REF_TIME) % 3600) // 60) > 0:
                embed_timer = self.make_timerEmbed(ctx)
                await self.showTimerEmbed.edit(embed=embed_timer)
        await self.showTimerEmbed.delete()

    async def record_process(self, ctx):
        if not self.NOW_STUDY:
            self.NOW_STUDY = True
            await ctx.send('공부 시작!')
            self.START_TIME = time()
            self.REF_TIME = self.START_TIME
            await self.timer(ctx)
        elif self.NOW_STUDY:
            self.NOW_STUDY = False
            await ctx.send('공부 끝!')
            embed_timer_end = discord.Embed(colour=self.Luby_color)
            embed_timer_end.set_thumbnail(url=self.NT_Emoji_URL)
            embed_timer_end.add_field(name='총 공부시간', value=make_time_str(time() - self.START_TIME), inline=False)
            embed_timer_end.set_footer(text=self.Luby_footer)
            embed_timer_end.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed_timer_end)

    @commands.command(aliases=['TI', 'Ti', 'ti', '공부시작', '공부하자'])
    async def lets_study(self, ctx):
        if ctx.author.id == int(self.eeLu175_id):
            if not self.NOW_STUDY:
                await self.record_process(ctx)

    @commands.command(aliases=['L', 'l'])
    async def lap(self, ctx):
        if ctx.author.id == int(self.eeLu175_id):
            if self.NOW_STUDY:
                await self.timer(ctx, LAP=True)

    @commands.command(aliases=['D', 'd'])
    async def done(self, ctx):
        if ctx.author.id == int(self.eeLu175_id):
            if self.NOW_STUDY:
                await self.record_process(ctx)

            # RESET
            self.showTimerEmbed = None
            self.START_TIME = None
            self.LAP_COUNT = 0
            self.LAP_TIME = []
            self.LAP_TIME_str = []
            self.REF_TIME = None


def setup(bot):
    bot.add_cog(StudyRecord(bot))
