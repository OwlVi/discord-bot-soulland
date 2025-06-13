import datetime as time
from discord.embeds import Embed
from discord.colour import Colour
from mcstatus.responses import JavaStatusResponse

import config

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

    def ipserver(self):
        self = Embed(
            title="🎮 IP เซิร์ฟเวอร์ Minecraft: play.soullandrealms.com",
            description=(
            "🌟 **พร้อมผจญภัยแล้วหรือยัง?**\n"
            "เชื่อมต่อเซิร์ฟเวอร์ Minecraft ของเราได้เลยที่:\n\n"
            "`play.soullandrealms.com`\n\n"
            "🧭 **เวอร์ชันที่รองรับ:** 1.21.4 ขึ้นไป\n"
            "มาร่วมเป็นส่วนหนึ่งของโลกแฟนตาซีใน **Soulland Realms** วันนี้!"
            ),
            color=Colour.green()
        )
        
        self.set_image(
            url="https://media.discordapp.net/attachments/938151480270127174/1382834134585446650/soulland.jpg?format=webp&width=1522&height=856"
        )
        
        self.set_footer(text="Soulland Realms | IP สำหรับเข้าเล่นเซิร์ฟเวอร์ Minecraft")
        
        return self

    def invite_link(self):
        self = Embed(
            title="🔗 ลิงก์เชิญเพื่อน https://discord.gg/mcsoulland",
            description=(
                "ร่วมผจญภัยไปกับโลกแฟนตาซีแห่ง **Soulland Realms** 🌍\n\n"
                "🧙‍♂️ **อย่าลืมชวนเพื่อนของคุณเข้าร่วมด้วย!**\n"
                "ลิงก์อยู่ที่นี่: https://discord.gg/mcsoulland 💌"
            ),
            color=Colour.blue()
        )

        self.set_image(
            url="https://media.discordapp.net/attachments/938151480270127174/1382834134585446650/soulland.jpg?format=webp&width=1522&height=856"
        )
        
        self.set_footer(text="Soulland Realms | Fantasy MMO Community")
        
        return self
    
    def website(self):
        self = Embed(
            title="🛒 ร้านค้าอย่างเป็นทางการ Soulland Realms",
            description=(
                "🎁 **สนับสนุนเซิร์ฟเวอร์และรับของรางวัลพิเศษ!**\n\n"
                "คุณสามารถซื้อไอเทม, ยศพิเศษ, และแพ็กเกจอื่น ๆ ได้ที่ร้านค้าของเรา:\n\n"
                "👉 [คลิกที่นี่เพื่อเข้าสู่ร้านค้า](https://store.soullandrealms.com/)\n\n"
                "ทุกการสนับสนุนจะช่วยพัฒนาเซิร์ฟเวอร์และชุมชนของเราให้ดียิ่งขึ้น ❤️"
            ),
            color=Colour.gold()
        )

        self.set_thumbnail(
            url="https://media.discordapp.net/attachments/938151480270127174/1382834134585446650/soulland.jpg?format=webp&width=300&height=170"
        )

        self.set_footer(text="Soulland Realms | สนับสนุนเซิร์ฟเวอร์เพื่อสิทธิพิเศษต่าง ๆ")
        return self
    
    def status_on(self,status:JavaStatusResponse):
        self = Embed(
            title="สถานะ : 🟢 เซิฟเวอร์ออนไลน์",
            description=f"🌍 **Server IP:** `{config.SERVER_IP}`",
            color=Colour.green(),
            timestamp=time.datetime.now()
        )
        
        player_list = "No players online."
        if status.players.sample:
            player_names = [player.name for player in status.players.sample]
            player_list = ", ".join(player_names)
            if len(player_list) > 1024:
                player_list = player_list[:1020] + "..."

        self.add_field(name="📝 Version", value="1.21.4", inline=True)
        self.add_field(name="👥 Players", value=f"{status.players.online}/{status.players.max}", inline=True)
        self.add_field(name="📊 Ping", value=f"{round(status.latency)}ms", inline=True)
        self.add_field(name="🎮 Online Players", value=player_list, inline=False)
        self.add_field(name="📢 MOTD", value=status.description.title(), inline=False)
        self.set_thumbnail(url=f"https://api.mcsrvstat.us/icon/{config.SERVER_IP}")
        self.set_image(url=f"https://mcapi.us/server/image?theme=dark&ip={config.SERVER_IP}")
        self.set_footer(text="Last updated", icon_url="https://cdn-icons-png.flaticon.com/512/906/906361.png")

        return self
    
    def status_off(self):
        self = Embed(
            title="สถานะ : 🔴 เซิฟเวอร์ออฟไลน์",
            description=f"🚫 ขณะนี้เซิฟเวอร์ `{config.SERVER_IP}` ออฟไลน์อยู่",
            color=Colour.red(),
            timestamp=time.datetime.now()
        )
        self.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1828/1828843.png")
        return self