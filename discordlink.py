import discord
from discord.ext import commands
from config import TOKEN, CHANNEL_ID

# print("Token =", TOKEN)
# print("Channel ID =", CHANNEL_ID)

# ใช้ TOKEN, CHANNEL_ID ต่อในโค้ดบอทได้เลย


intents = discord.Intents.default()
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
            await interaction.user.send(f"✅ คุณได้กรอกรหัสยืนยัน: `{code}` เรียบร้อยแล้ว!")
            await interaction.response.send_message("✅ ส่งรหัสเรียบร้อยแล้ว กรุณารอทีมงานตรวจสอบ", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message("❌ ไม่สามารถส่งข้อความ DM ได้ กรุณาเปิดรับ DM จากบอท", ephemeral=True)


@bot.event
async def on_ready():
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


@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.type == discord.InteractionType.component and interaction.data.get("custom_id") == "open_verify_modal":
        await interaction.response.send_modal(CodeModal())

bot.run(TOKEN)
