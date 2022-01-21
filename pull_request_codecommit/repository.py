import os
import re
from typing import Optional

from .config import Config
from .git_client import GitClient


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

                def resolve_match(match: Optional[re.Match[str]], index: int) -> str:
                    return match.group(index) if match else ""

                # This can use some more error handling
                match = re.search("^codecommit::(.*)://(.*)@(.*)$", self.__remote)
                self.__aws_region = resolve_match(match, 1)
                self.__aws_profile = resolve_match(match, 2)
                self.__repository_name = resolve_match(match, 3)

        return self.__remote

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

    def create_pull_request(self):
        """
        TODO:
            - We need to list all changes between the destination and current branch and create a comprehensive message.
            - Extract a possible JIRA issue from the commit message
            - Do we want to display ask for a confirmation?
            - Show an aggregated overview on what happened

        RESPONSE=$(AWS_PROFILE=${AWS_PROFILE} aws codecommit create-pull-request \
          --region ${AWS_REGION} \
          --title "${TITLE}" \
          --description "${DESCRIPTION}" \
          --targets repositoryName=${REPOSITORY},sourceReference=${BRANCH},destinationReference=development)

        """
        print(f"Create PR from {self.branch} to {self.__config('destination_branch')}")
        pass

    # def cleanup(self):
    #     """
    #     git checkout development
    #     git pull
    #     git branch -d ${BRANCH}
    #     """
    #     pass
