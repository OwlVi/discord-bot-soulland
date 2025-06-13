import discord
from discord.ext.commands import Bot
from features.listener import GiveRole, HandlerModal, SoullandEmbed, SoullandView
from discord.interactions import Interaction
from discord.channel import TextChannel
from config import TOKEN, VERIFY_CHANNEL_ID, GIVE_ROLE_CHANNEL_ID
from features.routing import ButtonType

intents = discord.Intents.all()
bot = Bot(command_prefix="!", intents=intents)

sent_message = None  # เก็บข้อความที่ส่งไว้ เพื่อลบตอนปิด
channel_list = []  # เก็บช่องทางที่ส่งข้อความไว้

@bot.event
async def on_ready():
    try:
        await bot.tree.sync()
        print(f"✅ Logged in as {bot.user}")
        
        # initialize channels and views
        
        verify_channel = bot.get_channel(VERIFY_CHANNEL_ID)
        if not verify_channel:
            print("❌ Channel not found")
            return

        if isinstance(verify_channel, TextChannel):
            await delete_sent_message(verify_channel)
            await verify_channel.send(
                embed=SoullandEmbed().verify(), 
                view=SoullandView().add(ButtonType.VERIFY.value))
            print("✅ Verify embed created successfully")
        else:
            print("❌ Verify channel is not a TextChannel")

        give_role_channel = bot.get_channel(GIVE_ROLE_CHANNEL_ID)
        if not give_role_channel:
            print("❌ Give role channel not found")
            return
        if isinstance(give_role_channel, TextChannel):
            await delete_sent_message(give_role_channel)
            await give_role_channel.send(
                embed=SoullandEmbed().give_role(), 
                view=SoullandView().add(ButtonType.GIVE_ROLE.value, ButtonType.LINK_DISCORD.value))
            print("✅ Give role embed created successfully")
        else:
            print("❌ Give role channel is not a TextChannel")
    
        channel_list.append(verify_channel)
        channel_list.append(give_role_channel)
            
        print("✅ Bot is ready and embeds are sent successfully")

    except Exception as e:
        print(f"❌ Error during on_ready: {e}")
        await bot.close()
        
@bot.event
async def on_interaction(interaction: Interaction):
    if interaction.data is None:
        print("Interaction not have")
        return 
    custom_id = interaction.data.get("custom_id")
    print("Interaction ID:",custom_id)
    match custom_id:
        case ButtonType.GIVE_ROLE.value:
            await GiveRole().on_submit(interaction)
        case ButtonType.VERIFY.value:
            await HandlerModal().handle_verify(interaction)
        
@bot.event
async def on_disconnect():
    print("🔌 Disconnected from Discord")
    for channel in channel_list:
        if isinstance(channel, TextChannel):
            await delete_sent_message(channel)
            print(f"🧹 Deleted messages in {channel.name}")

async def delete_sent_message(channel: TextChannel ):
    fetched_channel = bot.get_channel(channel.id) if channel else None
    if isinstance(fetched_channel, TextChannel):
        deleted = await fetched_channel.purge(limit=50, check=lambda m: m.author == bot.user)
        print(f"🧹 Deleted {len(deleted)} messages")
        
bot.run(TOKEN)
