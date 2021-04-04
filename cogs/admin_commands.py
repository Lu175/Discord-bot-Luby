import discord
from discord.ext import commands
import asyncio
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

    # @commands.command(aliases=['GP', 'Gp', 'gp'])
    # @commands.has_permissions(administrator=True)
    # async def ghost_ping(self, ctx, target_user_name=None):
    #     if target_user_name is None:
    #         GP_guide_msg = await ctx.send(f"누구를 **PING** 하시겠습니까?\n사용법: `./gp 닉네임`")
    #         await ctx.message.delete()
    #         await asyncio.sleep(1.5)
    #         await GP_guide_msg.delete()
    #     else:
    #         target_user = ctx.guild.get_member_named(target_user_name)
    #         print(target_user)
    #         if target_user is None:
    #             await ctx.send(f'<#{ctx.channel.id}>에서 `{target_user_name}`님을 찾을 수 없네요...')
    #             await ctx.message.delete()
    #         else:
    #             GP_msg = await ctx.send(f'<@{target_user.id}>')
    #             await ctx.message.delete()
    #             await asyncio.sleep(0.1)
    #             await GP_msg.delete()

    # Fake commands

    @commands.command(name='kick')
    async def fake_kick(self, ctx, target_user: discord.User = None):
        if target_user is None:
            await ctx.send(f"<@{ctx.author.id}>님, 누구를 **KICK** 하시겠습니까?")
        else:
            await ctx.send(f"<@{target_user.id}>님이 <@{ctx.author.id}>님에 의해 **KICK** 되셨습니다.")

    @commands.command(name='ban')
    async def fake_ban(self, ctx, target_user: discord.User = None):
        if target_user is None:
            await ctx.send(f"<@{ctx.author.id}>님, 누구를 **BAN** 하시겠습니까?")
        else:
            await ctx.send(f"<@{target_user.id}>님이 <@{ctx.author.id}>님에 의해 **BAN** 되셨습니다.")


def setup(bot):
    bot.add_cog(AdminCommand(bot))


