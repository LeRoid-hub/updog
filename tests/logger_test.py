import unittest
from unittest.mock import patch, MagicMock
from updog import Logger
from updog.logger import bcolors
import os

class TestLogger(unittest.TestCase):


    def setUp(self) -> None:
        os.environ["ENVIROMENT"] = ""
        self.log = Logger()

    def test_dev_log_with_no_env(self):
        with patch('builtins.print') as mock_print:
            self.log.dev_log("Your expected output")
            mock_print.assert_not_called()

    def test_dev_log_with_dev(self):
        os.environ["ENVIROMENT"] = "dev"
        self.log = Logger()
        with patch('builtins.print') as mock_print:
            self.log.dev_log("Your expected output")
            mock_print.assert_called_once_with(f"{bcolors.OKCYAN} {'Your expected output'} {bcolors.ENDC}")

    def test_dev_log_with_test(self):
        os.environ["ENVIROMENT"] = "test"
        self.log = Logger()
        with patch('builtins.print') as mock_print:
            self.log.dev_log("Your expected output")
            mock_print.assert_called_once_with(f"{bcolors.OKCYAN} {'Your expected output'} {bcolors.ENDC}")

    def test_dev_log_with_prod(self):
        os.environ["ENVIROMENT"] = "prod"
        self.log = Logger()
        with patch('builtins.print') as mock_print:
            self.log.dev_log("Your expected output")
            mock_print.assert_not_called()

    def test_error_log(self):
        with patch('builtins.print') as mock_print:
            self.log.error_log("Your expected output")
            mock_print.assert_called_once_with(f"{bcolors.FAIL} {'Your expected output'} {bcolors.ENDC}")

    def test_info_log(self):
        with patch('builtins.print') as mock_print:
            self.log.info_log("Your expected output")
            mock_print.assert_called_once_with(f"{bcolors.OKBLUE} {'Your expected output'} {bcolors.ENDC}")

    def test_warning_log(self):
        with patch('builtins.print') as mock_print:
            self.log.warning_log("Your expected output")
            mock_print.assert_called_once_with(f"{bcolors.WARNING} {'Your expected output'} {bcolors.ENDC}")
