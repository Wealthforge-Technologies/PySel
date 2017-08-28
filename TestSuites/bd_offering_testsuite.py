import unittest

from testcases import close_driver_spec
from testcases import set_window_size
from testcases.BDCases import bd_login_testcase
from testcases.BDCases import bd_offering_testcase
from testcases.BDCases import bd_offering_createoffering

def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests([loader.loadTestsFromModule(set_window_size),
                    loader.loadTestsFromModule(bd_login_testcase),
                    # loader.loadTestsFromModule(bd_offering_testcase), #opening another window?!?!
                    loader.loadTestsFromModule(bd_offering_createoffering),
                    loader.loadTestsFromModule(bd_offering_createoffering),
                    loader.loadTestsFromModule(close_driver_spec),
                    ])

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)

main()
