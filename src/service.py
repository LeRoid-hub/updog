from typing import TypeVar
import PostgreSQLBuilder
import HTTPGetBuilder

T = TypeVar('T', PostgreSQLBuilder, HTTPGetBuilder)

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
            return self.resFunc(result)
        else:
            if result:
                return True
            else:
                return False



