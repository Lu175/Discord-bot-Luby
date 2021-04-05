from discord.ext import commands
import util.study_timer as cogsST


class TimerCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_id_list = []
        self.timer_list = []

    @commands.command(aliases=['Ti', 'ti', '공부시작', '공부하자'])
    async def cmd_study_timer(self, ctx):
        if ctx.author.id not in self.user_id_list:
            self.user_id_list.append(ctx.author.id)
            user_id_idx = self.user_id_list.index(ctx.author.id)
            self.timer_list.append(cogsST.StudyTimer())
            await ctx.message.delete()
            await self.timer_list[user_id_idx]._lets_study(ctx)

    @commands.command(aliases=['L', 'l', 'lap'])
    async def cmd_lap(self, ctx):
        if ctx.author.id in self.user_id_list:
            user_id_idx = self.user_id_list.index(ctx.author.id)
            await ctx.message.delete()
            await self.timer_list[user_id_idx]._lap(ctx)

    @commands.command(aliases=['D', 'd', 'done'])
    async def cmd_done(self, ctx):
        if ctx.author.id in self.user_id_list:
            user_id_idx = self.user_id_list.index(ctx.author.id)
            self.user_id_list[user_id_idx] = []
            del self.user_id_list[user_id_idx]
            await ctx.message.delete()
            await self.timer_list[user_id_idx]._done(ctx)
            del self.timer_list[user_id_idx]


def setup(bot):
    bot.add_cog(TimerCommand(bot))
