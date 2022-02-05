from pull_request_codecommit.git import Commits


class PullRequest:
    """
    Understands pull requests
    """

    def __init__(self, commits: Commits) -> None:
        self.__title: str = ""
        self.__description: str = ""
        self.__link: str = ""
        self.__commits: Commits = commits

    def update(self, title: str, description: str) -> None:
        self.__title = title
        self.__description = description

    @property
    def has_changes(self) -> bool:
        return True if self.__commits.first else False

    @property
    def title(self) -> str:
        if self.__title:
            return self.__title

        if not self.__commits.first:
            return ""

        title = self.__commits.first.message.subject

        if self.__commits.issues:
            title += f" ({', '.join(self.__commits.issues)})"

        return title

    @property
    def description(self) -> str:
        if self.__description:
            return self.__description

        if len(self.__commits) == 1:
            description = (
                [self.__commits.first.message.body] if self.__commits.first else []
            )
        else:
            description = list(
                map(lambda commit: commit.message.subject, self.__commits)
            )

        if self.__commits.issues:
            description.append(f"\nIssues: " + ", ".join(self.__commits.issues))

        return "\n".join(description).lstrip("\n")

    @property
    def link(self) -> str:
        return self.__link

    def update_link(self, link: str):
        self.__link = link
