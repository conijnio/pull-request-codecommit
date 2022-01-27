import pytest
from unittest.mock import patch, MagicMock
from pull_request_codecommit.repository import Repository


@pytest.mark.parametrize(
    "region, profile, repository",
    [
        ("eu-west-1", "my-profile", "my-repository"),
        ("eu-central-1", "my-other-profile", "my-other-repository"),
    ],
)
@patch("pull_request_codecommit.repository.GitClient")
def test_remote(
    mock_git_client: MagicMock, region: str, profile: str, repository: str
) -> None:
    mock_git_client.return_value.remote.return_value = (
        f"codecommit::{region}://{profile}@{repository}"
    )
    repo = Repository("/my/repository")
    assert repo.remote.region == region
    assert repo.remote.profile == profile
    assert repo.remote.name == repository
