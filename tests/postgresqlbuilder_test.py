import unittest
from unittest.mock import patch, MagicMock
from updog import PostgreSQLBuilder
from urllib.request import Request

class TestPostgreSQLBuilder(unittest.TestCase):
    def setUp(self) -> None:
        self.postgresql = PostgreSQLBuilder()
        self.postgresql.connect("user","password","host","port","database")

    def test_connect(self):
        self.assertEqual(self.postgresql.user, "user")
        self.assertEqual(self.postgresql.password, "password")
        self.assertEqual(self.postgresql.host, "host")
        self.assertEqual(self.postgresql.port, "port")
        self.assertEqual(self.postgresql.database, "database")

    def test_query(self):
        self.postgresql.query("SELECT * FROM table")
        self.assertEqual(self.postgresql.sql, "SELECT * FROM table")

    @patch('updog.builder.postgresqlbuilder.psycopg2.connect')
    def test_execute(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [("row1", "row2")]

        self.postgresql.query("SELECT * FROM table")
        result = self.postgresql.execute()
        self.assertEqual(result, [("row1", "row2")])
        mock_connect.assert_called_once_with(user="user", password="password", host="host", port="port", database="database")
        mock_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT * FROM table")
        mock_cursor.fetchall.assert_called_once()

    def test_execute_no_query(self):
        result = self.postgresql.execute()
        self.assertEqual(result, "No query to execute")

    @patch('updog.builder.postgresqlbuilder.psycopg2.connect')
    def test_execute_exception(self, mock_connect):
        mock_connect.side_effect = Exception("Connection error")
        self.postgresql.query("SELECT * FROM table")
        result = self.postgresql.execute()
        self.assertEqual(result.args, ("Connection error",))

    def test_str(self):
        self.postgresql.query("SELECT * FROM table")
        self.assertEqual(str(self.postgresql), "PostgreSQLBuilder: SELECT * FROM table")

    def test_serialize(self):
        self.postgresql.query("SELECT * FROM table")
        sample = {
            "user": "user",
            "password": "password",
            "host": "host",
            "port": "port",
            "database": "database",
            "sql": "SELECT * FROM table"
        }
        self.assertEqual(self.postgresql.serialize(), sample)

    def test_serialize_no_query(self):
        sample = {
            "user": "user",
            "password": "password",
            "host": "host",
            "port": "port",
            "database": "database",
            "sql": ""
        }
        self.assertEqual(self.postgresql.serialize(), sample)

    def test_serialize_no_connection(self):
        self.postgresql = PostgreSQLBuilder()
        self.postgresql.query("SELECT * FROM table")
        sample = {
            "sql": "SELECT * FROM table"
        }
        self.assertEqual(self.postgresql.serialize(), sample)

    def test_serialize_no_query_no_connection(self):
        self.postgresql = PostgreSQLBuilder()
        self.assertEqual(self.postgresql.serialize().args, Exception("No user or sql query").args)
