import os
from typing import Optional

from .config import Config
from .git import Client as GitClient, Remote, Commits


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

    def commits(self) -> Commits:
        return self.__git.get_commit_messages(destination_branch=self.destination)

    def push(self) -> None:
        self.__git.push()

    def checkout_destination(self) -> None:
        branch = self.branch
        self.__git.checkout(self.destination)
        self.__git.pull()
        self.__git.delete_branch(branch)
