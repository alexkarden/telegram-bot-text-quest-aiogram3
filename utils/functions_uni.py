# Импортируем библиотеку asyncio для работы с асинхронным программированием.
import asyncio
# Импортируем библиотеку для логирования. Позволяет записывать события, ошибки и информацию о работе бота.
import logging
import configparser







await def read_ini(filepath)
# Создание объекта ConfigParser
config = configparser.ConfigParser()
# Чтение файла
config.read('games/games.ini')
# Получение всех секций
sections = config.sections()
# Чтение значения из секции и опции
for section in sections:
    print(section)
value = config.get('Game01', 'gamename')