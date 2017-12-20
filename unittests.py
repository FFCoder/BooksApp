import unittest

class addBook(unittest.TestCase):
    def testAddByUPC(self):
        """Tests to ensure that a proper book is added by UPC.
         In the case of this test, it ensures that 
         'Harry Potter and the Goblet of Fire' is added
         """
         shelf = BookShelf()