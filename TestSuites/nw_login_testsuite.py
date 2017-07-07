import unittest
from testcases.NWCases import nw_login_testcase
from testcases.BDCases import bd_login_testcase
from testcases import close_driver_spec
from testcases import set_window_size

def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests([loader.loadTestsFromModule(set_window_size),
        loader.loadTestsFromModule(bd_login_testcase),
        loader.loadTestsFromModule(nw_login_testcase),
        loader.loadTestsFromModule(close_driver_spec),
        ])

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)


main()