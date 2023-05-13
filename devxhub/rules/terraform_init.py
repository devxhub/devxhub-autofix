from devxhub.shells import shell
from devxhub.utils import for_app


@for_app('terraform')
def match(command):
    return ('this module is not yet installed' in command.output.lower() or
            'initialization required' in command.output.lower()
            )


def get_new_command(command):
    return shell.and_('terraform init', command.script)
