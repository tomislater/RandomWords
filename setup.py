# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='RandomWords',
    version='0.1.5',
    author='Tomek Święcicki',
    author_email='tomislater@gmail.com',
    packages=['random_words', 'random_words.test'],
    package_data={'': ['*.txt']},
    url='https://github.com/tomislater/RandomWords',
    license='LICENSE.txt',
    description='A useful module for a random text.',
    long_description=open('README.txt').read(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
)
