import aiosqlite
import logging
import time

from config import DATABASENAME

#-----------------------------------------------------------------------------------------------------------------------Инициализация базы данных
async def init_db():
    try:
        async with aiosqlite.connect(DATABASENAME) as db:
            # Создание таблицы users, если она еще не существует
            await db.execute(""
                             "CREATE TABLE IF NOT EXISTS users ("
                             "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                             "user_id INTEGER UNIQUE, "
                             "first_name TEXT, "
                             "last_name TEXT, "
                             "username TEXT, "
                             "user_added INTEGER NOT NULL, "
                             "user_blocked INTEGER NOT NULL, "              
                             "type_of_notification TEXT, "
                             "notification_frequency TEXT,"
                             "created_at INTEGER)"
                             "")
            # Создание таблицы users, если она еще не существует
            await db.execute(""
                             "CREATE TABLE IF NOT EXISTS states ("
                             "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                             "user_id INTEGER, "
                             "created_at INTEGER,"
                             "gamepath TEXT,"
                             "state TEXT)"
                             "")
            await db.commit()
    except aiosqlite.Error as e:
        logging.error(f"Ошибка при инициализации базы данных: {e}")
    except Exception as e:
        logging.error(f"Произошла неожиданная ошибка при инициализации базы данных: {e}")




#-----------------------------------------------------------------------------------------------------------------------Добавляем нового пользователя
# Добавление пользователя в базу данных
async def add_user_db(user_id, first_name, last_name, username):
    try:
        created_at = int(time.time())
        async with aiosqlite.connect(DATABASENAME) as db:
            # Проверка, существует ли пользователь в базе данных
            async with db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)) as cursor:
                result = await cursor.fetchone()
                if result is not None:
                    # Если пользователь существует, можно обновить его данные
                    await db.execute("UPDATE users SET first_name = ?, last_name = ?, username = ?, user_added = ? WHERE user_id = ? ", (first_name, last_name, username, 1, user_id))
                    logging.info(f"Пользователь с ID {user_id} обновлен в базе данных.")
                else:
                    # Если не существует, добавляем нового пользователя
                    await db.execute("INSERT INTO users (user_id, first_name, last_name, username, user_added, user_blocked, created_at, type_of_notification, notification_frequency ) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)", (user_id, first_name, last_name, username, 1, 0, created_at,'full','never'))
                    logging.info(f"Пользователь с ID {user_id} добавлен в базу данных.")
                await db.commit()
    except aiosqlite.Error as e:
        logging.error(f"Ошибка при добавлении пользователя в базу данных: {e}")
    except Exception as e:
        logging.error(f"Произошла неожиданная ошибка при добавлении пользователя в базу данных: {e}")


#-----------------------------------------------------------------------------------------------------------------------Сохраняем игру
# Сохраняем игру в базу данных
async def save_game_to_db(user_id, gamepath, state):
    try:
        created_at = int(time.time())
        async with aiosqlite.connect(DATABASENAME) as db:
            await db.execute("INSERT INTO states (user_id, created_at, gamepath, state) VALUES (?, ?, ?, ?)", (user_id, created_at, gamepath, state))
            await db.commit()
    except aiosqlite.Error as e:
        logging.error(f"Ошибка при сохранении игры в базу данных: {e}")
    except Exception as e:
        logging.error(f"Произошла неожиданная ошибка при сохранении игры в базу данных: {e}")

#-----------------------------------------------------------------------------------------------------------------------Загружаем игру
# Загружаем игру из базу данных
async def load_game_from_db(user_id, gamepath):
    try:
        async with aiosqlite.connect(DATABASENAME) as db:
            async with db.execute("SELECT * FROM states WHERE user_id = ? AND gamepath = ? ORDER BY created_at DESC", (user_id,gamepath,)) as cursor:
                rows = await cursor.fetchall()  # Извлекаем все найденные строки
                print(rows)
                return rows  # Возвращаем список строк
    except aiosqlite.Error as e:
        logging.error(f"Ошибка при извлечении состояний из базы данных: {e}")
        return []  # Возвращаем пустой список в случае ошибки

    except Exception as e:
        logging.error(f"Произошла неожиданная ошибка: {e}")
        return []  # Возвращаем пустой список в случае ошибки