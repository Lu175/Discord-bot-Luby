import discord
from discord.ext import commands
import func_Lu175 as FLU


class AdminCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='dd')
    @commands.has_permissions(administrator=True)
    async def _clear(self, ctx, amount=0):
        replied_msg = await FLU.get_replied_msg(bot=self.bot, context=ctx)
        if replied_msg:
            await ctx.channel.purge(after=replied_msg)
            await replied_msg.delete()
        else:
            await ctx.message.delete()
            if amount <= 0:
                await ctx.channel.send(f'사용법은 다음과 같습니다!\n`./dd (삭제할 메세지 개수 (N > 0))`')
            else:
                await ctx.channel.purge(limit=amount)

    # Fake commands

    @commands.command(name='kick')
    async def fake_kick(self, ctx, user: discord.User = None):
        if user is None:
            await ctx.send(f"<@{ctx.author.id}>님, 누구를 **KICK** 하시겠습니까?")
        else:
            await ctx.send(f"<@{user.id}>님이 <@{ctx.author.id}>님에 의해 **KICK** 되셨습니다.")

    @commands.command(name='ban')
    async def fake_ban(self, ctx, user: discord.User = None):
        if user is None:
            await ctx.send(f"<@{ctx.author.id}>님, 누구를 **BAN** 하시겠습니까?")
        else:
            await ctx.send(f"<@{user.id}>님이 <@{ctx.author.id}>님에 의해 **BAN** 되셨습니다.")


def setup(bot):
    bot.add_cog(AdminCommand(bot))


