# -*- coding: utf-8 -*-

import os
import random
import itertools

main_dir = os.path.split(os.path.abspath(__file__))[0]


class Random(dict):
    def __init__(self, file):
        self.load_file(file)

    def load_file(self, file):
        """Opening file.

        :param str file: filename
        """
        if file == 'nouns':
            self.load_nouns(file)
        elif file == 'nicknames':
            self.load_nicknames(file)

    def load_nouns(self, file):
        """Making dict for words.

        :param str file: filename
        """
        with open(os.path.join(main_dir, file + '.txt'), 'r') as f:
            for word in f:
                word = word.strip()
                letter = word[0]

                try:
                    self[letter].append(word)
                except KeyError:
                    self[letter] = [word]

    def load_nicknames(self, file):
        """Making dict for words.

        :param str file: filename
        """
        self['f'] = dict()
        self['m'] = dict()
        self['u'] = dict()

        with open(os.path.join(main_dir, file + '.txt'), 'r') as f:
            for word in f:
                word = word.strip()
                gender = word[0]
                letter = word[1].lower()
                nick = word[1:]

                try:
                    self[gender][letter].append(nick)
                    self['u'][letter].append(nick)
                except KeyError:
                    self[gender][letter] = [nick]
                    self['u'][letter] = [nick]

    def check_count(self, count):
        """Checks count

        :param int count: count number ;)
        :raises: ValueError
        """
        if count < 1:
            raise ValueError('Param "count" must be greater than 0.')


class RandomWords(Random):
    def __init__(self):
        super(RandomWords, self).__init__('nouns')
        self.available_letters = 'qwertyuiopasdfghjklzcvbnm'

    def random_word(self, letter=None):
        """Returns random word.

        :param str letter: letter
        :rtype: str
        :returns: random word
        """
        return self.random_words(letter)[0]

    def random_words(self, letter=None, count=1):
        """Returns list of random words.

        :param str letter: letter
        :param int count: how much words
        :rtype: list
        :returns: list of random words
        :raises: ValueError
        """
        self.check_count(count)

        if letter is None:
            all_words = list(itertools.chain.from_iterable(self.values()))

            try:
                words = random.sample(all_words, count)
            except ValueError:
                len_sample = len(all_words)
                raise ValueError('Param "count" must be less than {0}. \
(It is only {0} words)'.format(len_sample + 1, letter))

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


class RandomNicknames(Random):
    def __init__(self):
        super(RandomNicknames, self).__init__('nicknames')
        self.available_letters = 'qwertyuiopasdfghjklzxcvbnm'

    def random_nick(self, letter=None, gender=None):
        """Returns random nick.

        :param str letter: letter
        :param str gender: 'f' for female, 'm' for male and None for both
        :rtype: str
        :returns: random nick
        """
        return self.random_nicks(letter, gender)[0]

    def random_nicks(self, letter=None, gender=None, count=1):
        """Returns list of random nicks.

        :param str letter: letter
        :param str gender: 'f' for female, 'm' for male and None for both
        :param int count: how much nicks
        :rtype: list
        :returns: list of random nicks
        :raises: ValueError
        """
        self.check_count(count)

        if gender not in ('f', 'm', None):
            raise ValueError('Param "gender" must be in (f, m, None)')

        if letter is None:
            if not gender:
                g = 'u'
            else:
                g = gender

            all_nicks = list(itertools.chain.from_iterable(self[g].values()))

            try:
                nicks = random.sample(all_nicks, count)
            except ValueError:
                len_sample = len(all_nicks)
                raise ValueError('Param "count" must be less than {0}. \
(It is only {0} words.")'.format(len_sample + 1))

        elif type(letter) is not str:
            raise ValueError('Param "letter" must be string.')

        elif letter not in self.available_letters:
            raise ValueError('Param "letter" must be in "{0}".'.format(self.available_letters))

        elif letter in self.available_letters:
            if gender:
                g = gender
            else:
                g = 'u'

            try:
                nicks = random.sample(self[g][letter], count)
            except ValueError:
                len_sample = len(self[g][letter])
                raise ValueError('Param "count" must be less than {0}. \
(It is only {0} nicks for letter "{1}")'.format(len_sample + 1, letter))

        return nicks
