from devxhub.utils import replace_argument
from devxhub.specific.git import git_support


@git_support
def match(command):
    return ('add' in command.script_parts
            and 'Use -f if you really want to add them.' in command.output)


@git_support
def get_new_command(command):
    return replace_argument(command.script, 'add', 'add --force')
