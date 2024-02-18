from urllib.request import urlopen, Request

class HTTPGetBuilder:
    """
    HTTPGetBuilder class to build a HTTP GET request

    Attributes:
    - url (str): The URL of the request
    - headers (dict) - optinal: The headers of the request
    - payload (str) - optinal: The payload of the request
    - onlystatus (bool) - optinal: If only the status code should be returned
    """
    url: str
    headers: dict
    payload: str
    onlystatus: bool = False

    def __init__(self, *args, **kwargs):
        """
        Constructor for the HTTPGetBuilder class

        Parameters:
        - url (str): The URL of the request
        - headers (dict) - optinal: The headers of the request
        - payload (str) - optinal: The payload of the request
        - onlystatus (bool) - optinal: If only the status code should be returned

        Returns:
        - HTTPGetBuilder: The HTTPGetBuilder object
        - ValueError: If the URL is not provided

        Example:
        ```
        builder = HTTPGetBuilder(url="http://www.google.com", onlystatus=True)
        ```
        """

        self.url = kwargs.get("url")
        if not self.url:
            raise ValueError("URL is required")
        self.headers = kwargs.get("headers")
        self.payload = kwargs.get("payload")
        self.onlystatus = kwargs.get("onlystatus")

    def set_url(self, url: str) -> None:
        """
        Sets the URL of the request

        Parameters:
        - url (str): The URL of the request
        """
        self.url = url

    def set_headers(self, headers: str) -> None:
        """
        Sets the headers of the request

        Parameters:
        - headers (dict): The headers of the request
        """
        self.headers = headers

    def set_payload(self, payload: str) -> None:
        """
        Sets the payload of the request

        Parameters:
        - payload (str): The payload of the request
        """
        self.payload = payload

    def set_onlystatus(self, onlystatus: bool) -> None:
        """
        Sets if only the status code should be returned

        Parameters:
        - onlystatus (bool): If only the status code should be returned
        """
        self.onlystatus = onlystatus

    def buildRequest(self) -> Request:
        """
        Builds the request object

        Returns:
        - Request: The request object
        """
        req = Request(self.url)
        if self.headers:
            req.add_header(self.headers)
        if self.payload:
            req.add_data(self.payload)
        return req


    def execute(self):
        """
        Executes the request

        Returns:
        - str: The response of the request
        - Exception: If the request fails

        Example:
        ```
        builder = HTTPGetBuilder(url="http://www.google.com", onlystatus=True)
        print(builder.execute())
        ```
        """
        try:
            response = urlopen(self.buildRequest())
            if self.onlystatus:
                return response.status
            return response.read()
        except Exception as e:
            return e

    def to_dict(self):
        """
        Serializes the HTTPGetBuilder object into a dictionary

        Returns:
        - dict: The serialized HTTPGetBuilder object
        """
        return {"url": self.url, "headers": self.headers, "payload": self.payload}

    def serialize(self):
        """
        Serializes the HTTPGetBuilder object into a dictionary

        Returns:
        - dict: The serialized HTTPGetBuilder object
        """
        return {
            "url": self.url,
            "headers": self.headers,
            "payload": self.payload,
            "onlystatus": self.onlystatus
        }

