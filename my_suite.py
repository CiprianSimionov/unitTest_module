import unittest
import HtmlTestRunner

from elefant import TestElefant
from alerts import TestAlerts
from emag import TestEmag


class TestSuite(unittest.TestCase):
    def test_suite(self):
        running_tests = unittest.TestSuite()
        running_tests.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestElefant),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestEmag)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Unit Tests Results',
            report_name='unittests_report'
        )
        runner.run(running_tests)