import threading
from typing import Iterable


def calculate_squares(numbers: Iterable[int]) -> None:
    for number in numbers:
        print(f'Квадрат числа {number}: {number ** 2}')

def calculate_cubes(numbers: Iterable[int]) -> None:
    for number in numbers:
        print(f'Куб числа {number}: {number ** 3}')

def main() -> None:
    numbers: Iterable[int] = range(1, 11)  # Числа от 1 до 10

    thread1: threading.Thread = threading.Thread(target=calculate_squares, args=(numbers,))
    thread2: threading.Thread = threading.Thread(target=calculate_cubes, args=(numbers,))

    # Запускаем потоки
    thread1.start()
    thread2.start()

    # Ожидаем завершения потоков
    thread1.join()
    thread2.join()

    print("Вычисления завершены.")

if __name__ == "__main__":
    main()
