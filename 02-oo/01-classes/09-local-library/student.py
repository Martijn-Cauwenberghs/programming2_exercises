class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for lib_book in self.books:
            if book.title == lib_book.title and book.author == lib_book.author:
                self.books.remove(lib_book)

    def search_books(self, search_string: str):
        results = []
        for search_book in self.books:
            if (search_string.lower() in search_book.title.lower() or search_string.lower() in search_book.author.lower()):
                results.append(search_book)
        return results
