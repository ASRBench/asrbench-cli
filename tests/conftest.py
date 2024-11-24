from pytest import fixture
from typer.testing import CliRunner


@fixture
def runner() -> CliRunner:
    return CliRunner()
