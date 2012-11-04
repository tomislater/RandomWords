# -*- coding: utf-8 -*-

import unittest
import random

from random_words import RandomWords
from random_words import RandomNicknames

from random_words import LoremIpsum


class TestsRandomWords(unittest.TestCase):

    def setUp(self):
        self.rw = RandomWords()
        self.letters = 'qwertyuiopasdfghjklzcvbnm'

    def test_random_word(self):
        for letter in self.letters:
            word = self.rw.random_word(letter)
            self.assertEqual(word[0], letter)

    def test_random_word_value_error(self):
        self.assertRaises(ValueError, self.rw.random_word, 'x')
        self.assertRaises(ValueError, self.rw.random_word, 0)
        self.assertRaises(ValueError, self.rw.random_word, -1)
        self.assertRaises(ValueError, self.rw.random_word, 9)
        self.assertRaises(ValueError, self.rw.random_word, ['u'])
        self.assertRaises(ValueError, self.rw.random_word, 'fs')

    def test_random_words(self):
        for letter in self.letters:
            words = self.rw.random_words(letter)
            for word in words:
                self.assertEqual(word[0], letter)

    def test_random_words_value_error(self):
        self.assertRaises(ValueError, self.rw.random_words, 'fa')
        self.assertRaises(ValueError, self.rw.random_words, ['fha'])
        self.assertRaises(ValueError, self.rw.random_words, 0)
        self.assertRaises(ValueError, self.rw.random_words, -1)
        self.assertRaises(ValueError, self.rw.random_words, count=0)
        self.assertRaises(ValueError, self.rw.random_words, count=None)
        self.assertRaises(ValueError, self.rw.random_words, count=[8])
        self.assertRaises(ValueError, self.rw.random_words, count=-5)

    def test_random_words_length_list(self):
        len_words = len(self.rw.random_words())
        self.assertEqual(len_words, 1)

        len_words = len(self.rw.random_words(count=10))
        self.assertEqual(len_words, 10)

        len_words = len(self.rw.random_words(count=73))
        self.assertEqual(len_words, 73)

        for letter in self.letters:
            len_random = random.randint(1, 3)
            len_words = len(self.rw.random_words(letter, count=len_random))
            self.assertEqual(len_words, len_random)

        len_random = 1000000
        for letter in self.letters:
            self.assertRaises(ValueError, self.rw.random_words, letter, count=len_random)


class TestsRandomNicknames(unittest.TestCase):

    def setUp(self):
        self.rn = RandomNicknames()
        self.letters = 'qwertyuiopasdfghjklzxcvbnm'

    def test_random_nick(self):
        genders = ('f', 'm')
        for letter in self.letters:
            nick = self.rn.random_nick(letter, random.choice(genders))
            self.assertEqual(nick[0].lower(), letter)

    def test_random_nick_value_error(self):
        self.assertRaises(ValueError, self.rn.random_nick, 'a')
        self.assertRaises(ValueError, self.rn.random_nick, 'Ź', 'f')
        self.assertRaises(ValueError, self.rn.random_nick, 'ż', 'm')
        self.assertRaises(ValueError, self.rn.random_nick, 'ą', None)
        self.assertRaises(ValueError, self.rn.random_nick, 'ż')
        self.assertRaises(ValueError, self.rn.random_nick, 0)
        self.assertRaises(ValueError, self.rn.random_nick, -1, None)
        self.assertRaises(ValueError, self.rn.random_nick, 9)
        self.assertRaises(ValueError, self.rn.random_nick, 9, None)
        self.assertRaises(ValueError, self.rn.random_nick, ['u'])
        self.assertRaises(ValueError, self.rn.random_nick, 'fs')

    def test_random_nicks(self):
        genders = ('f', 'm')
        for letter in self.letters:
            nicks = self.rn.random_nicks(letter, random.choice(genders))
            for nick in nicks:
                self.assertEqual(nick[0].lower(), letter)

    def test_random_nicks_count(self):
        len_random = 1000000
        for letter in self.letters:
            self.assertRaises(ValueError, self.rn.random_nicks, letter, count=len_random)


class TestsRandomNicknames(unittest.TestCase):

    def setUp(self):
        self.li = LoremIpsum()

    def test_lorem_sentence(self):
        self.assertEqual(type(self.li.get_sentence()), str)

    def test_lorem_sentences(self):
        self.assertEqual(type(self.li.get_sentences()), str)

    def test_lorem_sentences_list(self):
        self.assertEqual(type(self.li.get_sentences_list()), list)

    def test_lorem_value_error(self):
        self.assertRaises(ValueError, self.li.get_sentences, sentences=0)
        self.assertRaises(ValueError, self.li.get_sentences, sentences=-2)

if __name__ == "__main__":
    unittest.main()
