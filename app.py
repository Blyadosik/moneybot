from aiogram import executor
from loader import bot, storage
from config import admins

async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)
    await bot.send_message(admins, f'Я запущен!')

async def on_shutdown(dp):
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
