import unittest

from .testpages.testpageutilities import setWindowSize
from .testcaseutilities.testinfo import TestInfo

class WindowSize(unittest.TestCase):

    def test_set_default_window_size(self):
        setWindowSize()

        # this needs to only be called once!!
        TestInfo().load_defaults()


if __name__ == "__main__":
    unittest.main()
