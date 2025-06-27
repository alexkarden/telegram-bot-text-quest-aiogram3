import configparser
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#-----------------------------------------------------------------------------------------------------------------------кнопки
button_main_menu = InlineKeyboardButton(text="☑️ Игры", callback_data="Игры")
button_help = InlineKeyboardButton(text="Помощь", callback_data='Помощь')
button_settings = InlineKeyboardButton(text="⚙️ Настройки", callback_data='Настройки')


#-----------------------------------------------------------------------------------------------------------------------клавиатура на старте
start_keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[
    [button_main_menu],
    [button_help,button_settings]
    ])
#-----------------------------------------------------------------------------------------------------------------------клавиатура списка игр
async def list_games_keyboard():
    keyboard = []
    # Создание объекта ConfigParser
    config = configparser.ConfigParser()
    # Чтение файла
    config.read('games/games.ini')
    # Получение всех секций
    sections = config.sections()
    if sections:
        for section in sections:
            gamename = config.get(section, 'gamename')
            gamepath = config.get(section, 'gamepath')
            button = InlineKeyboardButton(text=gamename, callback_data=gamepath)
            keyboard.append([button])
        return InlineKeyboardMarkup(inline_keyboard=keyboard)

    else:
        return InlineKeyboardMarkup(inline_keyboard=[])
