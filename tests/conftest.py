import pytest


@pytest.fixture
def card_number():
    return "1234567812345678"


@pytest.fixture
def account_number():
    return "40817810099910004312"


@pytest.fixture
def operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-10T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-03-01T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-12-31T09:00:00"},
    ]


@pytest.fixture
def transactions():
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "USD transaction",
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "RUB transaction",
        },
        {
            "id": 3,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Second USD transaction",
        },
    ]
