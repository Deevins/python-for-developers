from typing import List


# Функция для подсчета количества слов в файле
def count_words_in_file(file_name: str) -> int:
    total_words: int = 0

    try:
        # Открытие файла для чтения
        with open(file_name, 'r', encoding='utf-8') as file:
            # Чтение всех строк из файла
            for line_number, line in enumerate(file, start=1):
                # Удаление лишних пробелов и разделение строки на слова
                words: List[str] = line.strip().split()

                # Подсчет слов в строке
                line_word_count: int = len(words)

                # Добавление количества слов в общую сумму
                total_words += line_word_count

        return total_words

    except FileNotFoundError:
        raise FileNotFoundError(f"Ошибка: Файл '{file_name}' не найден.")

    except PermissionError:
        raise PermissionError(f"Ошибка: Нет доступа к файлу '{file_name}'.")

    except IOError as io_error:
        raise IOError(f"Ошибка ввода-вывода: {io_error}")


# Основная программа
def main() -> None:
    # Путь к файлу с текстом
    file_path: str = 'text_file.txt'

    try:
        # Подсчитываем количество слов в файле
        word_count: int = count_words_in_file(file_path)

        # Выводим результат на экран
        print(f"Количество слов в файле: {word_count}")

    except Exception as general_exception:
        print(f"Произошла ошибка: {general_exception}")


if __name__ == "__main__":
    main()
