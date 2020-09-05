import os
import re

from setuptools import setup, find_packages


def read_file(filename: str) -> str:
    current_directory = os.path.dirname(__file__)
    path = os.path.join(current_directory, filename)
    with open(path) as file:
        return file.read()


def get_version() -> str:
    code = read_file('xpathi/__init__.py')
    return re.search(r'__version__ = \'(.*?)\'', code).group(1)


def get_long_description() -> str:
    return read_file('README.rst')


setup(
    name='xpathi',
    version=get_version(),
    description='Library for generating XPath expressions as string using magic methods 🧙✨',
    long_description=get_long_description(),
    long_description_content_type='text/x-rst',
    author='Alex Ermolaev',
    author_email='abionics.dev@gmail.com',
    url='https://github.com/abionics/xpathi',
    license='MIT',
    keywords='xpath scraping magic methods markup',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Text Processing :: Markup :: XML',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages(exclude=['tests', ]),
    zip_safe=False
)
