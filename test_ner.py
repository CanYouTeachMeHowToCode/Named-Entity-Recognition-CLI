"""
Test goes here

"""
from click.testing import CliRunner
from ner import named_entity_recognition


def test_cli():
    runner = CliRunner()
    runner_res = runner.invoke(
        named_entity_recognition, ["--text", "New York is an interesting place"]
    )
    assert runner_res.exit_code == 0
    assert "['New York']" in runner_res.output
