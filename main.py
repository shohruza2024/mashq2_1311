class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__available = True

    def borrow(self):
        if self.__available:
            self.__available = False
            print(f"'{self.title}' kitobi olindi.")
        else:
            print(f"'{self.title}' hozir mavjud emas.")

    def return_book(self):
        self.__available = True
        print(f"'{self.title}' qaytarildi.")

    def is_available(self):
        return self.__available


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            holat = "mavjud" if book.is_available() else "olingan"
            print(f"{book.title} - {book.author} ({holat})")


class User:
    def __init__(self, name):
        self.name = name

    def borrow_book(self, library, book):
        if book in library.books:
            book.borrow()
        else:
            print("Bunday kitob kutubxonada yo‘q.")

    def return_book(self, library, book):
        if book in library.books:
            book.return_book()
        else:
            print("Bu kitob bu kutubxonaga tegishli emas.")

lib = Library()
b1 = Book("Python Asoslari", "Nozila N.")
b2 = Book("Flask Dasturlash", "Ozodbek O.")

lib.add_book(b1)
lib.add_book(b2)

user = User("Ali")

lib.list_books()
user.borrow_book(lib, b1)
lib.list_books()

user.return_book(lib, b1)
lib.list_books()
