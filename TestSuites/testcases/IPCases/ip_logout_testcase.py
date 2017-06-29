import unittest

from ..testpages.IPPages.ipgeneralpage import IPGeneral
from ..testcaseutilities.testinfo import TestInfo


class TestLogout(unittest.TestCase):
    def setUp(self):
        self.lookup = TestInfo()
        self.lookup.load_defaults()

    def test_login(self):
        IPGeneral().logout()


if __name__ == "__main__":
    unittest.main()
