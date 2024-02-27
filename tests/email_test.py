import unittest
from unittest.mock import patch, MagicMock
from updog import Email

class TestEmail(unittest.TestCase):

    def setUp(self) -> None:
        self.email = Email(587, "smtp.gmail.com", "user", "password", ["recipient1", "recipient2"])

    def test_addRecipient(self) -> None:
        self.email.addRecipient("recipient3")
        self.assertEqual(self.email.recipients, ["recipient1", "recipient2", "recipient3"])

    def test_removeRecipient(self) -> None:
        self.email.removeRecipient("recipient2")
        self.assertEqual(self.email.recipients, ["recipient1"])

    @patch('updog.notifier.email_mod.smtplib.SMTP_SSL')
    def test_send(self, mock_SMTP_SSL) -> None:
        mock_server = MagicMock()
        mock_SMTP_SSL.return_value = mock_server
        self.email.send("subject", "message")
        mock_server.login.assert_called_once_with("user", "password")
        print(f"Call count for sendmail: {mock_server.sendmail.call_count}")
        mock_server.sendmail.assert_called_once()
