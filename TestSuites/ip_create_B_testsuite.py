import unittest

from testcases import set_window_size
from testcases import close_driver_spec
from testcases.IPCases import ip_login_newuser_testcase
from testcases.IPCases import ip_create_account_testcase

from testcases.IPCases import ip_create_new_password_testcase

from testcases.IPCases import ip_getting_to_know_you_testcase
from testcases.IPCases import ip_login_testcase
from testcases.IPCases import ip_getstarted_testcase
from testcases.IPCases import ip_summary_testcase
from testcases.IPCases import ip_investor_type_individual_testcase
from testcases.IPCases import ip_investor_registration_testcase
from testcases.IPCases import ip_employstatus_testcase
from testcases.IPCases import ip_investor_accredidation_testcase
from testcases.IPCases import ip_investor_suitability_testcase
from testcases.IPCases import ip_document_upload_testcase
from testcases.IPCases import ip_payment_type_testcase
from testcases.IPCases import ip_docusign_testcase
from testcases.IPCases import ip_investor_confirmation_testcase
from testcases.IPCases import ip_investor_congratulations_testcase

def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests([loader.loadTestsFromModule(set_window_size),
                    loader.loadTestsFromModule(ip_login_newuser_testcase),
                    loader.loadTestsFromModule(ip_create_account_testcase),

                    loader.loadTestsFromModule(ip_create_new_password_testcase),

                    loader.loadTestsFromModule(ip_getting_to_know_you_testcase),
                    loader.loadTestsFromModule(ip_login_testcase),
                    loader.loadTestsFromModule(ip_getstarted_testcase),
                    loader.loadTestsFromModule(ip_summary_testcase),
                    loader.loadTestsFromModule(ip_investor_type_individual_testcase),
                    loader.loadTestsFromModule(ip_investor_registration_testcase),
                    loader.loadTestsFromModule(ip_employstatus_testcase),
                    loader.loadTestsFromModule(ip_investor_accredidation_testcase),
                    loader.loadTestsFromModule(ip_investor_suitability_testcase),
                    loader.loadTestsFromModule(ip_document_upload_testcase),
                    loader.loadTestsFromModule(ip_payment_type_testcase),
                    loader.loadTestsFromModule(ip_docusign_testcase),
                    loader.loadTestsFromModule(ip_investor_confirmation_testcase),
                    loader.loadTestsFromModule(ip_investor_congratulations_testcase),
                    loader.loadTestsFromModule(close_driver_spec)
                    ])

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)


main()