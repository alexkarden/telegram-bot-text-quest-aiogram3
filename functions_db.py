import aiosqlite
import logging
import time

from config import DATABASE_NAME

#-----------------------------------------------------------------------------------------------------------------------Инициализация базы данных
async def init_db():
    try:
        async with aiosqlite.connect(DATABASE_NAME) as db:
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
        async with aiosqlite.connect(DATABASE_NAME) as db:
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
