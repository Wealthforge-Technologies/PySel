import unittest
from testcases import bd_login_testcase
from testcases import close_driver_spec
from testcases import bd_bank_testcase
from testcases import bd_bank_createbank_testcase


def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests([loader.loadTestsFromModule(bd_login_testcase),
     loader.loadTestsFromModule(bd_bank_testcase),
     loader.loadTestsFromModule(bd_bank_createbank_testcase),
     loader.loadTestsFromModule(close_driver_spec),
     ])

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)

main()
