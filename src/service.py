from typing import TypeVar
import PostgresqlBuilder
import httpgetbuilder as HttpGetBuilder

T = TypeVar('T', PostgresqlBuilder, HttpGetBuilder)
class Service:
    builder: T
    resFunc = None

    def __init__(self, builder: T) -> None:
        self.builder = builder

    def setResFunc(self, resFunc) -> None:
        if not callable(resFunc):
            return
        self.resFunc = resFunc

    def run(self) -> bool:
        result = self.builder.execute()
        if self.resFunc:
            self.resFunc(result)
        else:
            if result:
                return True
            else:
                return False


if __name__ == "__main__":
    builder = PostgresqlBuilder.PostgreSQLBuilder()
    builder.connect("user", "password", "host", 5432, "database")
    builder.query("SELECT * FROM table")
    service = Service(builder)
    service.run()

    builder = HttpGetBuilder.HTTPGetBuilder(url="http://www.google.com", onlystatus=True)
    service = Service(builder)
    print(service.run())
    print("Service ran")
