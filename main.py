import asyncio
import random
import json
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# --- НАСТРОЙКИ ---
API_TOKEN = 'ТВОЙ_ТОКЕН_ОТ_BOT_FATHER'  # Замени на свой реальный токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Путь к твоему файлу с карточками (теперь он лежит в папке web)
CARDS_PATH = os.path.join('web', 'cards.json')


# --- ЛОГИКА БОТА ---

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    try:
        # 1. Читаем cards.json, чтобы узнать, какие ID существуют
        with open(CARDS_PATH, 'r', encoding='utf-8') as f:
            cards_data = json.load(f)

        # 2. Выбираем случайную карточку из списка
        random_card = random.choice(cards_data)
        card_id = random_card['id']

        # 3. Формируем ссылку для Mini App с передачей ID
        # Убедись, что ссылка на твой GitHub Pages верная!
        web_link = f"https://sspidermann30-design.github.io/fancards/web/index.html?id={card_id}"

        # 4. Создаем кнопку
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Открыть пак 🪄", web_app=WebAppInfo(url=web_link))]
        ])

        await message.answer(
            f"Привет, {message.from_user.first_name}! 👋\n\n"
            "Я подготовил для тебя новый магический пак. "
            "Нажми на кнопку ниже, чтобы узнать, кто тебе попался!",
            reply_markup=markup
        )

    except FileNotFoundError:
        await message.answer("Ошибка: файл cards.json не найден в папке web!")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")


# --- ЗАПУСК ---

async def main():
    print("--- Бот запущен и готов к работе! ---")
    print("Не забудь нажать STOP и потом снова RUN в PyCharm, если бот уже работал.")
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот остановлен")