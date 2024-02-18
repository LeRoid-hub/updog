import os
Enviroment = os.getenv("ENVIROMENT")

class bcolors:
    """
    This class is used to color the messages in the console

    Example:
    ```
    print(f"{bcolors.OKBLUE} This is a blue message {bcolors.ENDC}")
    ```
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Logger:
    """
    This class is used to log the messages in the console
    """
    def __init__(self):
        """
        Constructor for the Logger class
        """
        self.Enviroment = os.getenv("ENVIROMENT")

    def dev_log(self, message):
        """
        Logs the message in the console with cyan color if the enviroment is dev or test

        Parameters:
        - message (str): The message to be logged
        """
        if self.Enviroment == "dev" or self.Enviroment == "test":
            print(f"{bcolors.OKCYAN} {message} {bcolors.ENDC}")

    def error_log(self, message):
        """
        Logs the message in the console with red color

        Parameters:
        - message (str): The message to be logged
        """
        print(f"{bcolors.FAIL} {message} {bcolors.ENDC}")

    def warning_log(self, message):
        """
        Logs the message in the console with yellow color

        Parameters:
        - message (str): The message to be logged
        """
        print(f"{bcolors.WARNING} {message} {bcolors.ENDC}")

    def info_log(self, message):
        """
        Logs the message in the console with blue color

        Parameters:
        - message (str): The message to be logged
        """
        print(f"{bcolors.OKBLUE} {message} {bcolors.ENDC}")
