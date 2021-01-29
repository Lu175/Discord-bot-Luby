import discord
from discord.ext import commands
import Luby_info


class ShowHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Luby_color = Luby_info.Luby_color
        self.Luby_footer = Luby_info.Luby_footer
        self.BLANK = str(Luby_info.BLANK)
        self.cmd_dict = {
            "user": ("./info", "./ping", "./빙수먹자", "./draw", "./draw_ex", "./omok", "./LM"),
            "admin": ("./dd", "./draw_coyang"),
            "Lu": ("./board", "./card_test", "./test", "./c_test")
        }

    @commands.group(aliases=['help', 'HELP'])
    async def help_group(self, ctx):
        if ctx.invoked_subcommand is None:
            embed_help = discord.Embed(title=f"네, {str(ctx.author)[:-5]}님!\n무엇을 도와드릴까요?",
                                       colour=self.Luby_color,
                                       description='루비의 명령어들 입니다!')
            embed_help.set_thumbnail(url='https://lu175.com/pic/swan_1.png')
            embed_help.add_field(name='`./help user`로 자세한 설명 보기',
                                 value=str(self.cmd_dict["user"])[1:-1].replace("'", ""),
                                 inline=False)
            embed_help.add_field(name=self.BLANK*2 + './ 없이 사용하는 명령어',
                                 value=self.BLANK*2 + f'<:AMGO_peaceful:791301834345545728> 암고: `ㅋㅋ`, `^^`, `~`, `!`, `ㅜ`, `.`  ex) 암고 ㅋㅋ\n'
                                       + self.BLANK*2 + f'<:JASGO:800032661505572864> 자스고: `~`, `!`, `ㅜ`, `.`, `#`  ex) 자스고 ~~~!!\n'
                                       + self.BLANK*2 + f'<:AKUMA_666:800354093242515457> 악마: `.`  ex) 악마 ...\n'
                                       + self.BLANK,
                                 inline=False)
            embed_help.add_field(name='`./help admin`으로 자세한 설명 보기',
                                 value=str(self.cmd_dict["admin"])[1:-1].replace("'", "")
                                       + "\n" + self.BLANK,
                                 inline=False)
            embed_help.add_field(name='`./help Lu`로 자세한 설명 보기',
                                 value=str(self.cmd_dict["Lu"])[1:-1].replace("'", ""),
                                 inline=False)
            embed_help.set_footer(text=self.Luby_footer)
            await ctx.reply(embed=embed_help, mention_author=True)

    @help_group.command(name='user')
    async def help_user(self, ctx):
        embed_help = discord.Embed(title=f"네, {str(ctx.author)[:-5]}님!\n무엇을 도와드릴까요?",
                                   colour=self.Luby_color,
                                   description='모든 user가 사용가능한 명령어들 입니다!')
        embed_help.set_thumbnail(url='https://lu175.com/pic/swan_1.png')

        help_exp = [
            "루비는 어디에 살고 있을까요?",
            "루비는 몇 초간 밀당할까요?",
            "루비에게 맛있는 빙수를 먹여보세요!",
            "'-'와 숫자들(1~8)로 그림을 그린 후 답장으로 './draw'하기!",
            "'./draw'의 예시를 보여드릴게요~",
            "오목 게임하기! (13 x 13)",
            "Lu175님의 음악 리스트!"]

        for idx in range(len(self.cmd_dict["user"])):
            embed_help.add_field(name=f'`{self.cmd_dict["user"][idx]}`', value=help_exp[idx], inline=False)
        embed_help.add_field(name='./ 없이 사용하는 명령어', value='`암고`, `자스고`, `악마`', inline=False)

        embed_help.set_footer(text=self.Luby_footer)
        await ctx.reply(embed=embed_help, mention_author=True)

    @help_group.command(name='admin')
    async def help_user(self, ctx):
        embed_help = discord.Embed(title=f"네, {str(ctx.author)[:-5]}님!\n무엇을 도와드릴까요?",
                                   colour=self.Luby_color,
                                   description='admin만 사용 가능한 명령어들 입니다!')
        embed_help.set_thumbnail(url='https://lu175.com/pic/swan_1.png')

        help_exp = [
            "Dummy",
            "Dummy"]

        for idx in range(len(self.cmd_dict["admin"])):
            embed_help.add_field(name=f'`{self.cmd_dict["admin"][idx]}`', value=help_exp[idx], inline=False)

        embed_help.set_footer(text=self.Luby_footer)
        await ctx.reply(embed=embed_help, mention_author=True)

    @help_group.command(name='Lu')
    async def help_user(self, ctx):
        embed_help = discord.Embed(title=f"네, {str(ctx.author)[:-5]}님!\n무엇을 도와드릴까요?",
                                   colour=self.Luby_color,
                                   description='Lu님만 사용 가능한 명령어들 입니다!')
        embed_help.set_thumbnail(url='https://lu175.com/pic/swan_1.png')

        help_exp = [
            "Dummy",
            "Dummy",
            "Dummy",
            "Dummy",
            "Dummy"]

        for idx in range(len(self.cmd_dict["Lu"])):
            embed_help.add_field(name=f'`{self.cmd_dict["Lu"][idx]}`', value=help_exp[idx], inline=False)

        embed_help.set_footer(text=self.Luby_footer)
        await ctx.reply(embed=embed_help, mention_author=True)


def setup(bot):
    bot.add_cog(ShowHelp(bot))
