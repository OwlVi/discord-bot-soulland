from discord.ui import Button
from discord.enums import ButtonStyle
from features.routing import ButtonType

class SoulButton():
    def button_give_role(self):
        self=Button(
            label="รับยศ MEMBER",
            style=ButtonStyle.success,
            custom_id=ButtonType.GIVE_ROLE.value
        )
        return self
    
    def button_verify(self):
        self = Button(
            label="กรอกรหัสยืนยัน",
            style=ButtonStyle.success,
            custom_id=ButtonType.VERIFY.value
        )
        return self
        
    def button_link_discord(self):
        self = Button(
            label="วิธีเชื่อม Discord",
            style=ButtonStyle.link,
            url="https://www.youtube.com/watch?v=IUl0jDDN6Ug&t=1s",
        )
        return self
        
