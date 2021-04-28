import discord
from discord.ext import commands
import asyncio
import Luby_info


class ShowPresence(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Activity_names = Luby_info.Luby_Activity_names

    @commands.Cog.listener()
    async def on_ready(self):
        while True:
            for Activity_name in self.Activity_names:
                Activity_name = Activity_name + '-->'+Luby_info.BLANK+'./help 를'
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=Activity_name),
                                               status=discord.Status.online,
                                               afk=False)
                await asyncio.sleep(15)


def setup(bot):
    bot.add_cog(ShowPresence(bot))
