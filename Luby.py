import discord
from discord.ext import commands
import asyncio
import os.path
import Luby_info
import Luby_ctrl
import re
import func_Lu175 as FLU
import game_5mok as OM


# Luby_info
eeLu175_id = Luby_info.eeLu175_id
Luby_color = Luby_info.Luby_color
Luby_version = Luby_info.Luby_version
Luby_footer = Luby_info.Luby_footer
Luby_info.Luby_path = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")  # current abspath
print("Luby_path: " + Luby_info.Luby_path)


# Load Emoji list
f1 = open("C:/Users/jaehy/Desktop/# Lu-175/# Programming/Discord Bot/Discord-bot-Luby/twemoji_fileName.txt", 'r', encoding='utf-8')
unicodeEmoji = f1.read().split('\n')
f1.close()
unicodeEmoji.pop()
Luby_info.unicodeEmoji = unicodeEmoji


BLANK = chr(12644)  # '\u3164'
BLANK_unicode = chr(65039)  # '\uFE0F'
B_unicode_Emoji = chr(8205)  # '\u200D'

intents = discord.Intents.default()
intents.members = True

Luby = commands.Bot(command_prefix='./',
                    intents=intents,
                    help_command=None,
                    status=True)


# Bot Listen
@Luby.listen()
async def on_message(message):
    # don't respond to ourselves
    if message.author == Luby.user:
        return
    else:
        if message.content[:3] == '루님!':
            await message.channel.send(f'<@!622467096109908008>\n루님!! {message.author.display_name}님이 찾으세요!!', mention_author=True)


# Emoji for OmokBoard
Emoji_OmokBoard_dict = {
    '1': ':one:',
    '2': ':two:',
    '3': ':three:',
    '4': ':four:',
    '5': ':five:',
    '6': ':six:',
    '7': ':seven:',
    '8': ':eight:',
    '9': ':nine:',
    'r': ':keycap_ten:',
    's': '<:eleven:799094009419005962>',
    't': '<:twelve:799094008893931571>',
    'u': '<:thirteen:799094008949243924>',
    'a': ':regional_indicator_a:',
    'b': ':regional_indicator_b:',
    'c': ':regional_indicator_c:',
    'd': ':regional_indicator_d:',
    'e': ':regional_indicator_e:',
    'f': ':regional_indicator_f:',
    'g': ':regional_indicator_g:',
    'h': ':regional_indicator_h:',
    'i': ':regional_indicator_i:',
    'j': ':regional_indicator_j:',
    'k': ':regional_indicator_k:',
    'l': ':regional_indicator_l:',
    'm': ':regional_indicator_m:',
    '-': '<:BLANK:798862760909602836>',
    '=': '⬜',
    '!': '<:gray_large_square:798889465979994122>',
    'p': '🔴',
    'P': '<:omok_red_highlight:799324992818118716>',
    'q': '🟢',
    'Q': '<:omok_green_highlight:799324954822705152>'}


async def Omok_help(ctx):
    if ctx.author.id == int(eeLu175_id):
        embed_5mok_help = discord.Embed(title='🔴 오목 게임 매뉴얼! 🟢',
                                        colour=Luby_color,
                                        discription='아래의 내용으로 루비에게 `답장`해주세요 !')
        blank_board = await ctx.invoke(Luby.get_command('board'), show_help=True)
        embed_5mok_help.add_field(name='📕 좌표 입력하기 (`답장`)', value=BLANK + '`영문숫자`, `영문,숫자`, `숫자영문`, `숫자,영문`\n' + BLANK + '공백 추가 가능, 영문 대소문자 모두 가능',
                                  inline=False)
        embed_5mok_help.add_field(name='📙 좌표 입력예시', value=BLANK + '`g7`, `G,7`, `7G`, `7, g`\n' + BLANK + '(위의 입력은 모en 같은 위치를 나타냄)', inline=False)
        embed_5mok_help.add_field(name='📗 기권하기 (`답장`)', value=BLANK + '`GG` 또는 `gg`', inline=False)
        embed_5mok_help.add_field(name='📘 게임 보드 상태',
                                  value=f'{blank_board}',
                                  inline=False)
        embed_5mok_help.set_footer(text=Luby_footer)
        await ctx.send(embed=embed_5mok_help)


