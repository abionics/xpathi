======
xpathi
======

It is a library for generating XPath expressions as string 🧙✨

Reasons to use **xpathi**:

- Code expressions look like real xpath expressions
- Returns string type, you needn't convert it
- Implements many xpath features
- Dont have any dependencies
- Easy to extend, you can add custom methods and attributes in one line


Installation
------------

.. code-block:: bash

    pip install xpathi


Generating expressions
----------------------

Easily create xpath expression using magic methods:

.. code-block:: python

    from xpathi.elements import *

    xpath = div // a(text='link') / _href
    print(type(xpath))
    # <class 'str'>
    print(xpath)
    # .//div//a[text()="link"]/@href

    xpath = div / div(_class='wrapper')[last() - 1] // a(contains(_href, 'google'), text='click') / _href
    # .//div/div[@class="wrapper"][last()-1]//a[contains(@href, "google") and text()="click"]/@href

Result of expressions is always a valid xpath with string type. You can pass it like ``selector.xpath(div // a)``

Specify tag like ``tag1 / tag2``

Specify attribute like ``tag / _attribute`` (prefer this method) or ``tag.attribute``

Specify parameters like ``tag(_attr1=val1, _attr2=val2, text=val3)``

Specify order like ``tag[0]``, ``tag[last()]``, ``tag[last()-1]``, ``tag[-2]``


Usage examples
--------------

.. list-table::
   :widths: 10 20 20
   :header-rows: 1

   * - Description
     - Code
     - Result
   * - Single slash
     - ``div / a``
     - .//div/a
   * - Double slash
     - ``div // a``
     - .//div//a
   * - Parameters
     - ``div // a(_class='c1', _maxlength=10)``
     - .//div//a[@class="c1" and @maxlength=10]
   * - Parameters text()
     - ``div / a(text='short', _class='c1')``
     - .//div/a[text()="short" and @class="c1"]
   * - Get attribute
     - ``div / a / _href``
     - .//div/a/\@href
   * - Get attribute
     - ``div / a.href``
     - .//div/a/\@href
   * - Get text attribute
     - ``div / a / text()``
     - .//div/a/text()
   * - Index
     - ``div / a[3] / p``
     - .//div/a[3]/p
   * - Index using last
     - ``div / a[last() - 1] / _href``
     - .//div/a[last()-1]/@href
   * - Index negative
     - ``div / a[-2] / _href``
     - .//div/a[last()-1]/@href
   * - Contains
     - ``div / a(contains(_href, 'https'), _class='c1')``
     - .//div/a[contains(@href, "https") and @class="c1"]
   * - Contains
     - ``div / a(contains('@href', 'https'), _class='c1')``
     - .//div/a[contains(@href, "https") and @class="c1"]
   * - Contains text()
     - ``div / a(contains(text(), 'https'), _class='c1')``
     - .//div/a[contains(text(), "https") and @class="c1"]
   * - Any tag (*)
     - ``div / any / a``
     - .//div/\*/a

See more examples in tests

If you use only one tag (without slash), than you should call ``.execute()`` method
to convert it to string:

.. code-block:: python

    xpath = div(_class='wrapper').execute()
    print(xpath)
    # div[@class="wrapper"]


Custom tags and attributes
--------------------------

You can easy create custom tags, attributes and functions:

.. code-block:: python

    from xpathi.base import Element  # to create customs
    from xpathi.elements import *  # to build xpath

    tag = Element('tag')
    _attribute = Element('@attribute')
    function = Element('function()')

    xpath = tag / _attribute / function
    print(xpath)
    # .//tag/@attribute/function()

    xpath = tag(_attribute='val1', function='val2') // _attribute
    print(xpath)
    # .//tag[@attribute="val1" and function()="val2"]//@attribute


More
----

PyPI: https://pypi.org/project/xpathi

Repository: https://github.com/abionics/xpathi

Developer: Alex Ermolaev (Abionics)

Email: abionics.dev@gmail.com

License: MIT (see LICENSE.txt)
