import asyncio
import logging
from aiogram import Bot, Dispatcher

#Импорт переменных из файла config
from config import TOKEN_TG

#Импорт пользовательских функций
from handlers import router
from functions_db import init_db

bot = Bot(token=TOKEN_TG)
dp = Dispatcher()


#-----------------------------------------------------------------------------------------------------------------------Основная функция
async def main():
    #Создаем базу данных, если ее нет.
    await init_db()
    # Подключаем роутер
    dp.include_router(router)
    # Запускаем поллинг
    await dp.start_polling(bot)





if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.warning("A WARNING")
    logging.error("An ERROR")
    logging.critical("A message of CRITICAL severity")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.error('Exit')