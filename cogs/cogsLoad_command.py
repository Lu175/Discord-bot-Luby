import discord
from discord.ext import commands
import os.path
import Luby_info


def get_cog_files_list():
    cog_file_in_dir = []
    for cog_fName in os.listdir(Luby_info.Luby_path + "/cogs"):
        if cog_fName[-2:] == "py":
            cog_file_in_dir.append(cog_fName[:-3])
    return cog_file_in_dir


class CogsLoadCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.eeLu175_id = Luby_info.eeLu175_id
        self.Luby_color = Luby_info.Luby_color
        self.Luby_footer = Luby_info.Luby_footer
        self.Luby_thumbnail_url = Luby_info.Luby_thumbnail_url
        self.loaded_cogs_list = Luby_info.cogs_list
        self.cd_files_list = Luby_info.cogs_list

    def _make_resultEmbed(self, ctx, mode, contents):
        embed_load_result = discord.Embed.Empty
        if mode == 0:
            embed_load_result = discord.Embed(title='Cogs renewing complete !!', colour=self.Luby_color)
            embed_load_result.set_thumbnail(url=self.Luby_thumbnail_url)
            embed_load_result.add_field(name='List of Loaded Cogs', value=f'{contents}', inline=False)
        if mode == 1:
            embed_load_result = discord.Embed(title='Loading complete !!', colour=self.Luby_color)
            embed_load_result.set_thumbnail(url=self.Luby_thumbnail_url)
            embed_load_result.add_field(name='Target cog name', value=f'{contents}', inline=False)
        if mode == 2:
            embed_load_result = discord.Embed(title='Unloading complete !!', colour=self.Luby_color)
            embed_load_result.set_thumbnail(url=self.Luby_thumbnail_url)
            embed_load_result.add_field(name='Target cog name', value=f'{contents}', inline=False)
        if mode == 3:
            embed_load_result = discord.Embed(title='Reloading complete !!', colour=self.Luby_color)
            embed_load_result.set_thumbnail(url=self.Luby_thumbnail_url)
            embed_load_result.add_field(name='Target cog name', value=f'{contents}', inline=False)
            embed_load_result.set_footer(text=self.Luby_footer)
            embed_load_result.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        return embed_load_result

    def _check_new_cogs(self):
        self.cd_files_list = get_cog_files_list()
        rest_cogs_list = []
        LCL_deleted_cogs_list = []
        for idx in range(len(self.loaded_cogs_list)):
            if self.loaded_cogs_list[idx] not in self.cd_files_list:
                LCL_deleted_cogs_list.append(self.loaded_cogs_list[idx])
            else:
                rest_cogs_list.append(self.loaded_cogs_list[idx])
        CDFL_added_cogs_list = []
        for idx in range(len(self.cd_files_list)):
            if self.cd_files_list[idx] not in self.loaded_cogs_list:
                CDFL_added_cogs_list.append(self.cd_files_list[idx])
        return [LCL_deleted_cogs_list, CDFL_added_cogs_list, rest_cogs_list]

    @commands.group(aliases=['cogs', 'cs'])
    async def cmd_cogs(self, ctx):
        # await ctx.send('`list`, `load`')
        pass

    @cmd_cogs.command(aliases=['list', 'li'])
    async def cmd_cogs_list(self, ctx):
        [LCL_deleted_cogs_list, CDFL_added_cogs_list, rest_cogs_list] = self._check_new_cogs()
        CDFL_list = []
        for cog_name in LCL_deleted_cogs_list:
            CDFL_list.append('- '+cog_name)
        for cog_name in CDFL_added_cogs_list:
            CDFL_list.append('+ '+cog_name)
        for cog_name in rest_cogs_list:
            CDFL_list.append(cog_name)

        embed_cogs_list = discord.Embed(colour=self.Luby_color)
        embed_cogs_list.set_thumbnail(url=self.Luby_thumbnail_url)
        LCL_str = '\n'.join(self.loaded_cogs_list)
        embed_cogs_list.add_field(name='List of Loaded Cogs', value='```\n'+LCL_str+'```', inline=True)
        CDFL_str = '\n'.join(CDFL_list)
        embed_cogs_list.add_field(name='List of Cog Files in Directory', value='```diff\n'+CDFL_str+'```', inline=True)
        embed_cogs_list.set_footer(text=self.Luby_footer)
        embed_cogs_list.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed_cogs_list)

        return [LCL_deleted_cogs_list, CDFL_added_cogs_list, rest_cogs_list]

    @cmd_cogs.command(aliases=['load', 'lo'])
    async def cmd_cogs_load(self, ctx):
        if ctx.author.id == self.eeLu175_id:
            # self.cd_files_list = get_cog_files_list()
            [LCL_deleted_cogs_list, CDFL_added_cogs_list, rest_cogs_list] = await self.cmd_cogs_list(ctx)
            try:
                for cog_name in LCL_deleted_cogs_list:
                    del Luby_info.cogs_list[Luby_info.cogs_list.index(cog_name)]
                    extension = "cogs." + cog_name
                    self.bot.unload_extension(extension)
                for cog_name in CDFL_added_cogs_list:
                    Luby_info.cogs_list.append(cog_name)
                    extension = "cogs." + cog_name
                    self.bot.load_extension(extension)
                for cog_name in rest_cogs_list:
                    extension = "cogs." + cog_name
                    self.bot.reload_extension(extension)
            except Exception as e:
                exc = f"{type(e).__name__}: {e}"
                await ctx.send(f"Failed to load '{extension}'\n{exc}")

            self.loaded_cogs_list = Luby_info.cogs_list
            self.cd_files_list = Luby_info.cogs_list
            embed_load_result = self._make_resultEmbed(ctx, mode=0, contents='```'+'\n'.join(self.cd_files_list)+'```')
            await ctx.send(embed=embed_load_result)

    @commands.group(aliases=['cog', 'c'])
    async def cmd_cog(self, ctx):
        # await ctx.send('`load`, `unload`, `reload`')
        pass

    @cmd_cog.command(aliases=['load', 'lo'])
    async def cmd_cog_load(self, ctx, cog_name: str):
        if ctx.author.id == self.eeLu175_id:
            try:
                extension = "cogs." + cog_name
                self.bot.load_extension(extension)
                Luby_info.cogs_list.append(cog_name)
            except Exception as e:
                exc = f"{type(e).__name__}: {e}"
                await ctx.send(f"Failed to load '{extension}'\n{exc}")

            self.loaded_cogs_list = Luby_info.cogs_list
            self.cd_files_list = Luby_info.cogs_list
            embed_load_result = self._make_resultEmbed(ctx, mode=1, contents=cog_name)
            await ctx.send(embed=embed_load_result)

    @cmd_cog.command(aliases=['unload', 'unlo'])
    async def cmd_cog_unload(self, ctx, cog_name: str):
        if ctx.author.id == self.eeLu175_id:
            try:
                extension = "cogs." + cog_name
                self.bot.unload_extension(extension)
                del Luby_info.cogs_list[Luby_info.cogs_list.index(cog_name)]
            except Exception as e:
                exc = f"{type(e).__name__}: {e}"
                await ctx.send(f"Failed to load '{extension}'\n{exc}")

            self.loaded_cogs_list = Luby_info.cogs_list
            self.cd_files_list = Luby_info.cogs_list
            embed_load_result = self._make_resultEmbed(ctx, mode=2, contents=cog_name)
            await ctx.send(embed=embed_load_result)

    @cmd_cog.command(aliases=['reload', 'relo'])
    async def cmd_cog_reload(self, ctx, cog_name: str):
        if ctx.author.id == self.eeLu175_id:
            try:
                await ctx.invoke(self.bot.get_command('cmd_cog_unload'), cog_name=cog_name)
                await ctx.invoke(self.bot.get_command('cmd_cog_load'), cog_name=cog_name)
            except Exception as e:
                exc = f"{type(e).__name__}: {e}"
                await ctx.send(f"Failed to load '{extension}'\n{exc}")

            self.loaded_cogs_list = Luby_info.cogs_list
            self.cd_files_list = Luby_info.cogs_list
            embed_load_result = self._make_resultEmbed(ctx, mode=3, contents=cog_name)
            await ctx.send(embed=embed_load_result)


def setup(bot):
    bot.add_cog(CogsLoadCommand(bot))
