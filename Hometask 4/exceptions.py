# exceptions.py

class BookNotAvailable(Exception):
    """Исключение, если книга недоступна для заимствования."""
    def __init__(self, book_title: str):
        self.book_title = book_title
        super().__init__(f"Книга '{book_title}' недоступна для заимствования.")
