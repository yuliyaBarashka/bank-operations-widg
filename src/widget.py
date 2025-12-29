from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в строке.
    """
    parts = data.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if "Счет" in data:
        masked = get_mask_account(number)
    else:
        masked = get_mask_card_number(number)

    return f"{name} {masked}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из ISO-формата в ДД.ММ.ГГГГ
    """
    date = datetime.fromisoformat(date_str)
    return date.strftime("%d.%m.%Y")