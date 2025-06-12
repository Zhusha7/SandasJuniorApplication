import pytest
from main import *


def test_book_initialization():
    book = Book("test", "test", "2025-01-01")
    assert book.title == "test"
    assert book.author == "test"
    assert book.publish_date == "2025-01-01"
    assert book.available == True


def test_book_string_representation():
    book = Book("test", "test", "2025-01-01")
    assert str(book) == "test created by test at 2025-01-01 is available"


def test_book_equality():
    book1 = Book("test", "test", "2025-01-01")
    book2 = Book("test", "test", "2025-01-01")
    book3 = Book("nope", "nope", "2024-12-31")
    assert book1 == book2
    assert book1 != book3


def test_add_book_as_book():
    lib = Library(books=[])
    book = Book("test1", "test2", 1234)
    lib.add_book(book)
    assert lib.books == [book]


def test_add_book_with_details():
    lib = Library(books=[])
    lib.add_book("test1", "test2", 1234)
    assert lib.books[0] == Book("test1", "test2", 1234)


def test_search_book_existing():
    book1 = Book("First T", "First A", 1234)
    book2 = Book("Second T", "Second A", 5678)
    lib = Library(books=[book1, book2])
    search_result = lib.search_book("First")
    assert search_result.books == [book1]


def test_search_book_non_existing():
    book1 = Book("First T", "First A", 1234)
    book2 = Book("Second T", "Second A", 5678)
    lib = Library(books=[book1, book2])
    search_result = lib.search_book("Non-existent")
    assert search_result.books == []

def test_search_book_date_sorting():
    books = [
        Book("Python 3", "Third A", "2020-06-11"),
        Book("python 1", "First A", "2025-06-12"),
        Book("Python 2", "Second A", "2025-06-11")
    ]
    lib = Library(books)
    result = lib.search_book("python")
    assert len(result.books) == 3
    assert result.books[0].publish_date == "2025-06-12"
    assert result.books[1].publish_date == "2025-06-11"
    assert result.books[2].publish_date == "2020-06-11"


def test_borrow_book():
    lib = Library()
    lib.add_book("test1", "test2", "2025")
    assert lib.borrow_book(Book("test1", "test2", "2025")) == True
    assert lib.books[0].available == False
    assert lib.borrow_book(Book("test1", "test2", "2025")) == False


def test_return_book():
    lib = Library()
    lib.add_book("test1", "test2", "2025")
    lib.borrow_book(Book("test1", "test2", "2025"))
    assert lib.return_book(Book("test1", "test2", "2025")) == True
    assert lib.books[0].available == True
    assert lib.return_book(Book("test1", "test2", "2025")) == False


def test_library_representation_empty():
    lib = Library(books=[])
    assert repr(lib) == "Empty"


def test_library_representation_with_books():
    book1 = Book("First T", "First A", 1234)
    book2 = Book("Second T", "Second A", 5678)
    lib = Library(books=[book1, book2])
    expected_repr = ("1. First T created by First A at 1234 is available\n"
                     "2. Second T created by Second A at 5678 is available")
    assert repr(lib) == expected_repr


def test_initialization_with_invalid_books():
    with pytest.raises(TypeError, match="Books has to be a list of Book class"):
        Library(books="Invalid input")
