import discord
from discord.ext import commands
import asyncio


class EatingBingSu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.play_w_bingSu = True
        self.bingSu_prefix = 's!'

    def is_bingSu_msg(self, message):
        return message.author.id == int(796053822371397642)

    @commands.command(name='빙수먹자')
    async def eat_bingSu(self, ctx):
        TIME_OUT = 3.0

        try:
            await ctx.channel.send('와! 빙수다~~ :yum:')
            await asyncio.sleep(5)
            await ctx.channel.send('(빙수 가게에 들어간다) 딸랑~(E)')
            await asyncio.sleep(2)
            await ctx.channel.send(self.bingSu_prefix+'점장')
            await self.bot.wait_for('message', check=self.is_bingSu_msg, timeout=TIME_OUT)
            await asyncio.sleep(2)
        except asyncio.TimeoutError:
            self.play_w_bingSu = False
            await ctx.channel.send('어.. 점장님 안 계신가요?')
            await asyncio.sleep(3)
            await ctx.channel.send('인스타 빙수 맛집이라해서 멀리서왔는데.. :sob:')
            await asyncio.sleep(4)
            await ctx.channel.send(':cry: 다음에 또 기회가 있으려나?')
        if self.play_w_bingSu:
            try:
                await ctx.channel.send('음.. 일단 메뉴판 부터!')
                await asyncio.sleep(2)
                await ctx.channel.send(self.bingSu_prefix+'빙수메뉴판')
                await self.bot.wait_for('message', check=self.is_bingSu_msg, timeout=TIME_OUT)
                await asyncio.sleep(2)
            except asyncio.TimeoutError:
                self.play_w_bingSu = False
                await ctx.channel.send('가게에 메뉴판이 없어요??\n장사 한두번 해보시나;;')
            if self.play_w_bingSu:
                try:
                    await ctx.channel.send('헉..! 민초!!!')
                    await asyncio.sleep(2)
                    await ctx.channel.send(':yum: 민초는 못참지 ㅋㅋ')
                    await asyncio.sleep(2)
                    await ctx.channel.send(self.bingSu_prefix+'빙수 민트초코설빙')
                    await self.bot.wait_for('message', check=self.is_bingSu_msg, timeout=TIME_OUT)
                    await asyncio.sleep(2)
                except asyncio.TimeoutError:
                    self.play_w_bingSu = False
                    await ctx.send("음...")
                if self.play_w_bingSu:
                    try:
                        await ctx.channel.send('아아.. 찬란한 광채~')
                        await asyncio.sleep(2)
                        await ctx.channel.send(self.bingSu_prefix+'주문 민트초코설빙')
                        await self.bot.wait_for('message', check=self.is_bingSu_msg, timeout=TIME_OUT)
                        await asyncio.sleep(2)
                    except asyncio.TimeoutError:
                        self.play_w_bingSu = False
                        await ctx.send("음...")
                    if self.play_w_bingSu:
                        await ctx.channel.send('빨리빨리 내와라~~ ><')


def setup(bot):
    bot.add_cog(EatingBingSu(bot))
