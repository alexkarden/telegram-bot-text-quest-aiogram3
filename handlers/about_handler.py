import configparser

from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command('about','alexkarden'))
async def cmd_about(message: Message):
    # Создание объекта ConfigParser
    config = configparser.ConfigParser()
    # Чтение файла
    config.read('handlers/texts.ini')
    cmd_text = config.get('cmd_about', 'cmd_text')
    formatted_text = cmd_text

    # Отправляем пользователю приветствие
    await message.answer(formatted_text, parse_mode=ParseMode.HTML)






