class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self._is_checked_out
    
    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"'{title}' has been checked out successfully."
                else:
                    return f"'{title}' is already checked out."
        return f"Book '{title}' not found in the library."
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"'{title}' has been returned successfully."
                else:
                    return f"'{title}' was not checked out."
        return f"Book '{title}' not found in the library."
    
    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(book)