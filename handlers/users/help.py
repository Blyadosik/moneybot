from _tracemalloc import stop
import re
from config import admins
from aiogram.bot import bot
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.default import menu
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, Text
import random
from loader import dp, bot
from utils.misc import rate_limit
import sys

@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def show_menu(message: Message):
    chat_id = message.from_user.id

    bot_username = (await bot.me).username
    bot_link = f"https://t.me/{bot_username}?start={chat_id}"
    await message.answer(text=
            f"{message.from_user.first_name}!\n"
            f"Ваша реферальная ссылка на сайт aeremins.ru/ref={chat_id}\n"
            f"Ваша реферальная ссылка для приглашений: {bot_link}\n"
            f"Проверить рефералов можно по команде: Мои рефералы 👥\n"
            f"Посмотреть баланс: Мой баланс 💵\n"
            f"Ответы на вопросы: FAQ 📖\n"
            f"Вывести деньги: Вывести деньги 💳\n"
            f"Страна: интернет-магазина Украина\n"
            f"Доставка не осуществляется в Донецкую и Луганскую области",
                         reply_markup=menu
                         )


@dp.message_handler(Text(equals=["Мои рефералы 👥"]))
async def get_button(message: Message):
    file_words = open(f"dictionaries/{message.chat.id}ref.txt", 'a')
    with open(f"dictionaries/{message.chat.id}ref.txt") as file:  # Открываем для чтения
        read_words = [row.strip() for row in file]  # Записываем в массив
    new_words = []
    if len(read_words) == 0:
        await message.answer(f'У вас еще нет рефералов')
    else:
        [new_words.append(item) for item in read_words if item not in new_words]  # Фильтруем, чтобы не было схожих слов

        a = "\n".join(new_words)
        print(a)

        await message.answer(f'Ваши рефералы:\n{a}')

    file_words.close()

@dp.message_handler(Text(equals=["Мой баланс 💵"]))
async def get_button(message: Message):
    file_words = open(f"dictionaries/{message.chat.id}bal.txt", 'a')
    with open(f"dictionaries/{message.chat.id}bal.txt") as file:  # Открываем для чтения
        read_words = [row.strip() for row in file]  # Записываем в массив

    enteredWord = read_words
    print(enteredWord)
    if len(enteredWord) == 0:
        await message.answer(f"На вашем балансе пока ничего нет")
    else:
        balance = enteredWord[0]
        await message.answer(f"На вашем балансе {balance}грн\n"
                         f"Заказать выплату можно по кнопке: Вывести деньги 💳")


@dp.message_handler(Text(equals=["FAQ 📖"]))
async def get_button(message: Message):
    await message.answer(f"Что я за бот? - Я бот который помогает людям заработать на продажах без вложений\n"
                         f"Со скольки лет я могу зарабатывать? - Во сколько угодно, главное уметь\n"
                         f"Зачем реферальная ссылка на сайт? - Это ссылка на интернет магазин. Если человек совершил покупку по вашей реферальной ссылке, то вам начисляется 20% от прибыли на ваш баланс\n"
                         f"Как я могу проверить свой баланс? - Баланс вы можете проверить по кнопке: Мой баланс 💵, он обновляется каждую среду и воскресенье.\n"
                         f"Как я могу заработать на реферальной ссылке? - Вы просто даете ссылку своим знакомым или рекламируете ее в соц.сетях и получаете прибыль\n"
                         f"Как я могу вывести деньги? - Вывести деньги можно по кнопке: Вывести деньги 💳\n"
                         f"Зачем реферальная ссылка для приглашений? - Эта ссылка для приглашения людей в этого бота. Если человек пришел в бота по вашей ссылке, то вы получаете 5% его прибыли, при этом он получает все теже 20%."
                         f"То есть, если вы не можете приглашать людей на сайт, то вы можете приглашать людей в бота и получать пассивную прибыль\n"
                         )

@dp.message_handler(Text(equals=["Вывести деньги 💳"]))
async def get_button(message: Message):
    file_words = open(f"dictionaries/{message.chat.id}bal.txt", 'a')
    with open(f"dictionaries/{message.chat.id}bal.txt") as file:  # Открываем для чтения
        read_words = [row.strip() for row in file]  # Записываем в массив

    enteredWord = read_words
    print(enteredWord)
    if len(enteredWord) == 0:
        await message.answer(f"На вашем балансе пока ничего нет")
    else:
        balance = enteredWord[0]
        if int(balance) < 500:
            await message.answer(f"На вашем балансе недостаточно денег.\n"
                                 f"Минимальная сумма выплаты 500грн\n"
                                 f"На вашем балансе {balance}грн")
        elif int(balance) >= 500:
            await message.answer(f"На вашем балансе {balance}грн\n"
                                 f"Ваша заявка принята к обработке, ожидайте ответа")
            await bot.send_message(admins, f"Пользователь {message.chat.id}, @"f"{message.from_user.username}," f"{message.from_user.first_name} хочет заказать выплату")