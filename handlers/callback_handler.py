import configparser

from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery,FSInputFile

from keyboards.keyboards import list_games_keyboard



router = Router()

@router.callback_query()
async def callback_query(callback: CallbackQuery):
    data = callback.data
    if data == 'Игры':
        # await callback.message.answer(text=text, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
        await callback.message.answer(text='Игры', reply_markup= await list_games_keyboard(), parse_mode=ParseMode.HTML)