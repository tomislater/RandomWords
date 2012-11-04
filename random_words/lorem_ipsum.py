# -*- coding: utf-8 -*-

import os
import random

main_dir = os.path.split(os.path.abspath(__file__))[0]


class LoremIpsum(object):
    MIN_WORDS = 3

    def __init__(self):
        self.words = set()

        with open(os.path.join(main_dir, 'lorem_ipsum.txt'), 'r') as f:
            for word in f:
                word = word.strip()
                self.words.add(word)

        self.words = frozenset(self.words)

    def get_sentence(self, max_words=8):
        """
        :param int max_words: max words in sentence
        :returns: string with sentence
        :rtype: str
        """
        return self.get_sentences_list(max_words)[0]

    def get_sentences_list(self, max_words=8, sentences=1):
        """
        :param int max_words: max words in sentence
        :param int sentences: how many sentences
        :returns: list of strings with sentence
        :rtype: list
        """
        if max_words < self.MIN_WORDS:
            raise ValueError('Param "max_words" must be greater than {0}.'.format(self.MIN_WORDS - 1))
        elif max_words < 1:
            raise ValueError('Param "max_words" must be greater than 0.')
        elif sentences < 1:
            raise ValueError('Param "sentences" must be greater than 0.')
        elif max_words > len(self.words):
            raise ValueError('Param "max_words" must be less than {0}.'.format(len(self.words) + 1))

        sentences_list = []

        while sentences:
            num_rand_words = random.randint(self.MIN_WORDS, max_words)
            random_sentence = self.make_sentence(random.sample(self.words, num_rand_words))
            sentences_list.append(random_sentence)
            sentences -= 1
        return sentences_list

    def get_sentences(self, max_words=8, sentences=1):
        """
        :param int max_words: max words in sentence
        :param int sentences: how many sentences
        :returns: string with sentences
        :rtype: str
        """
        return ' '.join(self.get_sentences_list(max_words, sentences))

    def make_sentence(self, list_words):
        """Make a sentence from list of words

        :param list list_words: list of words
        :returns: sentence
        :rtype: str
        """
        sentence = ' '.join(list_words)
        return sentence[0].upper() + sentence[1:] + '.'
