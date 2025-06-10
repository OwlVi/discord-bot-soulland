import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", 0))
ROLE_ID = int(os.getenv("RESTART_ROLE_ID", 0))

if not TOKEN or CHANNEL_ID == 0 or ROLE_ID == 0:
    raise ValueError("Please set TOKEN, CHANNEL_ID, and RESTART_ROLE_ID in your .env file")