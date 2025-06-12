user_codes = {}

def save_user_code(user_id: int, code: str):
    user_codes[user_id] = code

def get_user_code(user_id: int):
    return user_codes.get(user_id)

async def setup(bot):
    bot.save_user_code = save_user_code
    bot.get_user_code = get_user_code
