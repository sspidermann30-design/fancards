import random  # Не забудь импортировать random в начале


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Допустим, мы выбираем случайный ID от 1 до 2 (Хагрид и Рон)
    card_id = random.randint(1, 2)

    # Добавляем ID к ссылке через знак вопроса
    web_link = f"https://sspidermann30-design.github.io/fancards/web/index.html?id={card_id}"

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть пак 🃏", web_app=WebAppInfo(url=web_link))]
    ])

    await message.answer("Твой ежедневный пак готов к открытию!", reply_markup=markup)