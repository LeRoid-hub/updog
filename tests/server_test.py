import unittest
from unittest.mock import patch, MagicMock
from updog import Server


class TestServer(unittest.TestCase):

    def setUp(self):
        self.server = Server("localhost", 8080)

    def test_getIP(self):
        self.assertEqual(self.server.getIP(), "localhost")

    def test_getPort(self):
        self.assertEqual(self.server.getPort(), 8080)

    def test_setMaster(self):
        self.server.setMaster(True)
        self.assertEqual(self.server.getMaster(), True)

    def test_getMaster(self):
        self.assertEqual(self.server.getMaster(), False)

    def test_setRank(self):
        self.server.setRank(1)
        self.assertEqual(self.server.rank, 1)

    def test_getRank(self):
        self.assertEqual(self.server.rank, 99)

    def test_serialize(self):
        t = {
            "ip": "localhost",
            "port": 8080,
            "master": False,
            "rank": 99
        }

        self.assertEqual(self.server.serialize(), t)

    @patch('updog.server.urlopen')
    def test_newMaster_Status200(self, mock_urlopen):
        # Arrange
        mock_response = MagicMock()
        mock_response.read.return_value.decode.return_value = 'Mocked data'
        mock_response.__enter__.return_value = mock_response
        mock_response.__enter__.return_value.status = 200
        mock_urlopen.return_value = mock_response

        # Create an instance of the Server class
        server_instance = Server("http://google.com",8080)

        # Act
        result = server_instance.newMaster({})

        # Assert
        self.assertEqual(result, True)
        #mock_urlopen.assert_called_once_with('http://example.com')

    @patch('updog.server.urlopen')
    def test_newMaster_Status404(self, mock_urlopen):
        # Arrange
        mock_response = MagicMock()
        mock_response.read.return_value.decode.return_value = 'Mocked data'
        mock_response.__enter__.return_value = mock_response
        mock_response.__enter__.return_value.status = 404
        mock_urlopen.return_value = mock_response

        # Create an instance of the Server class
        server_instance = Server("http://google.com",8080)

        # Act
        result = server_instance.newMaster({})

        # Assert
        self.assertEqual(result, False)
        #mock_urlopen.assert_called_once_with('http://example.com')

    @patch('updog.server.urlopen')
    def test_checkServer_Status200(self, mock_urlopen):
        # Arrange
        mock_response = MagicMock()
        mock_response.read.return_value.decode.return_value = 'Mocked data'
        mock_response.__enter__.return_value = mock_response
        mock_response.__enter__.return_value.status = 200
        mock_urlopen.return_value = mock_response

        # Create an instance of the Server class
        server_instance = Server("http://google.com",8080)

        # Act
        result = server_instance.newMaster({})

        # Assert
        self.assertEqual(result, True)
        #mock_urlopen.assert_called_once_with('http://example.com')

    @patch('updog.server.urlopen')
    def test_checkServer_Status404(self, mock_urlopen):
        # Arrange
        mock_response = MagicMock()
        mock_response.read.return_value.decode.return_value = 'Mocked data'
        mock_response.__enter__.return_value = mock_response
        mock_response.__enter__.return_value.status = 404
        mock_urlopen.return_value = mock_response

        # Create an instance of the Server class
        server_instance = Server("http://google.com",8080)

        # Act
        result = server_instance.newMaster({})

        # Assert
        self.assertEqual(result, False)
        #mock_urlopen.assert_called_once_with('http://example.com')



if __name__ == '__main__':
    unittest.main()
