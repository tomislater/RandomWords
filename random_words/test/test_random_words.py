# -*- coding: utf-8 -*-

import pytest
import random

from random_words import RandomWords
from random_words import RandomNicknames
from random_words import RandomEmails

from random_words import LoremIpsum


class TestsRandomWords:

    @classmethod
    def setup_class(cls):
        cls.rw = RandomWords()
        cls.letters = 'qwertyuiopasdfghjklzcvbnm'

    def test_random_word(self):
        for letter in self.letters:
            word = self.rw.random_word(letter)
            assert word[0] == letter

    def test_random_word_value_error(self):
        pytest.raises(ValueError, self.rw.random_word, 'x')
        pytest.raises(ValueError, self.rw.random_word, 0)
        pytest.raises(ValueError, self.rw.random_word, -1)
        pytest.raises(ValueError, self.rw.random_word, 9)
        pytest.raises(ValueError, self.rw.random_word, ['u'])
        pytest.raises(ValueError, self.rw.random_word, 'fs')

    def test_random_words(self):
        for letter in self.letters:
            words = self.rw.random_words(letter)
            for word in words:
                assert word[0] == letter

    def test_random_words_value_error(self):
        pytest.raises(ValueError, self.rw.random_words, 'fa')
        pytest.raises(ValueError, self.rw.random_words, ['fha'])
        pytest.raises(ValueError, self.rw.random_words, 0)
        pytest.raises(ValueError, self.rw.random_words, -1)

        pytest.raises(ValueError, self.rw.random_words, letter=None,
                      count=1000000)

        pytest.raises(ValueError, self.rw.random_words, count=0)
        pytest.raises(ValueError, self.rw.random_words, count=None)
        pytest.raises(ValueError, self.rw.random_words, count=[8])
        pytest.raises(ValueError, self.rw.random_words, count=-5)

    def test_random_words_length_list(self):
        len_words = len(self.rw.random_words())
        assert len_words == 1

        len_words = len(self.rw.random_words(count=10))
        assert len_words == 10

        len_words = len(self.rw.random_words(count=73))
        assert len_words == 73

        for letter in self.letters:
            len_random = random.randint(1, 3)
            len_words = len(self.rw.random_words(letter, count=len_random))
            assert len_words == len_random

        len_random = 1000000
        for letter in self.letters:
            pytest.raises(
                ValueError, self.rw.random_words, letter, count=len_random)


class TestsRandomNicknames:

    @classmethod
    def setup_class(cls):
        cls.rn = RandomNicknames()
        cls.letters = 'qwertyuiopasdfghjklzxcvbnm'

    def test_random_nick(self):
        genders = ('f', 'm')
        for letter in self.letters:
            nick = self.rn.random_nick(letter, random.choice(genders))
            assert nick[0].lower() == letter

    def test_random_nick_value_error(self):
        pytest.raises(ValueError, self.rn.random_nick, 'ą')
        pytest.raises(ValueError, self.rn.random_nick, 'Ź', 'f')
        pytest.raises(ValueError, self.rn.random_nick, 'ż', 'm')
        pytest.raises(ValueError, self.rn.random_nick, 'ą', None)
        pytest.raises(ValueError, self.rn.random_nick, 'ż')
        pytest.raises(ValueError, self.rn.random_nick, 0)
        pytest.raises(ValueError, self.rn.random_nick, -1, None)
        pytest.raises(ValueError, self.rn.random_nick, 9)
        pytest.raises(ValueError, self.rn.random_nick, 9, None)
        pytest.raises(ValueError, self.rn.random_nick, ['u'])
        pytest.raises(ValueError, self.rn.random_nick, 'fs')

    def test_random_nicks(self):
        genders = ('f', 'm')
        for letter in self.letters:
            nicks = self.rn.random_nicks(letter, random.choice(genders))
            for nick in nicks:
                assert nick[0].lower() == letter

    def test_random_nicks_count(self):
        len_random = 1000000
        for letter in self.letters:
            pytest.raises(
                ValueError, self.rn.random_nicks, letter, count=len_random)

    def test_random_nicks_not_gender(self):
        pytest.raises(ValueError, self.rn.random_nicks, gender=[])
        pytest.raises(ValueError, self.rn.random_nicks, gender=())
        pytest.raises(ValueError, self.rn.random_nicks, gender=set())
        pytest.raises(ValueError, self.rn.random_nicks, gender=frozenset())
        pytest.raises(ValueError, self.rn.random_nicks, gender="")
        pytest.raises(ValueError, self.rn.random_nicks, gender="dż")
        pytest.raises(ValueError, self.rn.random_nicks, gender="wtf")

    def test_random_nicks_gender_value_error(self):
        pytest.raises(
            ValueError, self.rn.random_nicks, letter=None, gender="f",
            count=1000000)

        pytest.raises(
            ValueError, self.rn.random_nicks, letter=None, gender="m",
            count=1000000)


class TestsRandomLoremIpsum:

    @classmethod
    def setup_class(cls):
        cls.li = LoremIpsum()

    def test_lorem_sentence(self):
        assert '.' in self.li.get_sentence()

    def test_lorem_sentences(self):
        assert '.' in self.li.get_sentences()

    def test_lorem_sentences_list(self):
        assert type(self.li.get_sentences_list()) == list

    def test_lorem_value_error(self):
        pytest.raises(ValueError, self.li.get_sentences, sentences=0)
        pytest.raises(ValueError, self.li.get_sentences, sentences=-2)


class TestsRandomEmails:

    @classmethod
    def setup_class(cls):
        cls.re = RandomEmails()

    def test_random_mail_type(self):
        assert '@' in self.re.randomMail()

    def test_random_mails_type(self):
        assert type(self.re.randomMails()) == list

    def test_random_mails_count(self):
        pytest.raises(ValueError, self.re.randomMails, count=-1)
        pytest.raises(ValueError, self.re.randomMails, count=0)
        pytest.raises(ValueError, self.re.randomMails, count=list())
        pytest.raises(ValueError, self.re.randomMails, count=dict())
        pytest.raises(ValueError, self.re.randomMails, count=set())
