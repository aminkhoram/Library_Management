from library.book import Book
from library.member import Member
from library.library import Library

def main():
    # Initialize the library
    lib = Library()

    # Add books to the library
    book1 = Book("1984", "George Orwell", 3)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 2)
    lib.add_book(book1)
    lib.add_book(book2)

    # Add members to the library
    member1 = Member("Alice")
    member2 = Member("Bob")
    lib.add_member(member1)
    lib.add_member(member2)

    # Borrow and return books
    print(f"Initial state:\n{book1}\n{book2}\n")

    print("Alice borrows '1984'")
    member1.borrow_book(book1)
    print(f"After borrowing:\n{book1}\n{book2}\n")

    print("Alice returns '1984'")
    member1.return_book(book1)
    print(f"After returning:\n{book1}\n{book2}\n")

if __name__ == "__main__":
    main()
