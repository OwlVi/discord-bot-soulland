import discord
import os
import sys
import asyncio
from discord.ext import commands
from config import TOKEN, CHANNEL_ID, ROLE_ID

# print("Token =", TOKEN)
# print("Channel ID =", CHANNEL_ID)

# ใช้ TOKEN, CHANNEL_ID ต่อในโค้ดบอทได้เลย


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


class CodeModal(discord.ui.Modal, title="กรอกรหัสยืนยัน"):
    code_input = discord.ui.TextInput(
        label="กรอกรหัส 4 หลักที่ได้รับจาก Wumpus",
        placeholder="เช่น 1234",
        max_length=4,
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        code = self.code_input.value.strip()

        if not code.isdigit() or len(code) != 4:
            await interaction.response.send_message(
                "❌ รหัสต้องเป็นตัวเลข 4 หลักเท่านั้น เช่น `1234`", ephemeral=True
            )
            return

        # ส่งรหัสกลับแบบ DM
        try:
            await interaction.user.send(f"""
✅ กรุณาส่งรหัสยืนยันลงในแชทนี้อีกครั้งเพื่อตกลง รหัสของคุณ: `{code}`
            

📺 คลิปแนะนำการเชื่อมดิสคอร์ด:
https://www.youtube.com/watch?v=IUl0jDDN6Ug&t=1s
            """)
            print("Code =", code)
            await interaction.response.send_message("✅ ส่งรหัสเรียบร้อยแล้ว! โปรดเช็คข้อความภายในเกม \nโปรดเช็ค 'กล่องข้อความ' ในดิสคอร์ดของคุณ", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message("❌ ไม่สามารถส่งข้อความ DM ได้ กรุณาเปิดรับ DM จากบอท", ephemeral=True)

@bot.event
async def on_ready():
    try:
        await bot.tree.sync()
        print(f"✅ Logged in as {bot.user}")

        channel = bot.get_channel(CHANNEL_ID)
        if not channel:
            print("❌ ไม่พบแชนแนลตาม ID ที่กำหนด")
            return

        embed = discord.Embed(
            title="SoullandRealms Verify",
            description=(
                "**ขั้นตอนการยืนยันตัวตน**\n\n"
                "1. โปรดเข้าร่วมเซิฟเวอร์ที่ `play.soullandrealms.com`\n"
                "2. คุยกับ Wumpus เพื่อขอรหัส 4 หลักมา\n"
                "3. กลับมาที่ดิสคอร์ดแล้วกดปุ่ม **กรอกรหัสยืนยัน**\n"
                "4. คุยกับ Wumpus แล้วเลือกคำตอบว่า **คุณได้ส่งรหัสแล้ว**\n\n"
                "หากพบปัญหา สามารถติดต่อทีมงานได้ทุกเมื่อ"
            ),
            color=discord.Color.green()
        )

        embed.add_field(
            name="📺 วิธีการยืนยันตัวตน (คลิกดูวิดีโอ)",
            value="[YouTube - คลิกที่นี่](https://www.youtube.com/watch?v=IUl0jDDN6Ug&t=1s)",
            inline=False
        )

        embed.set_image(
            url="https://media.discordapp.net/attachments/938151480270127174/1381839706651754517/aw_.png?format=webp&quality=lossless&width=1522&height=856"
        )
        embed.set_footer(text="SoullandRealms - ระบบยืนยันตัวตนอัตโนมัติ")

        view = discord.ui.View()
        view.add_item(discord.ui.Button(
            label="กรอกรหัสยืนยัน",
            style=discord.ButtonStyle.success,
            custom_id="open_verify_modal"
        ))

        await channel.send(embed=embed, view=view)
    except Exception as e:
        print(f"❌ Error during on_ready: {e}")
        await bot.close()

@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.type == discord.InteractionType.component and interaction.data.get("custom_id") == "open_verify_modal":
        await interaction.response.send_modal(CodeModal())

@bot.tree.command(name="restart", description="รีสตาร์ทบอท (เฉพาะผู้มี Role ที่กำหนด)")
async def restart(interaction: discord.Interaction):
    if not interaction.guild:
        await interaction.response.send_message("❌ คำสั่งนี้ใช้ได้เฉพาะในเซิร์ฟเวอร์", ephemeral=True)
        return

    member = interaction.guild.get_member(interaction.user.id)
    if not member:
        await interaction.response.send_message("❌ ไม่พบสมาชิกในเซิร์ฟเวอร์", ephemeral=True)
        return

    # ✅ ตรวจสอบสิทธิ์จาก Role ID
    has_permission = any(role.id == ROLE_ID for role in member.roles)
    if not has_permission:
        await interaction.response.send_message("❌ คุณไม่มีสิทธิ์ใช้คำสั่งนี้", ephemeral=True)
        return

    await interaction.response.send_message("🔁 กำลังรีสตาร์ทบอท...", ephemeral=True)
    await bot.close()
    os.execl(sys.executable, sys.executable, *sys.argv)

bot.run(TOKEN)
