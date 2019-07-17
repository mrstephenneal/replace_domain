import os
import shutil
import unittest

from replace_domain import replace_domain


DOMAIN = 'validation.example.com'
CONF_FILE = os.path.join(os.path.dirname(__file__), 'data', 'default.conf')
CONF_FILE_REPLACED = os.path.join(os.path.dirname(__file__), 'data', 'default_replaced.conf')
PLACEHOLDER = '@VALIDATION_DOMAIN'


def tests_cleaner():
    """Remove test result files."""
    if os.path.exists(CONF_FILE_REPLACED):
        os.remove(CONF_FILE_REPLACED)


def test_reader():
    """Return the contents of the test result file."""
    with open(CONF_FILE_REPLACED, 'r') as conf:
        return conf.read()


class TestReplaceDomain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Delete result files
        tests_cleaner()

        # Copy test conf file
        shutil.copyfile(CONF_FILE, CONF_FILE_REPLACED)

    @classmethod
    def tearDownClass(cls):
        # Show contents of the domain replaced conf
        print(test_reader())

        # Delete result files
        tests_cleaner()

    def test_replace_domain(self):
        # Replace domain
        replace_domain(DOMAIN, CONF_FILE_REPLACED, PLACEHOLDER)

        # Assert file contains the correct strings
        self.assertIn(DOMAIN, test_reader())
        self.assertNotIn(PLACEHOLDER, test_reader())


if __name__ == '__main__':
    unittest.main()
