import subprocess
from typing import List


class GitClient:
    """
    Understands git operations
    """

    def __init__(self, path: str):
        self.__path: str = path

    def execute(self, parameters: List[str]) -> str:
        parameters.insert(0, "git")
        response = subprocess.run(parameters, cwd=self.__path, stdout=subprocess.PIPE)

        return response.stdout.decode("utf-8").strip("\n")

    def remote(self, name: str = "origin") -> str:
        return self.execute(["config", "--get", f"remote.{name}.url"])

    @property
    def current_branch(self) -> str:
        return self.execute(["branch", "--show-current"])
