import re
import numpy as np
import asyncio
from time import time


class game_Omok:
    def __init__(self):
        self.Player_id = [0, 0]
        self.curr_player = 0
        self.prev_player = 1
        self.input_msg = None

    async def delete_msg(self, msg_list):
        if msg_list:
            for msg in msg_list:
                await msg.delete()

    def is_current_player_msg(self, message):
        input_msg = message.content.upper()
        MATCHED_MSG = False
        Regex_1 = re.compile(r' *[A-M] *,? *\d{1,2} *')
        Regex_2 = re.compile(r' *\d{1,2} *,? *[A-M] *')
        Regex_gg = re.compile(r' *GG *')
        if (Regex_1.fullmatch(input_msg)) or (Regex_2.fullmatch(input_msg)) or (Regex_gg.fullmatch(input_msg)):
            MATCHED_MSG = True
        return MATCHED_MSG and (message.author.id == int(self.Player_id[self.curr_player]))

    async def _play_Omok(self, bot, ctx, OMOK_CHANNEL_ID, Player_1_id=None, Player_2_id=None, AI=False):
        default_GameBoard_13x13 = """\
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

        # Message collection
        msg_buf_input_K = []
        msg_buf_timeout_K = []
        right_coordinate_K = None
        another_coordinate_K = None

        # Board & Stones
        Board_row, Board_col = (13, 13)
        ary_Board_TF = np.ones((Board_row, Board_col), dtype=bool)
        ary_player = np.zeros((2, Board_row, Board_col), dtype=int)

        # Player id
        self.Player_id[0] = int(Player_1_id)
        self.Player_id[1] = int(Player_2_id)

        # String for stone
        p_curr_str = ['P', 'Q']
        p_past_str = ['p', 'q']
        p_stone = ['🔴', '🟢']

        # Input
        ROW_input = None
        COL_input = None
        p_input = ['', '']
        p_coordinate = ['', '']

        # Flags
        GAME_END = False
        GG_FLAG = False
        MATCHED_INPUT_1 = None
        MATCHED_INPUT_1c = None
        MATCHED_INPUT_2 = None
        MATCHED_INPUT_2c = None
        OMOK_TURN_COUNT = 0

        # Times
        TIME = 10
        time_START = 0
        time_NOW = 0

        # Show blank

        board_blank_0 = await ctx.invoke(bot.get_command("board"), board=default_GameBoard_13x13)
        msg_Board = board_blank_0

        while True:

            # Get input from player A or B

            while True:  # Loop for Not available coordinate
                while True:  # Loop for Not available input
                    while True:  # Loop for Get input from reply
                        input_K = await ctx.send(f'{p_stone[self.curr_player] * 2} <@{self.Player_id[self.curr_player]}>님 차례입니다. {p_stone[self.curr_player] * 2}\n좌표를 입력해주세요!')
                        msg_buf_input_K.append(input_K)
                        try:
                            left_time_K = await ctx.send("**이번 턴이 60초 남았습니다.**")
                            time_START = time()
                            msg_buf_timeout_K.append(left_time_K)
                            self.input_msg = await bot.wait_for('message', check=self.is_current_player_msg, timeout=30)
                        except asyncio.TimeoutError:
                            try:
                                left_time_K = await ctx.send("**이번 턴이 30초 남았습니다.**")
                                msg_buf_timeout_K.append(left_time_K)
                                self.input_msg = await bot.wait_for('message', check=self.is_current_player_msg, timeout=TIME)
                            except asyncio.TimeoutError:
                                try:
                                    left_time_K = await ctx.send("**이번 턴이 20초 남았습니다.**")
                                    msg_buf_timeout_K.append(left_time_K)
                                    self.input_msg = await bot.wait_for('message', check=self.is_current_player_msg, timeout=TIME)
                                except asyncio.TimeoutError:
                                    try:
                                        left_time_K = await ctx.send("**이번 턴이 10초 남았습니다.**")
                                        msg_buf_timeout_K.append(left_time_K)
                                        self.input_msg = await bot.wait_for('message', check=self.is_current_player_msg, timeout=TIME)
                                    except asyncio.TimeoutError:
                                        if msg_buf_timeout_K:
                                            await self.delete_msg(msg_buf_timeout_K)
                                            msg_buf_timeout_K = []
                                        timeout_K = await ctx.send(f"**`TIME OUT`**\n**<@{self.Player_id[self.prev_player]}>님에게 차례가 넘어갑니다.**")
                                        msg_buf_timeout_K.append(timeout_K)

                                        player_temp = self.prev_player
                                        self.prev_player = self.curr_player
                                        self.curr_player = player_temp
                                        continue

                        if not (self.input_msg.channel.id == OMOK_CHANNEL_ID):
                            continue

                        if msg_buf_timeout_K:
                            await self.delete_msg(msg_buf_timeout_K)
                            msg_buf_timeout_K = []
                        if msg_buf_input_K:
                            await self.delete_msg(msg_buf_input_K)
                            msg_buf_input_K = []

                        if self.input_msg.author.id == int(self.Player_id[self.curr_player]):
                            if self.input_msg.content.strip().upper() in ('GG'):  # GG ~~~~
                                GG_FLAG = True
                                break

                            # RESET
                            MATCHED_INPUT_1 = None
                            MATCHED_INPUT_1c = None
                            MATCHED_INPUT_2 = None
                            MATCHED_INPUT_2c = None
                            p_input[self.curr_player] = self.input_msg.content.upper()
                            p_input[self.curr_player] = p_input[self.curr_player].strip()
                            # 영어 숫자
                            Regex_1 = re.compile(r' *[A-M] *\d{1,2} *')
                            if Regex_1.fullmatch(p_input[self.curr_player]):
                                MATCHED_INPUT_1 = True
                                break
                            # 영어, 숫자
                            Regex_1c = re.compile(r' *[A-M] *, *\d{1,2} *')
                            if Regex_1c.fullmatch(p_input[self.curr_player]):
                                MATCHED_INPUT_1c = True
                                break
                            # 숫자 영어
                            Regex_2 = re.compile(r' *\d{1,2} *[A-M] *')
                            if Regex_2.fullmatch(p_input[self.curr_player]):
                                MATCHED_INPUT_2 = True
                                break
                            # 숫자, 영어
                            Regex_2c = re.compile(r' *\d{1,2} *, *[A-M] *')
                            if Regex_2c.fullmatch(p_input[self.curr_player]):
                                MATCHED_INPUT_2c = True
                                break
                            else:
                                if right_coordinate_K is not None:
                                    await right_coordinate_K.delete()
                                right_coordinate_K = await ctx.send('**`좌표`를 제대로 입력해주세요!**')
                                continue

                    if GG_FLAG:  # GG ~~~~
                        break
                    if MATCHED_INPUT_1 or MATCHED_INPUT_1c or MATCHED_INPUT_2 or MATCHED_INPUT_2c:
                        await self.input_msg.delete()
                        break

                if GG_FLAG:  # GG ~~~~
                    break

                coordinate_buf = ''
                for char in p_input[self.curr_player]:
                    if char in (' '):
                        pass
                    else:
                        coordinate_buf += char
                # 문자 숫자
                if MATCHED_INPUT_1:
                    p_coordinate[self.curr_player] = [coordinate_buf[0], coordinate_buf[1:]]
                # 숫자 문자
                if MATCHED_INPUT_2:
                    p_coordinate[self.curr_player] = [coordinate_buf[0:-1], coordinate_buf[-1]]
                # 문자, 숫자 OR 숫자, 문자
                elif MATCHED_INPUT_1c or MATCHED_INPUT_2c:
                    p_coordinate[self.curr_player] = coordinate_buf.split(',')

                # ROW, COL  # 문자 숫자 OR 문자, 숫자
                if MATCHED_INPUT_1 or MATCHED_INPUT_1c:
                    COL_input = ord(p_coordinate[self.curr_player][0]) - ord('A')
                    ROW_input = int(p_coordinate[self.curr_player][1]) - 1
                    if (ROW_input in range(Board_row)) and (COL_input in range(Board_col)) and (ary_Board_TF[ROW_input, COL_input]):
                        ary_player[self.curr_player, ROW_input, COL_input] = 1
                        ary_Board_TF[ROW_input, COL_input] = False
                        break
                    else:
                        if another_coordinate_K is not None:
                            await another_coordinate_K.delete()
                        another_coordinate_K = await ctx.send('**`다른 좌표`를 입력해주세요!**')
                        continue
                # COL, ROW  # 숫자 문자 OR 숫자, 문자
                elif MATCHED_INPUT_2 or MATCHED_INPUT_2c:
                    COL_input = ord(p_coordinate[self.curr_player][1]) - ord('A')
                    ROW_input = int(p_coordinate[self.curr_player][0]) - 1
                    if (ROW_input in range(Board_row)) and (COL_input in range(Board_col)) and (ary_Board_TF[ROW_input, COL_input]):
                        ary_player[self.curr_player, ROW_input, COL_input] = 1
                        ary_Board_TF[ROW_input, COL_input] = False
                        break
                    else:
                        if another_coordinate_K is not None:
                            await another_coordinate_K.delete()
                        another_coordinate_K = await ctx.send('**다른 좌표를 입력해주세요!**')
                        continue

            if right_coordinate_K is not None:
                await right_coordinate_K.delete()
                right_coordinate_K = None
            if another_coordinate_K is not None:
                await another_coordinate_K.delete()
                another_coordinate_K = None

            # GG END

            if GG_FLAG:  # GG ~~~~
                if self.curr_player == 0:
                    await ctx.send(f'🔴<@{self.Player_id[0]}>: `GG`\n🟢🟢🟢🟢🟢 WINNER is <@{self.Player_id[1]}> !! 🟢🟢🟢🟢🟢')
                    await ctx.send("오목 게임 모드를 `종료`합니다.")
                    break
                elif self.curr_player == 1:
                    await ctx.send(f'🟢<@{self.Player_id[1]}>: `GG`\n🔴🔴🔴🔴🔴 WINNER is <@{self.Player_id[0]}> !! 🔴🔴🔴🔴🔴')
                    await ctx.send("오목 게임 모드를 `종료`합니다.")
                    break

            # Reflect input on Board

            renewed_Board_Buf = '-abcdefghijklm\n'
            row_index = '123456789rstu'
            draw_count = 14
            for row in range(Board_row):
                renewed_Board_Buf += row_index[row]
                draw_count += 1
                for col in range(Board_col):
                    draw_count += 1
                    if ary_Board_TF[row, col]:
                        # Board and Past
                        renewed_Board_Buf += default_GameBoard_13x13[draw_count]
                    elif ary_player[self.curr_player, row, col] == 1:
                        if (row == ROW_input) and (col == COL_input):
                            # curr_player input stone (one)
                            renewed_Board_Buf += p_curr_str[self.curr_player]
                        else:
                            # curr_player stones (all w/o [ROW_input, COL_input])
                            renewed_Board_Buf += p_past_str[self.curr_player]
                    else:
                        # prev_player stones (all)
                        renewed_Board_Buf += p_past_str[self.prev_player]
                renewed_Board_Buf += '\n'
                draw_count += 1
            playing_GameBoard_13x13 = renewed_Board_Buf

            # Show input coordinate

            await msg_Board.delete()
            board_K = await ctx.invoke(bot.get_command("board"),
                                       board=playing_GameBoard_13x13,
                                       current_player=self.curr_player,
                                       current_player_id=self.Player_id[self.curr_player],
                                       input_coordinate=p_coordinate[self.curr_player])
            msg_Board = board_K

            # Check 5 series dots [ - ] : Horizontal

            for row in range(Board_row):
                for col in range(Board_col - 4):
                    if np.sum(ary_player[self.curr_player, row, col:col + 5]) == 5:
                        GAME_END = True

            # Check 5 series dots [ | ] : Vertical

            for row in range(Board_row - 4):
                for col in range(Board_col):
                    if np.sum(ary_player[self.curr_player, row:row + 5, col]) == 5:
                        GAME_END = True

            # Check 5 series dots [ \ ] : Backslash

            for row in range(Board_row - 4):
                for col in range(Board_col - 4):
                    ele_sum = 0
                    for idx in range(5):
                        ele_sum += ary_player[self.curr_player, row + idx, col + idx]
                    if ele_sum == 5:
                        GAME_END = True

            # Check 5 series dots [ / ] : Slash

            for row in range(Board_row - 4):
                for col in range(4, Board_col):
                    ele_sum = 0
                    for idx in range(5):
                        ele_sum += ary_player[self.curr_player, row + idx, col - idx]
                    if ele_sum == 5:
                        GAME_END = True

            # Game over

            if GAME_END:
                if self.curr_player == 0:
                    await ctx.send(f'🔴🔴🔴🔴🔴 WINNER is <@{self.Player_id[0]}> !! 🔴🔴🔴🔴🔴')
                elif self.curr_player == 1:
                    await ctx.send(f'🟢🟢🟢🟢🟢 WINNER is <@{self.Player_id[1]}> !! 🟢🟢🟢🟢🟢')
                break
            else:
                OMOK_TURN_COUNT += 1
                if OMOK_TURN_COUNT == 169:
                    await ctx.send('🔴🟢🔴🟢🔴 !! DRAW !! 🟢🔴🟢🔴🟢')
                    break
                else:
                    player_temp = self.prev_player
                    self.prev_player = self.curr_player
                    self.curr_player = player_temp
