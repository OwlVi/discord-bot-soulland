from discord.ui import Modal, TextInput
from discord.interactions import Interaction
from discord.errors import Forbidden
from config import MEMBER_ROLE_ID

class HandlerModal():
    async def handle_verify(self,interaction: Interaction): 
        await interaction.response.send_modal(Verify())

class Verify(Modal):
    def __init__(self):
        super().__init__(title="ยืนยันตัวตน")
        self.code_input = TextInput(label="กรอกรหัส 4 หลัก", max_length=4, min_length=4)
        self.add_item(self.code_input)

    async def on_submit(self, interaction: Interaction):
        code = self.code_input.value.strip()
        

        if not code.isdigit() or len(code) != 4:
            await interaction.response.send_message(
                "❌ รหัสต้องเป็นตัวเลข 4 หลักเท่านั้น เช่น `1234`", ephemeral=True
            )
            return

        try:
            await interaction.user.create_dm()
        except Forbidden:
            await interaction.response.send_message(
                "❌ ไม่สามารถเปิด DM ได้ กรุณาเปิดรับ DM จากบอท", ephemeral=True
            )
            return

        print(f"รหัสยืนยันของ {interaction.user.id} คือ {code}")
        try:
            await interaction.user.send(f"""
✅ กรุณาส่งรหัสยืนยันลงในแชทนี้อีกครั้งเพื่อตกลง รหัสของคุณ: `{code}`

📺 คลิปแนะนำการเชื่อมดิสคอร์ด:
https://www.youtube.com/watch?v=IUl0jDDN6Ug&t=1s
            """)
            await interaction.response.send_message(
                "✅ ส่งรหัสเรียบร้อยแล้ว! โปรดเช็คข้อความใน DM ของคุณ", ephemeral=True
            )
        except Forbidden:
            await interaction.response.send_message(
                "❌ ไม่สามารถส่งข้อความ DM ได้ กรุณาเปิดรับ DM จากบอท", ephemeral=True
            )
            
class GiveRole(Modal):
    def __init__(self):
        super().__init__(title="รับยศ MEMBER")
    
    async def on_submit(self, interaction: Interaction):
        guild = interaction.guild
        if guild is None:
            print("Guild Not Found")
            return
        role = guild.get_role(MEMBER_ROLE_ID)
        member = guild.get_member(interaction.user.id)
        if member is None:
            print("Member Not Found")
            return
        if role is None:
            print("Role Not Found")
            return

        if member.get_role(MEMBER_ROLE_ID) is not None:
            print(f"User {interaction.user.id} already has the MEMBER role.")
            await interaction.response.send_message(":exclamation: คุณมียศ MEMBER อยู่แล้ว!", ephemeral=True)
        else:
                print(f"Adding MEMBER role to user {interaction.user.id}.")
                await member.add_roles(role)
                await interaction.response.send_message(":white_check_mark: รับยศเรียบร้อยแล้ว! ยินดีต้อนรับสู่ SoullandRealms :dizzy:", ephemeral=True)
