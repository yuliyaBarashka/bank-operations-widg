from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования работы функции.

    :param filename: имя файла для логов (если None — вывод в консоль)
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as error:  # noqa: BLE001
                message = (
                    f"{func.__name__} error: {error}. "
                    f"Inputs: {args}, {kwargs}"
                )
                _write_log(message, filename)
                raise
            _write_log(message, filename)
            return result

        return wrapper

    return decorator


def _write_log(message: str, filename: Optional[str]) -> None:
    """
    Записывает лог в файл или выводит в консоль.

    :param message: сообщение для логирования
    :param filename: имя файла или None
    """
    if filename:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(message + "\n")
    else:
        print(message)
