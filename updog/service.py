from .builder import PostgreSQLBuilder, HTTPGetBuilder
from typing import TypeVar


class Service:
    """
    Service class is a wrapper for the builder classes. It is used to execute the builder and return the result.

    Attributes:
    - T (TypeVar) -  The allowed types for the builder
    - builder (T): The builder object to be executed
    - resFunc (function) - Optinal: The result function to be executed after the builder is executed

    """

    T = TypeVar('T', PostgreSQLBuilder, HTTPGetBuilder)
    builder: T
    resFunc = None

    def __init__(self, builder: T) -> None:
        """
        Constructor for the Service class

        Parameters:
        - builder (T): The builder object to be executed

        Example:
        ```
        service = Service(PostgreSQLBuilder())
        ```
        """
        self.builder = builder

    def setResFunc(self, resFunc) -> None:
        """
        Sets a custom result function for the Service object.
        With the result function, the result of the builder can be manipulated before returning it.

        Parameters:
        - resFunc (function): The result function to be executed after the builder is executed

        """
        if not callable(resFunc):
            return
        self.resFunc = resFunc

    def run(self) -> bool:
        """
        Executes the builder and returns the result.

        Returns:
        - bool: The result of the builder
        """
        result = self.builder.execute()
        if self.resFunc:
            return self.resFunc(result)
        else:
            if result:
                return True
            else:
                return False

    def __str__(self) -> str:
        return f"Service: {self.builder.__str__()}"

    def serialize(self) -> dict:
        """
        Serializes the Service object into a dictionary

        Returns:
        - dict: The serialized Service object
        """
        return {
            "builder": self.builder.serialize(),
            "resFunc": self.resFunc
        }

    def addType (self, newType):
        types = self.T.__constraints__
        types_str = [str(t) for t in types]
        self.T = TypeVar('T', types_str, newType)
