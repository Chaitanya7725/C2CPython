class Library:
    def __init__(self):
        self.books = []
        self.borrowed = []
    def add_book(self, book):
        self.books.append(book)
    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            self.borrowed.append(book)
        else:
            print("This Book not available.")
    def return_book(self, book):
        if book in self.borrowed:
            self.borrowed.remove(book)
            self.books.append(book)
    def display_books(self):
        print("Available books:", self.books)
library = Library()
while True:
    print("Menu:")
    print("1. Add book")
    print("2. Borrow book")
    print("3. Return book")
    print("4. View available books")
    print("5. Exit")
    choice = input("Enter choice: ")

if choice == '1':
        booktitle = input("Enter book to add: ")
        library.add_book(booktitle)
elif choice == '2':
    booktitle = input("Enter book to borrow: ")
    library.borrow_book(booktitle)
elif choice == '3':
    booktitle = input("Enter book to return: ")
    library.return_book(booktitle)
elif choice == '4':
    library.display_books()
elif choice == '5':
    break
else:
    print("Invalid choice.")