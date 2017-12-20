import requests

class BookApi(object):
    def __init__(self):
        pass
    def getbyisbn(self,isbn):
        r = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:"+isbn)
        print(r.json)

b = BookApi()
b.getbyisbn("9780786229277")