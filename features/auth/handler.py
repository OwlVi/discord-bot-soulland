import asyncio

user_codes = {}
code_expiry = {}

def save_user_code(user_id: int, code: str, expire_seconds: int = 300):
    user_codes[user_id] = code
    if user_id in code_expiry:
        code_expiry[user_id].cancel()

    async def expire_code():
        await asyncio.sleep(expire_seconds)
        user_codes.pop(user_id, None)
        code_expiry.pop(user_id, None)

    code_expiry[user_id] = asyncio.create_task(expire_code())

def get_user_code(user_id: int):
    return user_codes.get(user_id)

async def setup(bot):
    bot.save_user_code = save_user_code
    bot.get_user_code = get_user_code
