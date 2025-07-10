# Импортируем модуль os для взаимодействия с операционной системой.
# Позволяет работать с файловой системой, получать доступ к переменным окружения и выполнять другие операции на уровне ОС.
import os

from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery,FSInputFile
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.keyboards import list_games_keyboard
from utils.functions_uni import read_ini



router = Router()

@router.callback_query()
async def callback_query(callback: CallbackQuery):
    data = callback.data
    if data == 'Игры':
        # await callback.message.answer(text=text, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
        await callback.message.answer(text='Игры', reply_markup= await list_games_keyboard(), parse_mode=ParseMode.HTML)

    elif data.startswith('start_'):
        gamepath = data.split('_')[1]
        infofromini = await read_ini(f'games/{gamepath}/game.ini')
        gamename = infofromini['gamename']
        gamedescription = infofromini['gamedescription']
        gameimagepath = infofromini['gameimagepath']
        gamejsonpath = infofromini['gamejsonpath']
        caption = (f'<b>{gamename}</b>\n'
                   f'\n'
                   f'{gamedescription}')
        game_start_keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Начать", callback_data=f"gamestart_{gamepath}"),InlineKeyboardButton(text="Загрузить", callback_data=f"gameload_{gamepath}")],
            [InlineKeyboardButton(text="Назад в меню", callback_data="menu")]
        ])


        # Проверяем, существует ли файл
        if os.path.exists(f'games/{gamepath}/{gameimagepath}'):
            # Создаем объект для фотографии
            photo = FSInputFile(f'games/{gamepath}/{gameimagepath}')
            # Отправляем фотографию с текстом
            await callback.message.answer_photo(photo=photo, caption=caption, reply_markup=game_start_keyboard_inline, parse_mode=ParseMode.HTML)
        else:
            await callback.message.answer(text=caption, reply_markup=game_start_keyboard_inline, parse_mode=ParseMode.HTML)