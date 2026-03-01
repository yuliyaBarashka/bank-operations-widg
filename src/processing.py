from datetime import datetime
from typing import Dict, List


def filter_by_state(
    operations: List[Dict],
    state: str = "EXECUTED"
) -> List[Dict]:
    """
    Фильтрует список операций по значению ключа 'state'.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
    operations: List[Dict],
    reverse: bool = True
) -> List[Dict]:
    """
    Сортирует список операций по дате.
    По умолчанию — по убыванию (сначала новые).
    """
    return sorted(
        operations,
        key=lambda op: datetime.fromisoformat(op["date"]),
        reverse=reverse
    )
