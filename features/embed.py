import datetime as time
from random import randint
from discord.embeds import Embed
from discord.colour import Colour
from mcstatus.responses import JavaStatusResponse
import config


class SoulEmbed:
    def __init__(self):
        self.last_player_count = None 
        self.last_image_url = None
        
    def give_role(self):
        embed = Embed(
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
        embed.set_image(url="https://media.discordapp.net/attachments/938151480270127174/1382746650224885852/promote1.jpg?format=webp&width=1522&height=856")
        embed.set_footer(text="Soulland Realms | ระบบรับยศอัตโนมัติ")
        return embed
    
    def verify(self):
        embed = Embed(
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

        embed.add_field(
            name="📺 วิธีการยืนยันตัวตน (คลิกดูวิดีโอ)",
            value="**[คลิกดูวิดีโอ YouTube](https://www.youtube.com/watch?v=IUl0jDDN6Ug&t=1s)**",
            inline=False
        )

        embed.set_image(
            url="https://media.discordapp.net/attachments/938151480270127174/1381839706651754517/aw_.png?format=webp&quality=lossless&width=1522&height=856"
        )
        embed.set_footer(text="Soulland Realms - ระบบยืนยันตัวตนอัตโนมัติ")
        return embed

    def ipserver(self):
        embed = Embed(
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
        
        embed.set_image(
            url="https://media.discordapp.net/attachments/938151480270127174/1382834134585446650/soulland.jpg?format=webp&width=1522&height=856"
        )
        
        embed.set_footer(text="Soulland Realms | IP สำหรับเข้าเล่นเซิร์ฟเวอร์ Minecraft")
        
        return embed

    def invite_link(self):
        embed = Embed(
            title="🔗 ลิงก์เชิญเพื่อน https://discord.gg/mcsoulland",
            description=(
                "ร่วมผจญภัยไปกับโลกแฟนตาซีแห่ง **Soulland Realms** 🌍\n\n"
                "🧙‍♂️ **อย่าลืมชวนเพื่อนของคุณเข้าร่วมด้วย!**\n"
                "ลิงก์อยู่ที่นี่: https://discord.gg/mcsoulland 💌"
            ),
            color=Colour.blue()
        )

        embed.set_image(
            url="https://media.discordapp.net/attachments/938151480270127174/1382834134585446650/soulland.jpg?format=webp&width=1522&height=856"
        )
        
        embed.set_footer(text="Soulland Realms | Fantasy MMO Community")
        
        return embed
    
    def website(self):
        embed = Embed(
            title="🛒 ร้านค้าอย่างเป็นทางการ Soulland Realms",
            description=(
                "🎁 **สนับสนุนเซิร์ฟเวอร์และรับของรางวัลพิเศษ!**\n\n"
                "คุณสามารถซื้อไอเทม, ยศพิเศษ, และแพ็กเกจอื่น ๆ ได้ที่ร้านค้าของเรา:\n\n"
                "👉 [คลิกที่นี่เพื่อเข้าสู่ร้านค้า](https://store.soullandrealms.com/)\n\n"
                "ทุกการสนับสนุนจะช่วยพัฒนาเซิร์ฟเวอร์และชุมชนของเราให้ดียิ่งขึ้น ❤️"
            ),
            color=Colour.gold()
        )

        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/938151480270127174/1382834134585446650/soulland.jpg?format=webp&width=300&height=170"
        )

        embed.set_footer(text="Soulland Realms | สนับสนุนเซิร์ฟเวอร์เพื่อสิทธิพิเศษต่าง ๆ")
        return embed
    

    def status_on(self, status: JavaStatusResponse):
        embed = Embed(
            title="สถานะ : 🟢 เซิฟเวอร์ออนไลน์",
            description=f"🌍 **Server IP:** `{config.SERVER_IP}`",
            color=Colour.green(),
            timestamp=time.datetime.now()
        )
        
        # รายชื่อผู้เล่น
        player_list = "No players online."
        if status.players.sample:
            player_names = [player.name for player in status.players.sample]
            player_list = ", ".join(player_names)
            if len(player_list) > 1024:
                player_list = player_list[:1020] + "..."

        # ข้อมูลเวอร์ชัน + ping
        embed.add_field(name="📝 Version", value=status.version.name, inline=True)
        embed.add_field(name="👥 Players", value=f"{status.players.online}/{status.players.max}", inline=True)
        embed.add_field(name="📊 Ping", value=f"{round(status.latency)}ms", inline=True)
        embed.add_field(name="🎮 Online Players", value=player_list, inline=False)

        # MOTD
        motd = status.description.get('clean', [''])[0] if isinstance(status.description, dict) else str(status.description)
        embed.add_field(name="📢 MOTD", value=motd, inline=False)

        # Thumbnail
        embed.set_thumbnail(url=f"https://api.mcstatus.io/v2/icon/{config.SERVER_IP}")
        
        # Image
        # เงื่อนไข: update รูปเฉพาะเมื่อจำนวนผู้เล่นเปลี่ยน
        player_count = status.players.online
        if self.last_player_count != player_count:
            url = f"https://mcapi.us/server/image?theme=dark&ip={config.SERVER_IP}&cache_bust={randint(0, 999999)}"
            print(f"Player count changed: {self.last_player_count} → {player_count}")
            embed.set_image(url=url)
            self.last_player_count = player_count
            self.last_image_url = url
        else:
            embed.set_image(url=self.last_image_url)
            print("Player count unchanged — image not updated")
            
        # Footer
        embed.set_footer(text="Last updated", icon_url="https://cdn-icons-png.flaticon.com/512/906/906361.png")

        return embed
    
    def status_off(self):
        embed = Embed(
            title="สถานะ : 🔴 เซิฟเวอร์ออฟไลน์",
            description=f"🚫 ขณะนี้เซิฟเวอร์ `{config.SERVER_IP}` ออฟไลน์อยู่",
            color=Colour.red(),
            timestamp=time.datetime.now()
        )
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1828/1828843.png")
        return embed