from .message import Message


class Commit:
    """
    Understands git commit
    """

    def __init__(self, commit: str, author: str, date: str, message: Message) -> None:
        self.__commit: str = commit
        self.__author: str = author
        self.__date: str = date
        self.__message: Message = message

    @property
    def message(self) -> Message:
        return self.__message
