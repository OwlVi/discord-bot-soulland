import asyncio
import logging
import config
from discord.ext.commands import Bot
from bot.tang_san import tang_san
from bot.soulland_community import soulland_community

logging.basicConfig(level=logging.INFO)

async def run_bot(bot:Bot, token_name: str, token: str):
    while True:
        try:
            logging.info(f"Starting bot: {token_name}")
            await bot.start(token)
        except Exception as e:
            logging.exception(f"Bot {token_name} crashed: {e}")
            logging.info(f"Restarting {token_name} in 5 seconds...")
            await asyncio.sleep(5)  # รอแล้วค่อย start ใหม่
        else:
            logging.info(f"Bot {token_name} shut down normally.")
            break

async def main():
    await asyncio.gather(
        run_bot(tang_san, "TANG_SAN", config.TANG_SAN),
        run_bot(soulland_community, "SOULLAND_COMMUNITY", config.SOULLAND_COMMUNITY)
    )

if __name__ == "__main__":
    asyncio.run(main())
