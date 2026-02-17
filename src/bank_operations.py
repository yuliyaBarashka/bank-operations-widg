import json
from typing import List, Dict

def load_json_file(file_path: str) -> List[Dict]:
    """
    Открывает JSON-файл и возвращает список словарей.
    Обрабатывает случаи:
      - файл не найден
      - пустой файл
      - некорректный JSON
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                # Если в файле не список, возвращаем пустой список
                print("Файл не содержит список данных, возвращаем пустой список")
                return []
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
        return []
    except json.JSONDecodeError:
        print(f"Файл {file_path} содержит некорректный JSON")
        return []
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return []