import discord
from discord.ext import commands
import Luby_info


class Testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.eeLu175_id = Luby_info.eeLu175_id
        self.Luby_color = Luby_info.Luby_color
        self.Luby_footer = Luby_info.Luby_footer
        self.Emoji_test_dict = {
            'shape': {
                'S': "<:Spade:800032748625592340>",
                'H': "<:Heart:800032761867927562>",
                'C': "<:Club:800032775759200376>",
                'D': "<:Diamond:800032787876937799>"
            },
            'black': {
                'A': "<:B_A:800474199792681000>",
                '2': "<:B_2:800474788907712542>",
                '3': "<:B_3:800476373159641148>",
                '4': "<:B_4:800476384426197022>",
                '5': "<:B_5:800476396484427816>",
                '6': "<:B_6:800476410698530826>",
                '7': "<:B_7:800476417993080841>",
                '8': "<:B_8:800476428209487882>",
                '9': "<:B_9:800476440927010836>",
                '10': "<:B_10:800478017860141058>",
                'J': "<:B_J:800478030149320775>",
                'Q': "<:B_Q:800478046259642378>",
                'K': "<:B_K:800478059924160542>"
            },
            'red': {
                'A': "<:R_A:800482738578260009>",
                '2': "<:R_2:800482753022787626>",
                '3': "<:R_3:800482766151221268>",
                '4': "<:R_4:800482778344980541>",
                '5': "<:R_5:800482789597249566>",
                '6': "<:R_6:800482800427073566>",
                '7': "<:R_7:800482815758041098>",
                '8': "<:R_8:800482829372620810>",
                '9': "<:R_9:800482843578204191>",
                '10': "<:R_10:800482854734790686>",
                'J': "<:R_J:800482868374929408>",
                'Q': "<:R_Q:800482886536396820>",
                'K': "<:R_K:800482899811631164>"
            }
        }

    @commands.command()
    async def card_test(self, ctx, embed=False):
        if ctx.author.id == int(self.eeLu175_id):
            for key_1 in self.Emoji_test_dict.keys():
                msg_for_send = ''
                for key_2 in self.Emoji_test_dict[key_1].keys():
                    msg_for_send += self.Emoji_test_dict[key_1][key_2]
                msg_for_send += '\n'

                if msg_for_send != '':
                    try:
                        if embed:
                            embed_draw = discord.Embed(colour=self.Luby_color)
                            embed_draw.add_field(name='This is Embed', value=f'{msg_for_send}', inline=False)
                            embed_draw.set_footer(text=self.Luby_footer)
                            await ctx.send(embed=embed_draw)
                        else:
                            await ctx.channel.send(msg_for_send)
                    except discord.errors.HTTPException:
                        await ctx.channel.send(':thinking: 이 그림은 좀 큰데요...?\n조금만 작게 그려주세요.')

    @commands.command(name='l')
    async def large_emoji(self, ctx, emoji: discord.Emoji):
        if ctx.author.id == int(self.eeLu175_id):
            await ctx.send(emoji.url)

    # @commands.command()
    # async def react(self, ctx, emoji: discord.PartialEmoji):
    #     if ctx.author.id == int(self.eeLu175_id):
    #         if emoji.is_custom_emoji():
    #             processed_emoji = self.bot.get_emoji(emoji.id)
    #         else:
    #             processed_emoji = emoji
    #         await ctx.message.add_reaction(processed_emoji)

    @commands.command()
    async def test(self, ctx):
        if ctx.author.id == int(self.eeLu175_id):
            embed_0 = discord.Embed(title='Google',
                                    colour=self.Luby_color,
                                    url='https://www.google.com',
                                    description='Description')
            embed_0.set_thumbnail(url='https://lu175.com/pic/HaNyang_PNG-34.png')
            embed_0.add_field(name='name', value=' 🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲', inline=False)
            if ctx.message.reference is not None:
                replied_msg = await self.bot.get_channel(ctx.message.reference.channel_id).fetch_message(ctx.message.reference.message_id)
                embed_0.add_field(name='replied_msg.content', value=replied_msg.content, inline=False)
                # embed_0.add_field(name='replied_msg.embeds', value=replied_msg.embeds, inline=False)
                # embed_0.add_field(name='replied_msg.embeds[0]', value=replied_msg.embeds[0], inline=False)
                # embed_0.add_field(name='replied_msg.embeds[0].fields', value=replied_msg.embeds[0].fields, inline=False)
                # count = 1
                # for field in replied_msg.embeds[0].fields:
                #     embed_0.add_field(name=f'for field in replied_msg.embeds[{count}].fields:', value=field, inline=False)
                #     embed_0.add_field(name='field.key()', value=field.key(), inline=False)
                #     count += 1
            embed_0.set_footer(text=self.Luby_footer)
            await ctx.send(embed=embed_0)

    @commands.command()
    async def c_test(self, ctx):
        if ctx.author.id == int(self.eeLu175_id):
            embed_0 = discord.Embed(title='Google',
                                    colour=self.Luby_color,
                                    url='https://www.google.com',
                                    description='Description')
            embed_0.set_image(url='https://lu175.com/pic/HaNyang_PNG-34.png')
            embed_0.add_field(name='Ping time', value=f'{round(self.bot.latency * (10 ** 3))} ms', inline=False)
            embed_0.add_field(name='AA', value='BB', inline=False)
            embed_0.add_field(name='AAA', value='BBB', inline=False)
            embed_0.set_footer(text=self.Luby_footer)
            await ctx.send(embed=embed_0)

    @commands.command()
    async def i_test(self, ctx):
        if ctx.author.id == int(self.eeLu175_id):
            embed_0 = discord.Embed(title='Google',
                                    colour=self.Luby_color,
                                    url='https://www.google.com',
                                    description='Description')
            embed_0.set_thumbnail(url='https://lu175.com/pic/HaNyang_PNG-34.png')
            embed_0.set_footer(text=self.Luby_footer)
            await ctx.send(embed=embed_0)

    # if ctx.author.id == int(Luby_info.eeLu175_id):
    #     pass
    # else:
    #     embed_on_test = discord.Embed(title='403 Forbidden',
    #                             colour=Lu_color_code,
    #                             description='죄송합니다!\n이 명령어는 현재 공사중입니다!')
    #     embed_on_test.set_thumbnail(url='https://lu175.com/pic/HaNyang_PNG-34.png')
    #     embed_on_test.add_field(name='NOW', value='TESTING...', inline=False)
    #     embed_on_test.set_footer(text=Luby_footer)
    #     await ctx.send(embed=embed_on_test)


def setup(bot):
    bot.add_cog(Testing(bot))
