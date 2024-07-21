class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
             print(f'Deleting ({self.title})')

    def __str__(self):
             print(f"({self.title}) by ({self.author}), published in ({self.year})")

    def __repr__(self):
             print(f"Book('{self.title}', '{self.author}', {self.year})")