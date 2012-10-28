# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='RandomWords',
    version='0.1.0',
    author='Tomek Święcicki',
    author_email='tomislater@gmail.com',
    packages=['random_words', 'random_words.test'],
    url='https://github.com/tomislater/RandomWords',
    license='LICENSE.txt',
    description='A useful module for random text.',
    long_description=open('README.md').read(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    data_files=[('random_words', ['nouns.txt'])],
)
