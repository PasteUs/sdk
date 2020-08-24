from __future__ import absolute_import, print_function

from urllib.parse import urljoin as base_urljoin


def urljoin(*args):
    if len(args) < 2:
        raise AssertionError(f'len(args) must greater or equal than 2')

    base: str = args[0] if args[0][-1] == '/' else f'{args[0]}/'
    if len(args) > 2:
        result = urljoin(base_urljoin(base, str(args[1])), *args[2:])
    else:
        result = base_urljoin(base, args[1])
    return result
