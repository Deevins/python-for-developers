import logging
from exceptions import BookNotAvailable
from models import Book, Library


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_operation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"Операция {func.__name__} выполнена с аргументами {args[1:]} и результатом: {result}")
        return result
    return wrapper



# Основная программа
def main() -> None:
    # инстанс библиотеки
    library = Library()


    first_book = Book(title="Python 101", author="Michael Driscoll", year=2020, categories=["Programming", "Python"])
    library.add_book(first_book)
    print(first_book)

    try:
        print(library.is_book_borrowed("Python 101"))

    except BookNotAvailable as e:
        print(e)


if __name__ == "__main__":
    main()
