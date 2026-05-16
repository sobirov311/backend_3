import asyncio
import aiohttp
from deep_translator import GoogleTranslator
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "8237583362:AAEV73uiXJ7nqrbKng8-i1RxbH7anrq9Mno"
API_KEY = "ad44fee456d6a1d090bd4842"

dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message) -> None:
    await message.answer("Bu bot aiogram yordamida qilingan")

@dp.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.reply("Bu bot test uchun yasalgan")

@dp.message(Command("tarjima"))
async def tarjima_handler(message: Message) -> None:
    matn = message.text.replace("/tarjima", "").strip()
    if not matn:
        await message.answer("Tarjima qilish uchun matn kiriting: /tarjima salom")
        return
    result = GoogleTranslator(source='uz', target='en').translate(matn)
    await message.answer(result)

@dp.message(Command("dollar"))
async def dollar_handler(message: Message) -> None:
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/USD/UZS"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            kurs = data['conversion_rate']
    await message.answer(f"Dollar kursi: {kurs} UZS")

@dp.message(Command("havo"))
async def havo_handler(message: Message) -> None:
    url = "https://wttr.in/Urgench?format=j1"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json(content_type=None)
            temp = data['current_condition'][0]['temp_C']
            feels = data['current_condition'][0]['FeelsLikeC']
            desc = data['current_condition'][0]['weatherDesc'][0]['value']
    await message.answer(
        f"🌤 Urgench havo:\n"
        f"🌡 Harorat: {temp}°C\n"
        f"🤔 His qilinishi: {feels}°C\n"
        f"📋 Holat: {desc}"
    )
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())