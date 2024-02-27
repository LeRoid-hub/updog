# __init__.py
import unittest

# Import your test modules
from .server_test import TestServer
from .httpgetbuilder_test import TestHTTPGetBuilder
from .postgresqlbuilder_test import TestPostgreSQLBuilder

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestServer))
    test_suite.addTest(unittest.makeSuite(TestHTTPGetBuilder))
    test_suite.addTest(unittest.makeSuite(TestPostgreSQLBuilder))
    # Add more test modules as needed
    return test_suite

# python3 -m unittest discover -p '*_test.py' tests
