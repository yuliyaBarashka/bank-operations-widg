import json
from pathlib import Path
from src.utils import load_transactions

def test_load_transactions_valid(tmp_path: Path):
    # подготовить корректный файл
    data = [
        {"id": 1, "amount": 100.0, "date": "2024-01-01"},
        {"id": 2, "amount": -20.5, "date": "2024-01-02"}
    ]
    p = tmp_path / "transactions.json"
    p.write_text(json.dumps(data), encoding="utf-8")

    result = load_transactions(str(p))
    assert result == data

def test_load_transactions_empty_file(tmp_path: Path):
    p = tmp_path / "empty.json"
    p.write_text("", encoding="utf-8")

    result = load_transactions(str(p))
    assert result == []

def test_load_transactions_not_list(tmp_path: Path):
    data = {"not": "a list"}
    p = tmp_path / "not_list.json"
    p.write_text(json.dumps(data), encoding="utf-8")

    result = load_transactions(str(p))
    assert result == []

def test_load_transactions_invalid_json(tmp_path: Path):
    p = tmp_path / "invalid.json"
    p.write_text("{ this is not: valid json }", encoding="utf-8")

    result = load_transactions(str(p))
    assert result == []

def test_load_transactions_missing_file(tmp_path: Path):
    p = tmp_path / "missing.json"
    # файл не создаётся
    result = load_transactions(str(p))
    assert result == []