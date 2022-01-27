import os
from typing import Optional

from .config import Config
from .git import Client as GitClient, Remote
from .aws import Client as AwsClient
from .pull_request import PullRequest


class Repository:
    """
    Understands CodeCommit repositories
    """

    def __init__(self, path: Optional[str] = None) -> None:
        self.__remote: Optional[Remote] = None
        self.__branch: str = ""

        if not path:
            path = os.getcwd()

        self.__git = GitClient(path)

    def __config(self, method: str) -> Optional[str]:
        return getattr(Config, method)(self.remote.profile)

    @property
    def remote(self) -> Remote:
        if not self.__remote:
            self.__remote = Remote(self.__git.remote("origin"))

        return self.__remote

    @property
    def branch(self) -> str:
        if not self.__branch:
            self.__branch = self.__git.current_branch

        return self.__branch

    @property
    def destination(self) -> str:
        destination = self.__config("destination_branch")
        return destination if destination else ""

    def pull_request_information(self) -> PullRequest:
        commits = self.__git.get_commit_messages(destination_branch=self.destination)
        return PullRequest(commits)

    def create_pull_request(self, title: str, description: str) -> str:
        self.__git.push()
        client = AwsClient(profile=self.remote.profile, region=self.remote.region)
        response = client.create_pull_request(
            title=title,
            description=description,
            repository=self.remote.name,
            source=self.branch,
            destination=self.destination,
        )
        return f"https://{self.remote.region}.console.aws.amazon.com/codesuite/codecommit/repositories/{self.remote.name}/pull-requests/{response.get('pullRequestId')}/details?region={self.remote.region}"
