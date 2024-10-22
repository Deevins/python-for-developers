import asyncio
from typing import List

async def compute_square(number: int) -> int:
    """Асинхронно вычисляет квадрат числа с задержкой в 1 секунду."""
    await asyncio.sleep(1)
    return number * number

async def process_numbers(numbers: List[int]) -> List[int]:
    """Асинхронно обрабатывает список чисел, вычисляя их квадраты."""
    tasks = [compute_square(num) for num in numbers]
    results = await asyncio.gather(*tasks)  # Ожидаем завершения всех задач
    return results


async def main() -> None:
    """Основная функция для запуска асинхронной обработки."""
    numbers = [1, 2, 3, 4, 5]  # Пример списка чисел
    squares = await process_numbers(numbers)
    print(f"Квадраты чисел: {squares}")

if __name__ == "__main__":
    asyncio.run(main())
