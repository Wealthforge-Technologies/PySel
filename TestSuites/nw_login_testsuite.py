import unittest
from testcases import nw_login_testcase


def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(nw_login_testcase))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)


main()
