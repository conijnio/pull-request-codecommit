COMMIT2 = """commit my-hash-1
Author: John Doe <john@doe.nl>
Date:   Fri Jan 21 21:01:00 2022 +0100

    feat: my first commit"""

COMMIT1 = """commit my-hash-2
Author: John Doe <john@doe.nl>
Date:   Fri Jan 21 21:01:00 2022 +0100

    feat: my second commit"""

COMMITS = f"{COMMIT1}\n\n    Issue #1\n\n{COMMIT2}\n\n    Issue #2"
COMMITS_NO_ISSUES = f"{COMMIT1}\n\n{COMMIT2}"

SCENARIOS = [
    (
        "codecommit::eu-west-1://my-profile@my-repository",
        "eu-west-1",
        "my-profile",
        b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
        COMMITS,
    ),
    (
        "codecommit::eu-west-1://my-profile@my-repository",
        "eu-central-1",
        "my-profile",
        b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
        COMMITS_NO_ISSUES,
    ),
    (
        "codecommit::eu-west-1://my-profile@my-repository",
        "eu-west-1",
        "my-other-profile",
        b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
        COMMITS_NO_ISSUES,
    ),
    (
        "codecommit::eu-west-1://my-profile@my-repository",
        "eu-central-1",
        "my-other-profile",
        b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
        COMMITS,
    ),
    (
        "codecommit::eu-west-1://my-repository",
        "eu-central-1",
        None,
        b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
        COMMITS,
    ),
    (
        "codecommit::://my-profile@my-repository",
        None,
        "my-profile",
        b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
        COMMITS,
    ),
    (
        "codecommit::://my-repository",
        None,
        None,
        b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
        COMMITS,
    ),
    (
        "codecommit://my-profile@my-repository",
        None,
        "my-profile",
        b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
        COMMITS,
    ),
    (
        "codecommit://my-repository",
        None,
        None,
        b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
        COMMITS,
    ),
    (
        "codecommit://my-repository-pr-failure",
        None,
        None,
        b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
        COMMITS,
    ),
    (
        "codecommit://my-repository-open-pr",
        None,
        None,
        b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
        COMMITS,
    ),
    (
        "codecommit://my-repository-other-open-pr",
        None,
        None,
        b"[default]\nbranch: my-main\n[profile my-profile]\nbranch: my-master",
        COMMITS,
    ),
]
