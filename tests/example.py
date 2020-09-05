from xpathi.elements import *

xpath = div // a(text='link') / _href
print(type(xpath))
print(xpath)

xpath = div / div(_class='wrapper')[last() - 1] // a(contains(_href, 'google'), text='click') / _href
print(xpath)
