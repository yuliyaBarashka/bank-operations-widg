from src.widget import mask_account_card, get_date


def test_mask_account_card_with_card():
    data = "Visa Classic 1234567812345678"
    expected = "Visa Classic 1234 56** **** 5678"
    assert mask_account_card(data) == expected


def test_mask_account_card_with_account():
    data = "Счет 40817810099910004312"
    expected = "Счет **4312"
    assert mask_account_card(data) == expected


def test_get_date():
    date_str = "2024-03-11T15:30:00"
    expected = "11.03.2024"
    assert get_date(date_str) == expected