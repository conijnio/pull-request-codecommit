from __future__ import annotations
from typing import List
import os.path
import subprocess
from .commits import Commits


class Client:
    """
    Understands git operations
    """

    def __init__(self, path: str):
        if not os.path.isdir(path):
            raise NotADirectoryError(f"The {path} is not a directory.")

        self.__path: str = path

    def __execute(self, parameters: List[str]) -> str:
        parameters.insert(0, "git")
        response = subprocess.run(parameters, cwd=self.__path, stdout=subprocess.PIPE)

        return response.stdout.decode("utf-8").strip("\n")

    def remote(self, name: str = "origin") -> str:
        return self.__execute(["config", "--get", f"remote.{name}.url"])

    @property
    def current_branch(self) -> str:
        return self.__execute(["branch", "--show-current"])

    def get_commit_messages(self, destination_branch: str) -> Commits:
        messages = self.__execute(
            ["log", f"{destination_branch}..{self.current_branch}"]
        )

        return Commits(messages)
