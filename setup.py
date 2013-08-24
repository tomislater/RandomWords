# -*- coding: utf-8 -*-

from setuptools import setup

from random_words import __version__

setup(
    name='RandomWords',
    version=__version__,
    author='Tomek Święcicki',
    author_email='tomislater@gmail.com',
    packages=['random_words', 'test'],
    package_data={'': ['*.txt', '*.dat']},
    url='https://github.com/tomislater/RandomWords',
    license='LICENSE.txt',
    description='A useful module for a random text, e-mails and lorem ipsum.',
    long_description=open('README.rst').read(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Development Status :: 5 - Production/Stable',
    ],
    install_requires=['ujson'],
    test_suite="pytest",
)
