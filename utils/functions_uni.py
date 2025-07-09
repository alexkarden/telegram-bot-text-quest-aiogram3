# Импортируем библиотеку asyncio для работы с асинхронным программированием.
import asyncio

# Импортируем библиотеку для логирования.
# Позволяет записывать события, ошибки и информацию о работе приложения, что полезно для отладки и мониторинга.
import logging

# Импортируем библиотеку configparser для работы с конфигурационными файлами.
# Позволяет читать, записывать и управлять данными в конфигурационных файлах формата .ini.
import configparser

# Импортируем модуль os для взаимодействия с операционной системой.
# Позволяет работать с файловой системой, получать доступ к переменным окружения и выполнять другие операции на уровне ОС.
import os






async def read_ini(filepath):
    try:

        # Создание объекта ConfigParser
        config = configparser.ConfigParser()
        # Чтение файла
        config.read(filepath)
        # Извлекаем название игры из секции Game
        gamename = config.get('game', 'gamename')
        gamedescription = config.get('game', 'gamedescription')
        gameimagepath = config.get('game', 'gameimagepath')
        gamejsonpath=config.get('game', 'gamejsonpath')
        return {'gamename':gamename,'gamedescription':gamedescription,'gameimagepath':gameimagepath,'gamejsonpath':gamejsonpath}
    except Exception as e:
        logging.error(f"Произошла ошибка при чтении ini: {e}")
        return {}

async def get_dir(path):
    try:
        all_entries = os.listdir(path)
        directories = [entry for entry in all_entries if os.path.isdir(os.path.join(path, entry))]
        return directories
    except FileNotFoundError:
        print(f"Ошибка: Каталог '{path}' не найден.")
        return []
    except PermissionError:
        print(f"Ошибка: Недостаточно прав для доступа к каталогу '{path}'.")
        return []
