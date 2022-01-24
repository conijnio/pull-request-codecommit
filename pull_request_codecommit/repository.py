import os
import re
from typing import Optional, Tuple

from .config import Config
from .git import Client as GitClient
from .aws import Client as AwsClient


class Repository:
    """
    Understands CodeCommit repositories
    """

    def __init__(self, path: Optional[str] = None) -> None:
        self.__remote: str = ""
        self.__aws_region: str = ""
        self.__aws_profile: str = ""
        self.__repository_name: str = ""
        self.__branch: str = ""

        if not path:
            path = os.getcwd()

        self.__git = GitClient(path)

    def __config(self, method: str) -> Optional[str]:
        return getattr(Config, method)(self.aws_profile)

    @property
    def supported(self) -> bool:
        return self.remote.startswith("codecommit::")

    @property
    def remote(self) -> str:
        if not self.__remote:
            self.__remote = self.__git.remote("origin")

            if self.supported:
                self.__extract_from_remote(self.__remote)

        return self.__remote

    def __extract_from_remote(self, remote: str) -> None:
        def resolve(resolver: Optional[re.Match], index: int) -> str:
            return resolver.group(index) if resolver else ""

        # This can use some more error handling
        match = re.search(r"^codecommit::(.*)://(.*)@(.*)$", remote)
        self.__aws_region = resolve(match, 1)
        self.__aws_profile = resolve(match, 2)
        self.__repository_name = resolve(match, 3)

    @property
    def aws_region(self) -> str:
        return self.__aws_region

    @property
    def aws_profile(self) -> str:
        return self.__aws_profile

    @property
    def repository_name(self) -> str:
        return self.__repository_name

    @property
    def branch(self) -> str:
        if not self.__branch:
            self.__branch = self.__git.current_branch

        return self.__branch

    @property
    def destination(self) -> str:
        destination = self.__config("destination_branch")
        return destination if destination else ""

    def pull_request_information(self) -> Tuple[str, str]:
        title_postfix = ""
        commits = self.__git.get_commit_messages(destination_branch=self.destination)

        issues = ", ".join(commits.issues)
        description = list(map(lambda commit: commit.message.subject, commits))
        if issues:
            description.append(f"\nIssues: {issues}")
            title_postfix = f" ({issues})"

        title = f"{commits.first.message.subject}{title_postfix}"
        return title, "\n".join(description)

    def create_pull_request(self, title: str, description: str) -> str:
        client = AwsClient(profile=self.__aws_profile, region=self.__aws_region)
        response = client.create_pull_request(
            title=title,
            description=description,
            repository=self.repository_name,
            source=self.branch,
            destination=self.destination,
        )
        return f"https://{self.__aws_region}.console.aws.amazon.com/codesuite/codecommit/repositories/{self.repository_name}/pull-requests/{response.get('pullRequestId')}/details?region={self.__aws_region}"
