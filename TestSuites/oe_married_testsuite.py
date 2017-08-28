import unittest

from testcases import set_window_size
from testcases import close_driver_spec
from testcases.IPCases import oe_login_testcase
from testcases.IPCases import oe_choose_account_testcase
from testcases.IPCases import oe_investment_married_testcase
from testcases.IPCases import oe_investor_married_testcase
from testcases.IPCases import oe_suitability_individual_testcase
from testcases.IPCases import ip_employstatus_testcase

def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests([loader.loadTestsFromModule(set_window_size),
                    loader.loadTestsFromModule(oe_login_testcase),
                    loader.loadTestsFromModule(oe_choose_account_testcase),
                    loader.loadTestsFromModule(oe_investment_married_testcase),
                    loader.loadTestsFromModule(oe_investor_married_testcase),
                    loader.loadTestsFromModule(oe_suitability_individual_testcase),
                    loader.loadTestsFromModule(ip_employstatus_testcase),
                    loader.loadTestsFromModule(close_driver_spec)
                    ])

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)


main()
