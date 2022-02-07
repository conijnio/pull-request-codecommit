from typing import Optional

from .pull_request_codecommit import PullRequestCodeCommit
from .repository import Repository
from .git import Commits
from .aws import Client as AwsClient


class PullRequest:
    """
    Understands pull requests
    """

    def __init__(self, repo: Repository) -> None:
        self.__repo: Repository = repo
        self.__commits: Commits = self.__repo.commits()
        self.__title: str = ""
        self.__description: str = ""
        self.__link: str = ""
        self.__pull_request: PullRequestCodeCommit = PullRequestCodeCommit(
            repository=repo
        )

    def update(self, title: str, description: str) -> None:
        self.__title = title
        self.__description = description

    def save(self) -> None:
        self.__repo.push()
        self.__pull_request.save(self.title, self.description)

    def merge(self) -> str:
        return self.__pull_request.merge()

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
        return self.__pull_request.link
