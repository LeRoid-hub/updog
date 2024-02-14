import psycopg2

class PostgreSQLBuilder:
    user: str
    password: str
    host: str
    port: int
    database: str

    sql: str
    def __init__(self):
        self._query = None

    def connect(self, user: str, password: str, host: str, port: int, database: str):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def query(self, query: str):
        self.sql = query

    def execute(self):
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
        finally:
            if conn is not None:
                conn.close()

