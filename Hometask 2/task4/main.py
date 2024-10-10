from typing import Set


# Функция для чтения уникальных строк из файла
def read_unique_lines(input_file: str) -> Set[str]:
    unique_strings: Set[str] = set()

    try:
        # Открытие файла для чтения
        with open(input_file, 'r', encoding='utf-8') as file:
            # Чтение всех строк и добавление их в множество (уникальные значения)
            for line in file:
                unique_strings.add(line.strip())  # Удаление пробелов в начале и конце строки

        return unique_strings

    except FileNotFoundError:
        raise FileNotFoundError(f"Ошибка: Файл '{input_file}' не найден.")

    except PermissionError:
        raise PermissionError(f"Ошибка: Нет доступа к файлу '{input_file}'.")

    except IOError as io_error:
        raise IOError(f"Ошибка ввода-вывода: {io_error}")


# Функция для записи уникальных строк в файл
def write_unique_lines(output_file_path: str, unique_strings: Set[str]) -> None:
    try:
        # Открытие файла для записи
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for line in unique_strings:
                file.write(line + '\n')  # Запись каждой уникальной строки с новой строки

    except PermissionError:
        logging.critical(f"Нет доступа для записи в файл '{output_file_path}'.")
        raise PermissionError(f"Ошибка: Нет доступа для записи в файл '{output_file_path}'.")

    except IOError as io_error:
        logging.critical(f"Ошибка ввода-вывода при записи: {io_error}")
        raise IOError(f"Ошибка ввода-вывода при записи: {io_error}")


# Основная программа
def main() -> None:
    input_file: str = 'input.txt'
    output_file: str = 'unique_output.txt'

    try:
        # Чтение уникальных строк из входного файла
        unique_lines_set: Set[str] = read_unique_lines(input_file)

        # Запись уникальных строк в выходной файл
        write_unique_lines(output_file, unique_lines_set)

        # Сообщение об успешной записи
        print(f"Уникальные строки успешно записаны в файл '{output_file}'.")

    except Exception as general_exception:
        print(f"Произошла ошибка: {general_exception}")


if __name__ == "__main__":
    main()
