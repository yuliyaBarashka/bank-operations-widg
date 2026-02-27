from pathlib import Path
import json
from typing import List, Dict, Any
from src.logger_config import setup_logger


logger = setup_logger(__name__)


def load_transactions(json_path: str) -> List[Dict[str, Any]]:
    logger.debug(f"Попытка загрузить транзакции из {json_path}")
    path = Path(json_path)
    if not path.exists():
        logger.error(f"Файл не найден: {json_path}")
        return []

    try:
        with path.open("r", encoding="utf-8") as f:
            content = f.read().strip()
        if not content:
            logger.warning(f"Файл пустой: {json_path}")
            return []
        data = json.loads(content)
        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            logger.debug(f"Успешно загружено {len(data)} транзакций")
            return data
        logger.error("Некорректный формат файла")
        return []
    except (IOError, OSError, json.JSONDecodeError) as e:
        logger.error(f"Ошибка при чтении файла: {e}")
        return []
