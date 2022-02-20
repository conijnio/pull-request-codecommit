from typing import Optional

import click

from .pull_request import PullRequest
from .repository import Repository


@click.command()
@click.option("-r", "--repository-path", default=None)
@click.option("-b", "--branch", default=None)
@click.option("--auto-merge/--no-auto-merge", default=False)
def main(
    repository_path: Optional[str], branch: Optional[str], auto_merge: bool
) -> None:
    """
    pull-request-codecommit
    """
    try:
        repo = __load_repository(repository_path=repository_path, target_branch=branch)
        __display_repository_information(repo)
        pr = __create_pull_request(repo)

        if auto_merge:
            status = pr.merge()
            click.echo(f"Auto merging resulted in: {status}")
    except Exception as exception:
        raise click.ClickException(str(exception))


def __load_repository(
    repository_path: Optional[str], target_branch: Optional[str]
) -> Repository:
    repo = Repository(path=repository_path, target_branch=target_branch)

    if not repo.remote.supported:
        raise click.ClickException("The repository is not compatible with this tool!")

    return repo


def __create_pull_request(repo: Repository) -> PullRequest:
    pr = PullRequest(repo)

    if not pr.has_changes:
        click.echo(
            f"There are no differences between {repo.destination} and {repo.branch}!"
        )
        exit(0)

    __propose_title_description(pr)
    pr.save()

    click.echo(f"Please review/approve: {pr.link}")
    click.echo()
    click.echo(click.style(pr.title, bold=True))
    click.echo(pr.description)

    return pr


def __display_repository_information(repo: Repository) -> None:
    click.echo(f"Remote: {repo.remote.url}")
    click.echo(f"Region: {repo.remote.region}")
    click.echo(f"Profile: {repo.remote.profile}")
    click.echo(f"Repo: {repo.remote.name}")
    click.echo(f"Branch: {repo.branch}")
    click.echo()


def __propose_title_description(pr: PullRequest) -> None:
    message = click.edit(f"{pr.title}\n\n{pr.description}")

    if message is None:
        raise click.ClickException("Pull request was not created")

    title = message.splitlines()[0]
    description = "\n".join(message.splitlines()[1:]).lstrip("\n")

    pr.update(title, description)


if __name__ == "__main__":
    main()
