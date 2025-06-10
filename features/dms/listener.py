import discord
from discord.ext import commands
from features.auth.handler import get_user_code

class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        if isinstance(message.channel, discord.DMChannel):
            expected_code = get_user_code(message.author.id)
            if expected_code and message.content.strip() == expected_code:
                await message.channel.send("✅ ยืนยันตัวตนสำเร็จแล้ว! 🎉")
                # TODO: เพิ่ม role หรือทำงานอื่นๆ ได้ที่นี่
            else:
                await message.channel.send("❌ รหัสไม่ถูกต้องหรือหมดอายุ")

        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(Listener(bot))
