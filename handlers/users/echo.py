import logging
import re
from aiogram.types import Message, CallbackQuery
from config import admins
from keyboards.inline.choice_buttons import choice
from loader import dp, bot
from array import *




@dp.message_handler()
async def echo_bot(message: Message):

    alphabet = "&"
    s = message.text
    parts1 = s.rsplit(' + ', 1)
    parts2 = s.rsplit(' - ', 1)
    parts3 = s.rsplit(' = ', 1)
    res1 = parts1[0]
    res2 = parts2[0]
    res3 = parts3[1]
    for one_char in message.text:
        if one_char in alphabet:
            
            file = open(f"dictionaries/{res3}bal.txt")  # Открываем для чтения
            lines = file.readlines()  # Записываем в массив
            file.close()  # Закрываем
            file = open(f"dictionaries/{res3}bal.txt", "w")  # Открываем для записи
            if "+" in message.text:
                if len(lines) == 0:
                    bal = 0
                    deletedWord = res1
                    nbal = int(deletedWord)
                    line = int(bal) + int(nbal)

                    file.write(str(line))  # Записываем в файл, то что вышло
                    await bot.send_message(admins, deletedWord + " грн зачислены\n"
                                                       "На балансе " + str(line) + " грн")
                else:

                    deletedWord = res1
                    bal = lines[0]
                    print(bal)
                    nbal = int(deletedWord)
                    line = int(bal) + int(nbal)

                    file.write(str(line))  # Записываем в файл, то что вышло
                    await bot.send_message(admins, deletedWord + " грн зачислены\n"
                                     "На балансе " + str(line) + " грн")
            if "-" in message.text:
                if len(lines) == 0:
                    bal = 0
                    deletedWord = res2
                    nbal = int(deletedWord)
                    line = int(bal) - int(nbal)

                    file.write(str(line))  # Записываем в файл, то что вышло
                    await bot.send_message(admins, deletedWord + " грн зачислены\n"
                                                       "На балансе " + str(line) + " грн")
                else:

                    deletedWord = res2
                    bal = lines[0]
                    print(bal)
                    nbal = int(deletedWord)
                    line = int(bal) - int(nbal)

                    file.write(str(line))  # Записываем в файл, то что вышло
                    await bot.send_message(admins, deletedWord + " грн зачислены\n"
                                     "На балансе " + str(line) + " грн")

            file.close()
            await message.edit_reply_markup()
            break


    alphabet = "%"
    s = message.text
    parts1 = s.rsplit(' + ', 1)
    parts3 = s.rsplit(' = ', 1)
    res1 = parts1[0]
    res3 = parts3[1]
    for one_char in message.text:
        if one_char in alphabet:

            file_words = open(f"dictionaries/{res3}ref.txt", 'a')  # Открываем для записи
            with open(f"dictionaries/{res3}ref.txt") as file:  # Отрываем для чтения - with автоматический закрывает файл
                reads_words = [row.strip() for row in file]
            get_button = res1  # Вводим желаемое слово
            file_words.write("@" + get_button + '\n')  # Записываем слово, если новое
            await bot.send_message(admins, f"Реферал - " + get_button + " добавлено \n"
                                                                     f"Все рефералы: {reads_words }" +f"@{get_button}")
            print(get_button)
            file_words.close()

            await message.edit_reply_markup()
            break

    alphabet = "№"
    for one_char in message.text:
        if one_char in alphabet:
            file_words = open(f"dictionaries/database.txt", 'a')
            with open(f"dictionaries/database.txt") as file:  # Открываем для чтения
                read_words = [row.strip() for row in file]  # Записываем в массив
            new_words = []
            if len(read_words) == 0:
                await message.answer(admins, f'База пустая')
            else:
                [new_words.append(item) for item in read_words if
                 item not in new_words]  # Фильтруем, чтобы не было схожих слов

                a = "\n".join(new_words)
                print(a)

                await bot.send_message(admins, f'База\n{a}')

            file_words.close()