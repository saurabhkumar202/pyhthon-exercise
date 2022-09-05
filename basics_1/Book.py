from dataclasses import dataclass
from Animal import Animal


@dataclass
class Book:
    def __init__(self, name, price, page, author):
        self.name = "swati"
        self.price = price
        self.page = page
        self.author = author

    def __str__(self):
        return f"{self.name} of author {self.author} having {self.page} is priced at {self.price}"


class Author:
    def __init__(self, author_name, author_age):
        self.author_name = author_name
        self.author_age = author_age

    def __str__(self):
        return f"{self.author_name} and {self.author_age}"


author = Author("Saurabh", 32)
book = Book(None, 500.75, 150, author)
print(book)

a = Animal("PET", True, False)
print(a)
