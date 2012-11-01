RandomWords
============

Overview
--------

RandomWords is a useful package for generate random words, nicks and senteces (soon).

Requirements
------------

* Python 2.6 or 2.7
* Liunx, Windows?, Mac OSX?, BSD?

Install
-------

Quick way::

    pip install RandomWords

or::

    git clone https://github.com/tomislater/RandomWords.git
    cd RandomWords
    python setup.py install

How to use
----------

*Random words*::

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

*Random nicks*::

    >>> from random_words import RandomNicknames
    >>> rn = RandomNicknames()
    
    >>> rn.random_nick()
    'Fredrick'
    
    >>> rn.random_nick('y')
    'York'
    
    >>> rn.random_nick(letter='r', gender='m')
    'Roosevelt'
    
    >>> rn.random_nick(letter='r', gender='f')
    'Rene'
    
    >>> rn.random_nicks()
    ['Fionn']
    
    >>> rn.random_nicks(count=10)
    ['Kristy', 'Imani', 'Delbert', 'Brevyn', 'Jasmin', 'Genevieve', 'Clodagh', 'Graham', 'Sondra', 'Ed']
    
    >>> rn.random_nicks(letter='u', gender='f', count=4)
    ['Una', 'Uma', 'Ursula', 'Ulrica']

    >>> rn.random_nicks(letter='a', gender='m', count=4)
    ['Anthony', 'Alec', 'Antonio', 'Adam']
    
    >>> rn.random_nicks(gender='m', count=5)
    ['Elijah', 'Abraham', 'Noel', 'Myles', 'Pedro']

    >>> rn.random_nicks(gender='f', count=5)
    ['Sabrina', 'Debbie', 'Jerri', 'Savannah', 'Wendy']

TODO
----

* random sentence/sentences
* random lorem ipsum