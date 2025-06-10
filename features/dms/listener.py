import discord
from discord.ext import commands
from features.auth.handler import get_user_code

class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        if isinstance(message.channel, discord.DMChannel):
            user_id = message.author.id
            code = message.content.strip()

            if not code.isdigit() or len(code) != 4:
                await message.channel.send("❌ รหัสไม่ถูกต้อง ต้องเป็นเลข 4 หลัก เช่น `1234`")
                return

            correct_code = self.bot.get_user_code(user_id)
            if correct_code is None:
                await message.channel.send("⚠️ ยังไม่มีการขอรหัสหรือรหัสหมดอายุ กรุณากด 'กรอกรหัสยืนยัน' ใหม่")
                return

            if code != correct_code:
                await message.channel.send("❌ รหัสไม่ตรง กรุณาตรวจสอบอีกครั้ง")
                return

            await message.channel.send("✅ ยืนยันตัวตนสำเร็จ! ขอบคุณที่เข้าร่วมเซิร์ฟเวอร์ของเรา ❤️")

        await self.bot.process_commands(message)


async def setup(bot):
    await bot.add_cog(Listener(bot))
