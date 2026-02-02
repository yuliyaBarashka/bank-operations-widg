import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize(
    "currency, expected_count",
    [
        ("USD", 2),
        ("RUB", 1),
        ("EUR", 0),
    ],
)
def test_filter_by_currency(transactions, currency, expected_count):
    result = list(filter_by_currency(transactions, currency))
    assert len(result) == expected_count


def test_filter_by_currency_empty_list():
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == [
        "USD transaction",
        "RUB transaction",
        "Second USD transaction",
    ]


def test_transaction_descriptions_empty():
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 3, [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
        ]),
        (9999_9999_9999_9998, 9999_9999_9999_9999, [
            "9999 9999 9999 9998",
            "9999 9999 9999 9999",
        ]),
    ],
)
def test_card_number_generator(start, stop, expected):
    assert list(card_number_generator(start, stop)) == expected
