import unittest
from unittest.mock import patch, MagicMock
from updog import Discord

class TestDiscord(unittest.TestCase):
    def test_init(self):
        self.assertRaises(AssertionError, Discord.__init__)
