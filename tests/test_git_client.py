import pytest
from unittest.mock import patch, MagicMock

from pull_request_codecommit.git_client import GitClient


def test_git_client() -> None:
    with pytest.raises(Exception) as exc:
        GitClient("fake-path")

    assert str(exc.value) == "The fake-path is not a directory."


@pytest.mark.parametrize(
    "path, remote",
    [
        ("my-path", "codecommit::eu-west-1://my-profile@my-repository"),
        (
            "my-other-path",
            "codecommit::eu-central-1://my-other-profile@my-other-repository",
        ),
    ],
)
@patch("pull_request_codecommit.git_client.subprocess.run")
@patch("pull_request_codecommit.git_client.os.path.isdir")
def test_remote(
    mock_isdir: MagicMock, mock_run: MagicMock, path: str, remote: str
) -> None:
    mock_isdir.return_value = True

    def execute(parameters, cwd, stdout):
        assert path == cwd
        assert -1 == stdout
        mock_stdout = MagicMock()
        mock_stdout.stdout = bytes(f"\n\n{remote}\n\n", "utf-8")
        return mock_stdout

    mock_run.side_effect = execute

    client = GitClient(path)

    assert client.remote() == remote
    assert client.remote("origin") == remote


@pytest.mark.parametrize(
    "path, branch",
    [
        ("my-path", "main"),
        (
            "my-other-path",
            "master",
        ),
    ],
)
@patch("pull_request_codecommit.git_client.subprocess.run")
@patch("pull_request_codecommit.git_client.os.path.isdir")
def test_current_branch(
    mock_isdir: MagicMock, mock_run: MagicMock, path: str, branch: str
) -> None:
    mock_isdir.return_value = True

    def execute(parameters, cwd, stdout):
        assert path == cwd
        assert -1 == stdout
        mock_stdout = MagicMock()
        mock_stdout.stdout = bytes(f"\n\n{branch}\n\n", "utf-8")
        return mock_stdout

    mock_run.side_effect = execute
    client = GitClient(path)
    assert client.current_branch == branch
