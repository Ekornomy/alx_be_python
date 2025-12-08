class Book:
    def __init__(self, title: str, author: str):
        """
        Base Class: Book
        Attributes: title (str) and author (str)
        """
        self.title = title
        self.author = author
    
    def __str__(self):
        """String representation of Book"""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """
        Derived Class: EBook
        Inherits from Book
        Additional attribute: file_size (int)
        """
        # Call the parent class __init__ method
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """String representation of EBook"""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """
        Derived Class: PrintBook
        Inherits from Book
        Additional attribute: page_count (int)
        """
        # Call the parent class __init__ method
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """String representation of PrintBook"""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """
        Composition: Library
        Attributes: books (a list to store instances of Book, EBook, and PrintBook)
        """
        self.books = []
    
    def add_book(self, book):
        """
        Method: add_book(self, book)
        Adds a Book, EBook, or PrintBook instance to the library
        """
        self.books.append(book)
    
    def list_books(self):
        """
        Method: list_books(self)
        Prints details of each book in the library
        """
        for book in self.books:
            print(book)