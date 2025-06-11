class Book:
    def __init__(self, title, author, publish_date):
        self.title = title
        self.author = author
        self.publish_date = publish_date

    def __str__(self):
        return f"{self.title} created by {self.author} at {self.publish_date}"

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
        result = []
        for book in self.books:
            if search_string.lower() in repr(book).lower():
                result.append(book)
        return Library(result)

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
            4: "Exit"
        }


    def display_menu(self):
        print("\nLibrary Menu")
        print("=" * 30)
        for key, value in self.menu_options.items():
            print(f"{key}. {value}")


    def handle_menu_choice(self, library):
        while True:
            self.display_menu()
            try:
                choice = int(input("\nEnter your choice (1-4): "))
                if choice == 1:
                    title = input("Enter book title: ")
                    author = input("Enter book author: ")
                    publish_date = input("Enter publish date: ")
                    library.add_book(title, author, publish_date)
                    print("Book added successfully!")
                elif choice == 2:
                    search_term = input("Enter search term: ")
                    result = library.search_book(search_term)
                    print("\nSearch Results:")
                    print(result)
                elif choice == 3:
                    print("\nLibrary Contents:")
                    print(library)
                elif choice == 4:
                    print("Goodbye!")
                    return
                else:
                    print("Invalid choice. Please select 1-4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except TypeError as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    library = Library()
    menu = Menu()
    menu.handle_menu_choice(library)
