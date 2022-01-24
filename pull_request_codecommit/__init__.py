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

    if not repo.supported:
        raise click.ClickException("The repository is not compatible with this tool!")

    click.echo(f"Remote: {repo.remote}")
    click.echo(f"Region: {repo.aws_region}")
    click.echo(f"Profile: {repo.aws_profile}")
    click.echo(f"Repo: {repo.repository_name}")
    click.echo(f"Branch: {repo.branch}")
    click.echo()
    title, description = repo.pull_request_information()

    message = click.edit(f"{title}\n\n{description}")

    if message is None:
        raise click.ClickException("Pull request was not created")

    title = message.splitlines()[0]
    description = "\n".join(message.splitlines()[1:])
    link = repo.create_pull_request(title, description)
    click.echo(f"Please review/approve: {link}")
    click.echo()
    click.echo(click.style(title, bold=True))
    click.echo(description)


if __name__ == "__main__":
    main()
