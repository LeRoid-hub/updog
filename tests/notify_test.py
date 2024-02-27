import unittest
from unittest.mock import patch, MagicMock
from updog import Notify, Email

class TestNotify(unittest.TestCase):
    def setUp(self) -> None:
        mail = Email(587, "smtp.gmail.com", "user", "password", ["recipient1", "recipient2"])

    def test_init(self):
        n = Notify(self.mail)
