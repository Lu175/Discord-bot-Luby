import discord
from discord.ext import commands
import Luby_ctrl
import func_Lu175 as FLU
import random as rnd


class ReplyQuotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.zoomEmojiEmbedFlag = False
        self.CURR_QUOTE = None
        self.LAST_QUOTE = None
        self.QUOTES = [
            '삶이 있는 한 희망은 있다.\n-키케로',
            '산다는것 그것은 치열한 전투이다.\n-로망로랑',
            '피할수 없으면 즐겨라\n–로버트 엘리엇',
            '먼저핀꽃은 먼저진다. 남보다 먼저 공을 세우려고 조급히 서둘것이 아니다.\n–채근담',
            '꿈을 계속 간직하고 있으면 반드시 실현할 때가 온다.\n-괴테',
            '좋은 성과를 얻으려면 한 걸음 한 걸음이 힘차고 충실하지 않으면 안 된다.\n-단테',
            '삶을 사는 데는 단 두가지 방법이 있다.\n하나는 기적이 전혀 없다고 여기는 것이고 또 다른 하나는 모든 것이 기적이라고 여기는방식이다.\n–알베르트 아인슈타인'
        ]

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        else:
            replied_msg = await FLU.get_replied_msg(bot=self.bot, message=message)
            if replied_msg:
                if replied_msg.embeds is not None:
                    if replied_msg.embeds[0].author != self.bot.user:
                        self.zoomEmojiEmbedFlag = True
                if Luby_ctrl.REPLY_QUOTE and (replied_msg.author == self.bot.user) and (not self.zoomEmojiEmbedFlag):
                    reply_str = f'`오늘도 빛나는 {message.author.display_name}님, 파이팅입니다 !!`\n'
                    if self.LAST_QUOTE:  # if it is not None
                        while self.LAST_QUOTE == self.CURR_QUOTE:
                            self.CURR_QUOTE = rnd.randint(0, len(self.QUOTES) -1)
                    else:
                        self.CURR_QUOTE = rnd.randint(0, len(self.QUOTES) -1)
                    quote_str = self.QUOTES[self.CURR_QUOTE]
                    await message.reply(reply_str + quote_str, mention_author=True)


def setup(bot):
    bot.add_cog(ReplyQuotes(bot))
