from unittest.mock import MagicMock, patch

import pytest

from pull_request_codecommit.git import Commits
from pull_request_codecommit.pull_request import PullRequest


COMMIT_SIMPLE_MESSAGE = """commit my-hash-1
Author: John Doe <john@doe.nl>
Date:   Fri Jan 21 21:01:00 2022 +0100

    feat: my first commit"""

COMMIT_DETAILED_MESSAGE = """commit my-hash-1
Author: John Doe <john@doe.nl>
Date:   Fri Jan 21 21:01:00 2022 +0100

    feat: my first commit

    Some additional information"""

COMMIT_SIMPLE_MESSAGE_ISSUE = """commit my-hash-1
Author: John Doe <john@doe.nl>
Date:   Fri Jan 21 21:01:00 2022 +0100

    feat: my first commit

    Issue: #1"""

COMMIT_DETAILED_MESSAGE_ISSUE = """commit my-hash-1
Author: John Doe <john@doe.nl>
Date:   Fri Jan 21 21:01:00 2022 +0100

    feat: my first commit

    Some additional information

    Issue: #1"""


@pytest.mark.parametrize(
    "commits, expected_title, expected_description",
    [
        (Commits(COMMIT_SIMPLE_MESSAGE), "feat: my first commit", ""),
        (
            Commits(COMMIT_DETAILED_MESSAGE),
            "feat: my first commit",
            "Some additional information",
        ),
        (
            Commits(COMMIT_SIMPLE_MESSAGE_ISSUE),
            "feat: my first commit (#1)",
            "Issues: #1",
        ),
        (
            Commits(COMMIT_DETAILED_MESSAGE_ISSUE),
            "feat: my first commit (#1)",
            "Some additional information\n\nIssues: #1",
        ),
        (
            Commits(""),
            "",
            "",
        ),
    ],
)
@patch("pull_request_codecommit.pull_request_codecommit.AwsClient")
def test_git_client(
    mock_aws_client: MagicMock,
    commits: Commits,
    expected_title: str,
    expected_description: str,
) -> None:
    mock_aws_client.return_value.get_open_pull_request.return_value = {}

    mock_repo = MagicMock()
    mock_repo.commits.return_value = commits

    pull_request = PullRequest(mock_repo)
    assert pull_request.title == expected_title
    assert pull_request.description == expected_description


@patch("pull_request_codecommit.pull_request_codecommit.AwsClient")
def test_update_pull_request(mock_aws_client: MagicMock) -> None:
    mock_aws_client.return_value.get_open_pull_request.return_value = {
        "pullRequestId": "1",
        "title": "feat: test update pull request",
        "authorArn": "arn:aws:sts::111122223333:assumed-role/Role/john.doe@acme.com",
        "description": "my committed description",
    }

    mock_repo = MagicMock()
    mock_repo.commits.return_value = Commits(COMMIT_DETAILED_MESSAGE_ISSUE)
    mock_repo.remote.name = "my-repository"
    mock_repo.remote.region = "eu-west-1"
    pull_request = PullRequest(mock_repo)

    assert pull_request.title == "feat: test update pull request"
    assert "my committed description" in pull_request.description
    assert "Existing pull request found: #1" in pull_request.description
    assert "Author: john.doe@acme.com" in pull_request.description
    assert "Issues: #1" in pull_request.description

    pull_request.proposal.update(pull_request.title, pull_request.description)
    pull_request.save()
