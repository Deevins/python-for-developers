def divide_numbers(first_num: float, second_num: float) -> float:
    try:
        result = first_num / second_num

        return result

    # Обработка исключения деления на ноль
    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно.")


# P. S - я уже реализовал проверку кривого ввода в прошлой задаче - поэтому просто копирую.
def main() -> None:
    try:
        num1 = input("Введите первое число: ")
        # Проверка, если введенное значение не число
        if not num1.replace('.', '', 1).isdigit():
            raise ValueError("Ошибка: введено не число.")

        num1 = float(num1)

        num2 = input("Введите второе число: ")
        # Проверка, если введенное значение не число
        if not num2.replace('.', '', 1).isdigit():
            raise ValueError("Ошибка: введено не число.")
        num2 = float(num2)

        print(f"Результат деления {num1} на {num2}: {divide_numbers(num1, num2)}")

    except ValueError as ve:
        print(ve)


if __name__ == "__main__":
    main()
