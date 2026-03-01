import pytest

from src.mask import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1111222233334444", "1111 22** **** 4444"),
    ]
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account, expected",
    [
        ("40817810099910004312", "**4312"),
        ("1234567890123456", "**3456"),
    ]
)
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected
