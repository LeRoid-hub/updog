import unittest
from unittest.mock import patch, MagicMock
from updog import HTTPGetBuilder
from urllib.request import Request

class TestHTTPGetBuilder(unittest.TestCase):
    def setUp(self) -> None:
        self.http = HTTPGetBuilder(url="http://www.google.com")

    def test_init(self):
        self.assertEqual(self.http.url, "http://www.google.com")
        self.assertIsNone(self.http.headers)
        self.assertIsNone(self.http.payload)
        self.assertIsNone(self.http.onlystatus)

        http2 = HTTPGetBuilder(url="http://www.google.com", headers={"key":"value"}, payload="payload", onlystatus=True)
        self.assertEqual(http2.url, "http://www.google.com")
        self.assertEqual(http2.headers, {"key":"value"})
        self.assertEqual(http2.payload, "payload")
        self.assertEqual(http2.onlystatus, True)

    def test_set_url(self):
        self.http.set_url("http://www.yahoo.com")
        self.assertEqual(self.http.url, "http://www.yahoo.com")

    def test_set_headers(self):
        self.http.set_headers({"key":"value"})
        self.assertEqual(self.http.headers, {"key":"value"})

    def test_set_payload(self):
        self.http.set_payload("payload")
        self.assertEqual(self.http.payload, "payload")

    def test_set_onlystatus(self):
        self.assertFalse(self.http.onlystatus)
        self.http.set_onlystatus(True)
        self.assertTrue(self.http.onlystatus)

    def test_buildRequest(self):
        req = self.http.buildRequest()
        sample = Request("http://www.google.com")
        self.assertEqual(req.full_url,sample.full_url)

        self.http.set_headers({"key":"value"})
        sample.add_header("key","value")
        req = self.http.buildRequest()
        self.assertEqual(req.full_url,sample.full_url)
        self.assertEqual(req.header_items(),sample.header_items())

        self.http.set_payload("payload")
        sample.data = "payload".encode("utf-8")
        req = self.http.buildRequest()
        self.assertEqual(req.full_url,sample.full_url)
        self.assertEqual(req.header_items(),sample.header_items())
        self.assertEqual(req.data,sample.data)


    @patch('updog.builder.httpgetbuilder.urlopen')
    def test_execute(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value.decode.return_value = 'Mocked data'
        mock_response.__enter__.return_value = mock_response
        mock_response.__enter__.return_value.status = 200
        mock_urlopen.return_value = mock_response

        mock_urlopen.return_value.read.return_value.decode.return_value = 'Mocked data'

        self.assertEqual(self.http.execute(), 'Mocked data')

        self.http.set_onlystatus(True)
        self.assertEqual(self.http.execute(), 200)

        mock_response.__enter__.return_value.status = 404
        self.assertEqual(self.http.execute(), 404)

        mock_urlopen.side_effect = Exception('Mocked exception')
        self.assertEqual(self.http.execute(), 'Mocked exception')

    def test_todict(self):
        self.assertEqual(self.http.to_dict(), {"url":"http://www.google.com","headers":None,"payload":None})

        self.http.set_headers({"key":"value"})
        self.assertEqual(self.http.to_dict(), {"url":"http://www.google.com","headers":{"key":"value"},"payload":None})

        self.http.set_payload("payload")
        self.assertEqual(self.http.to_dict(), {"url":"http://www.google.com","headers":{"key":"value"},"payload":"payload"})

        self.http.set_onlystatus(True)
        self.assertEqual(self.http.to_dict(), {"url":"http://www.google.com","headers":{"key":"value"},"payload":"payload"})

    def test_serialize(self):
        self.assertEqual(self.http.serialize(), {'url': 'http://www.google.com', 'headers': None, 'payload': None, 'onlystatus': None})

        self.http.set_headers({"key":"value"})
        self.assertEqual(self.http.serialize(), {'url': 'http://www.google.com', 'headers': {'key': 'value'}, 'payload': None, 'onlystatus': None})

        self.http.set_payload("payload")
        self.assertEqual(self.http.serialize(), {'url': 'http://www.google.com', 'headers': {'key': 'value'}, 'payload': 'payload', 'onlystatus': None})

        self.http.set_onlystatus(True)
        self.assertEqual(self.http.serialize(), {'url': 'http://www.google.com', 'headers': {'key': 'value'}, 'payload': 'payload', 'onlystatus': True})


if __name__ == '__main__':
    unittest.main()
