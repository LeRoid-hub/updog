class type1:
    some: str
    vars: int

    def __init__(self, some: str, vars: int) -> None:
        self.some = some
        self.vars = vars

    def run(self) -> None:
        print("Running type1")

class type2:
    some: str
    vars: int

    def __init__(self, some: str, vars: int) -> None:
        self.some = some
        self.vars = vars

    def run(self) -> None:
        print("Doing type2 things")

class type3:
    some: str
    vars: int

    def __init__(self, some: str, vars: int) -> None:
        self.some = some
        self.vars = vars

    def run(self) -> None:
        print("Doing type3 things")

from typing import TypeVar
class wrapper:
    T = TypeVar('T', type1, type2)
    obj: T

    def __init__(self, obj: T) -> None:
        self.obj = obj

    def run(self) -> None:
        self.obj.run()

    def addType (self, newType):
        types = self.T.__constraints__
        types_str = [str(t) for t in types]
        self.T = TypeVar('T', types_str, newType)

    def getTypes(self):
        print(self.T.__constraints__)

if __name__ == "__main__":
    t1 = type1("Hello", 1)
    w1 = wrapper(t1)
    w1.addType(type3)
    print(w1.getTypes())
