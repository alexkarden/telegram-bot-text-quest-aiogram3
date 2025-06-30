import configparser

from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

#Импорт пользовательских функций
from utils.functions_db import add_user_db

#Импорт пользовательских клавиатур
from keyboards.keyboards import start_keyboard_inline



router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    # Создание объекта ConfigParser
    config = configparser.ConfigParser()
    # Чтение файла
    config.read('handlers/texts.ini')
    cmd_text = config.get('cmd_start', 'cmd_text')
    formatted_text = cmd_text.format(f"👋",message.from_user.first_name,f"\n")
    # Записываем пользователя в базу
    await add_user_db(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)
    # Отправляем пользователю приветствие
    await message.answer(formatted_text, reply_markup=start_keyboard_inline, parse_mode=ParseMode.HTML)






