from discord.ui import Modal, TextInput, View, Button
from discord.interactions import Interaction
from discord.errors import Forbidden
from discord.embeds import Embed
from discord.colour import Colour
from discord.enums import ButtonStyle
from config import MEMBER_ROLE_ID
from features.routing import ButtonType
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

class SoullandView(View):
    def __init__(self):
        super().__init__()
        self.timeout = None

    def add(self, *buttons: str):
        for name in buttons:
            match name:
                case ButtonType.VERIFY.value:
                    self.add_item(Button(
                        label="กรอกรหัสยืนยัน",
                        style=ButtonStyle.success,
                        custom_id=ButtonType.VERIFY.value
                    ))

                case ButtonType.GIVE_ROLE.value:
                    self.add_item(Button(
                        label="รับยศ MEMBER",
                        style=ButtonStyle.success,
                        custom_id=ButtonType.GIVE_ROLE.value
                    ))

                case ButtonType.LINK_DISCORD.value:
                    self.add_item(Button(
                        label="วิธีเชื่อม Discord",
                        style=ButtonStyle.link,
                        url="https://www.youtube.com/watch?v=IUl0jDDN6Ug&t=1s",
                    ))

                case _:
                    raise ValueError(f"Unknown button name: {name}")
        return self

class SoullandEmbed:
    def give_role(self):
        self = Embed(
            title=":wave: ยินดีต้อนรับสู่ Soulland Realms!",
            description=(
                "สวัสดีผู้เล่นใหม่! หากคุณเพิ่งเข้าร่วมดิสคอร์ดเซิร์ฟเวอร์ของเรา และยังไม่ได้รับยศ...\n\n"
                ":tada: กดปุ่ม **รับยศ MEMBER** ด้านล่าง เพื่อเริ่มต้นการใช้งานและเข้าถึงห้องพื้นฐาน\n\n"
                ":exclamation: หากคุณต้องการเข้าถึงห้องทั้งหมด โปรดเชื่อมบัญชี Discord กับ Minecraft ของคุณ\n"
                ":tv: สามารถกดปุ่ม 'วิธีเชื่อม Discord' เพื่อดูวิดีโอแนะนำ\n\n"
                "หากพบปัญหา ติดต่อทีมงานได้ทุกเมื่อ :heart:"
            ),
            color=Colour.blurple()
        )
        self.set_image(url="https://media.discordapp.net/attachments/938151480270127174/1382746650224885852/promote1.jpg?format=webp&width=1522&height=856")
        self.set_footer(text="Soulland Realms | ระบบรับยศอัตโนมัติ")
        return self
    
    def verify(self):
        self = Embed(
            title=":wave: ยินดีต้อนรับสู่ Soulland Realms!",
            description=(
                "**ขั้นตอนการยืนยันตัวตน**\n\n"
                "1. โปรดเข้าร่วมเซิฟเวอร์ที่ `play.soullandrealms.com`\n"
                "2. คุยกับ Wumpus เพื่อขอรหัส 4 หลักมา\n"
                "3. กลับมาที่ดิสคอร์ดแล้วกดปุ่ม **กรอกรหัสยืนยัน**\n"
                "4. คุยกับ Wumpus แล้วเลือกคำตอบว่า **คุณได้ส่งรหัสแล้ว**\n\n"
                "หากพบปัญหา สามารถติดต่อทีมงานได้ทุกเมื่อ"
            ),
            color=Colour.green()
        )

        self.add_field(
            name="📺 วิธีการยืนยันตัวตน (คลิกดูวิดีโอ)",
            value="**[คลิกดูวิดีโอ YouTube](https://www.youtube.com/watch?v=IUl0jDDN6Ug&t=1s)**",
            inline=False
        )

        self.set_image(
            url="https://media.discordapp.net/attachments/938151480270127174/1381839706651754517/aw_.png?format=webp&quality=lossless&width=1522&height=856"
        )
        self.set_footer(text="Soulland Realms - ระบบยืนยันตัวตนอัตโนมัติ")
        return self

    
        
