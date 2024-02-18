import psycopg2

class PostgreSQLBuilder:
    """
    PostgreSQLBuilder class for the Service class
    Connects to a PostgreSQL database and executes a SQL query

    Attributes:
    - user (str): The user of the database
    - password (str): The password of the database
    - host (str): The host of the database
    - port (int): The port of the database
    - database (str): The database name
    - sql (str): The SQL query to be executed
    """
    user: str
    password: str
    host: str
    port: int
    database: str

    sql: str
    def __init__(self):
        """
        Constructor for the PostgreSQLBuilder class
        """
        self._query = None

    def connect(self, user: str, password: str, host: str, port: int, database: str):
        """
        Connects to the PostgreSQL database

        Parameters:
        - user (str): The user of the database
        - password (str): The password of the database
        - host (str): The host of the database
        - port (int): The port of the database
        - database (str): The database name

        Example:
        ```
        builder = PostgreSQLBuilder()
        builder.connect(user="user", password="password", host="localhost", port=5432, database="test")
        ```
        """
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def query(self, query: str):
        """
        Sets the SQL query to be executed

        Parameters:
        - query (str): The SQL query to be executed
        """
        self.sql = query

    def execute(self):
        """
        Executes the SQL query and returns the result

        Returns:
        - list: The result of the SQL query
        - Exception: The exception if the query fails
        """
        conn = None
        try:
            conn = psycopg2.connect(user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    port=self.port,
                                    database=self.database)
            cur = conn.cursor()
            cur.execute(self.sql)
            fetch = cur.fetchall()
            conn.commit()
            cur.close()
            return fetch
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            if conn is not None:
                conn.close()

    def __str__(self):
        """
        String representation of the PostgreSQLBuilder object

        Returns:
        - str: The sql query
        """
        return f"PostgreSQLBuilder: {self.sql}"

    def serialize(self):
        """
        Serializes the PostgreSQLBuilder object into a dictionary

        Returns:
        - dict: The serialized PostgreSQLBuilder object

        Example:
        ```
        {
            "user": "user",
            "password": "password",
            "host": "localhost",
            "port": 5432,
            "database": "test",
            "sql": "SELECT * FROM test"
        }
        """
        return {
            "user": self.user,
            "password": self.password,
            "host": self.host,
            "port": self.port,
            "database": self.database,
            "sql": self.sql
        }
