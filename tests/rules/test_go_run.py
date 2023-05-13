import pytest
from devxhub.rules.go_run import match, get_new_command
from devxhub.types import Command


@pytest.mark.parametrize('command', [
    Command('go run foo', ''),
    Command('go run bar', '')])
def test_match(command):
    assert match(command)


@pytest.mark.parametrize('command, new_command', [
    (Command('go run foo', ''), 'go run foo.go'),
    (Command('go run bar', ''), 'go run bar.go')])
def test_get_new_command(command, new_command):
    assert get_new_command(command) == new_command
