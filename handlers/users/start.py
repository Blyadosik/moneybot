from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from config import admins
from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    file_words = open(f"dictionaries/database.txt", 'a')  # Открываем для записи
    with open(f"dictionaries/database.txt") as file:  # Отрываем для чтения - with автоматический закрывает файл
        reads_words = [row.strip() for row in file]
    get_button = f"{message.chat.id}, @"f"{message.from_user.username}," f"{message.from_user.first_name}"
    file_words.write(get_button + '\n')  # Записываем слово, если новое
    await bot.send_message(admins, f"Пользователь {message.chat.id}, @"f"{message.from_user.username}," f"{message.from_user.first_name} присоединился")
    print(get_button)
    file_words.close()


    file_words = open(f"dictionaries/{message.from_user.id}ref.txt", 'a')
    file_words.close()
    file_words = open(f"dictionaries/{message.from_user.id}bal.txt", 'a')
    file_words.close()

    chat_id = message.from_user.id
    referral = message.get_args()

    bot_username = (await bot.me).username
    bot_link = f"https://t.me/{bot_username}?start={chat_id}"

    await message.answer(f"Привет, {message.from_user.first_name}!\n"
                         f"Ваша реферальная ссылка на сайт aeremins.ru?ref={chat_id}\n"
                         f"Ваша реферальная ссылка для приглашений: {bot_link}\n"
                         f"Проверить рефералов можно по команде: Мои рефералы 👥\n"
                         f"Вызвать справку: /help \n"
                         f"Посмотреть баланс: Мой баланс 💵")