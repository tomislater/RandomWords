# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='RandomWords',
    version='0.1.7',
    author='Tomek Święcicki',
    author_email='tomislater@gmail.com',
    packages=['random_words', 'random_words.test'],
    package_data={'': ['*.txt', '*.dat']},
    url='https://github.com/tomislater/RandomWords',
    license='LICENSE.txt',
    description='A useful module for a random text, e-mails and lorem ipsum.',
    long_description=open('README.txt').read(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Development Status :: 5 - Production/Stable',
    ],
    install_requires=['ujson'],
)
