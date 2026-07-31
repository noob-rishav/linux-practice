from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.\n")

    def display_books(self):
        if not self.books:
            print("Library is empty.\n")
            return

        for book in self.books:
            book.display_info()

    def search_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def remove_book(self, isbn):
        book = self.search_book(isbn)

        if book:
            self.books.remove(book)
            print("Book removed successfully.\n")
        else:
            print("Book not found.\n")

    def issue_book(self, isbn):
        book = self.search_book(isbn)

        if book:
            if book.available:
                book.available = False
                print("Book issued successfully.\n")
            else:
                print("Book is already issued.\n")
        else:
            print("Book not found.\n")

    def return_book(self, isbn):
        book = self.search_book(isbn)

        if book:
            if not book.available:
                book.available = True
                print("Book returned successfully.\n")
            else:
                print("Book was already available.\n")
        else:
            print("Book not found.\n")



