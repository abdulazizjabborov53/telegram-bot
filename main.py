import os
import asyncio
from pyrogram import Client, filters

# Render muhitidan olinadigan maxfiy kalitlar
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
SESSION_STRING = os.environ.get("SESSION_STRING")

app = Client(
    "my_userbot",
    api_id=int(API_ID) if API_ID else None,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

# Faqat shaxsiy chatlarga (PM) kelgan va siz yubormagan xabarlarga javob qaytaradi
@app.on_message(filters.private & ~filters.me)
async def auto_reply(client, message):
    reply_text = "Assalomu alaykum! Hozir bandman, tez orada javob yozaman."
    await asyncio.sleep(2)
    await message.reply_text(reply_text)

async def main():
    async with app:
        print("Userbot muvaffaqiyatli ishga tushdi va ishlamoqda...")
        await asyncio.Event().wait()  # Botni doimiy ochiq ushlab turadi

if __name__ == "__main__":
    asyncio.run(main())
