from typing import List


# Создание пользовательских классов исключений
class EvenNumberError(Exception):
    """Исключение вызывается, если в списке найдено четное число."""

    def __init__(self, number: int):
        self.number = number
        super().__init__(f"Найдено четное число: {number}")


class NegativeNumberError(Exception):
    """Исключение вызывается, если в списке найдено отрицательное число."""

    def __init__(self, number: int):
        self.number = number
        super().__init__(f"Найдено отрицательное число: {number}")


# Функция для вычисления суммы списка с обработкой исключений
def sum_of_list(num_list: List[int]) -> int:
    total_sum: int = 0

    # Проход по каждому элементу списка
    for num in num_list:
        # Проверка на отрицательное число
        if num < 0:
            raise NegativeNumberError(num)

        # Проверка на четное число
        if num % 2 == 0:
            raise EvenNumberError(num)

        # Суммирование чисел, если не было исключений
        total_sum += num

    return total_sum


# Основная программа
def main() -> None:
    input_numbers:List[int] = list(map(int, input("Введите список чисел через пробел:").split()))

    try:
        # Попытка вычислить сумму списка
        result: int = sum_of_list(input_numbers)
        print(f"Сумма списка: {result}")

    # Обработка исключений для четного числа
    except EvenNumberError as e:
        print(e)

    # Обработка исключений для отрицательного числа
    except NegativeNumberError as e:
        print(e)
