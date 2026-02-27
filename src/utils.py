import json
from typing import List, Dict, Any
from pathlib import Path

def load_transactions(json_path: str) -> List[Dict[str, Any]]:
    """
    Загружает транзакции из файла JSON.

    Пояснения:
    - Ожидается, что файл содержит список словарей (массив транзакций).
    - Если файл пустой, содержит не список, не найден или некорректен - возвращает []
    - Путь может быть любым путём к файлу.

    Возвращаемое:
    - список словарей (каждый элемент - транзакция). Если формат другой - пустой список.
    """
    path = Path(json_path)

    # Файл не существует
    if not path.exists():
        return []

    try:
        # Открываем файл и загружаем JSON
        with path.open("r", encoding="utf-8") as f:
            content = f.read().strip()

        # Пустой файл
        if not content:
            return []

        data = json.loads(content)

        # Ожидаем список словарей
        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            return data

        # Неподходящий формат
        return []

    except (IOError, OSError, json.JSONDecodeError):
        # Любая проблема при чтении/разборе
        return []