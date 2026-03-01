from src.readers import (
    read_transactions_from_csv,
    read_transactions_from_excel,
)
from src.utils import load_transactions
from src.processor import process_bank_search
from src.logger_config import setup_logger


setup_logger(__name__)


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        data = load_transactions("data/operations.json")
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        data = read_transactions_from_csv("data/operations.csv")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        data = read_transactions_from_excel("data/operations.xlsx")
    else:
        print("Некорректный выбор")
        return

    statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        status = input(
            f"Введите статус, по которому необходимо выполнить фильтрацию.\n"
            f"Доступные статусы: {', '.join(statuses)}\n"
            "Пользователь: "
        ).upper()

        if status in statuses:
            data = [
                op for op in data
                if op.get("state", "").upper() == status
            ]
            print(f'Операции отфильтрованы по статусу "{status}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    sort_input = input(
        "Отсортировать операции по дате? Да/Нет\nПользователь: "
    ).lower()

    if sort_input == "да":
        asc_input = input(
            "Отсортировать по возрастанию или по убыванию?\nПользователь: "
        ).lower()

        reverse = asc_input == "по убыванию"
        data.sort(key=lambda x: x.get("date", ""), reverse=reverse)

    currency_input = input(
        "Выводить только рублевые транзакции? Да/Нет\nПользователь: "
    ).lower()

    if currency_input == "да":
        data = [
            op for op in data
            if op.get("operationAmount", {})
            .get("currency", {})
            .get("code") == "RUB"
        ]

    search_input = input(
        "Отфильтровать список транзакций по определенному слову "
        "в описании? Да/Нет\nПользователь: "
    ).lower()

    if search_input == "да":
        word = input("Введите слово для поиска: ")
        data = process_bank_search(data, word)

    if not data:
        print(
            "Не найдено ни одной транзакции, "
            "подходящей под ваши условия фильтрации"
        )
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(data)}")

    for op in data:
        print(op)

if __name__ == "__main__":
    main()
