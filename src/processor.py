import logging
import re
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """
    Фильтрует транзакции, у которых в description есть search.
    Используется re для поиска, регистр игнорируется.
    """
    logger.info(f"Фильтрация по слову: {search}")
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    filtered = [item for item in data if 'description' in item and pattern.search(item['description'])]
    logger.info(f"Найдено {len(filtered)} подходящих операций")
    return filtered


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчёт операций по категориям.
    """
    logger.info("Подсчёт операций по категориям")
    result = {category: 0 for category in categories}
    for item in data:
        desc = item.get('description', '')
        for category in categories:
            if desc.lower() == category.lower():
                result[category] += 1
    return result
