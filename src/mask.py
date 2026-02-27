import logging

logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: str) -> str:
    logger.info("Начало маскирования номера карты")

    if len(card_number) < 16:
        logger.error("Некорректная длина номера карты")
        raise ValueError("Неверный номер карты")

    masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info("Номер карты успешно замаскирован")

    return masked


def get_mask_account(account: str) -> str:
    logger.info("Начало маскирования счета")

    if len(account) < 4:
        logger.error("Некорректный номер счета")
        raise ValueError("Неверный номер счета")

    masked = f"**{account[-4:]}"
    logger.info("Счет успешно замаскирован")

    return masked