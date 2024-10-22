import threading
import time
from typing import List

# примитив синхронизации
print_lock = threading.Lock()


def print_numbers() -> None:
    for i in range(1, 11):
        # Захват блокировки перед выводом
        with print_lock:
            print(i)
        time.sleep(1)


def create_threads(num_threads: int) -> None:
    threads: List[threading.Thread] = []

    for _ in range(num_threads):
        thread = threading.Thread(target=print_numbers)
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

# Основная программа
def main() -> None:
    create_threads(3)  # Создаем 3 потока

if __name__ == "__main__":
    main()
