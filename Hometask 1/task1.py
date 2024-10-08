# Функция для выполнения деления с обработкой исключений
def divide_numbers(num1:float, num2:float) -> float:
    try:
        result = num1 / num2


        return result
    # Обработка исключения деления на ноль
    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно.")


if __name__ == "__main__":
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
