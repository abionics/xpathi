from . import TAGS_AND_ATTRIBUTES
from ..base import Element

ALL_ATTRIBUTES = [value for value in TAGS_AND_ATTRIBUTES
                  if value.startswith('_')]

__all__ = ALL_ATTRIBUTES + ['ALL_ATTRIBUTES']


def _create_element(tag_name: str, variable_name: str):
    xpath = Element(tag_name)
    globals()[variable_name] = xpath


for attribute in ALL_ATTRIBUTES:
    name = attribute.replace('_', '@', 1)
    _create_element(name, attribute)
