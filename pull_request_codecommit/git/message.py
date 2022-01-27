import re
from typing import List


class Message:
    """
    Understands git message that follow the conventional commits standard.

    See: https://www.conventionalcommits.org/en/v1.0.0/
    """

    def __init__(self, message: str) -> None:
        lines = []

        for line in iter(message.splitlines()):
            lines.append(line.strip(" "))

        self.__issue: str = ""
        self.__lines: List[str] = list(filter(None, lines))

        if "issue" in self.__lines[-1].lower():
            self.__detect_issue(self.__lines.pop())

    def __detect_issue(self, line: str) -> None:
        match = re.search(r"(?i)issue(:|) (.*)", line)
        self.__issue = f"{match.group(2)}" if match else ""

    @property
    def issue(self) -> str:
        """
        Issue reference should be in the footer of the commit message
        """
        return self.__issue

    @property
    def subject(self) -> str:
        """
        Subject is the first line of the commit message
        """
        return self.__lines[0] if len(self.__lines) > 0 else ""

    @property
    def body(self) -> str:
        """
        Body is all except the first line
        """
        return "\n".join(self.__lines[1:]).lstrip("\n")
