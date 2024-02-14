from urllib.request import urlopen, Request

class HTTPGetBuilder:
    url: str
    headers: dict
    payload: str
    onlystatus: bool = False

    def __init__(self, *args, **kwargs):
        self.url = kwargs.get("url")
        self.headers = kwargs.get("headers")
        self.payload = kwargs.get("payload")
        self.onlystatus = kwargs.get("onlystatus")

    def set_url(self, url: str) -> None:
        self.url = url

    def set_headers(self, headers: str) -> None:
        self.headers = headers

    def set_payload(self, payload: str) -> None:
        self.payload = payload

    def set_onlystatus(self, onlystatus: bool) -> None:
        self.onlystatus = onlystatus

    def buildRequest(self) -> Request:
        req = Request(self.url)
        if self.headers:
            req.add_header(self.headers)
        if self.payload:
            req.add_data(self.payload)
        return req

        

    def execute(self):
        try:
            response = urlopen(self.buildRequest())
            if self.onlystatus:
                return response.status
            return response.read()
        except Exception as e:
            return e

    def to_dict(self):
        return {"url": self.url, "headers": self.headers, "payload": self.payload}

if __name__ == "__main__":

    builder = HTTPGetBuilder(url="http://www.google.com", onlystatus=True)
    print(builder.to_dict())
    print(builder.execute())

