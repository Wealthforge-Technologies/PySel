import unittest
import sys
import os
from testcases.bd import Login


def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(Login))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    driver().close()


main()
