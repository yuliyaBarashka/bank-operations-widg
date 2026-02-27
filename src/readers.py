import pandas as pd
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из CSV-файла.

    :param file_path: путь к CSV-файлу
    :return: список словарей с транзакциями
    """
    logger.info(f"Чтение CSV-файла: {file_path}")

    try:
        df = pd.read_csv(file_path)
        transactions = df.to_dict(orient="records")
        logger.info("CSV успешно загружен")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV: {e}")
        return []


def read_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из Excel-файла.

    :param file_path: путь к XLSX-файлу
    :return: список словарей с транзакциями
    """
    logger.info(f"Чтение Excel-файла: {file_path}")

    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient="records")
        logger.info("Excel успешно загружен")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel: {e}")
        return []
