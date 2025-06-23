import logging
import time
import os
import configparser

from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery,FSInputFile


from functions_db import add_user_db







router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    welcome_text = (
        f"👋 <b>Добро пожаловать, {message.from_user.first_name}!</b>\n")
    # Записываем пользователя в базу
    await add_user_db(message.from_user.id, message.from_user.first_name, message.from_user.last_name,
                      message.from_user.username)
    await message.answer(welcome_text, parse_mode=ParseMode.HTML)






