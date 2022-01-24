from __future__ import annotations

import json
from typing import List
import subprocess


class Client:
    """
    Understands aws operations

    We use the AWS CLI for these operations so that we can use tha MFA toke cache from the cli.
    """

    def __init__(self, profile: str, region: str) -> None:
        self.__profile = profile
        self.__region = region

    def __execute(self, parameters: List[str]) -> str:
        command = ["aws", "--profile", self.__profile, "--region", self.__region]
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
        response = self.__execute(command)
        data = json.loads(response)
        return data.get("pullRequest")
