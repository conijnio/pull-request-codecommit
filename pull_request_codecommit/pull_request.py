from pull_request_codecommit.git import Commits


class PullRequest:
    """
    Understands pull requests
    """

    def __init__(self, commits: Commits) -> None:
        self.__commits = commits

    @property
    def has_changes(self) -> bool:
        return True if self.__commits.first else False

    @property
    def title(self) -> str:
        if not self.__commits.first:
            return ""

        title = self.__commits.first.message.subject

        if self.__commits.issues:
            title += f" ({', '.join(self.__commits.issues)})"

        return title

    @property
    def description(self) -> str:
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
