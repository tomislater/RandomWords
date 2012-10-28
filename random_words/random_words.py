# -*- coding: utf-8 -*-

import os
import random
import itertools

main_dir = os.path.split(os.path.abspath(__file__))[0]
f_words = os.path.join(main_dir, 'nouns.txt')


class RandomWords(dict):
    def __init__(self):
        self.available_letters = 'qwertyuiopasdfghjklzcvbnm'
        self.load_nouns()

    def load_nouns(self):
        with open(f_words, 'r') as f:
            for word in f:
                word = word.strip()
                letter = word[0]

                try:
                    self[letter].append(word)
                except KeyError:
                    self[letter] = [word]

    def random_word(self, letter=None):
        """Returns random word.

        :param str letter: letter
        :returns: str
        :raises: ValueError
        """
        return random.choice(self.random_words(letter))

    def random_words(self, letter=None, count=1):
        """Returns list of random words.

        :param str letter: letter
        :param int count: how much words
        :returns: list
        :raises: ValueError
        """
        if count < 1:
            raise ValueError('Param "count" must be greater than 0.')

        if letter is None:
            all_words = itertools.chain.from_iterable(self.values())
            words = random.sample(list(all_words), count)
        elif type(letter) is not str:
            raise ValueError('Param "letter" must be string.')
        elif letter not in self.available_letters:
            raise ValueError('Param "letter" must be in {0}.'.format(self.available_letters))
        elif letter in self.available_letters:
            try:
                words = random.sample(self[letter], count)
            except ValueError:
                len_sample = len(self[letter])
                raise ValueError('Param "count" must be less than {0}. \
(It is only {0} words for letter "{1}")'.format(len_sample + 1, letter))

        return words
