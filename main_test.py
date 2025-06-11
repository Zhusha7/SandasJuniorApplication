import pytest
from main import *


def test_book_initialization():
    book = Book("Sample Title", "Sample Author", "2025-01-01")
    assert book.title == "Sample Title"
    assert book.author == "Sample Author"
    assert book.publish_date == "2025-01-01"
    assert book.available == True


def test_book_string_representation():
    book = Book("Sample Title", "Sample Author", "2025-01-01")
    assert str(book) == "Sample Title created by Sample Author at 2025-01-01 is available"


def test_book_equality():
    book1 = Book("Sample Title", "Sample Author", "2025-01-01")
    book2 = Book("Sample Title", "Sample Author", "2025-01-01")
    book3 = Book("Another Title", "Another Author", "2024-12-31")
    assert book1 == book2
    assert book1 != book3


def test_add_book_as_book():
    lib = Library(books=[])
    book = Book("Sample Title", "Sample Author", 1234)
    lib.add_book(book)
    assert lib.books == [book]


def test_add_book_with_details():
    lib = Library(books=[])
    lib.add_book("Sample Title", "Sample Author", 1234)
    assert lib.books[0] == Book("Sample Title", "Sample Author", 1234)


def test_search_book_existing():
    book1 = Book("First Title", "First Author", 1234)
    book2 = Book("Second Title", "Second Author", 5678)
    lib = Library(books=[book1, book2])
    search_result = lib.search_book("First")
    assert search_result.books == [book1]


def test_search_book_non_existing():
    book1 = Book("First Title", "First Author", 1234)
    book2 = Book("Second Title", "Second Author", 5678)
    lib = Library(books=[book1, book2])
    search_result = lib.search_book("Non-existent")
    assert search_result.books == []


def test_borrow_book():
    lib = Library()
    lib.add_book("Test Book", "Test Author", "2025")
    assert lib.borrow_book(0) == True
    assert lib.books[0].available == False
    assert lib.borrow_book(0) == False


def test_return_book():
    lib = Library()

    lib.add_book("Test Book", "Test Author", "2025")
    lib.borrow_book(0)
    assert lib.return_book(0) == True
    assert lib.books[0].available == True
    assert lib.return_book(0) == False


def test_library_representation_empty():
    lib = Library(books=[])
    assert repr(lib) == "Empty"


def test_library_representation_with_books():
    book1 = Book("First Title", "First Author", 1234)
    book2 = Book("Second Title", "Second Author", 5678)
    lib = Library(books=[book1, book2])
    expected_repr = ("1. First Title created by First Author at 1234 is available\n"
                     "2. Second Title created by Second Author at 5678 is available")
    assert repr(lib) == expected_repr


def test_initialization_with_invalid_books():
    with pytest.raises(TypeError, match="Books has to be a list of Book class"):
        Library(books="Invalid input")
