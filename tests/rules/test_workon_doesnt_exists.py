import pytest
from devxhub.rules.workon_doesnt_exists import match, get_new_command
from devxhub.types import Command


@pytest.fixture(autouse=True)
def envs(mocker):
    return mocker.patch(
        'devxhub.rules.workon_doesnt_exists._get_all_environments',
        return_value=['devxhub', 'code_view'])


@pytest.mark.parametrize('script', [
    'workon tehdxh', 'workon code-view', 'workon new-env'])
def test_match(script):
    assert match(Command(script, ''))


@pytest.mark.parametrize('script', [
    'workon devxhub', 'workon code_view', 'work on tehdxh'])
def test_not_match(script):
    assert not match(Command(script, ''))


@pytest.mark.parametrize('script, result', [
    ('workon tehdxh', 'workon devxhub'),
    ('workon code-view', 'workon code_view'),
    ('workon zzzz', 'mkvirtualenv zzzz')])
def test_get_new_command(script, result):
    assert get_new_command(Command(script, ''))[0] == result
