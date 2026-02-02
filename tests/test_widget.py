import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Visa Classic 1234567812345678", "Visa Classic 1234 56 **** 5678"),
        ("Счет 40817810099910004312", "Счет **4312"),
    ]
)
def test_mask_account_card(data, expected):
    assert mask_account_card(data) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T15:30:00", "11.03.2024"),
        ("2023-01-01T00:00:00", "01.01.2023"),
    ]
)
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected