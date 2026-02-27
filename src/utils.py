import json
import logging
from typing import List, Dict, Any
from pathlib import Path

logger = logging.getLogger(__name__)


def load_transactions(json_path: str) -> List[Dict[str, Any]]:
    logger.info(f"Попытка загрузки файла: {json_path}")

    path = Path(json_path)

    if not path.exists():
        logger.error("Файл не найден")
        return []

    try:
        with path.open("r", encoding="utf-8") as f:
            content = f.read().strip()

        if not content:
            logger.warning("Файл пустой")
            return []

        data = json.loads(content)

        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            logger.info("Файл успешно загружен")
            return data

        logger.warning("Неверный формат данных")
        return []

    except (IOError, OSError):
        logger.error("Ошибка чтения файла")
        return []

    except json.JSONDecodeError:
        logger.error("Ошибка декодирования JSON")
        return []