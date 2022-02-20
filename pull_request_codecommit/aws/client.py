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
        base_command = ["aws", "--output", "json"]

        if self.__profile:
            base_command.extend(["--profile", self.__profile])

        if self.__region:
            base_command.extend(["--region", self.__region])

        return base_command

    def __execute(self, parameters: List[str]) -> str:
        command = self.base_command
        command.extend(parameters)
        response = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        if response.returncode != 0:
            message = response.stderr.decode("utf-8").strip("\n")
            last_line = message.splitlines()[-1]
            raise Exception(
                f"Failed to execute: `{command}`\n\n{last_line}\n\nYou can execute the command manually to troubleshoot!"
            )

        return response.stdout.decode("utf-8").strip("\n")

    def get_open_pull_request(
        self, repository: str, source: str, destination: str
    ) -> dict:
        response = self.__execute(
            [
                "codecommit",
                "list-pull-requests",
                "--repository-name",
                repository,
                "--pull-request-status",
                "OPEN",
            ]
        )
        data = json.loads(response)
        open_pull_requests = data.get("pullRequestIds")

        for pull_request_id in open_pull_requests:
            pr = self.__get_pull_request(pull_request_id)
            target = pr.get("pullRequestTargets", [{}])[0]

            if (
                target.get("sourceReference") == f"refs/heads/{source}"
                and target.get("destinationReference") == f"refs/heads/{destination}"
            ):
                return pr

        return {}

    def __get_pull_request(self, pull_request_id: int) -> dict:
        response = self.__execute(
            [
                "codecommit",
                "get-pull-request",
                "--pull-request-id",
                str(pull_request_id),
            ]
        )
        data = json.loads(response)
        return data.get("pullRequest", {})

    def create_pull_request(
        self,
        title: str,
        description: str,
        repository: str,
        source: str,
        destination: str,
    ) -> dict:
        response = self.__execute(
            [
                "codecommit",
                "create-pull-request",
                "--title",
                title,
                "--description",
                description,
                "--targets",
                f"repositoryName={repository}, sourceReference={source}, destinationReference={destination}",
            ]
        )
        data = json.loads(response)

        return data.get("pullRequest")

    def update_pull_request(
        self,
        pull_request_id: int,
        description: str,
    ) -> dict:
        response = self.__execute(
            [
                "codecommit",
                "update-pull-request-description",
                "--pull-request-id",
                str(pull_request_id),
                "--description",
                description,
            ]
        )
        data = json.loads(response)

        return data.get("pullRequest")

    def merge_pull_request(
        self, repository: str, pull_request_id: int, branch: str
    ) -> dict:
        response = self.__execute(
            [
                "codecommit",
                "merge-pull-request-by-fast-forward",
                "--pull-request-id",
                str(pull_request_id),
                "--repository-name",
                repository,
            ]
        )
        data = json.loads(response)
        pull_request = data.get("pullRequest")

        if pull_request.get("pullRequestStatus", "") == "CLOSED":
            self.__execute(
                [
                    "codecommit",
                    "delete-branch",
                    "--repository-name",
                    repository,
                    "--branch-name",
                    branch,
                ]
            )

        return pull_request
