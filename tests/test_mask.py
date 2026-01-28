from src.mask import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    card_number = "1234567812345678"
    expected = "1234 56** **** 5678"
    assert get_mask_card_number(card_number) == expected


def test_get_mask_account():
    account = "40817810099910004312"
    expected = "**4312"
    assert get_mask_account(account) == expected