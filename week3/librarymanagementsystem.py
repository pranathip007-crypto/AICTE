class Book:
    def __init__(self, book_id, title, author, copies=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = copies
        self.available_copies = copies

    def __str__(self):
        return (f"[{self.book_id}] {self.title} by {self.author} "
                f"(Available: {self.available_copies}/{self.total_copies})")


class Library:
    def __init__(self):
        self.books = {}          # book_id -> Book
        self.issued_to = {}      # book_id -> list of borrower names

    def add_book(self, book_id, title, author, copies=1):
        """Add a new book, or increase copies if it already exists."""
        if book_id in self.books:
            self.books[book_id].total_copies += copies
            self.books[book_id].available_copies += copies
            print(f"Added {copies} more copies of '{title}'.")
        else:
            self.books[book_id] = Book(book_id, title, author, copies)
            self.issued_to[book_id] = []
            print(f"Book '{title}' added to the library.")

    def remove_book(self, book_id):
        """Remove a book entirely from the library."""
        if book_id not in self.books:
            print("Book not found.")
            return
        book = self.books[book_id]
        if book.available_copies < book.total_copies:
            print("Cannot remove: some copies are still issued.")
            return
        del self.books[book_id]
        del self.issued_to[book_id]
        print(f"Book '{book.title}' removed from the library.")

    def issue_book(self, book_id, borrower_name):
        """Issue a book to a borrower."""
        if book_id not in self.books:
            print("Book not found.")
            return
        book = self.books[book_id]
        if book.available_copies <= 0:
            print(f"No available copies of '{book.title}' right now.")
            return
        book.available_copies -= 1
        self.issued_to[book_id].append(borrower_name)
        print(f"'{book.title}' issued to {borrower_name}.")

    def return_book(self, book_id, borrower_name):
        """Return a previously issued book."""
        if book_id not in self.books:
            print("Book not found.")
            return
        if borrower_name not in self.issued_to[book_id]:
            print(f"No record of '{borrower_name}' borrowing this book.")
            return
        self.issued_to[book_id].remove(borrower_name)
        self.books[book_id].available_copies += 1
        print(f"'{self.books[book_id].title}' returned by {borrower_name}.")

    def list_books(self):
        """Display all books in the library."""
        if not self.books:
            print("No books in the library.")
            return
        print("\n--- Library Catalog ---")
        for book in self.books.values():
            print(book)


def show_menu():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. List All Books")
    print("6. Exit")


def main():
    print("=== Library Management System ===")
    library = Library()

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            book_id = input("Enter book ID: ").strip()
            title = input("Enter title: ").strip()
            author = input("Enter author: ").strip()
            try:
                copies = int(input("Enter number of copies: ").strip())
            except ValueError:
                copies = 1
            library.add_book(book_id, title, author, copies)

        elif choice == "2":
            book_id = input("Enter book ID to remove: ").strip()
            library.remove_book(book_id)

        elif choice == "3":
            book_id = input("Enter book ID to issue: ").strip()
            borrower = input("Enter borrower name: ").strip()
            library.issue_book(book_id, borrower)

        elif choice == "4":
            book_id = input("Enter book ID to return: ").strip()
            borrower = input("Enter borrower name: ").strip()
            library.return_book(book_id, borrower)

        elif choice == "5":
            library.list_books()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 6.")


if __name__ == "__main__":
    main()