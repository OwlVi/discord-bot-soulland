import logging
import traceback
import discord
import config
from mcstatus import JavaServer
from discord.ext import tasks
from discord.errors import NotFound
from discord.ext.commands import Bot
from discord.channel import TextChannel
from discord.flags import Intents
from discord.message import Message
from features.embed import SoulEmbed

intents = Intents().all()
intents.message_content = True
sent_message = None
status_message = None
channel_list = []  

soulland_community = Bot(command_prefix="!", intents=intents)
logging.basicConfig(level=logging.INFO)


@soulland_community.event
async def on_ready():
    try:
        await soulland_community.tree.sync()
        print(f"✅ Logged in as {soulland_community.user}")
        
        # initialize channels and views
        
        invite_link_channel = soulland_community.get_channel(config.INVITE_LINK_CHANNEL_ID)

        if not invite_link_channel:
            print(f"❌{soulland_community.user} Channel not found")
            return

        if isinstance(invite_link_channel, TextChannel):
            await delete_sent_message(invite_link_channel)
            await invite_link_channel.send(
                embed=SoulEmbed().invite_link()
                )
            print(f"✅{soulland_community.user} Invite embed created successfully")
        else:
            print(f"❌{soulland_community.user} Invite channel is not a TextChannel")

        ipserver_channel = soulland_community.get_channel(config.IP_SERVER_CHANNEL_ID)

        if not ipserver_channel:
            print(f"❌{soulland_community.user} IP Server channel not found")
            return
        if isinstance(ipserver_channel, TextChannel):
            await delete_sent_message(ipserver_channel)
            await ipserver_channel.send(
                embed=SoulEmbed().ipserver()
                )
            print(f"✅{soulland_community.user} IP Server embed created successfully")
        else:
            print(f"❌{soulland_community.user} IP Server channel is not a TextChannel")
            
        web_store_channel = soulland_community.get_channel(config.WEB_STORE_CHANNEL_ID)

        if not web_store_channel:
            print(f"❌{soulland_community.user} Web store channel not found")
            return
        if isinstance(web_store_channel, TextChannel):
            await delete_sent_message(web_store_channel)
            await web_store_channel.send(
                embed=SoulEmbed().website()
                )
            print(f"✅{soulland_community.user} Web store embed created successfully")
        else:
            print(f"❌{soulland_community.user} Web store channel is not a TextChannel")
        update_server_status.start()
            
        print(f"✅{soulland_community.user} Bot is ready and SoulEmbed are sent successfully")
    except Exception as e:
        print(f"❌{soulland_community.user} Error during on_ready: {e}")
        traceback.print_exc()

@tasks.loop(seconds=60)
async def update_server_status():
    global status_message

    try:
        server = JavaServer.lookup(f"{config.SERVER_IP}:{config.SERVER_PORT}")
        status = server.status()
        embed = SoulEmbed().status_on(status=status)
        print(f"{soulland_community.user} Minecraft server connecting")
    except Exception as e:
        print(f"❌{soulland_community.user} Error fetching Minecraft server status: {e}")
        embed = SoulEmbed().status_off()

    # ดึง channel และตรวจสอบข้อความเก่า
    status_channel = soulland_community.get_channel(config.STATUS_CHANNEL_ID)
    if not isinstance(status_channel, TextChannel):
        print(f"❌{soulland_community.user} Status channel not found or invalid.")
        return

    # ค้นหาข้อความเดิม (ส่งโดยบอทตัวเอง)
    if not status_message:
        async for msg in status_channel.history(limit=10):
            if msg.author == soulland_community.user:
                status_message = msg
                break

    # ถ้ายังไม่มีข้อความเลย ให้ส่งใหม่
    if not status_message:
        status_message = await status_channel.send("🔄 Loading server status...")

    try:
        await status_message.edit(content=None, embed=embed)
        print(f"✅{soulland_community.user} Server status updated")
    except Exception as edit_error:
        print(f"⚠️{soulland_community.user} Failed to edit status message: {edit_error}")
        status_message = await status_channel.send(embed=embed)
        traceback.print_exc()



@soulland_community.event
async def on_message(message: Message):
    """ดักจับทุกข้อความเพื่อควบคุมช่องที่กำหนด"""
    
    # ข้ามข้อความจากบอททั้งหมด (รวมถึงตัวเอง)
    if message.author.bot:
        return

    # ตรวจสอบว่าอยู่ในแชนแนลที่กำหนดหรือไม่
    if message.channel.id == config.DOT_CHANNEL_ID:

        # ยอมรับเฉพาะข้อความที่เป็นจุดเดียวเท่านั้น
        if message.content.strip() != ".":
            try:
                await message.delete()
                logging.info(
                    "Delete User [%s]: %r",

                    message.author,
                    message.content,
                )
            except discord.Forbidden:
                logging.error("No permission")
            except discord.HTTPException as exc:
                logging.error("Error: %s", exc)

    # ให้ระบบคำสั่งอื่นทำงานต่อได้ตามปกติ
    await soulland_community.process_commands(message)
        
@soulland_community.event
async def on_disconnect():
    print(f"{soulland_community.user} Disconnected from Discord")
    for channel in channel_list:
        if isinstance(channel, TextChannel):
            await delete_sent_message(channel)
            print(f"{soulland_community.user} Deleted messages in {channel.name}")

async def delete_sent_message(channel: TextChannel ):
    fetched_channel = soulland_community.get_channel(channel.id) if channel else None
    if isinstance(fetched_channel, TextChannel):
        deleted = await fetched_channel.purge(limit=50, check=lambda m: m.author == soulland_community.user)
        print(f"{soulland_community.user} Deleted {len(deleted)} messages")
          