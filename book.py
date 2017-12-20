class Book(object):
    def __init__(self,title,author,isbn=None,genre=None,coverimage=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.coverimage = coverimage

    def set_isbn(self,isbn):
        """Setter Method for isbn
        TODO: Add Logic to check isbn
        """
        self.isbn = isbn

    def __str__(self):
        return self.title
