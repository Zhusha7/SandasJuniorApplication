class Book:
    def __init__(self, title, author, publish_date):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.available = True

    def __str__(self):
        return f"{self.title} created by {self.author} at {self.publish_date} is {'available' if self.available else 'taken'}"

    def __repr__(self):
        return f"{self.title} {self.author} {self.publish_date}"

    def __eq__(self, other):
        return repr(self) == repr(other)


class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        elif isinstance(books, list) and all(isinstance(book, Book) for book in books):
            self.books = books
        else:
            raise TypeError("Books has to be a list of Book class")

    def add_book(self, *args):
        if len(args) == 1 and isinstance(args[0], Book):
            self.books.append(args[0])
        elif len(args) == 3:
            self.books.append(Book(args[0], args[1], args[2]))
        else:
            raise TypeError("Book has to be of Book class or provide title, author, publish_date")

    def search_book(self, search_string):
        seen = set()
        result = []
        for book in self.books:
            key = (book.title.lower(), book.author.lower(), book.publish_date)
            if (search_string.lower() in book.title.lower() or
                search_string.lower() in book.author.lower()) and key not in seen:
                result.append(book)
                seen.add(key)
        result.sort(key=lambda x: x.publish_date, reverse=True)
        return Library(result)

    def borrow_book(self, book):
        for lib_book in self.books:
            if lib_book == book and lib_book.available:
                lib_book.available = False
                return True
        return False

    def return_book(self, book):
        for lib_book in self.books:
            if lib_book == book and not lib_book.available:
                lib_book.available = True
                return True
        return False

    def __repr__(self):
        if not self.books:
            return "Empty"
        result = ""
        for index in range(len(self.books)):
            result += f"{index + 1}. {self.books[index]}\n"
        return result.strip()


class Menu:
    def __init__(self):
        self.menu_options = {
            1: "Add book",
            2: "Search books",
            3: "Display all books",
            4: "Borrow book",
            5: "Return book",
            6: "Exit"
        }

    def display_menu(self):
        print("\nLibrary Menu")
        print("=" * 30)
        for key, value in self.menu_options.items():
            print(f"{key}. {value}")

    def handle_menu_choice(self, lib):
        while True:
            self.display_menu()
            try:
                choice = int(input("\nEnter your choice (1-6): "))
                if choice == 1:
                    title = input("Enter book title: ")
                    author = input("Enter book author: ")
                    publish_date = input("Enter publish date: ")
                    lib.add_book(title, author, publish_date)
                    print("Book added successfully!")
                elif choice == 2:
                    search_term = input("Enter search term: ")
                    result = lib.search_book(search_term)
                    print("\nSearch Results:")
                    print(result)
                elif choice == 3:
                    print("\nLibrary Contents:")
                    print(lib)
                elif choice == 4:
                    print("\nLibrary Contents:")
                    print(lib)
                    book_index = int(input("Enter book number to borrow: ")) - 1
                    if 0 <= book_index < len(lib.books):
                        if lib.borrow_book(lib.books[book_index]):
                            print("Book borrowed successfully!")
                        else:
                            print("Book cannot be borrowed!")
                    else:
                        print("Invalid book number!")
                elif choice == 5:
                    print("\nLibrary Contents:")
                    print(lib)
                    book_index = int(input("Enter book number to return: ")) - 1
                    if 0 <= book_index < len(lib.books):
                        if lib.return_book(lib.books[book_index]):
                            print("Book returned successfully!")
                        else:
                            print("Book cannot be returned!")
                    else:
                        print("Invalid book number!")
                elif choice == 6:
                    print("Goodbye!")
                    return
                else:
                    print("Invalid choice. Please select 1-6.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except TypeError as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    library = Library()
    menu = Menu()
    menu.handle_menu_choice(library)
