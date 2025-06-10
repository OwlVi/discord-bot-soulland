# bot.py

import discord
import asyncio
from discord.ext import commands
from features.auth.modal import VerifyCodeModal
from config import TOKEN, CHANNEL_ID

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

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
        await interaction.response.send_modal(VerifyCodeModal())
        
async def delete_sent_message():
    global sent_message
    if sent_message is not None:
        try:
            await sent_message.delete()
            print("✅ ลบข้อความสำเร็จ")
        except Exception as e:
            print(f"❌ ลบข้อความล้มเหลว: {e}")

@bot.event
async def on_disconnect():
    # จะเกิดตอนบอทตัดการเชื่อมต่อ (อาจไม่เสมอไป)
    await delete_sent_message()

def on_exit():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(delete_sent_message())

bot.run(TOKEN)
