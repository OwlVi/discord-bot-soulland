import asyncio
from bot.tang_san import tang_san
from bot.soulland_community import soulland_community

async def main():
    await asyncio.gather(
        tang_san.start("TOKEN_1"),
        soulland_community.start("TOKEN_2")
    )

asyncio.run(main())
