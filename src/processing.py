def filter_by_state(transactions, state='EXECUTED'):
    """
    Описание: принимает список словарей и необязательное значение для ключа state (по умолчанию 'EXECUTED').
    Возвращает новый список словарей с элементами, где словарь['state'] == state.
    """

    return [t for t in transactions if t.get('state') == state]

def sort_by_date(transactions, order='desc'):
    """
    Описание: принимает список словарей и необязательный параметр order
    (по умолчанию 'desc' для убывания)
    Сортирует по дате в поле 'date' и возвращает новый отсортированный список.
    """

    return sorted(transactions, key=key, reverse=reverse)


