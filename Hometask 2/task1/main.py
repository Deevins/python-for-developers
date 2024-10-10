# Функция для копирования содержимого файла
def copy_file(source_path: str, destination_path: str) -> None:
    try:
        # Открытие исходного файла для чтения
        with open(source_path, 'r', encoding='utf-8') as source_file:
            # Чтение содержимого исходного файла
            content: str = source_file.read()

        # Открытие файла назначения для записи
        with open(destination_path, 'w', encoding='utf-8') as destination_file:
            # Запись содержимого в файл назначения
            destination_file.write(content)

        print(f"Файл '{source_path}' успешно скопирован в '{destination_path}'.")

    # Обработка исключения, если файл не найден
    except FileNotFoundError:
        print(f"Ошибка: Файл '{source_path}' не найден.")

    # Обработка ошибок доступа или других проблем с файлами
    except PermissionError:
        print(f"Ошибка: Нет доступа к файлу '{source_path}' или '{destination_path}'.")

    except IOError as e:
        print(f"Ошибка ввода-вывода: {e}")


# Основная программа
def main() -> None:
    # Пути к исходному файлу и файлу назначения
    source_file_path: str = 'source.txt'
    destination_file_path: str = 'destination.txt'

    # Вызов функции для копирования файла
    copy_file(source_file_path, destination_file_path)


if __name__ == "__main__":
    main()
