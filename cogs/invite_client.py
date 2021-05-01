import discord
from discord.ext import commands
import asyncio
import Luby_info


class InviteClient(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Luby_id = Luby_info.Luby_id
        self.Luby_color = Luby_info.Luby_color
        self.Luby_footer = Luby_info.Luby_footer
        self.ctx = None

    def is_message_owner(self, reaction, user):
        return self.ctx.author == user

    @commands.command(aliases=['join', 'j', '초대'])
    async def _join_bot(self, ctx, input_id: int = Luby_info.Luby_id):
        target = self.bot.get_user(input_id)
        if target.bot:
            # target is bot
            embed_join_bot = discord.Embed(title='Click URL for inviting bot',
                                           colour=self.Luby_color)
            embed_join_bot.add_field(name=Luby_info.BLANK,
                                     value=f'**{target.name}**'+Luby_info.BLANK+
                                           f'[**`Click here`**](https://discord.com/oauth2/authorize?client_id={target.id}&permissions=0&scope=bot)',
                                     inline=False)
            embed_join_bot.set_thumbnail(url=target.avatar_url)
            if input_id == self.Luby_id:
                embed_join_bot.add_field(name=Luby_info.BLANK,
                                         value='You can use `./join <bot_id>` command for another bot.\n',
                                         inline=False)
            embed_join_bot.set_footer(text=self.Luby_footer)
            await ctx.send(embed=embed_join_bot)
        else:
            # target is user
            embed_join_user = discord.Embed(title='Send DM for inviting user',
                                            colour=self.Luby_color)
            embed_join_user.add_field(name=Luby_info.BLANK,
                                      value=f'Do you want to invite **`{target.name}`** to **`{ctx.guild.name}`**?\n'
                                            f'please click `⭕` or `❌`',
                                      inline=False)
            embed_join_user.set_thumbnail(url=target.avatar_url)
            embed_join_user.set_footer(text=self.Luby_footer)
            pf_embed = await ctx.send(embed=embed_join_user)

            target_dm_channel = target.dm_channel
            if target_dm_channel is None:
                target_dm_channel = await target.create_dm()
            try:
                self.ctx = ctx
                await pf_embed.add_reaction('⭕')
                await pf_embed.add_reaction('❌')
                reaction, user = await self.bot.wait_for('reaction_add', check=self.is_message_owner, timeout=30)
                print(reaction)
                print(user)
            except asyncio.TimeoutError:
                await pf_embed.clear_reactions()
                await pf_embed.add_reaction('🇪')
                await pf_embed.add_reaction('🇳')
                await pf_embed.add_reaction('🇩')
            else:
                if reaction.emoji == '⭕':
                    await target_dm_channel.send(await ctx.channel.create_invite(max_age=0, unique=False))
                    await pf_embed.clear_reactions()
                    await pf_embed.add_reaction('🇩')
                    await pf_embed.add_reaction('🇴')
                    await pf_embed.add_reaction('🇳')
                    await pf_embed.add_reaction('🇪')
                elif reaction.emoji == '❌':
                    await pf_embed.clear_reactions()
                    await pf_embed.add_reaction('🇪')
                    await pf_embed.add_reaction('🇳')
                    await pf_embed.add_reaction('🇩')
            self.ctx = None


def setup(bot):
    bot.add_cog(InviteClient(bot))
