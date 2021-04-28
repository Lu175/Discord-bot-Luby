import discord
from discord.ext import commands
import Luby_info


class InviteBotClient(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Luby_id = Luby_info.Luby_id
        self.Luby_color = Luby_info.Luby_color
        self.Luby_footer = Luby_info.Luby_footer

    @commands.command(aliases=['join', '초대'])
    async def _join_bot(self, ctx, input_id: int = Luby_info.Luby_id):
        target_bot = self.bot.get_user(input_id)
        embed_join = discord.Embed(title='URL for inviting bot',
                                   colour=self.Luby_color)
        embed_join.add_field(name=Luby_info.BLANK,
                             value=f'**{target_bot.name}**'+Luby_info.BLANK+f'[**`Click here`**](https://discord.com/oauth2/authorize?client_id={target_bot.id}&permissions=0&scope=bot)',
                             inline=False)
        embed_join.set_thumbnail(url=target_bot.avatar_url)
        if input_id == self.Luby_id:
            embed_join.add_field(name=Luby_info.BLANK,
                                 value='You can use `./join <bot_id>` command for another bot.',
                                 inline=False)
        embed_join.set_footer(text=self.Luby_footer)
        await ctx.send(embed=embed_join)


def setup(bot):
    bot.add_cog(InviteBotClient(bot))
