from typing import List


# Функция для подсчета общей стоимости заказа
def calculate_total_cost(file_path: str) -> float:
    total_cost: float = 0.0

    try:
        # Открываем файл для чтения
        with open(file_path, 'r', encoding='utf-8') as file:
            # Проход по строкам файла
            for line in file:
                # Разделяем строку на части (название товара, количество, цена)
                parts: List[str] = line.strip().split('\t')

                # Проверяем, что в строке 3 элемента
                if len(parts) != 3:
                    raise ValueError(f"Ошибка: Неверный формат строки: '{line.strip()}'")

                # Извлекаем данные и конвертируем их в нужные типы
                item_name: str = parts[0]
                quantity: int = int(parts[1])
                price: float = float(parts[2])

                # Добавляем стоимость данного товара к общей стоимости
                total_cost += quantity * price

        return total_cost

    # Обработка ошибки, если файл не найден
    except FileNotFoundError:
        raise FileNotFoundError(f"Ошибка: Файл '{file_path}' не найден.")

    # Обработка ошибки при неверном формате данных в файле
    except ValueError as ve:
        raise ValueError(f"Ошибка данных в файле: {ve}")

    # Обработка ошибок доступа или других проблем с файлами
    except PermissionError:
        raise PermissionError(f"Ошибка: Нет доступа к файлу '{file_path}'.")


# Основная программа
def main() -> None:
    # Путь к файлу с ценами
    file_path: str = 'prices.txt'

    try:
        # Подсчитываем общую стоимость заказа
        total_cost: float = calculate_total_cost(file_path)

        # Выводим общую стоимость
        print(f"Общая стоимость заказа: {total_cost:.2f} рублей")

    # Обработка ошибок
    except FileNotFoundError as fnf_error:
        print(fnf_error)

    except ValueError as value_error:
        print(value_error)

    except PermissionError as permission_error:
        print(permission_error)


if __name__ == "__main__":
    main()
