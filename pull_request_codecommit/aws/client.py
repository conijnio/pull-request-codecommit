from __future__ import annotations

import json
from typing import List, Optional
import subprocess


class Client:
    """
    Understands aws operations

    We use the AWS CLI for these operations so that we can use tha MFA toke cache from the cli.
    """

    def __init__(self, profile: Optional[str], region: Optional[str]) -> None:
        self.__base_command: List[str] = []
        self.__profile: Optional[str] = profile
        self.__region: Optional[str] = region

    @property
    def base_command(self) -> List[str]:
        base_command = ["aws"]

        if self.__profile:
            base_command.extend(["--profile", self.__profile])

        if self.__region:
            base_command.extend(["--region", self.__region])

        return base_command

    def __execute(self, parameters: List[str]) -> str:
        command = self.base_command
        command.extend(parameters)
        response = subprocess.run(command, stdout=subprocess.PIPE)

        return response.stdout.decode("utf-8").strip("\n")

    def create_pull_request(
        self,
        title: str,
        description: str,
        repository: str,
        source: str,
        destination: str,
    ) -> dict:
        command = [
            "codecommit",
            "create-pull-request",
            "--title",
            title,
            "--description",
            description,
            "--targets",
            f"repositoryName={repository}, sourceReference={source}, destinationReference={destination}",
        ]
        # print(command)
        # return {"pullRequestId": 1}
        response = self.__execute(command)
        data = json.loads(response)
        return data.get("pullRequest")
