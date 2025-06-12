import discord
from discord.ui import Modal, TextInput, View, Button
from config import MEMBER_ROLE_ID, SERVER_ID
from features.auth.handler import save_user_code

class Verify(Modal):
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

        save_user_code(interaction.user.id, code)
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
        except discord.Forbidden:
            await interaction.response.send_message(
                "❌ ไม่สามารถส่งข้อความ DM ได้ กรุณาเปิดรับ DM จากบอท", ephemeral=True
            )

class GiveRole(Modal):
    def __init__(self):
        super().__init__(title="รับยศ MEMBER")
    
    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        if not guild or guild.id != int(SERVER_ID):
            await interaction.response.send_message(":exclamation: No Found SoullandRealms!", ephemeral=True)
            return
        role = guild.get_role(int(MEMBER_ROLE_ID))
        member = guild.get_member(interaction.user.id)
        if not member:
            await interaction.response.send_message(":exclamation: ไม่พบสมาชิกในเซิร์ฟเวอร์!", ephemeral=True)
            return
        if role in member.roles:
            print(f"User {interaction.user.id} already has the MEMBER role.")
            await interaction.response.send_message(":exclamation: คุณมียศ MEMBER อยู่แล้ว!", ephemeral=True)
        else:
            if role is None:
                await interaction.response.send_message(":exclamation: ไม่พบยศ MEMBER ในเซิร์ฟเวอร์!", ephemeral=True)
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
                case "verify":
                    self.add_item(Button(
                        label="กรอกรหัสยืนยัน",
                        style=discord.ButtonStyle.success,
                        custom_id="verify"
                    ))

                case "give_role":
                    self.add_item(Button(
                        label="รับยศ MEMBER",
                        style=discord.ButtonStyle.success,
                        custom_id="give_role"
                    ))

                case "link":
                    self.add_item(Button(
                        label="วิธีเชื่อม Discord",
                        style=discord.ButtonStyle.link,
                        url="https://www.youtube.com/watch?v=IUl0jDDN6Ug&t=1s"
                    ))

                case _:
                    raise ValueError(f"Unknown button name: {name}")
        return self

class SoullandEmbed:
    def give_role(self):
        self = discord.Embed(
            title=":wave: ยินดีต้อนรับสู่ SoullandRealms!",
            description=(
                "สวัสดีผู้เล่นใหม่! หากคุณเพิ่งเข้าร่วมดิสคอร์ดเซิร์ฟเวอร์ของเรา และยังไม่ได้รับยศ...\n\n"
                ":tada: กดปุ่ม **รับยศ MEMBER** ด้านล่าง เพื่อเริ่มต้นการใช้งานและเข้าถึงห้องพื้นฐาน\n\n"
                ":exclamation: หากคุณต้องการเข้าถึงห้องทั้งหมด โปรดเชื่อมบัญชี Discord กับ Minecraft ของคุณ\n"
                ":tv: สามารถกดปุ่ม 'วิธีเชื่อม Discord' เพื่อดูวิดีโอแนะนำ\n\n"
                "หากพบปัญหา ติดต่อทีมงานได้ทุกเมื่อ :heart:"
            ),
            color=discord.Color.blurple()
        )
        self.set_image(url="https://media.discordapp.net/attachments/938151480270127174/1382746650224885852/promote1.jpg?format=webp&width=1522&height=856")
        self.set_footer(text="SoullandRealms | ระบบรับยศอัตโนมัติ")
        return self
    
    def verify(self):
        self = discord.Embed(
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

        self.add_field(
            name="📺 วิธีการยืนยันตัวตน (คลิกดูวิดีโอ)",
            value="**[คลิกดูวิดีโอ YouTube](https://www.youtube.com/watch?v=IUl0jDDN6Ug&t=1s)**",
            inline=False
        )

        self.set_image(
            url="https://media.discordapp.net/attachments/938151480270127174/1381839706651754517/aw_.png?format=webp&quality=lossless&width=1522&height=856"
        )
        self.set_footer(text="SoullandRealms - ระบบยืนยันตัวตนอัตโนมัติ")
        return self
    
        
