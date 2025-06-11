import pytest
from main import *

def test_book_initialization():
    book = Book("Sample Title", "Sample Author", "2025-01-01")
    assert book.title == "Sample Title"
    assert book.author == "Sample Author"
    assert book.publish_date == "2025-01-01"


def test_book_string_representation():
    book = Book("Sample Title", "Sample Author", "2025-01-01")
    assert str(book) == "Sample Title created by Sample Author at 2025-01-01"


def test_book_equality():
    book1 = Book("Sample Title", "Sample Author", "2025-01-01")
    book2 = Book("Sample Title", "Sample Author", "2025-01-01")
    book3 = Book("Another Title", "Another Author", "2024-12-31")
    assert book1 == book2
    assert book1 != book3


def test_add_book_as_book():
    library = Library(books=[])
    book = Book("Sample Title", "Sample Author", 1234)
    library.add_book(book)
    assert library.books == [book]


def test_add_book_with_details():
    library = Library(books=[])
    library.add_book("Sample Title", "Sample Author", 1234)
    assert library.books[0] == Book("Sample Title", "Sample Author", 1234)


def test_search_book_existing():
    book1 = Book("First Title", "First Author", 1234)
    book2 = Book("Second Title", "Second Author", 5678)
    library = Library(books=[book1, book2])
    search_result = library.search_book("First")
    assert search_result.books == [book1]


def test_search_book_non_existing():
    book1 = Book("First Title", "First Author", 1234)
    book2 = Book("Second Title", "Second Author", 5678)
    library = Library(books=[book1, book2])
    search_result = library.search_book("Non-existent")
    assert search_result.books == []


def test_library_representation_empty():
    library = Library(books=[])
    assert repr(library) == "Empty"


def test_library_representation_with_books():
    book1 = Book("First Title", "First Author", 1234)
    book2 = Book("Second Title", "Second Author", 5678)
    library = Library(books=[book1, book2])
    expected_repr = "1. First Title created by First Author at 1234\n2. Second Title created by Second Author at 5678"
    assert repr(library) == expected_repr


def test_initialization_with_invalid_books():
    with pytest.raises(TypeError, match="Books has to be a list of Book class"):
        Library(books="Invalid input")
