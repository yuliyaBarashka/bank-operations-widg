from typing import Dict, Iterator, List


def filter_by_currency(
    transactions: List[Dict],
    currency_code: str
) -> Iterator[Dict]:
    """
    Фильтрует транзакции по коду валюты.

    :param transactions: список транзакций
    :param currency_code: код валюты (например, USD)
    :return: итератор транзакций с указанной валютой
    """
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency_code:
                yield transaction
        except KeyError:
            continue


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генерирует описания транзакций.

    :param transactions: список транзакций
    :return: итератор строк с описанием операций
    """
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: начальное значение диапазона
    :param stop: конечное значение диапазона
    :return: итератор номеров карт
    """
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        yield (
            f"{card_number[0:4]} "
            f"{card_number[4:8]} "
            f"{card_number[8:12]} "
            f"{card_number[12:16]}"
        )