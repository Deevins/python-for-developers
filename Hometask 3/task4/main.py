import multiprocessing
from multiprocessing import Lock
from typing import List


def factorial(n: int, lock: Lock) -> None:
    result = 1

    for i in range(2, n + 1):
        result *= i

    with lock:  # Синхронизация вывода результатов
        print(f"Факториал числа {n} равен {result}")


def main() -> None:
    numbers: List[int] = list(range(1, 200))
    lock = Lock()  # Примитив синхронизации

    processes: List[multiprocessing.Process] = []

    # Создание и запуск процессов
    for number in numbers:
        process = multiprocessing.Process(target=factorial, args=(number, lock))
        processes.append(process)
        process.start()

    # Ожидание завершения всех процессов
    for process in processes:
        process.join()


if __name__ == "__main__":
    main()
