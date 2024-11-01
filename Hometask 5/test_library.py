import unittest
from models import Book, Library, BookNotAvailable
from uuid import uuid4

class TestLibraryMethods(unittest.TestCase):
    def setUp(self):
        """Настройка библиотеки и добавление книг перед каждым тестом."""
        self.library = Library()
        self.book1 = Book(title="Python 101", author="Michael Driscoll", year=2020, categories=["Programming", "Python"])
        self.book2 = Book(title="Python 201", author="Michael Driscoll", year=2021, categories=["Programming", "Advanced Python"])
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_and_find_book(self):
        """Тест добавления и поиска книги по UUID."""
        found_books = self.library.find_book(book_uuid=self.book1.uuid)
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0].title, "Python 101")

    def test_borrow_book(self):
        """Тест взятия книги и проверки её статуса."""
        borrowed_book = self.library.borrow_book(self.book1.uuid)
        print("rofl")
        self.assertFalse(borrowed_book.is_available)
        self.assertIn(borrowed_book, self.library.borrowed_books)
        self.assertNotIn(borrowed_book, self.library.available_books)

    def test_return_book(self):
        """Тест возврата книги и восстановления её доступности."""
        self.library.borrow_book(self.book1.uuid)
        self.library.return_book(self.book1.uuid)
        self.assertTrue(self.book1.isAvailable)
        self.assertIn(self.book1, self.library.available_books)
        self.assertNotIn(self.book1, self.library.borrowed_books)

    def test_is_book_borrowed(self):
        """Тест проверки занятости книги."""
        self.library.borrow_book(self.book1.uuid)
        with self.assertRaises(BookNotAvailable):
            self.library.is_book_borrowed(self.book1.uuid)

    def test_borrow_unavailable_book(self):
        """Тест попытки взять уже занятую книгу."""
        self.library.borrow_book(self.book1.uuid)
        with self.assertRaises(BookNotAvailable):
            self.library.borrow_book(self.book1.uuid)

    def test_book_not_found(self):
        """Тест исключения, если книга с данным UUID не найдена."""
        non_existing_id = uuid4()
        with self.assertRaises(ValueError):
            self.library.is_book_borrowed(non_existing_id)

if __name__ == "__main__":
    unittest.main()
