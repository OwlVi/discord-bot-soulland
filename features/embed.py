from discord.embeds import Embed
from discord.colour import Colour

class SoulEmbed:
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

