from typing import Optional

from .repository import Repository
from pull_request_codecommit.git import Commits
from .aws import Client as AwsClient


class PullRequest:
    """
    Understands pull requests
    """

    __aws_client: Optional[AwsClient] = None

    def __init__(self, repo: Repository) -> None:
        self.__repo: Repository = repo
        self.__commits: Commits = self.__repo.commits()
        self.__title: str = ""
        self.__description: str = ""
        self.__link: str = ""
        self.__pull_request_id: int = 0

    @property
    def __client(self) -> AwsClient:
        if not self.__aws_client:
            self.__aws_client = AwsClient(
                profile=self.__repo.remote.profile, region=self.__repo.remote.region
            )

        return self.__aws_client

    def update(self, title: str, description: str) -> None:
        self.__title = title
        self.__description = description

    def create(self) -> None:
        self.__repo.push()
        response = self.__client.create_pull_request(
            title=self.title,
            description=self.description,
            repository=self.__repo.remote.name,
            source=self.__repo.branch,
            destination=self.__repo.destination,
        )

        self.__pull_request_id = int(response.get("pullRequestId", 0))

        self.__link = "".join(
            [
                f"https://{self.__repo.remote.region}.console.aws.amazon.com/",
                "codesuite/codecommit/repositories/",
                f"pull-requests/{self.__pull_request_id}/details",
                f"?region={self.__repo.remote.region}",
            ]
        )

    def merge(self) -> str:
        response = self.__client.merge_pull_request(
            repository=self.__repo.remote.name, pull_request_id=self.__pull_request_id
        )
        status = response.get("pullRequestStatus", "")

        if status == "CLOSED":
            self.__repo.checkout_destination()

        return status

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
