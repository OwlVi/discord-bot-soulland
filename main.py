import asyncio
import config
from bot.tang_san import tang_san
from bot.soulland_community import soulland_community

async def main():
    await asyncio.gather(
        tang_san.start(config.TANG_SAN),
        soulland_community.start(config.SOULLAND_COMMUNITY)
    )

asyncio.run(main())
