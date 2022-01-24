# pull-request-codecommit

[![License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE.md)
[![Maintenance](https://img.shields.io/badge/Maintained-yes-green.svg)](https://github.com/Nr18/pull-request-codecommit/graphs/commit-activity)
[![GitHub release](https://img.shields.io/github/release/Nr18/pull-request-codecommit.svg)](https://github.com/Nr18/pull-request-codecommit/releases/)
[![Continuous Integration](https://github.com/Nr18/pull-request-codecommit/actions/workflows/ci.yml/badge.svg)](https://github.com/Nr18/pull-request-codecommit/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/Nr18/pull-request-codecommit/branch/main/graph/badge.svg?token=H6zsiLbNjP)](https://codecov.io/gh/Nr18/pull-request-codecommit)

> Note, this project is still under development and is not functional yet!

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

## Alternative installation: Docker

Build the docker image

```bash
docker build -t pull-request-codecommit-docker .
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

#### Docker usage

Run the `pull-request-codecommit` command as follows

```bash
docker run --rm -it -v `pwd`:/tests pull-request-codecommit-docker pull-request-codecommit
```

## Usage

To use `pull-request-codecommit` you just execute the following command:

```bash
pull-request-codecommit
```

## Testing locally

```bash
./create_repo.sh
```
