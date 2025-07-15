# Импортируем модуль os для взаимодействия с операционной системой.
# Позволяет работать с файловой системой, получать доступ к переменным окружения и выполнять другие операции на уровне ОС.
import os
import configparser

from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery,FSInputFile
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.keyboards import list_games_keyboard, start_keyboard_inline
from utils.fuctions_game import send_chapter
from utils.functions_state import set_state,get_state
from utils.functions_uni import read_gameini, get_hero_stats




router = Router()

@router.callback_query()
async def callback_query(callback: CallbackQuery):
    data = callback.data
    if data == 'Игры':
        # await callback.message.answer(text=text, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
        await callback.message.answer(text='Игры', reply_markup= await list_games_keyboard(), parse_mode=ParseMode.HTML)

    elif data == 'mainmenu':
        # Создание объекта ConfigParser
        config = configparser.ConfigParser()
        # Чтение файла
        config.read('handlers/texts.ini')
        cmd_text = config.get('cmd_mainmenu', 'cmd_text')
        formatted_text = cmd_text.format(f"\n")
        await callback.message.answer(formatted_text, reply_markup=start_keyboard_inline, parse_mode=ParseMode.HTML)

    elif data.startswith('start_'):
        gamepath = data.split('_')[1]
        infofromini = await read_gameini(f'games/{gamepath}/game.ini')
        gamename = infofromini['gamename']
        gamedescription = infofromini['gamedescription']
        gameimagepath = infofromini['gameimagepath']
        caption = (f'<b>{gamename}</b>\n'
                   f'\n'
                   f'{gamedescription}')
        game_start_keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Начать", callback_data=f"gamestart_{gamepath}"),InlineKeyboardButton(text="Загрузить", callback_data=f"gameload_{gamepath}")],
            [InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")]
        ])


        # Проверяем, существует ли файл
        if os.path.exists(f'games/{gamepath}/{gameimagepath}'):
            # Создаем объект для фотографии
            photo = FSInputFile(f'games/{gamepath}/{gameimagepath}')
            # Отправляем фотографию с текстом
            await callback.message.answer_photo(photo=photo, caption=caption, reply_markup=game_start_keyboard_inline, parse_mode=ParseMode.HTML)
        else:
            await callback.message.answer(text=caption, reply_markup=game_start_keyboard_inline, parse_mode=ParseMode.HTML)



    elif data.startswith('gamestart_'):
        gamepath = data.split('_')[1]
        set_state(callback.from_user.id, gamepath,'location:start')
        fromsendchapter = send_chapter(callback.from_user.id)
        caption = fromsendchapter['text']
        keyboards = fromsendchapter['keyboards']
        gameimagepath = fromsendchapter['image']
        # Проверяем, существует ли файл
        print(f'games/{gamepath}/{gameimagepath}')
        if os.path.exists(f'games/{gamepath}/{gameimagepath}'):
            # Создаем объект для фотографии
            photo = FSInputFile(f'games/{gamepath}/{gameimagepath}')
            await callback.message.answer_photo(photo=photo, caption=caption, reply_markup=keyboards,parse_mode=ParseMode.HTML)
        else:
            await callback.message.answer(text=caption, reply_markup=keyboards, parse_mode=ParseMode.HTML)

    elif data.startswith('location:'):
        gamelocation = data.split(':')[1]
        gamepath = get_state(callback.from_user.id)['gamepath']
        set_state(callback.from_user.id, gamepath, f'location:{gamelocation}')
        fromsendchapter = send_chapter(callback.from_user.id)
        caption = fromsendchapter['text']
        keyboards = fromsendchapter['keyboards']
        gameimagepath=fromsendchapter['image']
        if os.path.exists(f'games/{gamepath}/{gameimagepath}'):
            # Создаем объект для фотографии
            photo = FSInputFile(f'games/{gamepath}/{gameimagepath}')
            await callback.message.answer_photo(photo=photo, caption=caption, reply_markup=keyboards, parse_mode=ParseMode.HTML)
        else:
            await callback.message.answer(text=caption, reply_markup=keyboards, parse_mode=ParseMode.HTML)

    elif data == 'Менюигры':
        gamepath = get_state(callback.from_user.id)['gamepath']
        location = get_state(callback.from_user.id)['chapter']
        caption=f'{gamepath} {location}'

        game_continue_keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Сохранить", callback_data=f"gamestart_{gamepath}"),
             InlineKeyboardButton(text="Загрузить", callback_data=f"gameload_{gamepath}")],
            [InlineKeyboardButton(text="Продолжить", callback_data=location)]
        ])


        await callback.message.answer(text=caption, reply_markup=game_continue_keyboard_inline, parse_mode=ParseMode.HTML)