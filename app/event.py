import discord
from discord.ext import commands

class BotEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot พร้อมใช้งานแล้ว! Logged in as {self.bot.user}')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name='general')
        if channel:
            await channel.send(f'Welcome to the server, {member.mention}!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels, name='general')
        if channel:
            await channel.send(f'{member.mention} has left the server.')
            
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("❌ คำสั่งนี้ไม่ถูกต้อง หรือไม่มีคำสั่งนี้ในระบบ")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌ กรุณาระบุพารามิเตอร์ที่จำเป็น")
        else:
            await ctx.send(f"❌ เกิดข้อผิดพลาด: {str(error)}")
def setup(bot):
    bot.add_cog(BotEvents(bot))