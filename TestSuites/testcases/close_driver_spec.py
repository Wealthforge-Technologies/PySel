import unittest

from .testpages.testpageutilities import closeDriver

class CloseDriver(unittest.TestCase):


    def test_close(self):
        closeDriver()

# if __name__ == "__main__":
#     unittest.main()
