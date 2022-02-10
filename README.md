# pull-request-codecommit

[![License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE.md)
[![Maintenance](https://img.shields.io/badge/Maintained-yes-green.svg)](https://github.com/Nr18/pull-request-codecommit/graphs/commit-activity)
[![GitHub release](https://img.shields.io/github/release/Nr18/pull-request-codecommit.svg)](https://github.com/Nr18/pull-request-codecommit/releases/)
[![Continuous Integration](https://github.com/Nr18/pull-request-codecommit/actions/workflows/ci.yml/badge.svg)](https://github.com/Nr18/pull-request-codecommit/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/Nr18/pull-request-codecommit/branch/main/graph/badge.svg?token=H6zsiLbNjP)](https://codecov.io/gh/Nr18/pull-request-codecommit)

This tool makes it easy to create pull requests for [AWS CodeCommit](https://aws.amazon.com/codecommit/). It relies on the
[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) standard. It looks at the git commits between the
current and the destination branch. Then it tries to create a pull request with this information as input.

## Installation

You can install the `pull-request-codecommit` tool by running the following command:

```bash
pip install pull_request_codecommit
```

### Installation in venv

Typically, you would want to run your dependencies isolated. You can install [pull-request-codecommit][pull-request-codecommit] in a `venv`
using the following commands:

```bash
python -m venv .venv
source .venv/bin/activate
pip install pull_request_codecommit
```

## Configuration

The tool uses the following file `~/.aws/pull-request-codecommit`. It will first load the `default` profile and then, if
provided the profile specific settings.

```ini
[profile default]
branch=main

[profile acme-profile]
branch=develop
```

## Usage

To use `pull-request-codecommit` you just execute the following command:

```bash
pull-request-codecommit
```

### Auto merge

In some cases it makes sense to directly merge the pull request, in those cases you can use:

```bash
pull-request-codecommit --auto-merge
```

This will directly merge the pull request using the fast-forward merge strategy.
If the merge is successful, it will:

- Merge and close the pull request.
- Checkout the destination branch.
- Pull the latest changes. (This will pull the just merged changes locally)
- Remove the working branch.

From this point you are ready for the next change.

### Update existing pull request

When a pull requests exists a proposal is made to update the existing pull request.

### Overwrite target branch

When you want to overwrite the target branch you need to supply the `--branch <name>` option:

```bash
pull-request-codecommit --branch my-target-branch
```

## Testing locally

```bash
./create_repo.sh
```
