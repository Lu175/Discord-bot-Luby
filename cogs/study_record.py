import discord
from discord.ext import commands
import Luby_info
import asyncio
from time import time


def make_time_str(time_sec):
    return str(int(time_sec // 3600)) + '시간 ' + str(int((time_sec % 3600) // 60)) + '분 ' + str(round(time_sec % 60)) + '초'


class StudyRecord(commands.Cog):
    def __init__(self, bot):
        self.eeLu175_id = Luby_info.eeLu175_id
        self.NOW_STUDY = False
        self.showTimerMsg = None
        self.START_TIME = None
        self.LAP_TIME = []
        self.REF_TIME = None

    async def timer(self, ctx, LAP=False, RESET=False):
        if LAP:
            self.NOW_STUDY = False
            self.LAP_TIME.append(time())
            await ctx.send(f'Lap Time: {make_time_str(self.LAP_TIME[-1] - self.REF_TIME)}')
            self.REF_TIME = self.LAP_TIME[-1]
            await asyncio.sleep(1)
            self.NOW_STUDY = True
        elif RESET:
            self.LAP_TIME = []

        self.showTimerMsg = await ctx.send(f'Timer: {make_time_str(time() - self.REF_TIME)}')
        while self.NOW_STUDY:
            await asyncio.sleep(1)
            await self.showTimerMsg.edit(content=f'Timer: {make_time_str(time() - self.REF_TIME)}')
        await self.showTimerMsg.delete()

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
            await ctx.send(f'총 공부시간: `'+make_time_str(time() - self.START_TIME)+'`')

    @commands.command(aliases=['공부시작', '공부하자'])
    async def lets_study(self, ctx):
        if ctx.author.id == int(self.eeLu175_id):
            if not self.NOW_STUDY:
                await self.record_process(ctx)

    @commands.command()
    async def lap(self, ctx):
        if ctx.author.id == int(self.eeLu175_id):
            if self.NOW_STUDY:
                await self.timer(ctx, LAP=True)

    @commands.command()
    async def done(self, ctx):
        if ctx.author.id == int(self.eeLu175_id):
            if self.NOW_STUDY:
                await self.record_process(ctx)


def setup(bot):
    bot.add_cog(StudyRecord(bot))
