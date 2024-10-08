from typing import List


# Функция для получения элемента списка по индексу с обработкой исключений
def get_element_at_index(lst: List[int], index: int) -> int:
    try:
        # Попытка вернуть элемент по индексу
        return lst[index]
    except IndexError:
        # Обработка ошибки выхода индекса за пределы списка
        raise IndexError(f"Ошибка: индекс {index} выходит за пределы списка.")


# Основная программа
def main() -> None:
    # Пример списка чисел
    elements: List[int] = [10, 20, 30, 40, 50]

    try:
        # Запрос индекса у пользователя
        user_input: str = input("Введите индекс элемента списка: ")

        # Проверка ввода пользователя
        if not user_input.isdigit():
            raise ValueError("Ошибка: введено не число.")

        # Преобразование строки в целое число
        index: int = int(user_input)

        # Получение элемента по индексу
        element: int = get_element_at_index(elements, index)

        # Вывод результата
        print(f"Значение элемента с индексом {index}: {element}")

    # Обработка ошибок, если индекс выходит за пределы списка
    except IndexError as e:
        print(e)

    # Обработка ошибок некорректного ввода
    except ValueError as ve:
        print(ve)
