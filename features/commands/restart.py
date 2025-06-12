from discord.ext import commands

class RestartCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx):
        await ctx.send("♻️ กำลังรีสตาร์ทบอท...")
        await self.bot.close()

async def setup(bot):
    await bot.add_cog(RestartCommand(bot))
