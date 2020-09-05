from ..base import Element
from ..utils import _format_parameter

__all__ = ('input_', 'any', 'text', 'name', 'contains', 'last')

input_ = Element('input')
any = Element('*')
text = Element('text()')
name = Element('name()')


def contains(value, subset: str) -> str:
    value = _format_parameter(value)
    subset = _format_parameter(subset)
    return f'contains({value}, {subset})'


def last() -> int:
    return -1
