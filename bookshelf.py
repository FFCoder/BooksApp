from gbooks import BookApi

class Bookshelf(object):
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)
    def addbyisbn(self,isbn):
        book = BookApi().getbyisbn(isbn)
        self.books.append(book)
        return book

    def removeBook(self, book):
        pass

    def getAllBooks(self):
        pass

    def getBook(self):
        pass
