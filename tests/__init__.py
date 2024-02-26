# __init__.py
import unittest

# Import your test modules
from .server_test import TestServer

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestServer))
    # Add more test modules as needed
    return test_suite

# python3 -m unittest discover -p '*_test.py' tests
