import traceback
from discord.ext.commands import Bot
from discord.interactions import Interaction
from discord.channel import TextChannel
from discord.flags import Intents
from discord.ui import  View
from config import VERIFY_CHANNEL_ID, GIVE_ROLE_CHANNEL_ID
from features.button import SoulButton
from features.embed import SoulEmbed
from features.routing import ButtonType
from features.modal import GiveRole, HandlerModal

tang_san = Bot(command_prefix="!", intents=Intents().all())

sent_message = None  # เก็บข้อความที่ส่งไว้ เพื่อลบตอนปิด
channel_list = []  # เก็บช่องทางที่ส่งข้อความไว้

@tang_san.event
async def on_ready():
    
        await tang_san.tree.sync()
        print(f"Logged in as {tang_san.user}")
        
        # initialize channels and views
        
        verify_channel = tang_san.get_channel(VERIFY_CHANNEL_ID)
        if not verify_channel:
            print(f"{tang_san.user} Channel not found")
            return

        if isinstance(verify_channel, TextChannel):
            await delete_sent_message(verify_channel)
            await verify_channel.send(
                embed=SoulEmbed().verify(), 
                view=View(timeout=None).add_item(SoulButton().button_verify()))
            print(f"{tang_san.user} Verify embed created successfully")
        else:
            print(f"{tang_san.user} Verify channel is not a TextChannel")

        give_role_channel = tang_san.get_channel(GIVE_ROLE_CHANNEL_ID)
        if not give_role_channel:
            print(f"{tang_san.user} Give role channel not found")
            return
        if isinstance(give_role_channel, TextChannel):
            button = View(timeout=None)
            button.add_item(SoulButton().button_give_role())
            button.add_item(SoulButton().button_link_discord())
            await delete_sent_message(give_role_channel)
            await give_role_channel.send(
                embed=SoulEmbed().give_role(), 
                view=button)
            print(f"{tang_san.user} Give role embed created successfully")
        else:
            print(f"{tang_san.user} Give role channel is not a TextChannel")
            
        print(f"{tang_san.user} Bot is ready and SoulEmbed are sent successfully")


        traceback.print_exc()
        
@tang_san.event
async def on_interaction(interaction: Interaction):
    if interaction.data is None:
        print(f"{tang_san.user} Interaction not have")
        return 
    custom_id = interaction.data.get("custom_id")
    print(f"{tang_san.user} Interaction ID:",custom_id)
    match custom_id:
        case ButtonType.GIVE_ROLE.value:
            await GiveRole().on_submit(interaction)
        case ButtonType.VERIFY.value:
            await HandlerModal().handle_verify(interaction)
        
@tang_san.event
async def on_disconnect():
    print(f"{tang_san.user} Disconnected from Discord")
    for channel in channel_list:
        if isinstance(channel, TextChannel):
            await delete_sent_message(channel)
            print(f"{tang_san.user} Deleted messages in {channel.name}")

async def delete_sent_message(channel: TextChannel ):
    fetched_channel = tang_san.get_channel(channel.id) if channel else None
    if isinstance(fetched_channel, TextChannel):
        deleted = await fetched_channel.purge(limit=50, check=lambda m: m.author == tang_san.user)
        print(f"{tang_san.user} Deleted {len(deleted)} messages")
