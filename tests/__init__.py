# __init__.py
import unittest

# Import your test modules
from .server_test import TestServer
from .httpgetbuilder_test import TestHTTPGetBuilder
from .postgresqlbuilder_test import TestPostgreSQLBuilder
from .discord_test import TestDiscord
from .telegram_test import TestTelegram
from .email_test import TestEmail
from .logger_test import TestLogger
from .notify_test import TestNotify
from .updog_test import TestUpdog

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestServer))
    test_suite.addTest(unittest.makeSuite(TestHTTPGetBuilder))
    test_suite.addTest(unittest.makeSuite(TestPostgreSQLBuilder))
    test_suite.addTest(unittest.makeSuite(TestDiscord))
    test_suite.addTest(unittest.makeSuite(TestTelegram))
    test_suite.addTest(unittest.makeSuite(TestEmail))
    test_suite.addTest(unittest.makeSuite(TestLogger))
    test_suite.addTest(unittest.makeSuite(TestNotify))
    test_suite.addTest(unittest.makeSuite(TestUpdog))
    # Add more test modules as needed
    return test_suite

# python3 -m unittest discover -p '*_test.py' tests
