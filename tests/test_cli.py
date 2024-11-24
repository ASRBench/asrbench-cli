from asrbench_cli.cli import app


def test_app_return_exit_code_2(runner):
    result = runner.invoke(app)
    assert result.exit_code == 2
