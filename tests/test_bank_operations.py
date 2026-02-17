import pytest
from unittest.mock import mock_open, patch
from src.bank_operations import load_json_file  # Замени your_module на название твоего файла

# 1. Тест корректного JSON с данными
def test_load_json_file_success():
    mock_data = '[{"name": "Alice", "balance": 100}, {"name": "Bob", "balance": 200}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_json_file("fake_file.json")
        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0]["name"] == "Alice"

# 2. Тест файла, который не существует
def test_load_json_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_json_file("missing_file.json")
        assert result == []

# 3. Тест некорректного JSON
def test_load_json_file_invalid_json():
    mock_data = '{"name": "Alice", "balance": 100'  # пропущена закрывающая скобка
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_json_file("invalid.json")
        assert result == []

# 4. Тест пустого файла
def test_load_json_file_empty():
    with patch("builtins.open", mock_open(read_data="")):
        result = load_json_file("empty.json")
        assert result == []

# 5. Тест, когда JSON не список (например, словарь)
def test_load_json_file_not_list():
    mock_data = '{"name": "Alice", "balance": 100}'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_json_file("dict.json")
        assert result == []