import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", 0))
if not TOKEN or CHANNEL_ID == 0:
    raise ValueError("Please set DISCORD_TOKEN and CHANNEL_ID in your .env file")