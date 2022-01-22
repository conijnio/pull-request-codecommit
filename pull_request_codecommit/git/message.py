import re


class Message:
    """
    Understands git message that follow the conventional commits standard.

    See: https://www.conventionalcommits.org/en/v1.0.0/
    """

    def __init__(self, message: str) -> None:
        lines = []

        for line in iter(message.splitlines()):
            lines.append(line.strip(" "))

        self.__lines = list(filter(None, lines))
        self.__message = "\n".join(self.__lines)

    @property
    def issue(self) -> str:
        """
        Issue reference should be in the footer of the commit message
        """
        match = re.search(r"(?i)issue(:|) (.*)", self.__lines[-1])
        return f"{match.group(2)}" if match else ""

    @property
    def subject(self) -> str:
        """
        Subject is the first line of the commit message
        """
        return self.__lines[0]
