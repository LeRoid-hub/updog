import ssl
import smtplib

class Email:
    port: int
    smt_server: str
    user: str
    password: str
    recipients: list

    def __init__(self, port: int, smt_server: str, user: str, password: str, recipients: list) -> None:
        """
        Constructor for the Email class

        Parameters:
        - port (int): The port of the email server
        - smt_server (str): The SMTP server
        - user (str): The user of the email server
        - password (str): The password of the email server
        - recipients (list): The list of recipients
        """
        self.port = port
        self.smt_server = smt_server
        self.user = user
        self.password = password
        self.recipients = recipients

    def addRecipient(self, recipient: str) -> None:
        """
        Adds a recipient to the list of recipients

        Parameters:
        - recipient (str): The recipient to be added
        """
        self.recipients.append(recipient)

    def removeRecipient(self, recipient: str) -> None:
        """
        Removes a recipient from the list of recipients

        Parameters:
        - recipient (str): The recipient to be removed
        """
        self.recipients.remove(recipient)

    def send(self, subject: str, message: str) -> None:
        """
        Sends an email to the list of recipients

        Parameters:
        - subject (str): The subject of the email
        - message (str): The message of the email
        """

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smt_server, self.port, context=context) as server:
            server.login(self.user, self.password)
            sender = self.user
            for recipient in self.recipients:
                server.sendmail(sender, recipient, f"Subject: {subject}\n\n{message}")
