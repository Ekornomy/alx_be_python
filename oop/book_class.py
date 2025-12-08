class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Constructor (__init__): Initializes a Book instance with title, author, and year.
        
        Parameters:
        title (str): The title of the book
        author (str): The author of the book
        year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor (__del__): Called when the object is about to be destroyed.
        Prints "Deleting (title of the book)" upon object deletion.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self) -> str:
        """
        String Representation (__str__): Returns a user-friendly string representation.
        Format: "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self) -> str:
        """
        Official Representation (__repr__): Returns a string that would recreate the Book instance.
        Format: f"Book('{self.title}', '{self.author}', {self.year})"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"