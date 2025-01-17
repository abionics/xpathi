from xpathi.base import Element
from xpathi.elements import *


def test_single_slash():
    xpath = div / a
    assert xpath == './/div/a'


def test_double_slash():
    xpath = div // a
    assert xpath == './/div//a'


def test_parameters_1():
    xpath = div // a(_class='c1', _maxlength=10)
    assert xpath == './/div//a[@class="c1" and @maxlength=10]'


def test_parameters_2():
    xpath = div // a(_class)
    assert xpath == './/div//a[@class]'


def test_parameters_3():
    xpath = div // a('@class')
    assert xpath == './/div//a[@class]'


def test_parameters_text():
    xpath = div / a(text='short', _class='c1')
    assert xpath == './/div/a[text()="short" and @class="c1"]'


def test_parameters_name():
    xpath = div / a(name='short', _class='c1')
    assert xpath == './/div/a[name()="short" and @class="c1"]'


def test_attribute_1():
    xpath = div / a / _href
    assert xpath == './/div/a/@href'


def test_attribute_2():
    xpath = div / a.href
    assert xpath == './/div/a/@href'


def test_attribute_text_1():
    xpath = div / a / text()
    assert xpath == './/div/a/text()'


def test_attribute_text_2():
    xpath = div / a / text
    assert xpath == './/div/a/text()'


def test_attribute_text_3():
    xpath = div / a.text()
    assert xpath == './/div/a/text()'


def test_attribute_text_4():
    xpath = div / a.text
    assert xpath == './/div/a/text()'


def test_order_1():
    xpath = div / a[3] / p
    assert xpath == './/div/a[3]/p'


def test_order_2():
    xpath = div / a[last() - 1] / _href
    assert xpath == './/div/a[last()-1]/@href'


def test_order_3():
    xpath = div / a[-2] / _href
    assert xpath == './/div/a[last()-1]/@href'


def test_contains_1():
    xpath = div / a(contains(_href, 'https'), _class='c1')
    assert xpath == './/div/a[contains(@href, "https") and @class="c1"]'


def test_contains_2():
    xpath = div / a(contains('@href', 'https'), _class='c1')
    assert xpath == './/div/a[contains(@href, "https") and @class="c1"]'


def test_contains_3():
    xpath = div / a(contains(text(), 'https'), _class='c1')
    assert xpath == './/div/a[contains(text(), "https") and @class="c1"]'


def test_contains_4():
    xpath = div / a(contains('text()', 'https'), _class='c1')
    assert xpath == './/div/a[contains(text(), "https") and @class="c1"]'


def test_any():
    xpath = div / any / a
    assert xpath == './/div/*/a'


def test_same_tag():
    xpath = div(_class='c1') / div(_class='c2')
    assert xpath == './/div[@class="c1"]/div[@class="c2"]'


def test_with_start_str():
    xpath = '//div' / a / _href
    assert xpath == '//div/a/@href'


def test_one_tag_execute():
    xpath = div(_class='c1').execute()
    assert xpath == 'div[@class="c1"]'


def test_one_tag_execute_with_mode():
    from xpathi.base import XPathMode
    xpath = div(_class='c1').execute(mode=XPathMode.DOUBLE)
    assert xpath == '//div[@class="c1"]'


def test_same_tag_and_attribute():
    xpath = div(contains(name(), _name)) / a
    assert xpath == './/div[contains(name(), @name)]/a'


def test_long_1():
    xpath = div / div(_class='wrapper')[last() - 1] // a(contains(text(), 'click'), _href='google') / _href[0]
    assert xpath == './/div/div[@class="wrapper"][last()-1]//a[contains(text(), "click") and @href="google"]/@href[0]'


def test_long_2():
    xpath = div / div(_class='wrapper')[last() - 1] // a(contains(_href, 'google'), text='click') / _href[0]
    assert xpath == './/div/div[@class="wrapper"][last()-1]//a[contains(@href, "google") and text()="click"]/@href[0]'


def test_custom_1():
    tag = Element('tag')
    _attribute = Element('@attribute')
    function = Element('function()')
    xpath = tag / _attribute / function
    assert xpath == './/tag/@attribute/function()'


def test_custom_2():
    tag = Element('tag')
    _attribute = Element('@attribute')
    xpath = tag(_attribute='val1', function='val2') // _attribute
    assert xpath == './/tag[@attribute="val1" and function()="val2"]//@attribute'
