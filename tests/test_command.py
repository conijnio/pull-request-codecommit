from io import TextIOWrapper, BytesIO
from unittest.mock import patch, MagicMock

import pytest
from click.testing import CliRunner
from pull_request_codecommit import main
from pull_request_codecommit.config import configparser


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
@patch("pull_request_codecommit.repository.GitClient")
def test_invoke(
    mock_git_client: MagicMock, region: str, profile: str, config: bytes
) -> None:

    mock_git_client.return_value.remote.return_value = (
        f"codecommit::{region}://{profile}@my-repository"
    )
    mock_git_client.return_value.current_branch.return_value = "feat/my-feature"
    configparser.open = MagicMock(return_value=TextIOWrapper(BytesIO(config)))  # type: ignore

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
@patch("pull_request_codecommit.repository.GitClient")
def test_invoke_with_path(
    mock_git_client: MagicMock, region: str, profile: str, config: bytes
) -> None:

    mock_git_client.return_value.remote.return_value = (
        f"codecommit::{region}://{profile}@my-repository"
    )
    mock_git_client.return_value.current_branch.return_value = "feat/my-feature"
    configparser.open = MagicMock(return_value=TextIOWrapper(BytesIO(config)))  # type: ignore

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
