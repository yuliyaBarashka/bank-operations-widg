# Проект: Виджет банковских операций
## 📌 Описание проекта
Проект представляет собой набор функций для обработки и отображения банковских операций клиента.
Реализована логика маскировки номеров карт и счетов, фильтрации операций по статусу и сортировки по дате.
Проект покрыт автоматическими тестами с использованием pytest, используется Poetry для управления зависимостями.

## 🗂 Структура проекта
HOMEWORKE9_2/\
├── data/\
│   ├── operations.json\
│\
├── logs/\
│   ├── app.log\
│\
├── src/\
│   ├── masks.py          # Маскировка карт и счетов\
│   ├── bank_operations.py\
│   ├── decorators.py\
│   ├── external_api.py\
│   ├── generators.py\
│   ├── logger_config.py\
│   ├── readers.py\
│   ├── utils.py\
│   ├── processing.py    # Обработка операций\
│   └── widget.py        # Основная логика виджета\
│\
├── tests/\
│   ├── conftest.py       # Фикстуры pytest\
│   ├── test_mask.py\
│   ├── test_bank_operations.py\
│   ├── test_decorators.py\
│   ├── test_external_api.py\
│   ├── test_generators.py\
│   ├── test_processing.py\
│   ├── test_reders.py\
│   ├── test_utils.py\
│   └── test_widget.py\
│\
├── htmlcov/              # HTML-отчёт покрытия тестами\
│   └── index.html\
│\
├── pyproject.toml\
├── poetry.lock\
├── README.md\
└── requirements.txt\

## ⚙️ Установка и запуск
### 1️⃣ Клонирование репозитория
git clone <url_репозитория>
cd HOMEWORKE9_2
### 2️⃣ Установка зависимостей
poetry install

### 🧪 Тестирование
В проекте используются pytest, pytest-cov, параметризация и фикстуры.\
Запуск тестов\
poetry run pytest\
Проверка покрытия кода\
poetry run python -m pytest --cov=src --cov-report=html\
После выполнения команды будет создана папка htmlcov.\
Для просмотра отчёта открой файл:\
htmlcov/index.html\
Покрытие кода тестами — не менее 80%.\

## 🛠 Используемые технологии
Python 3.14\
Poetry\
Pytest\
Pytest-cov\

## ✅ Реализованный функционал
Маскировка номеров банковских карт\
Маскировка номеров счетов\
Определение типа данных (карта / счёт)\
Фильтрация операций по статусу\
Сортировка операций по дате\
Полное тестовое покрытие с параметризацией и фикстурами\
