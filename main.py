import asyncio
import os

# Pyrogram import bo'lishidan oldin event loop o'rnatamiz
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from pyrogram import Client, filters

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
SESSION_STRING = os.environ.get("SESSION_STRING")

app = Client(
    "my_userbot",
    api_id=int(API_ID) if API_ID else None,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

@app.on_message(filters.private & ~filters.me)
async def auto_reply(client, message):
    await asyncio.sleep(2)
    await message.reply_text("Assalomu alaykum! Hozir bandman, tez orada javob yozaman.")

async def start_bot():
    async with app:
        print("Userbot muvaffaqiyatli ishga tushdi!")
        await asyncio.Event().wait()

if __name__ == "__main__":
    loop.run_until_complete(start_bot())
