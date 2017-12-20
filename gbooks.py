import requests
from book import Book

class BookApi(object):
    def __init__(self):
        pass
    def getbyisbn(self,isbn):
        r = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:"+isbn)
        data = r.json()["items"][0]["volumeInfo"]
        book = Book(data["title"],data["authors"][0],data["industryIdentifiers"][1]["identifier"],data["categories"][0],data["imageLinks"]["thumbnail"])
        return book

