import unittest
from testcases import bd_admin_testcase
from testcases import bd_login_testcase


def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(bd_admin_testcase))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)

main()
