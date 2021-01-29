import discord
from discord.ext import commands
import asyncio
import func_Lu175 as FLU


class DrawingPixel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Emoji_paint_dict = {
                                    0: {
                                        '-': '⚫',
                                        '1': '⚪',
                                        '2': '🔴',
                                        '3': '🟠',
                                        '4': '🟡',
                                        '5': '🟢',
                                        '6': '🔵',
                                        '7': '🟣',
                                        '8': '🟤'
                                    },
                                    1: {
                                        '-': '⬛',
                                        '1': '⬜',
                                        '2': '🟥',
                                        '3': '🟧',
                                        '4': '🟨',
                                        '5': '🟩',
                                        '6': '🟦',
                                        '7': '🟪',
                                        '8': '🟫'
                                    }
                                }

    @commands.command()
    async def draw(self, ctx, pixel_shape=1, board=None, pixel_info=True):
        if (board is not None) or (ctx.message.reference is not None):
            if pixel_info:
                if pixel_shape == 0:
                    await ctx.channel.send('`동그란 픽셀을 사용할게요!`')
                elif pixel_shape == 1:
                    await ctx.channel.send('`네모난 픽셀을 사용할게요!`')
            else:
                pass

            if board is not None:
                paint = board
            else:
                replied_msg = await FLU.get_replied_msg(bot=self.bot, context=ctx)
                if replied_msg:
                    paint = replied_msg.content
                else:
                    await ctx.send("ERROR !!")
                    return
            paint_for_send = ''
            for char in paint:
                if char in self.Emoji_paint_dict[pixel_shape].keys():
                    paint_for_send += self.Emoji_paint_dict[pixel_shape][char]
                elif char == '\n':
                    paint_for_send += '\n'
                else:
                    pass

            if paint_for_send != '':
                try:
                    await ctx.channel.send(paint_for_send)
                except discord.errors.HTTPException:
                    await ctx.channel.send(':thinking: 이 그림은 좀 큰데요...?\n조금만 작게 그려주세요.')
            else:
                await ctx.channel.send(":eyes: 꼭꼭 숨어라, 튀어나온 픽셀 보인다~\n아, 저 지금 '-'랑 숫자들(1~8)이랑 같이 숨바꼭질 중이예요!\n같이 하실래요?")

    @commands.command()
    async def draw_ex(self, ctx):
        paint = """\
```
23-111-----76
34-1-------65
45-111-1-1-54
56-1----1--43
67-111-1-1-32
```
"""
        await ctx.channel.send('잘 보세요~')
        await asyncio.sleep(1)
        paint_msg = await ctx.channel.send(paint)
        await asyncio.sleep(1)
        await ctx.channel.send("이렇게 '-'와 숫자들(0~8)로 그림을 그리고!")
        await asyncio.sleep(1)
        reply_msg = await paint_msg.reply('./draw')
        await asyncio.sleep(1)
        await ctx.channel.send("그린 그림의 메세지에 './draw'라고 답장을 해주면~")
        await asyncio.sleep(1)

        replied_msg = await self.bot.get_channel(reply_msg.reference.channel_id).fetch_message(reply_msg.reference.message_id)
        paint_for_send = ''
        for char in replied_msg.content:
            if char in self.Emoji_paint_dict[1].keys():
                paint_for_send += self.Emoji_paint_dict[1][char]
            elif char == '\n':
                paint_for_send += '\n'
            else:
                pass
        await ctx.channel.send(paint_for_send)
        await asyncio.sleep(1)

        msg_for_send = '네모 픽셀 사용시\n`./draw` 또는 `./draw 1`\n'
        for char in self.Emoji_paint_dict[1].keys():
            msg_for_send += self.Emoji_paint_dict[1][char]
        await ctx.channel.send(msg_for_send)

        msg_for_send = '동그라미 픽셀 사용시\n`./draw 0`\n'
        for char in self.Emoji_paint_dict[0].keys():
            msg_for_send += self.Emoji_paint_dict[0][char]
        await ctx.channel.send(msg_for_send)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def draw_coyang(self, ctx, pixel_shape=1):
        pixel_coyang_1 = """\
111111111111111111111111111
111111111111111111111111111
111111111111111111-11111111
111111111111111111-11111111
1111--111111111111--1111111
11111-11111-----1-1-1111111
11111---1--11111--1--111111
"""
        pixel_coyang_2 = """\
1111--11-1111111-111-1--111
1111-1111111111111111-1-111
111--1111111111111111111-11
111-1111111111111---1111-11
11-11111---111111-1-1111-11
11-11111-1-11-111---1111-11
11-11111---11--11111111-111
"""
        pixel_coyang_3 = """\
11-111111111-----111111-111
111-1111111--111--11111-111
1111-11111111111111111-1111
11111--1111111111111--11111
1111111-------------1111111
111111111111111111111111111
111111111111111111111111111
"""

        await self.draw(ctx, pixel_shape=pixel_shape, board=pixel_coyang_1, pixel_info=True)
        await self.draw(ctx, pixel_shape=pixel_shape, board=pixel_coyang_2, pixel_info=False)
        await self.draw(ctx, pixel_shape=pixel_shape, board=pixel_coyang_3, pixel_info=False)
        await ctx.send("`모바일 환경이신 분들은 가로 화면을 이용해주세요~~`")


def setup(bot):
    bot.add_cog(DrawingPixel(bot))
