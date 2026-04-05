from typing import Any, Dict, List

"""Функция filter_by_state, которая принимает список словарей и
опционально значение для ключа state (по умолчанию 'EXECUTED').
Функция возвращает новый список словарей, содержащий только те словари,
у которых ключ state соответствует указанному значению."""


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:

    # Проверка на некорректность типа введенных данных
    if not isinstance(data, list):
        raise TypeError("Тип вводимых данных должен быть 'списком' или 'словарем'")

    if not isinstance(state, str):
        raise TypeError("Тип аргумента 'State' должен быть строкой")

    return [item for item in data if item.get("state") == state]


"""Функция sort_by_date, которая принимает список словарей и необязательный
параметр, задающий порядок сортировки (по умолчанию — убывание).
Функция должна возвращать новый список, отсортированный по дате (date)."""


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    # Проверка на некорректность типа введенных данных
    if not isinstance(data, list):
        raise TypeError("Тип вводимых данных должен быть 'списком' или 'словарем'")
    # Проверка на отсутствие данных, для ускорения отработки кода
    if not data:
        return []

    # Проверяем что все словари имеют ключ date
    for item in data:
        if "date" not in item:
            raise KeyError("Все словари должны содержать ключ 'date'")

        # Сортируем по дате
    return sorted(data, key=lambda x: x["date"], reverse=descending)
