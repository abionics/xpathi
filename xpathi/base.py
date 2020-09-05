from copy import deepcopy
from enum import Enum

from .utils import _format_parameter


class XPathMode(Enum):
    NONE = ''
    SINGLE = '/'
    DOUBLE = '//'


class Element:
    def __init__(self, tag: str):
        self.tag = tag
        self.parameters = list()
        self.order = None
        self.attribute = None

    def __truediv__(self, element: 'Element') -> str:
        return self.execute(XPathMode.DOUBLE, root=True) + element.execute(XPathMode.SINGLE)

    def __floordiv__(self, element: 'Element') -> str:
        return self.execute(XPathMode.DOUBLE, root=True) + element.execute(XPathMode.DOUBLE)

    def __rtruediv__(self, element: str) -> str:
        return element + self.execute(XPathMode.SINGLE)

    def __rfloordiv__(self, element: str) -> str:
        return element + self.execute(XPathMode.DOUBLE)

    def execute(self, mode: XPathMode = XPathMode.NONE, root: bool = False) -> str:
        start = '.' if root else ''
        return start + mode.value + self.__str__()

    def __call__(self, *args, **kwargs) -> 'Element':
        if len(args) + len(kwargs) == 0:
            return self
        element = deepcopy(self)
        for arg in args:
            arg = str(arg)
            element.parameters.append(arg)
        for key, value in kwargs.items():
            key = self._format_parameter_key(key)
            value = _format_parameter(value, special=False)
            element.parameters.append(f'{key}={value}')
        return element

    @staticmethod
    def _format_parameter_key(key: str):
        if key.startswith('_'):
            return '@' + key.lstrip('_')
        return f'{key}()'

    def __getitem__(self, value: int):
        element = deepcopy(self)
        element.order = value
        return element

    def __getattr__(self, attribute: str) -> 'Element':
        if attribute.startswith('__') and attribute.endswith('__'):
            super().__getattr__(attribute)
        element = deepcopy(self)
        element.attribute = attribute
        return element

    def __str__(self) -> str:
        return self.tag + self._parameters_to_str() + self._order_to_str() + self._attribute_to_str()

    def _parameters_to_str(self) -> str:
        if len(self.parameters) == 0:
            return ''
        condition = ' and '.join(self.parameters)
        return f'[{condition}]'

    def _order_to_str(self) -> str:
        if self.order is None:
            return ''
        if self.order == -1:
            return '[last()]'
        if self.order < -1:
            return f'[last(){self.order + 1}]'
        return f'[{self.order}]'

    def _attribute_to_str(self) -> str:
        if self.attribute is None:
            return ''
        if self.attribute in ['text']:
            return f'/{self.attribute}()'
        return f'/@{self.attribute}'

    def __repr__(self) -> str:
        return f'<tag={self.tag}, parameters={self.parameters}, order={self.order}, attribute={self.attribute}>'
