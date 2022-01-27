from typing import Optional

import click

from pull_request_codecommit.repository import Repository


@click.command()
@click.option("-r", "--repository-path", default=None)
def main(repository_path: Optional[str]) -> None:
    """
    pull-request-codecommit
    """
    repo = Repository(repository_path)

    if not repo.remote.supported:
        raise click.ClickException("The repository is not compatible with this tool!")

    click.echo(f"Remote: {repo.remote.url}")
    click.echo(f"Region: {repo.remote.region}")
    click.echo(f"Profile: {repo.remote.profile}")
    click.echo(f"Repo: {repo.remote.name}")
    click.echo(f"Branch: {repo.branch}")
    click.echo()
    pull_request = repo.pull_request_information()

    if not pull_request.has_changes:
        click.echo(
            f"There are no differences between {repo.destination} and {repo.branch}!"
        )
        exit(0)

    message = click.edit(f"{pull_request.title}\n\n{pull_request.description}")

    if message is None:
        raise click.ClickException("Pull request was not created")

    title = message.splitlines()[0]
    description = "\n".join(message.splitlines()[1:]).lstrip("\n")
    link = repo.create_pull_request(title, description)
    click.echo(f"Please review/approve: {link}")
    click.echo()
    click.echo(click.style(title, bold=True))
    click.echo(description)


if __name__ == "__main__":
    main()
