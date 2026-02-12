import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from logic import get_random_card

# Вставь сюда свой токен!
API_TOKEN = '8545249940:AAFktK5Y-wwPlXngUglUxpyXZ8mLw3ECwlU'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n"
        "Добро пожаловать в мир коллекционных карточек.\n"
        "Каждые 12 часов ты можешь открыть бесплатный пак!"
    )

    # Сразу дадим игроку попробовать вытянуть карту
    card = get_random_card()

    if card:
        # Формируем текст под карточкой (фраза + описание)
        caption_text = (
            f"🌟 Тебе выпала карта: **{card['name']}**\n"
            f"✨ Редкость: {card['rarity']}\n"
            f"💬 *\"{card['phrase']}\"*\n\n"
            f"📜 {card['description']}"
        )

        # Отправляем карту (если файл картинки лежит в папке с проектом)
        try:
            # Важно: файлы должны лежать прямо в папке проекта
            photo = types.FSInputFile(card['image'])
            await message.answer_photo(photo, caption=caption_text, parse_mode="Markdown")
        except Exception as e:
            await message.answer(f"Картинка не найдена, но персонаж выпал: {card['name']}\n(Ошибка: {e})")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
