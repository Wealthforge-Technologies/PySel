import unittest
from testcases import bd_admin_createbank_testcase


def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(bd_admin_createbank_testcase))

    suite.addTests([loader.loadTestsFromModule(bd_login_testcase),
     loader.loadTestsFromModule(bd_admin_testcase),
     loader.loadTestsFromModule(bd_admin_createbank_testcase),
     loader.loadTestsFromModule(close_driver_spec),
     ])

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)

main()