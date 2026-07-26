import os
import asyncio
from aiohttp import web
from pyrogram import Client, filters

# Render beradigan PORT yoki standart 8080
PORT = int(os.environ.get("PORT", 8080))

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
SESSION_STRING = os.environ.get("SESSION_STRING")

app = Client(
    "my_userbot",
    api_id=int(API_ID) if API_ID else None,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

# Render'ning port so'roviga "OK" javob beruvchi feyk veb-server
async def handle_ping(request):
    return web.Response(text="Userbot is running!")

@app.on_message(filters.private & ~filters.me)
async def auto_reply(client, message):
    await asyncio.sleep(2)
    await message.reply_text("Assalomu alaykum! Hozir bandman, tez orada javob yozaman.")

async def main():
    # Web serverni orqa fonda ishga tushirish
    server_app = web.Application()
    server_app.router.add_get("/", handle_ping)
    runner = web.AppRunner(server_app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    
    # Telegram Userbot'ni ishga tushirish
    async with app:
        print(f"Userbot muvaffaqiyatli ishga tushdi (Port: {PORT})...")
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
