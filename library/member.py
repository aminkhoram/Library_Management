class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name}, Borrowed books: {[book.title for book in self.borrowed_books]}"

    def borrow_book(self, book):
        if book.borrow_book():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False
