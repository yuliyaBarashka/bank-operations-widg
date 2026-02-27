from typing import cast, List, Dict, Any
import pandas as pd
import logging

logger = logging.getLogger(__name__)


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    logger.info(f"Чтение CSV-файла: {file_path}")
    try:
        df = pd.read_csv(file_path)
        transactions = cast(List[Dict[str, Any]], df.to_dict(orient="records"))
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV: {e}")
        return []


def read_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    logger.info(f"Чтение Excel-файла: {file_path}")
    try:
        df = pd.read_excel(file_path)
        transactions = cast(List[Dict[str, Any]], df.to_dict(orient="records"))
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel: {e}")
        return []
