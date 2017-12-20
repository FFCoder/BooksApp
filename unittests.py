import unittest
from bookshelf import Bookshelf
import re


class addBook(unittest.TestCase):
    def testAddByUPC(self):
        """Tests to ensure that a proper book is added by UPC.
         In the case of this test, it ensures that 
         'Harry Potter and the Goblet of Fire' is added
         """
        sampleUPC = "9780786229277"
        shelf = Bookshelf()
        book = shelf.addbyisbn(sampleUPC)
        self.assertEquals(re.search("goblet of fire",book.title,re.IGNORECASE),True)
    
if __name__ == "__main__":
    unittest.main()