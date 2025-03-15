Стек: Python, FastApi, Pydantic, SQLAlchemy, Uvicorn, Aiogram, Nginx/Tuna
Асинхронный вебхук телеграм бот для записи на прием/услуги со всем необходимым функционалом.
Имеется админка, просмотр записей с информацией о записи и клиенте.
Данный код адаптирован под автомойку с тестовой БД SQLite, при желании можно прикрутить PosgreSQL.
В файле .env требуется прописать свой тг-токен, веб-сервер telegram-id админа. Запуск осуществляется через uvicorn командой uvicorn app.main:app --port 5050
