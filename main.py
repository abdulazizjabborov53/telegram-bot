import asyncio
from aiogram import Bot, Dispatcher, types

# BotFather'dan olingan token
BOT_TOKEN = "8882163183:AAGeHzRrXf1mn6dapaSozjTf3DRk2m1w_jI"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Botga kelgan har qanday xabarga avto-javob qaytarish
@dp.message()
async def auto_reply(message: types.Message):
    reply_text = (
        "Assalomu Alaykum"
    )
    await message.reply(reply_text)

async def main():
    print("Bot muvaffaqiyatli ishga tushdi va xabarlarni kutmoqda...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
