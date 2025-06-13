import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

TANG_SAN = os.getenv("TANG_SAN").__str__()
SOULLAND_COMMUNITY = os.getenv("SOULLAND_COMMUNITY").__str__()
ROLE_ID = int(os.getenv("ROLE_ID", 0)).__int__()
GIVE_ROLE_CHANNEL_ID = int(os.getenv("GIVE_ROLE_CHANNEL_ID", 0)).__int__()
SERVER_ID = int(os.getenv("SERVER_ID", 0)).__int__()
DOT_CHANNEL_ID = int(os.getenv("DOT_CHANNEL_ID", 0)).__int__()
MEMBER_ROLE_ID = int(os.getenv("MEMBER_ROLE_ID", 0)).__int__()
VERIFY_CHANNEL_ID = int(os.getenv("VERIFY_CHANNEL_ID", 0)).__int__()
STATUS_CHANNEL_ID = int(os.getenv("STATUS_CHANNEL_ID", 0)).__int__()
INVITE_LINK_CHANNEL_ID = int(os.getenv("INVITE_LINK_CHANNEL_ID", 0)).__int__()
GIVE_ROLE_CHANNEL_ID = int(os.getenv("GIVE_ROLE_CHANNEL_ID", 0)).__int__()
IP_SERVER_CHANNEL_ID = int(os.getenv("IP_SERVER_CHANNEL_ID", 0)).__int__()
WEB_STORE_CHANNEL_ID = int(os.getenv("WEB_STORE_CHANNEL_ID", 0)).__int__()


def get_env_variable(var_name: str, default: Optional[str] = None) -> str:
    value = os.getenv(var_name, default)
    if value is None:
        raise ValueError(f"Environment variable '{var_name}' not set")
    return value
