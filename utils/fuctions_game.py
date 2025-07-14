from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import configparser
import re

from utils.functions_state import get_state



def send_chapter(chat_id):
  buttons = []
  keyboard = []
  state = get_state(chat_id)
  # Создание объекта ConfigParser
  config = configparser.ConfigParser()
  # Чтение файла
  filepath = f'games/{state['gamepath']}/quest.ini'
  config.read(filepath)
  location = state['chapter']
  if location in config:
    image = config.get(location, 'image')

    text = config.get(location, 'text')

    # Итерируемся по всем ключам в секции, чтобы найти кнопки
    for key in config[location]:
      # Проверяем, что ключ начинается с "button"
      if key.startswith('button'):
        # Извлекаем текст и колбэк для кнопки
        if 'text' in key:
          match = re.search(r'button(\d+)_text', key)
          button_index = match.group(1)
          button_text = config.get(location, key)
          button_callback = config.get(location, f'button{button_index}_callback')
          # Добавляем текст и колбэк кнопки в список
          button = InlineKeyboardButton(text=button_text, callback_data=button_callback)
          # Добавляем кнопку в клавиатуру
          keyboard.append([button])




  returnkeyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
  
  return {"image":image,
          "text":text,
          "keyboards": returnkeyboard}
