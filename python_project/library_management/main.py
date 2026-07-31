from book import Book
from library import Library

library = Library()

while True:
    print("\n========== Library ==========")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Display All Books")
    print("7. Exit")
    print("=============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Title : ")
        author = input("Author : ")
        isbn = input("ISBN : ")

        new_book = Book(title, author, isbn)
        library.add_book(new_book)

    elif choice == "2":
        isbn = input("Enter ISBN: ")
        library.remove_book(isbn)

    elif choice == "3":
        isbn = input("Enter ISBN: ")
        book = library.search_book(isbn)

        if book:
            print("\nBook Found")
            book.display_info()
        else:
            print("Book not found.\n")

    elif choice == "4":
        isbn = input("Enter ISBN: ")
        library.issue_book(isbn)

    elif choice == "5":
        isbn = input("Enter ISBN: ")
        library.return_book(isbn)

    elif choice == "6":
        library.display_books()

    elif choice == "7":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice.")