import discord
import func_Lu175 as FLU
import Luby_info
import asyncio
from time import time


def make_time_str(time_sec):
    return str(int(time_sec // 3600)) + '시간 ' + str(int((time_sec % 3600) // 60)) + '분'


class StudyTimer:
    def __init__(self):
        self.USER_ID = 0
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
        self.TIMER_Emoji_URL = FLU.def_get_emoji_url('23f2', mode=3)
        self.NT_Emoji_URL = FLU.def_get_emoji_url('1f914', mode=3)
        self.T_Emoji_URL = FLU.def_get_emoji_url('667750969592774676', mode=1)

    def _timer_cmd_help(self, ctx):
        embed_timer_help = discord.Embed(colour=self.Luby_color, description='**Timer command**')
        embed_timer_help.set_thumbnail(url=self.TIMER_Emoji_URL)
        embed_timer_help.add_field(name='START (auto start)', value='`Ti`, `ti`, `공부시작`, `공부하자`', inline=False)
        embed_timer_help.add_field(name='Lap', value='`L`, `l`, `lap`', inline=False)
        embed_timer_help.add_field(name='END', value='`D`, `d`, `done`', inline=False)
        embed_timer_help.set_footer(text=self.Luby_footer)
        embed_timer_help.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        return embed_timer_help

    def _make_timerEmbed(self, ctx):
        embed_timer = discord.Embed(colour=self.Luby_color)
        embed_timer.set_thumbnail(url=self.T_Emoji_URL)
        embed_timer.add_field(name='Timer', value=f'{make_time_str(time() - self.REF_TIME)}', inline=False)
        if len(self.LAP_TIME_str) != 0:
            LAP_TIME_STR = '\n'.join(self.LAP_TIME_str)
            embed_timer.add_field(name=f'Laps  | counting: {self.LAP_COUNT}', value=f"{LAP_TIME_STR}", inline=False)
        embed_timer.set_footer(text=self.Luby_footer)
        embed_timer.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        return embed_timer

    async def _timer(self, ctx, LAP=False, RESET=False):
        if LAP:
            self.NOW_STUDY = False
            self.LAP_TIME.insert(0, time())
            self.LAP_COUNT += 1
            if len(self.LAP_TIME_str) == 5:
                self.LAP_TIME_str.pop()
            self.LAP_TIME_str.insert(0, str(self.LAP_COUNT) +'. '+ make_time_str(self.LAP_TIME[0] - self.REF_TIME))
            self.REF_TIME = self.LAP_TIME[0]
            await asyncio.sleep(1)
            self.NOW_STUDY = True
        elif RESET:
            self.LAP_TIME = []

        embed_timer = self._make_timerEmbed(ctx)
        self.showTimerEmbed = await ctx.send(embed=embed_timer)

        while self.NOW_STUDY:
            await asyncio.sleep(0.5)
            if (((time() - self.REF_TIME) % 3600) // 60) > 0:
                embed_timer = self._make_timerEmbed(ctx)
                await self.showTimerEmbed.edit(embed=embed_timer)
        await self.showTimerEmbed.delete()

    async def _timer_process(self, ctx):
        if not self.NOW_STUDY:
            self.NOW_STUDY = True
            await ctx.send('공부 시작!')
            embed_timer_help = self._timer_cmd_help(ctx)
            self.showTimerEmbed = await ctx.send(embed=embed_timer_help)
            self.START_TIME = time()
            self.REF_TIME = self.START_TIME
            await self._timer(ctx)
        elif self.NOW_STUDY:
            self.NOW_STUDY = False
            await ctx.send('공부 끝!')
            embed_timer_end = discord.Embed(colour=self.Luby_color)
            embed_timer_end.set_thumbnail(url=self.NT_Emoji_URL)
            embed_timer_end.add_field(name='총 공부시간', value=make_time_str(time() - self.START_TIME), inline=False)
            embed_timer_end.set_footer(text=self.Luby_footer)
            embed_timer_end.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed_timer_end)

    async def _lets_study(self, ctx):
        self.USER_ID = ctx.author.id
        if ctx.author.id == self.USER_ID:
            if not self.NOW_STUDY:
                await self._timer_process(ctx)

    async def _lap(self, ctx):
        if ctx.author.id == self.USER_ID:
            if self.NOW_STUDY:
                await self._timer(ctx, LAP=True)

    async def _done(self, ctx):
        if ctx.author.id == self.USER_ID:
            if self.NOW_STUDY:
                await self._timer_process(ctx)

            # RESET
            self.showTimerEmbed = None
            self.START_TIME = None
            self.LAP_COUNT = 0
            self.LAP_TIME = []
            self.LAP_TIME_str = []
            self.REF_TIME = None
