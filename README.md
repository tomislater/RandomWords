RandomWords
============

Overview
--------

RandomWords is a useful package for generate random words and senteces (soon).

Requirements
------------

* Python 2.6 or 2.7
* Liunx, Windows?, Mac OSX?, BSD?

Install
-------

Quick way: `pip install RandomWords`

or:

`git clone https://github.com/tomislater/RandomWords.git`

`cd RandomWords`

`python setup.py install`


How to use
----------

    >>> from random_words import RandomWords
    >>> rw = RandomWords()
    >>> word = rw.random_word()
    >>> print word
    factors
    
    >>> word = rw.random_word('y')
    >>> print word
    yards
    
    >>> words = rw.random_words(count=10)
    >>> print words
    ['runs', 'experience', 'comments', 'freedom', 'permit', 'honks', 'pins', 'texts', 'grant', 'fathers']
    
    >>> words = rw.random_words(letter='r', count=5)
    >>> print words
    ['raincoat', 'reactance', 'room', 'relocation', 'rudders']
    
    >>> words = rw.random_words(letter=None, count=2)
    >>> print words
    ['tides', 'eights']



TODO
----

* random sentence/sentences
* random lorem ipsum
* random names