from typing import Optional, Tuple

import click

from pull_request_codecommit.pull_request import PullRequest
from pull_request_codecommit.repository import Repository


@click.command()
@click.option("-r", "--repository-path", default=None)
def main(repository_path: Optional[str]) -> None:
    """
    pull-request-codecommit
    """
    repo = __load_repository(repository_path)
    __display_repository_information(repo)
    __create_pull_request(repo)


def __load_repository(repository_path: Optional[str]) -> Repository:
    repo = Repository(repository_path)

    if not repo.remote.supported:
        raise click.ClickException("The repository is not compatible with this tool!")

    return repo


def __create_pull_request(repo: Repository) -> None:
    pr = repo.pull_request_information()
    if not pr.has_changes:
        click.echo(
            f"There are no differences between {repo.destination} and {repo.branch}!"
        )
        exit(0)
    description, title = __propose_title_description(pr)
    link = repo.create_pull_request(title, description)

    click.echo(f"Please review/approve: {link}")
    click.echo()
    click.echo(click.style(title, bold=True))
    click.echo(description)


def __display_repository_information(repo: Repository) -> None:
    click.echo(f"Remote: {repo.remote.url}")
    click.echo(f"Region: {repo.remote.region}")
    click.echo(f"Profile: {repo.remote.profile}")
    click.echo(f"Repo: {repo.remote.name}")
    click.echo(f"Branch: {repo.branch}")
    click.echo()


def __propose_title_description(pr: PullRequest) -> Tuple[str, str]:
    message = click.edit(f"{pr.title}\n\n{pr.description}")
    if message is None:
        raise click.ClickException("Pull request was not created")
    title = message.splitlines()[0]
    description = "\n".join(message.splitlines()[1:]).lstrip("\n")
    return description, title


if __name__ == "__main__":
    main()
