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

    click.echo(f"Remote detected: {repo.remote}")
    click.echo(f"Region: {repo.aws_region}")
    click.echo(f"Profile: {repo.aws_profile}")
    click.echo(f"Repo: {repo.repository_name}")
    click.echo(f"Branch: {repo.branch}")

    repo.create_pull_request()


if __name__ == "__main__":
    main()
