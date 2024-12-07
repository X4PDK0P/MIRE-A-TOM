# Структура проекта

Проект организован следующим образом:

```plaintext
project/
├── app/
│   ├── __init__.py
│   ├── main.py                # Точка входа в приложение
│   ├── config.py              # Настройки приложения
│   ├── api/                   # Основные маршруты API
│   │   ├── __init__.py
│   │   ├── routes/            # Роуты
│   │   │   ├── __init__.py
│   │   │   ├── formulas.py    # Роуты для работы с формулами
│   │   │   ├── analysis.py    # Роуты для анализа формул
│   ├── models/                # Модели данных (SQLAlchemy)
│   │   ├── __init__.py
│   │   ├── formula.py         # Модель для формулы
│   ├── schemas/               # Pydantic-схемы
│   │   ├── __init__.py
│   │   ├── formula.py         # Схемы для формулы
│   │   ├── analysis.py        # Схемы для анализа
│   ├── db/                    # Работа с базой данных
│   │   ├── __init__.py
│   │   ├── database.py        # Подключение к БД
│   │   ├── migrations/        # Миграции для Alembic
│   ├── services/              # Логика приложения
│   │   ├── __init__.py
│   │   ├── formula_service.py # Логика обработки формул
│   │   ├── analysis_service.py# Логика анализа формул
│   ├── utils/                 # Утилиты
│   │   ├── __init__.py
│   │   ├── helpers.py         # Вспомогательные функции
│   │   ├── latex_parser.py    # Конвертер LaTeX-формул
├── tests/                     # Тесты
│   ├── __init__.py
│   ├── test_routes.py         # Тесты для API
│   ├── test_services.py       # Тесты для сервисов
├── .env                       # Конфигурации среды (пароли, доступы)
├── Dockerfile                 # Docker-образ
├── docker-compose.yml         # Docker-оркестрация
├── alembic.ini                # Конфигурация для Alembic
├── requirements.txt           # Зависимости проекта
├── README.md                  # Описание проекта
