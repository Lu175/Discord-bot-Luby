import discord
from discord.ext import commands
import Luby_info
import re


class ZoomingEmoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Luby_color = Luby_info.Luby_color
        self.Luby_footer = Luby_info.Luby_footer
        self.unicodeEmoji = Luby_info.unicodeEmoji

    @commands.Cog.listener()
    async def on_message(self, message):
        A_Custom_Emoji_list = re.findall(r'<a:\w*:\d*>', message.content)
        if len(A_Custom_Emoji_list) == 1:
            if A_Custom_Emoji_list[0] == message.content:
                # https://cdn.discordapp.com/emojis/<Emoji_id>.gif?v=1
                Emoji_id = (A_Custom_Emoji_list[0].split(":")[2])[:-1]
                embed_Emoji = discord.Embed(colour=self.Luby_color)
                # Emoji_URL = Luby.get_emoji(id=int(Emoji_id)).url
                Emoji_URL = "https://cdn.discordapp.com/emojis/" + Emoji_id + ".gif?v=1"
                embed_Emoji.set_image(url=Emoji_URL)
                embed_Emoji.set_footer(text=self.Luby_footer)
                embed_Emoji.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
                await message.delete()
                await message.channel.send(embed=embed_Emoji)

        Custom_Emoji_list = re.findall(r'<:\w*:\d*>', message.content)
        if len(Custom_Emoji_list) == 1:
            if Custom_Emoji_list[0] == message.content:
                # https://cdn.discordapp.com/emojis/<Emoji_id>.png
                Emoji_id = (Custom_Emoji_list[0].split(":")[2])[:-1]
                embed_Emoji = discord.Embed(colour=self.Luby_color)
                # Emoji_URL = Luby.get_emoji(id=int(Emoji_id)).url
                Emoji_URL = "https://cdn.discordapp.com/emojis/" + Emoji_id + ".png"
                embed_Emoji.set_image(url=Emoji_URL)
                embed_Emoji.set_footer(text=self.Luby_footer)
                embed_Emoji.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
                await message.delete()
                await message.channel.send(embed=embed_Emoji)

        if not (A_Custom_Emoji_list or Custom_Emoji_list):
            Non_words = "`~!@#$%^&*()-=_+[]{}\\|;'\",<.>/? "
            msg = message.content
            Emoji_for_send = ''

            if len(msg) == 3:
                if msg[2] == "\u20e3":  # case of number keys ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '#', '*']
                    Emoji_for_send += str(hex(ord(msg[0]))[2:])  # append "number"
                    Emoji_for_send += '-' + str(hex(ord(msg[2]))[2:])  # append "box"
            for rm in Non_words:
                msg = msg.replace(rm, '')  # remove Non_words
            filtered_msg = re.findall(r'\W*', msg)
            if (len(filtered_msg) == 2) and (filtered_msg[0] != ''):
                # https://twemoji.maxcdn.com/v/latest/72x72/<CODE>.png
                data_for_send = []
                for data in msg:
                    data_for_send.append(str(hex(ord(data))[2:]))
                if (len(data_for_send) == 2) and (data_for_send[1] == "fe0f"):
                    data_for_send.pop()  # remove "fe0f"
                Emoji_for_send = data_for_send[0]
                for data in data_for_send[1:]:
                    Emoji_for_send += '-' + data
            if Emoji_for_send in self.unicodeEmoji:
                # It's available
                embed_Emoji = discord.Embed(colour=self.Luby_color)
                Emoji_URL = "https://twemoji.maxcdn.com/v/latest/72x72/" + Emoji_for_send + ".png"
                embed_Emoji.set_image(url=Emoji_URL)
                embed_Emoji.set_footer(text=self.Luby_footer)
                embed_Emoji.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
                await message.delete()
                await message.channel.send(embed=embed_Emoji)


def setup(bot):
    bot.add_cog(ZoomingEmoji(bot))
