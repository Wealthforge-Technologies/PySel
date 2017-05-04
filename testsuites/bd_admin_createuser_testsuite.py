import unittest
import sys
import os
sys.path.append(os.path.abspath('../TestCases/BD'))
import Login
import BDAdmin
from __init__ import driver


def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(Login))
    suite.addTests(loader.loadTestsFromModule(BDAdmin))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    driver().close()

main()
