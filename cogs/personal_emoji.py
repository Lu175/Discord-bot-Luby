import discord
from discord.ext import commands
import Luby_info


class ReleaseLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Activity_name = Luby_info.Luby_Activity_name

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        else:
            if message.content[:2] == '냠냠':
                await message.channel.send('<:Green_chicken:787024373457747968> <:Green_chicken:787024373457747968> <:Green_chicken:787024373457747968> <:Green_chicken:787024373457747968>')

            if message.content[:2] == '암고':
                # Filtering
                filtered_msg = ''
                for char in message.content[2:len(message.content)]:
                    if char != ' ':
                        filtered_msg += char
                # MSG send
                msg_for_send = ''
                if filtered_msg == 'ㅋㅋ':
                    await message.channel.send("""\
    <:AMGO_peaceful:791301834345545728><:AMGO_peaceful:791301834345545728><:AMGO_peaceful:791301834345545728><:AMGO_peaceful:791301834345545728><:BLANK:798862760909602836><:AMGO_peaceful:791301834345545728><:AMGO_peaceful:791301834345545728><:AMGO_peaceful:791301834345545728><:AMGO_peaceful:791301834345545728>
    <:BLANK:798862760909602836><:BLANK:798862760909602836><:BLANK:798862760909602836><:AMGO_peaceful:791301834345545728><:BLANK:798862760909602836><:BLANK:798862760909602836><:BLANK:798862760909602836><:BLANK:798862760909602836><:AMGO_peaceful:791301834345545728>
    <:AMGO_peaceful:791301834345545728><:AMGO_peaceful:791301834345545728><:AMGO_peaceful:791301834345545728><:AMGO_peaceful:791301834345545728><:BLANK:798862760909602836><:AMGO_peaceful:791301834345545728><:AMGO_peaceful:791301834345545728><:AMGO_peaceful:791301834345545728><:AMGO_peaceful:791301834345545728>
    <:BLANK:798862760909602836><:BLANK:798862760909602836><:BLANK:798862760909602836><:AMGO_peaceful:791301834345545728><:BLANK:798862760909602836><:BLANK:798862760909602836><:BLANK:798862760909602836><:BLANK:798862760909602836><:AMGO_peaceful:791301834345545728>
    """)
                elif filtered_msg == '^^':
                    await message.channel.send("""\
    <:BLANK:798862760909602836><:BLANK:798862760909602836><:AMGO_peaceful:791301834345545728><:BLANK:798862760909602836><:BLANK:798862760909602836><:BLANK:798862760909602836><:BLANK:798862760909602836><:BLANK:798862760909602836><:AMGO_peaceful:791301834345545728><:BLANK:798862760909602836><:BLANK:798862760909602836>
    <:BLANK:798862760909602836><:AMGO_peaceful:791301834345545728><:BLANK:798862760909602836><:AMGO_peaceful:791301834345545728><:BLANK:798862760909602836><:BLANK:798862760909602836><:BLANK:798862760909602836><:AMGO_peaceful:791301834345545728><:BLANK:798862760909602836><:AMGO_peaceful:791301834345545728><:BLANK:798862760909602836>
    <:AMGO_peaceful:791301834345545728><:BLANK:798862760909602836><:BLANK:798862760909602836><:BLANK:798862760909602836><:AMGO_peaceful:791301834345545728><:BLANK:798862760909602836><:AMGO_peaceful:791301834345545728><:BLANK:798862760909602836><:BLANK:798862760909602836><:BLANK:798862760909602836><:AMGO_peaceful:791301834345545728>
    """)
                else:
                    for text in filtered_msg:
                        if text == '~':
                            msg_for_send += '<:AMGO_peaceful:791301834345545728> '
                        if text == '!':
                            msg_for_send += '<:AMGO_angry:791303295540264960> '
                        if text == 'ㅜ':
                            msg_for_send += '<:AMGO_sad:791303907296280617> '
                        if text == '.':
                            msg_for_send += '<:AMGO_despair:791302162906480721> '
                    if msg_for_send != '':
                        await message.channel.send(msg_for_send)

            if message.content[:3] == '자스고':
                # Filtering
                filtered_msg = ''
                for char in message.content[2:len(message.content)]:
                    if char != ' ':
                        filtered_msg += char
                # MSG send
                msg_for_send = ''
                for text in filtered_msg:
                    if text == '~':
                        msg_for_send += '<:JASGO_peaceful:798218621460807690> '
                    if text == '!':
                        msg_for_send += '<:JASGO_angry:798218621326983179> '
                    if text == 'ㅜ':
                        msg_for_send += '<:JASGO_sad:798218621225795605> '
                    if text == '.':
                        msg_for_send += '<:JASGO_despair:798218659670917151> '
                    if text == '#':
                        msg_for_send += '<:JASGO:800032661505572864> '
                if msg_for_send != '':
                    await message.channel.send(msg_for_send)

            if message.content[:2] == '악마':
                # Filtering
                filtered_msg = ''
                for char in message.content[2:len(message.content)]:
                    if char != ' ':
                        filtered_msg += char
                # MSG send
                msg_for_send = ''
                for text in filtered_msg:
                    if text == '.':
                        msg_for_send += '<:AKUMA_666:800354093242515457> '
                if msg_for_send != '':
                    await message.channel.send(msg_for_send)


def setup(bot):
    bot.add_cog(ReleaseLog(bot))
