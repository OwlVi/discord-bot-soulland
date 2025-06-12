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
                        print(f"Loaded {ext} successfully")
                    except Exception as e:
                        print(f"Failed to load {ext}: {e}")
    print("Download extensions successfully")