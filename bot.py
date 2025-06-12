import discord
from discord.ext import commands
from features.listener import SoullandEmbed, SoullandView
from config import TOKEN, VERIFY_CHANNEL_ID, GIVE_ROLE_CHANNEL_ID

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

sent_message = None  # เก็บข้อความที่ส่งไว้ เพื่อลบตอนปิด
channel_list = []  # เก็บช่องทางที่ส่งข้อความไว้

@bot.event
async def on_ready():
    try:
        await bot.tree.sync()
        print(f"✅ Logged in as {bot.user}")
        
        # initialize channels and views
        
        verify_channel = bot.get_channel(VERIFY_CHANNEL_ID.__int__())
        if not verify_channel:
            print("❌ Channel not found")
            return

        if isinstance(verify_channel, discord.TextChannel):
            await delete_sent_message(verify_channel)
            await verify_channel.send(embed=SoullandEmbed().verify(), view=SoullandView().add("verify"))
            print("✅ Verify embed created successfully")
        else:
            print("❌ Verify channel is not a TextChannel")

        give_role_channel = bot.get_channel(GIVE_ROLE_CHANNEL_ID.__int__())
        if not give_role_channel:
            print("❌ Give role channel not found")
            return
        if isinstance(give_role_channel, discord.TextChannel):
            await delete_sent_message(give_role_channel)
            await give_role_channel.send(embed=SoullandEmbed().give_role(), view=SoullandView().add("give_role", "link"))
            print("✅ Give role embed created successfully")
        else:
            print("❌ Give role channel is not a TextChannel")
    
        channel_list.append(verify_channel)
        channel_list.append(give_role_channel)
            
        print("✅ Bot is ready and embeds are sent successfully")

    except Exception as e:
        print(f"❌ Error during on_ready: {e}")
        await bot.close()

async def delete_sent_message(channel: discord.TextChannel ):
    fetched_channel = bot.get_channel(channel.id) if channel else None
    if isinstance(fetched_channel, discord.TextChannel):
        deleted = await fetched_channel.purge(limit=50, check=lambda m: m.author == bot.user)
        print(f"🧹 Deleted {len(deleted)} messages")
     
@bot.event
async def on_disconnect():
    print("🔌 Disconnected from Discord")
    for channel in channel_list:
        if isinstance(channel, discord.TextChannel):
            await delete_sent_message(channel)
            print(f"🧹 Deleted messages in {channel.name}")

bot.run(TOKEN.__str__())
