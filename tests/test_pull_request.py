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
def test_git_client(
    commits: Commits, expected_title: str, expected_description: str
) -> None:
    pull_request = PullRequest(commits)
    assert pull_request.title == expected_title
    assert pull_request.description == expected_description
