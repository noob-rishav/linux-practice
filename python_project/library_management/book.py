class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def display_info(self):
        print(f"Title  : {self.title}")
        print(f"Author : {self.author}")
        print(f"ISBN   : {self.isbn}")

        if self.available:
            print("Status : Available")
        else:
            print("Status : Issued")

        print("-" * 30)
