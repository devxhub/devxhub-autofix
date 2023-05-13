import pytest
from devxhub.argument_parser import Parser
from devxhub.const import ARGUMENT_PLACEHOLDER


def _args(**override):
    args = {'alias': None, 'command': [], 'yes': False,
            'help': False, 'version': False, 'debug': False,
            'force_command': None, 'repeat': False,
            'enable_experimental_instant_mode': False,
            'shell_logger': None}
    args.update(override)
    return args


@pytest.mark.parametrize('argv, result', [
    (['devxhub'], _args()),
    (['devxhub', '-a'], _args(alias='dxh')),
    (['devxhub', '--alias', '--enable-experimental-instant-mode'],
     _args(alias='dxh', enable_experimental_instant_mode=True)),
    (['devxhub', '-a', 'fix'], _args(alias='fix')),
    (['devxhub', 'git', 'branch', ARGUMENT_PLACEHOLDER, '-y'],
     _args(command=['git', 'branch'], yes=True)),
    (['devxhub', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-y'],
     _args(command=['git', 'branch', '-a'], yes=True)),
    (['devxhub', ARGUMENT_PLACEHOLDER, '-v'], _args(version=True)),
    (['devxhub', ARGUMENT_PLACEHOLDER, '--help'], _args(help=True)),
    (['devxhub', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-y', '-d'],
     _args(command=['git', 'branch', '-a'], yes=True, debug=True)),
    (['devxhub', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-r', '-d'],
     _args(command=['git', 'branch', '-a'], repeat=True, debug=True)),
    (['devxhub', '-l', '/tmp/log'], _args(shell_logger='/tmp/log')),
    (['devxhub', '--shell-logger', '/tmp/log'],
     _args(shell_logger='/tmp/log'))])
def test_parse(argv, result):
    assert vars(Parser().parse(argv)) == result
