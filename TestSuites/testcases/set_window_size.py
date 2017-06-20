import unittest

from .testpages.testpageutilities import setWindowSize


class WindowSize(unittest.TestCase):

    def test_set_default_window_size(self):
        setWindowSize()

if __name__ == "__main__":
    unittest.main()
