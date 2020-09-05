======
xpathi
======

It is a library for generating XPath expressions as string using magic methods 🧙✨


Generating expressions
----------------------

Easily create expression using magic methods:

.. code-block:: python

    >>> from xpathi.elements import *

    >>> xpath = div // a(text='link') / _href
    >>> print(type(xpath))
    <class 'str'>
    >>> print(xpath)
    .//div//a[text()="link"]/@href

    >>> xpath = div / div(_class='wrapper')[last() - 1] // a(contains(_href, 'google'), text='click') / _href
    .//div/div[@class="wrapper"][last()-1]//a[contains(@href, "google") and text()="click"]/@href
