import unittest

from testcases import set_window_size
from testcases import close_driver_spec
from testcases.IPCases import ip_login_testcase
from testcases.IPCases import ip_getstarted_testcase
from testcases.IPCases import ip_investmin_notmet_testcase

def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests([loader.loadTestsFromModule(set_window_size),
                    loader.loadTestsFromModule(ip_login_testcase),
                    loader.loadTestsFromModule(ip_getstarted_testcase),
                    loader.loadTestsFromModule(ip_investmin_notmet_testcase),
                    loader.loadTestsFromModule(close_driver_spec)
                    ])

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)


main()
