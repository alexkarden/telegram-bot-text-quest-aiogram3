# Telegram Text Quest Bot

Интерактивный текстовый квест для Telegram на **aiogram 3**. Игрок проходит
сюжет, выбирает действия через inline-кнопки и получает разные концовки
в зависимости от решений.

## Возможности

- Интерактивный текстовый квест в Telegram
- Выбор действий через inline-кнопки
- Хранение прогресса игрока в базе данных
- Несколько сценариев или ветвлений сюжета
- Асинхронная архитектура на aiogram 3
- Запуск через Docker

## Как работает

```text
Игрок
  │
  ▼
Telegram
  │
  ▼
aiogram 3 handlers
  │
  ▼
Quest service
  │
  ├──▶ games/: сценарий и варианты выбора
  └──▶ database/: прогресс игрока
```

1. Игрок отправляет `/start`.
2. Бот загружает текущий шаг квеста.
3. Игрок выбирает действие через inline-кнопку.
4. Сервис квеста определяет следующий шаг и сохраняет прогресс.
5. Бот показывает новый текст и варианты выбора.

## Технологии

- Python 3
- aiogram 3
- SQLite
- Docker

## Быстрый старт

```bash
git clone [https://github.com/alexkarden/telegram-bot-text-quest-aiogram3.git](https://github.com/alexkarden/telegram-bot-text-quest-aiogram3.git)
cd telegram-bot-text-quest-aiogram3

cp .env.example .env
```

Укажите токен бота в `.env`:

```env
BOT_TOKEN=your_telegram_bot_token
DATABASE_PATH=database/quest.db
```

Локальный запуск:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
python run.py
```

Запуск через Docker:

```bash
docker compose up -d --build
```

## Команды бота

| Команда | Описание |
|---|---|
| `/start` | Начать квест или продолжить сохранённый прогресс |
| `/help` | Краткая справка |
| `/restart` | Начать квест заново |

## Пример игрового процесса

```text
Ты находишься в тёмном коридоре.
Впереди две двери: деревянная и металлическая.

[ Открыть деревянную дверь ]
[ Открыть металлическую дверь ]
[ Осмотреть коридор ]
```

## Структура проекта

```text
handlers/   # Обработчики сообщений и callback-запросов
keyboards/  # Inline-клавиатуры
games/      # Сценарии квеста
database/   # Работа с прогрессом игроков
utils/      # Вспомогательные функции
```

## Лицензия

MIT
