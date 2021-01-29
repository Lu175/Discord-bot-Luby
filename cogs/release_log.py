import discord
from discord.ext import commands
import Luby_info
import Luby_ctrl
import func_Lu175 as FLU
import time


class ReleaseLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Activity_name = Luby_info.Luby_Activity_name

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=self.Activity_name),
                                       status=discord.Status.online,
                                       afk=False)
        launch_msg = f"############\n" \
                     f"Time: [{time.ctime()}]\n" \
                     f"Logged in as {self.bot.user.name}\n" \
                     f"{Luby_info.Luby_footer}\n" \
                     f"------------"
        print(launch_msg)
        self._log_msg(launch_msg)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        else:
            Luby_ctrl.speaking_id_set.add(str(message.author.id))
            self._log_msg(f'[{message.channel}]{message.author.id}({message.author.display_name}): {message.content}')
            replied_msg = await FLU.get_replied_msg(bot=self.bot, message=message)
            if replied_msg:
                self._log_msg('Replied message: ' + replied_msg.content)

    def _log_msg(self, message: str):
        f_log = open(Luby_info.Luby_path + "/Luby_log.out", 'a', encoding='utf-8')
        f_log.write(f"{message}\n")
        f_log.close()


def setup(bot):
    bot.add_cog(ReleaseLog(bot))
