from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default():
    operations = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
    ]

    result = filter_by_state(operations)

    assert result == [
        {"id": 1, "state": "EXECUTED"},
        {"id": 3, "state": "EXECUTED"},
    ]


def test_filter_by_state_custom():
    operations = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]

    result = filter_by_state(operations, state="CANCELED")

    assert result == [
        {"id": 2, "state": "CANCELED"},
    ]


def test_sort_by_date_descending():
    operations = [
        {"id": 1, "date": "2024-01-10T10:00:00"},
        {"id": 2, "date": "2024-03-01T12:00:00"},
        {"id": 3, "date": "2023-12-31T09:00:00"},
    ]

    result = sort_by_date(operations)

    assert [op["id"] for op in result] == [2, 1, 3]


def test_sort_by_date_ascending():
    operations = [
        {"id": 1, "date": "2024-01-10T10:00:00"},
        {"id": 2, "date": "2024-03-01T12:00:00"},
        {"id": 3, "date": "2023-12-31T09:00:00"},
    ]

    result = sort_by_date(operations, reverse=False)

    assert [op["id"] for op in result] == [3, 1, 2]
