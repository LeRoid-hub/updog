import unittest
from unittest.mock import patch, MagicMock
from updog import Telegram

class TestTelegram(unittest.TestCase):
    def test_init(self):
        self.assertRaises(AssertionError, Telegram.__init__)
