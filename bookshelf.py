class Bookshelf(object):
    def __init__(self):
        pass

    def addBook(self, book):
        pass
    def addbyisbn(self,isbn):
        pass

    def removeBook(self, book):
        pass

    def getAllBooks(self):
        pass

    def getBook(self):
        pass

class Book(object):
    def __init__(self,title,author,isbn=None,genre=None,coverimage=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.coverimage = coverimage

    def setisbn(self,isbn):
        """Setter Method for isbn
        TODO: Add Logic to check isbn
        """
        self.isbn = isbn

