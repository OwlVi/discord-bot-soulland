# features/auth/modal.py

import discord
from discord.ui import Modal, TextInput
from features.auth.handler import save_user_code

class VerifyCodeModal(Modal):
    def __init__(self):
        super().__init__(title="ยืนยันตัวตน")
        self.code_input = TextInput(label="กรอกรหัส 4 หลัก", max_length=4, min_length=4)
        self.add_item(self.code_input)

    async def on_submit(self, interaction: discord.Interaction):
        code = self.code_input.value.strip()

        if not code.isdigit() or len(code) != 4:
            await interaction.response.send_message(
                "❌ รหัสต้องเป็นตัวเลข 4 หลักเท่านั้น เช่น `1234`", ephemeral=True
            )
            return

        try:
            await interaction.user.create_dm()
        except discord.Forbidden:
            await interaction.response.send_message(
                "❌ ไม่สามารถเปิด DM ได้ กรุณาเปิดรับ DM จากบอท", ephemeral=True
            )
            return

        save_user_code(interaction.user.id, code, expire_seconds=300)

        try:
            await interaction.user.send(f"""
✅ กรุณาส่งรหัสยืนยันลงในแชทนี้อีกครั้งเพื่อตกลง รหัสของคุณ: `{code}`

📺 คลิปแนะนำการเชื่อมดิสคอร์ด:
https://www.youtube.com/watch?v=IUl0jDDN6Ug&t=1s
            """)
            await interaction.response.send_message(
                "✅ ส่งรหัสเรียบร้อยแล้ว! โปรดเช็คข้อความใน DM ของคุณ", ephemeral=True
            )
        except discord.Forbidden:
            await interaction.response.send_message(
                "❌ ไม่สามารถส่งข้อความ DM ได้ กรุณาเปิดรับ DM จากบอท", ephemeral=True
            )
