from src.processor import process_bank_operations, process_bank_search

data = [
    {"description": "Перевод на карту", "status": "EXECUTED"},
    {"description": "Открытие вклада", "status": "PENDING"},
    {"description": "Перевод организации", "status": "EXECUTED"},
    {"description": "Перевод со счета на счет", "status": "CANCELED"},
]


def test_process_bank_search():
    result = process_bank_search(data, "перевод")
    assert len(result) == 3
    result2 = process_bank_search(data, "вклад")
    assert len(result2) == 1


def test_process_bank_operations():
    categories = ["Перевод на карту", "Открытие вклада"]
    result = process_bank_operations(data, categories)
    assert result["Перевод на карту"] == 1
    assert result["Открытие вклада"] == 1
