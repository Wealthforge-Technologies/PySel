import unittest
from testcases import nw_login_testcase
from testcases import bd_login_testcase
from testcases import close_driver_spec


def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(nw_login_testcase))

    suite.addTests([loader.loadTestsFromModule(bd_login_testcase),
     loader.loadTestsFromModule(nw_login_testcase),
     loader.loadTestsFromModule(close_driver_spec),
     ])

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)


main()
