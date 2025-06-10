import os

async def setup(bot):
    for folder in os.listdir("./features"):
        folder_path = f"./features/{folder}"
        if os.path.isdir(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith(".py") and filename != "__init__.py":
                    ext = f"features.{folder}.{filename[:-3]}"
                    try:
                        await bot.load_extension(ext)
                        print(f"โหลด {ext} สำเร็จ")
                    except Exception as e:
                        print(f"โหลด {ext} ไม่สำเร็จ: {e}")
    print("โหลด extensions เสร็จสิ้น")