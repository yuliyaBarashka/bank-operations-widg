import os
from typing import Any, Dict

import requests


def convert_to_rubles(transaction: Dict[str, Any]) -> float:
    """
    Возвращает сумму транзакции в рублях (float).

    Если валюта RUB — возвращает amount как есть.
    Если валюта USD или EUR — конвертирует в RUB через внешний API.
    """
    amount_str = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    amount = float(amount_str)

    if currency == "RUB":
        return amount

    if currency not in ("USD", "EUR"):
        # если попалась другая валюта — можно вернуть как есть
        # или выбросить ошибку (но обычно в задании просто не встречается)
        return amount

    api_key = os.getenv("APILAYER_API_KEY")
    if not api_key:
        raise ValueError("APILAYER_API_KEY not found in environment variables")

    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {
        "to": "RUB",
        "from": currency,
        "amount": amount,
    }
    headers = {"apikey": api_key}

    response = requests.get(url, params=params, headers=headers, timeout=10)
    response.raise_for_status()

    data = response.json()

    # apilayer обычно возвращает результат в ключе result
    return float(data["result"])
