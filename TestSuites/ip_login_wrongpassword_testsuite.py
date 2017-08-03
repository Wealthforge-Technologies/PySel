import unittest

from testcases import set_window_size
from testcases import close_driver_spec
from testcases.IPCases import ip_login_wrongpassword_testcase


def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests([loader.loadTestsFromModule(set_window_size),
                    loader.loadTestsFromModule(ip_login_wrongpassword_testcase)
                    ])

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)


main()
