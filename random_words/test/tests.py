# -*- coding: utf-8 -*-

import unittest
import random

from random_words import RandomWords


class TestsRandomWords(unittest.TestCase):

    def setUp(self):
        self.rw = RandomWords()
        self.available_words = 'qwertyuiopasdfghjklzcvbnm'

    def test_random_word(self):
        for letter in self.available_words:
            word = self.rw.random_word(letter)
            self.assertEqual(word[0], letter)

        with self.assertRaises(ValueError):
            self.rw.random_word('x')
            self.rw.random_word(0)
            self.rw.random_word(-1)
            self.rw.random_word(9)
            self.rw.random_words(['u'])
            self.rw.random_word('fs')

    def test_random_words(self):
        for letter in self.available_words:
            words = self.rw.random_words(letter)
            for word in words:
                self.assertEqual(word[0], letter)

        with self.assertRaises(ValueError):
            self.rw.random_words('fa')
            self.rw.random_words(['fha'])
            self.rw.random_words(0)
            self.rw.random_words(-1)
            self.rw.random_words(count=0)
            self.rw.random_words(count=None)
            self.rw.random_words(count=[8])
            self.rw.random_words(count=-5)

    def test_random_words_length_list(self):
        len_words = len(self.rw.random_words())
        self.assertEqual(len_words, 1)

        len_words = len(self.rw.random_words(count=10))
        self.assertEqual(len_words, 10)

        len_words = len(self.rw.random_words(count=73))
        self.assertEqual(len_words, 73)

        for letter in self.available_words:
            len_random = random.randint(1, 3)
            len_words = len(self.rw.random_words(letter, count=len_random))
            self.assertEqual(len_words, len_random)

        len_random = 1000000
        for letter in self.available_words:
            with self.assertRaises(ValueError):
                self.rw.random_words(letter, count=len_random)

if __name__ == "__main__":
    unittest.main()