@Luby.command(name='omok')
async def play_Omok(ctx):
    def is_replyMsg_on_OMOK_CHANNEL(message):
        return (message.channel.id == Luby_ctrl.OMOK_CHANNEL_ID) and (message.reference is not None)

    def is_Msg_on_OMOK_CHANNEL(message):
        return message.channel.id == Luby_ctrl.OMOK_CHANNEL_ID

    def get_user_id_from_mention(message):
        Regex_pc = re.compile(r'<@!\d{18}>')
        Regex_mobile = re.compile(r'<@\d{18}>')
        if Regex_pc.fullmatch(message.content):
            return message.content[3:-1]  # return user.id
        elif Regex_mobile.fullmatch(message.content):
            return message.content[2:-1]  # return user.id

    TIME_OUT = 60.0  # sec
    OUT_FLAG = False

    if isinstance(ctx.channel, discord.channel.DMChannel):
        pass
    else:
        if Luby_ctrl.OMOK_CHANNEL_ID is None:
            Luby_ctrl.OMOK_CHANNEL_ID = ctx.channel.id
        else:
            await ctx.send(f"이미 <#{Luby_ctrl.OMOK_CHANNEL_ID}>에서 오목이 진행중입니다!")

        if Luby_ctrl.REPLY_QUOTE:
            Luby_ctrl.REPLY_QUOTE = False
            while True:
                await ctx.send("`오목 게임 모드`\n다음 중 `원하는 명령어`를 입력 후 루비에게 `답장` 부탁드려요!")
                await ctx.send("```help: 오목 게임 방법\nplay 1: AI와 오목 두기\nplay 2: 사람과 오목두기\nexit: 게임 모드 종료\n```")
                try:
                    cmd_msg = await Luby.wait_for("message", check=is_replyMsg_on_OMOK_CHANNEL, timeout=TIME_OUT)
                except asyncio.TimeoutError:
                    await ctx.send("`TIME OUT`\n오목 게임 모드를 `종료`합니다.")
                    Luby_ctrl.REPLY_QUOTE = True
                    break

                user_command = cmd_msg.content.lower().replace(' ', '')
                if user_command == 'help':
                    await Omok_help(ctx)
                elif user_command == 'play1':
                    await ctx.send(f'<@!{ctx.author.id}>\t**VS**\t<@!{Luby.user.id}>')
                    await ctx.send(f'죄송합니다.. 😭😭\n아직 루비가 오목을 배우는 중입니다!')
                    # await OM._play_Omok(Luby, ctx, Luby_ctrl.OMOK_CHANNEL_ID, Player_1_id=ctx.author.id, Player_2_id=Luby.user.id, AI=True)
                    break
                elif user_command == 'play2':
                    while True:
                        await ctx.send(f'```누구와 플레이 하실건가요?\n같이 플레이 하고싶은 분을 멘션해주세요!\n(이전 메뉴로 가기: ee)```')
                        user_command_play2 = await Luby.wait_for("message", check=is_Msg_on_OMOK_CHANNEL, timeout=30)
                        if user_command_play2.content.lower() == 'ee':
                            break
                        called_user_id = get_user_id_from_mention(user_command_play2)
                        if called_user_id:
                            await ctx.send(f'<@!{ctx.author.id}>\t**VS**\t<@!{called_user_id}>')
                            try:
                                await OM._play_Omok(Luby, ctx, Luby_ctrl.OMOK_CHANNEL_ID, Player_1_id=ctx.author.id, Player_2_id=called_user_id)
                            except e:
                                await ctx.send(e)
                            OUT_FLAG = True
                            break
                        else:
                            continue
                    if OUT_FLAG:
                        OUT_FLAG = False
                        break
                elif user_command == 'exit':
                    await ctx.send("오목 게임 모드를 `종료`합니다.")
                    break
                # await ctx.send("`오목 게임 모드`\n다음 중 `원하는 명령어`를 입력 후 루비에게 `답장` 부탁드려요!")
                # await ctx.send("```help: 오목 게임 방법\nplay 1: AI와 오목 두기\nplay 2: 사람과 오목두기\nexit: 게임 모드 종료\n```")

            # END
            Luby_ctrl.REPLY_QUOTE = True
            Luby_ctrl.OMOK_CHANNEL_ID = None

        else:
            pass


@Luby.command(name='board')
async def show_OmokBoard(ctx, board=None, current_player=None, current_player_id=None, input_coordinate=None, show_help=None):
    GameBoard_13x13 = """\
-abcdefghijklm
1=============
2=============
3=============
4=============
5=============
6=============
7=============
8=============
9=============
r=============
s=============
t=============
u=============
"""
    if board is None:
        board = GameBoard_13x13

    if ctx.author.id in (int(eeLu175_id), int(Luby.user.id)):
        paint_for_send = ''
        for char in board:
            if char in Emoji_OmokBoard_dict.keys():
                paint_for_send += Emoji_OmokBoard_dict[char]
            elif char == '\n':
                paint_for_send += '\n'
            else:
                pass
        if show_help is True:
            return paint_for_send
        else:
            embed_board = discord.Embed(colour=Luby_color)
            if current_player is not None:
                embed_board.add_field(name=f'{Emoji_OmokBoard_dict[chr(current_player + 80)]} {Luby.get_user(int(current_player_id)).display_name}님의 입력:  '
                                           f'[ {input_coordinate[0]}, {input_coordinate[1]} ]',
                                      value=f'{BLANK}',
                                      inline=False)
            embed_board.add_field(name='현재 게임 보드 상태',
                                  value=f'{paint_for_send}',
                                  inline=False)
            embed_board.set_footer(text=Luby_footer)
            if current_player == 0:
                return await ctx.send(embed=embed_board)
            else:  # current_player == 1
                return await ctx.send(embed=embed_board)
    else:
        pass


# Cogs
if __name__ == "__main__":
    for cog_fName in os.listdir(Luby_info.Luby_path + "/cogs"):
        if cog_fName[-2:] == "py":
            try:
                extension = "cogs." + cog_fName[:-3]
                Luby.load_extension(extension)
            except Exception as e:
                exc = f"{type(e).__name__}: {e}"
                print(f"Failed to load '{extension}'\n{exc}")

    # RUN

    f = open('C:/Users/jaehy/Desktop/# Lu-175/# Programming/Discord Bot/Discord-bot-Luby/Luby_token.txt', 'r')
    Luby_token = f.readline()
    f.close()
    Luby.run(Luby_token)
