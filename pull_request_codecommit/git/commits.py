from typing import List
import re

from .commit import Commit
from .message import Message


class Commits:
    """
    Understands git commits
    """

    __index: int

    def __init__(self, messages: str) -> None:
        self.__index = 0
        self.__commits: List[Commit] = list(
            map(
                self.__read_commit_message,
                map(
                    lambda x: f"\ncommit {x}",
                    list(filter(None, messages.split("\ncommit "))),
                ),
            )
        )
        self.__commits.reverse()

    @property
    def first(self) -> Commit:
        return self.__commits[0]

    def __iter__(self):
        """
        We will skip the first commit that can be retrieved by using the `first` property.
        """
        return iter(self.__commits[1:])

    def __next__(self) -> Commit:
        item = self.__commits[self.__index]
        self.__index += 1
        return item

    @property
    def issues(self) -> List[str]:
        return list(set(map(lambda commit: commit.message.issue, self.__commits)))

    @staticmethod
    def __read_commit_message(message: str) -> Commit:
        def extract(regex: str) -> str:
            match = re.search(regex, message)
            return match.group(1).strip(" ") if match else ""

        return Commit(
            commit=extract(r"^commit (.*)"),
            author=extract(r"Author: (.*)"),
            date=extract(r"Date: (.*)"),
            message=Message(message=extract(r"(?sm)^    (.*)")),
        )
