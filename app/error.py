from discord.ext import commands

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("❌ คำสั่งนี้ไม่มีในบอทนะครับ")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ คุณไม่มีสิทธิ์ใช้คำสั่งนี้")
        else:
            await ctx.send(f"❌ เกิดข้อผิดพลาด: {error}")

async def setup(bot):
    await bot.add_cog(ErrorHandler(bot))
