# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
from dotenv import load_dotenv
import requests
import src.logger_config

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной GITHUB_TOKEN из .env-файла
github_token = os.getenv('GITHUB_TOKEN')

# Создание заголовка с токеном доступа API
headers = {
    'Authorization': f'token {github_token}'
}

# Отправка GET-запроса к API
response = requests.get('https://api.github.com/user', headers=headers)

# Обработка ответа
print(response.json())
