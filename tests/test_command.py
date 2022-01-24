import json
from io import TextIOWrapper, BytesIO
from unittest.mock import patch, MagicMock

import pytest
from click.testing import CliRunner
from pull_request_codecommit import main
from pull_request_codecommit.config import configparser
from pull_request_codecommit.git import Commits
from .test_git_client import COMMITS, COMMITS_NO_ISSUES


def edit_message(message: str) -> str:
    return message


@pytest.mark.parametrize(
    "region, profile, config, commits",
    [
        (
            "eu-west-1",
            "my-profile",
            b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
            COMMITS,
        ),
        (
            "eu-central-1",
            "my-profile",
            b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
            COMMITS_NO_ISSUES,
        ),
        (
            "eu-west-1",
            "my-other-profile",
            b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
            COMMITS_NO_ISSUES,
        ),
        (
            "eu-central-1",
            "my-other-profile",
            b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
            COMMITS,
        ),
    ],
)
@patch("pull_request_codecommit.aws.client.subprocess.run")
@patch("pull_request_codecommit.repository.GitClient")
@patch("pull_request_codecommit.click.edit")
def test_invoke(
    mock_edit: MagicMock,
    mock_git_client: MagicMock,
    mock_aws_client: MagicMock,
    region: str,
    profile: str,
    config: bytes,
    commits: str,
) -> None:
    mock_edit.side_effect = edit_message
    mock_git_client.return_value.get_commit_messages.return_value = Commits(commits)

    mock_git_client.return_value.remote.return_value = (
        f"codecommit::{region}://{profile}@my-repository"
    )
    mock_git_client.return_value.current_branch.return_value = "feat/my-feature"
    configparser.open = MagicMock(return_value=TextIOWrapper(BytesIO(config)))  # type: ignore

    def execute(parameters, stdout):
        assert -1 == stdout
        mock_stdout = MagicMock()
        data = {"pullRequest": {"pullRequestId": 1}}
        mock_stdout.stdout = bytes(json.dumps(data), "utf-8")
        return mock_stdout

    mock_aws_client.side_effect = execute

    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 0


@pytest.mark.parametrize(
    "region, profile, config",
    [
        (
            "eu-west-1",
            "my-profile",
            b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
        ),
        (
            "eu-central-1",
            "my-profile",
            b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
        ),
        (
            "eu-west-1",
            "my-other-profile",
            b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
        ),
        (
            "eu-central-1",
            "my-other-profile",
            b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
        ),
    ],
)
@patch("pull_request_codecommit.aws.client.subprocess.run")
@patch("pull_request_codecommit.repository.GitClient")
@patch("pull_request_codecommit.click.edit")
def test_invoke_with_path(
    mock_edit: MagicMock,
    mock_git_client: MagicMock,
    mock_aws_client: MagicMock,
    region: str,
    profile: str,
    config: bytes,
) -> None:
    mock_edit.side_effect = edit_message
    mock_git_client.return_value.remote.return_value = (
        f"codecommit::{region}://{profile}@my-repository"
    )
    mock_git_client.return_value.current_branch.return_value = "feat/my-feature"
    configparser.open = MagicMock(return_value=TextIOWrapper(BytesIO(config)))  # type: ignore

    def execute(parameters, stdout):
        assert -1 == stdout
        mock_stdout = MagicMock()
        data = {"pullRequest": {"pullRequestId": 1}}
        mock_stdout.stdout = bytes(json.dumps(data), "utf-8")
        return mock_stdout

    mock_aws_client.side_effect = execute

    runner = CliRunner()
    result = runner.invoke(main, ["--repository-path", "./some/path/to/repo"])
    assert result.exit_code == 0


@patch("pull_request_codecommit.repository.GitClient")
def test_invoke_github(mock_git_client: MagicMock) -> None:
    mock_git_client.return_value.remote.return_value = (
        "git@github.com:Nr18/pull-request-codecommit.git"
    )
    mock_git_client.return_value.current_branch.return_value = "feat/my-feature"

    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 1


@patch("pull_request_codecommit.repository.GitClient")
@patch("pull_request_codecommit.click.edit")
def test_invoke_quit_edit(
    mock_edit: MagicMock,
    mock_git_client: MagicMock,
) -> None:
    mock_edit.return_value = None
    mock_git_client.return_value.remote.return_value = (
        f"codecommit::eu-west-1://my-profile@my-repository"
    )
    mock_git_client.return_value.current_branch.return_value = "feat/my-feature"
    config = b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master"
    configparser.open = MagicMock(return_value=TextIOWrapper(BytesIO(config)))  # type: ignore

    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 1
