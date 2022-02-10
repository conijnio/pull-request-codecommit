import pytest
from unittest.mock import patch, MagicMock

from pull_request_codecommit.git import Commit
from pull_request_codecommit.git.client import Client
from tests import COMMITS


def test_git_client() -> None:
    with pytest.raises(Exception) as exc:
        Client("fake-path")

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
@patch("pull_request_codecommit.git.client.subprocess.run")
@patch("pull_request_codecommit.git.client.os.path.isdir")
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

    client = Client(path)

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
@patch("pull_request_codecommit.git.client.subprocess.run")
@patch("pull_request_codecommit.git.client.os.path.isdir")
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
    client = Client(path)
    assert client.current_branch == branch


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
@patch("pull_request_codecommit.git.client.subprocess.run")
@patch("pull_request_codecommit.git.client.os.path.isdir")
def test_get_commit_messages(
    mock_isdir: MagicMock, mock_run: MagicMock, path: str, branch: str
) -> None:
    mock_isdir.return_value = True

    def execute(parameters, cwd, stdout):
        assert path == cwd
        assert -1 == stdout
        mock_stdout = MagicMock()
        mock_stdout.stdout = bytes(COMMITS, "utf-8")
        return mock_stdout

    mock_run.side_effect = execute
    client = Client(path)

    commits = client.get_commit_messages("main")

    first: Commit = next(commits)
    second: Commit = next(commits)

    assert first == commits.first
    assert first.message.subject == "feat: my first commit"
    assert second.message.subject == "feat: my second commit"


@patch("pull_request_codecommit.git.client.subprocess.run")
@patch("pull_request_codecommit.git.client.os.path.isdir")
def test_get_no_commit_messages(mock_isdir: MagicMock, mock_run: MagicMock) -> None:
    mock_isdir.return_value = True

    def execute(parameters, cwd, stdout):
        assert -1 == stdout
        mock_stdout = MagicMock()
        mock_stdout.stdout = bytes("", "utf-8")
        return mock_stdout

    mock_run.side_effect = execute
    client = Client("my-path")

    commits = client.get_commit_messages("main")
    assert commits.first is None


@patch("pull_request_codecommit.git.client.subprocess.run")
@patch("pull_request_codecommit.git.client.os.path.isdir")
def test_push(mock_isdir: MagicMock, mock_run: MagicMock) -> None:
    mock_isdir.return_value = True

    def execute(parameters, cwd, stdout):
        assert parameters == ["git", "push", "--set-upstream", "origin", "HEAD"]
        assert -1 == stdout
        mock_stdout = MagicMock()
        mock_stdout.stdout = bytes("", "utf-8")
        return mock_stdout

    mock_run.side_effect = execute
    Client("my-path").push()


@patch("pull_request_codecommit.git.client.subprocess.run")
@patch("pull_request_codecommit.git.client.os.path.isdir")
def test_pull(mock_isdir: MagicMock, mock_run: MagicMock) -> None:
    mock_isdir.return_value = True

    def execute(parameters, cwd, stdout):
        assert parameters == ["git", "pull"]
        assert -1 == stdout
        mock_stdout = MagicMock()
        mock_stdout.stdout = bytes("", "utf-8")
        return mock_stdout

    mock_run.side_effect = execute
    Client("my-path").pull()


@patch("pull_request_codecommit.git.client.subprocess.run")
@patch("pull_request_codecommit.git.client.os.path.isdir")
def test_delete_branch(mock_isdir: MagicMock, mock_run: MagicMock) -> None:
    mock_isdir.return_value = True

    def execute(parameters, cwd, stdout):
        assert parameters == ["git", "branch", "-d", "feat/my-feature"]
        assert -1 == stdout
        mock_stdout = MagicMock()
        mock_stdout.stdout = bytes("", "utf-8")
        return mock_stdout

    mock_run.side_effect = execute
    Client("my-path").delete_branch("feat/my-feature")


@patch("pull_request_codecommit.git.client.subprocess.run")
@patch("pull_request_codecommit.git.client.os.path.isdir")
def test_checkout(mock_isdir: MagicMock, mock_run: MagicMock) -> None:
    mock_isdir.return_value = True

    def execute(parameters, cwd, stdout):
        assert parameters == ["git", "checkout", "master"]
        assert -1 == stdout
        mock_stdout = MagicMock()
        mock_stdout.stdout = bytes("", "utf-8")
        return mock_stdout

    mock_run.side_effect = execute
    Client("my-path").checkout("master")
