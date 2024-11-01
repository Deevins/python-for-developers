# models.py
from typing import List, Optional

from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from exceptions import BookNotAvailable


class Book(BaseModel):
    uuid: UUID = Field(default_factory=uuid4)
    title: str
    author: str
    year: int
    is_available: bool = True
    categories: List[str] = Field(...)



class User(BaseModel):
    name: str
    email: str
    membership_id: int


class Library(BaseModel):
    books: List[Book] = []
    users: List[User] = []
    borrowed_books: List[Book] = []
    available_books: List[Book] = []

    def total_books(self) -> int:
        return len(self.books)

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        self.available_books.append(book)

    def find_book(self, book_uuid: Optional[UUID] = None, title: Optional[str] = None, author: Optional[str] = None) ->  List[Book]:
        """
        Ищет книги по UUID, названию или автору.
        :param book_uuid: UUID книги (если требуется поиск по уникальному идентификатору).
        :param title: Название книги или его часть (опционально).
        :param author: Имя автора или его часть (опционально).
        :return: Список найденных книг или одна книга, если указан UUID.
        """
        if book_uuid:
            # Поиск книги по уникальному идентификатору
            for book in (self.available_books + self.borrowed_books):
                if book.uuid == book_uuid:
                    return [book]
            return []

        # Фильтрация по названию и автору
        found_books = [
            book for book in (self.available_books + self.borrowed_books)
            if (title is None or title.lower() in book.title.lower()) and
               (author is None or author.lower() in book.author.lower())
        ]

        return found_books

    def is_book_borrowed(self, book_uuid: UUID) -> bool:
        """
        Проверяет, занята ли книга по её UUID.
        :param book_uuid: UUID книги.
        :return: True, если книга занята, иначе False.
        """
        found_books = self.find_book(book_uuid=book_uuid)
        if not found_books:
            raise ValueError(f"Книга с UUID '{book_uuid}' не найдена в библиотеке.")

        book = found_books[0]
        if not book.is_available:
            raise BookNotAvailable(f"Книга с UUID '{book_uuid}' уже занята.")

        return not book.is_available

    def borrow_book(self, book_uuid: UUID) -> Book:
        """
        Позволяет пользователю взять книгу из библиотеки по UUID.
        :param book_uuid: UUID книги, которую хочет взять пользователь.
        :return: Книга, если она успешно заимствована.
        """
        for book in self.available_books:
            if book.uuid == book_uuid and book.is_available:
                book.is_available = False
                self.available_books.remove(book)
                self.borrowed_books.append(book)
                return book
        raise BookNotAvailable(f"Книга с UUID {book_uuid} недоступна для заимствования.")

    def return_book(self, book_uuid: UUID) -> None:
        """Возвращает книгу в библиотеку по UUID, делая её доступной."""
        for book in self.borrowed_books:
            if book.uuid == book_uuid:
                book.is_available = True
                self.borrowed_books.remove(book)
                self.available_books.append(book)
                return

        raise ValueError(f"Книга с UUID {book_uuid} не найдена в списке занятых.")
