import math
from typing import Union


def get_square_root(value: Union[int, float]) -> Union[float, str]:
    # Возвращает квадратный корень числа, если оно неотрицательное.
    # В случае отрицательного числа возвращает сообщение об ошибке.
    try:
        if value < 0:
            raise ValueError("Квадратный корень не определен для отрицательных чисел.")
        return math.sqrt(value)
    except ValueError as e:
        return str(e)


def main() -> None:
    # Основная функция, запрашивающая ввод пользователя и выводящая результат.
    try:
        user_input: str = input("Введите число для вычисления квадратного корня: ")
        number: float = float(user_input)
        result: Union[float, str] = get_square_root(number)
        print(result)
    except ValueError:
        print("Ошибка: введено некорректное число.")
    except ImportError:
        print("Ошибка: не удалось импортировать модуль math.")


if __name__ == "__main__":
    main()
