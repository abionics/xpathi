from xpathi.base import Element
from xpathi.elements import *

# base
xpath = div // a(text='link') / _href
print(type(xpath))
print(xpath)

xpath = div / div(_class='wrapper')[last() - 1] // a(contains(_href, 'google'), text='click') / _href
print(xpath)

# one tag (execute)
xpath = div(_class='wrapper').execute()
print(xpath)

# custom
tag = Element('tag')
_attribute = Element('@attribute')
function = Element('function()')

xpath = tag / _attribute / function
print(xpath)

xpath = tag(_attribute='val1', function='val2') // _attribute
print(xpath)
