import unittest
import sys
import os
sys.path.append(os.path.abspath('../TestCases'))
import QALogin

def main():
  loader = unittest.TestLoader()
  suite  = unittest.TestSuite()

  suite.addTests(loader.loadTestsFromModule(QALogin))

  runner = unittest.TextTestRunner(verbosity=3)
  result = runner.run(suite)



main()
