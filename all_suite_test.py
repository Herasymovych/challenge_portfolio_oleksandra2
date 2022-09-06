import unittest

from unittest.loader import makeSuite

from test_cases.add_player_tests import AddPlayerTest
from test_cases.dashboard_page_test import DashboardTest
from test_cases.login_page_tests import LoginPageTest



def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(AddPlayerTest))
   test_suite.addTest(makeSuite(DashboardTest))
   test_suite.addTest(makeSuite(LoginPageTest))

   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())