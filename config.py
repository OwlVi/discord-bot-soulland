import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

TOKEN = os.getenv("TOKEN").__str__()
VERIFY_CHANNEL_ID = int(os.getenv("VERIFY_CHANNEL_ID", 0)).__int__()
GIVE_ROLE_CHANNEL_ID = int(os.getenv("GIVE_ROLE_CHANNEL_ID", 0)).__int__()
ROLE_ID = int(os.getenv("ROLE_ID", 0)).__int__()
GIVE_ROLE_CHANNEL_ID = int(os.getenv("GIVE_ROLE_CHANNEL_ID", 0)).__int__()
SERVER_ID = int(os.getenv("SERVER_ID", 0)).__int__()
MEMBER_ROLE_ID = int(os.getenv("MEMBER_ROLE_ID", 0)).__int__()


def get_env_variable(var_name: str, default: Optional[str] = None) -> str:
    value = os.getenv(var_name, default)
    if value is None:
        raise ValueError(f"Environment variable '{var_name}' not set")
    return value
