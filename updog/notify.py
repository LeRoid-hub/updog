from .notifier import Email, Discord, Telegram
from typing import TypeVar


class Notify:
    T = TypeVar('T', Email, Discord, Telegram)
    notifier: T

    def __init__(self, notifier) -> None:
        self.notifier = notifier

    def notify(self, info: str, message: str ):
        self.notifier.send(info, message)

    def addType (self, newType):
        types = self.T.__constraints__
        types_str = [str(t) for t in types]
        self.T = TypeVar('T', types_str, newType)
