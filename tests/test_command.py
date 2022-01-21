from click.testing import CliRunner
from pull_request_codecommit import main


def test_invoke() -> None:
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 0
