import json
from io import TextIOWrapper, BytesIO
from typing import List, Tuple, Any, Optional
from unittest.mock import patch, MagicMock

import pytest
from click.testing import CliRunner
from pull_request_codecommit import main
from pull_request_codecommit.config import configparser
from pull_request_codecommit.git import Commits
from tests import SCENARIOS


def edit_message(message: str) -> str:
    return message


def aws_client_execute_side_effect(parameters, stdout):
    assert -1 == stdout
    mock_stdout = MagicMock()

    if "create-pull-request" in parameters:
        data = {"pullRequest": {"pullRequestId": 1}}

    elif "merge-branches-by-fast-forward" in parameters:
        data = {"pullRequest": {"pullRequestStatus": "CLOSED"}}

    mock_stdout.stdout = bytes(json.dumps(data), "utf-8")
    return mock_stdout


def generate_invoke_parameters(
    cli_parameters,
) -> List[Tuple[str, Optional[str], Optional[str], bytes, str, List[str]]]:
    """
    Generate pytest parameters that are used to invoke the test
    """
    pytest_parameters = []

    for cli_parameter in cli_parameters:
        for scenario in SCENARIOS:
            pytest_parameters.append(scenario + (cli_parameter,))

    return pytest_parameters


@pytest.mark.parametrize(
    "remote, region, profile, config, commits, parameters",
    generate_invoke_parameters([[], ["--auto-merge"]]),
)
@patch("pull_request_codecommit.aws.client.subprocess.run")
@patch("pull_request_codecommit.repository.GitClient")
@patch("pull_request_codecommit.click.edit")
def test_invoke(
    mock_edit: MagicMock,
    mock_git_client: MagicMock,
    mock_aws_client: MagicMock,
    remote: str,
    region: str,
    profile: str,
    config: bytes,
    commits: str,
    parameters: List[str],
) -> None:
    mock_edit.side_effect = edit_message
    mock_git_client.return_value.get_commit_messages.return_value = Commits(commits)

    mock_git_client.return_value.remote.return_value = remote
    mock_git_client.return_value.current_branch.return_value = "feat/my-feature"
    configparser.open = MagicMock(return_value=TextIOWrapper(BytesIO(config)))  # type: ignore
    mock_aws_client.side_effect = aws_client_execute_side_effect

    runner = CliRunner()
    result = runner.invoke(main, parameters)
    assert result.exit_code == 0


@patch("pull_request_codecommit.repository.GitClient")
@patch("pull_request_codecommit.click.edit")
def test_invoke_no_commits(
    mock_edit: MagicMock,
    mock_git_client: MagicMock,
) -> None:
    mock_edit.side_effect = edit_message
    mock_git_client.return_value.get_commit_messages.return_value = Commits("")

    mock_git_client.return_value.remote.return_value = (
        f"codecommit::eu-west-1://my-profile@my-repository"
    )
    mock_git_client.return_value.current_branch.return_value = "feat/my-feature"
    config = b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master"
    configparser.open = MagicMock(return_value=TextIOWrapper(BytesIO(config)))  # type: ignore

    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 0
    assert "There are no differences between" in result.output


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
    mock_aws_client.side_effect = aws_client_execute_side_effect

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


@patch("pull_request_codecommit.repository.GitClient")
def test_invoke_no_repository_name(
    mock_git_client: MagicMock,
) -> None:
    mock_git_client.return_value.remote.return_value = f"codecommit::eu-west-1://"
    mock_git_client.return_value.current_branch.return_value = "feat/my-feature"
    config = b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master"
    configparser.open = MagicMock(return_value=TextIOWrapper(BytesIO(config)))  # type: ignore

    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 1
    assert "Error: The repository is not compatible with this tool!" in result.output
