# Импортируем библиотеку asyncio для работы с асинхронным программированием.
import asyncio
# Импортируем библиотеку для логирования. Позволяет записывать события, ошибки и информацию о работе бота.
import logging
# Импортируем классы Bot и Dispatcher из библиотеки aiogram для создания Telegram-бота.
from aiogram import Bot, Dispatcher
# Импортируем токен бота из файла конфигурации config.py
from config import TOKENTG

# Импортируем функцию инициализации базы данных из database.functions_db
from utils.functions_db import init_db
# Создаем объект Bot, передавая токен, который позволяет боту взаимодействовать с Telegram API.
bot = Bot(token=TOKENTG)
# Создаем объект Dispatcher для обработки обновлений и маршрутизации сообщений.
dp = Dispatcher()

# Импортируем роутеры из файлов обработчиков
from handlers.start_handler import router as start_router
from handlers.about_handler import router as about_router
from handlers.callback_handler import router as callback_router
# Подключаем роутер
dp.include_router(start_router)
dp.include_router(about_router)
dp.include_router(callback_router)



#-----------------------------------------------------------------------------------------------------------------------Основная функция
async def main():
    #Создаем базу данных, если ее нет.
    await init_db()
    # Запускаем поллинг
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        filename='logfile.log',
        filemode='w',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.error('Exit')
