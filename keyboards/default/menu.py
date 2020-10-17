from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Мои рефералы 👥"),
            KeyboardButton(text="Мой баланс 💵")
        ],
        [
            KeyboardButton(text="FAQ 📖"),
            KeyboardButton(text="Вывести деньги 💳")
        ]
    ],
    resize_keyboard=True
)