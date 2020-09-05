from . import TAGS_AND_ATTRIBUTES
from ..base import Element

ALL_TAGS = [value for value in TAGS_AND_ATTRIBUTES
            if not value.startswith('_')]

__all__ = ALL_TAGS + ['ALL_TAGS']


def _create_element(tag_name: str, variable_name: str):
    xpath = Element(tag_name)
    globals()[variable_name] = xpath


for tag in ALL_TAGS:
    _create_element(tag, tag)
