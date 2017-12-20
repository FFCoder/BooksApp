from gbooks import BookApi

class Bookshelf(object):
    def __init__(self):
        self.books = []

    def addBook(self, book):
        pass
    def addbyisbn(self,isbn):
        self.books.append(BookApi().getbyisbn(isbn))

    def removeBook(self, book):
        pass

    def getAllBooks(self):
        pass

    def getBook(self):
        pass