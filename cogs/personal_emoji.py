import discord
from discord.ext import commands
import Luby_info
import func_Lu175 as FLU


class ReleaseLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Luby_color = Luby_info.Luby_color
        self.Luby_footer = Luby_info.Luby_footer
        self.Activity_name = Luby_info.Luby_Activity_name

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        else:
            if message.content == '코딩해':
                replied_msg = await FLU.get_replied_msg(bot=self.bot, message=message)
                embed_Emoji = discord.Embed(colour=self.Luby_color)
                # Emoji_URL = Luby.get_emoji(id=int(Emoji_id)).url
                # <a:coco:806893600591446017>
                Emoji_URL = "https://cdn.discordapp.com/emojis/806893600591446017.gif?v=1"
                embed_Emoji.set_image(url=Emoji_URL)
                embed_Emoji.set_footer(text=self.Luby_footer)
                embed_Emoji.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
                await message.delete()
                if replied_msg is not None:
                    if replied_msg.embeds:
                        if replied_msg.embeds[0].author != self.bot.user:
                            embed_author_id = replied_msg.embeds[0].author.icon_url.split('/')[4]
                            await message.channel.send(f'<@!{embed_author_id}>\n')
                            await message.channel.send(embed=embed_Emoji)
                    else:
                        await replied_msg.reply(embed=embed_Emoji)
                else:
                    await message.channel.send(embed=embed_Emoji)

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
