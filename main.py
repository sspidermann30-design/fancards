import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from logic import get_random_card

# 1. Вставь сюда свой токен
API_TOKEN = '8545249940:AAFktK5Y-wwPlXngUglUxpyXZ8mLw3ECwlU'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # 2. Твоя ссылка на GitHub Pages (проверь, чтобы ник и название были верными)
    web_link = "https://sspidermann30-design.github.io/fancards/web/index.html"

    # Создаем кнопку для открытия Mini App
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть коллекцию 🃏", web_app=WebAppInfo(url=web_link))]
    ])

    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n"
        "Добро пожаловать в игру! Нажми на кнопку ниже, чтобы открыть своё Mini App:",
        reply_markup=markup
    )


@dp.message(Command("pack"))
async def open_pack(message: types.Message):
    """Команда для быстрой проверки выпадения карт в чате"""
    card = get_random_card()
    if card:
        caption = (
            f"🌟 Тебе выпала карта: **{card['name']}**\n"
            f"✨ Редкость: {card['rarity']}\n"
            f"💬 *\"{card['phrase']}\"*"
        )
        try:
            photo = types.FSInputFile(card['image'])
            await message.answer_photo(photo, caption=caption, parse_mode="Markdown")
        except:
            await message.answer(f"Выпал {card['name']}, но картинка не найдена!")


async def main():
    print("Бот запущен и готов к работе!")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())