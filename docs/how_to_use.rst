How to use
==========

**Random words**::

    >>> from random_words import RandomWords
    >>> rw = RandomWords()
    >>> rw.random_word()
    'ditto'

    >>> rw.random_word(min_letter_count=10)
    'recombinations'

    >>> rw.random_word('y')
    yards

    >>> rw.random_word('a', min_letter_count=14)
    'accomplishments'

    >>> rw.random_words(count=10)
    ['runs', 'experience', 'comments', 'freedom', 'permit', 'honks', 'pins', 'texts', 'grant', 'fathers']

    >>> rw.random_words(count=10, min_letter_count=14)
    ['superstructure', 'documentations', 'authorizations', 'administrations', 'responsibilities', 'multiplication', 'representative', 'reinforcements', 'accountabilities', 'telecommunication']

    >>> rw.random_words(letter='r', count=5)
    ['raincoat', 'reactance', 'room', 'relocation', 'rudders']

    >>> rw.random_words(letter='r', count=5, min_letter_count=6)
    ['recordkeeping', 'return', 'recapitulation', 'rowers', 'rheostat']

    >>> rw.random_words(letter=None, count=2)
    ['tides', 'eights']

    >>> rw.random_words(letter=None, count=2, min_letter_count=10)
    ['centerline', 'forecastles']

**Random nicks**::

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

**Random e-mails**::

    >>> from random_words import RandomEmails
    >>> rand_mails = RandomEmails()

    >>> rand_mails.randomMail()
    'ernest@mail2java.com'

    >>> rand_mails.randomMails()
    ['annmarie@mail2xox.com']

    >>> rand_mails.randomMails(15)
    ['patrice@keko.com.ar', 'conor@mail2atom.com', 'vihan@mail2carolyn.com', 'felicia@looksmart.com.au', 'quinlan@accessgcc.com', 'aimee@china.net.vg', 'kate@mail2christmas.com', 'geoffrey@frommiami.com', 'lillie@comic.com', 'trinity@nagpal.net', 'bennett@webmail.co.za', 'jesse@chaiyomail.com', 'chase@iespana.es', 'mya@ijustdontcare.com', 'ramona@uole.com']

**Lorem ipsum**::

    >>> from random_words import LoremIpsum
    >>> li = LoremIpsum()
    >>> li.get_sentence()
    'Luctus molestie mazim netus temporsuspendisse, tristique nihil vestibulumnulla clita possim.'

    >>> li.get_sentences(5)
    'Esse erosin magnis cursus, in ullamcorper sapien et accusam. Arcu fringilla metusdonec. Magna tempus elitr lorem esse antesuspendisse, mi fusce luctus lacusnulla nullam porta. Takimata tation porttitor, amet aliquammauris enimsed dapibus. Assum lectus accusam fermentumfusce, iaculis turpis senectus id nunccurabitur.'

    >>> li.get_sentences_list(5)
    ['Platea egestas delenit curae iaculis ullamcorper.', 'Felissed sagittis volutpat vitae, lacus nullam massapellentesque urnapraesent.', 'Dapibusnam vitae nulla, consectetuer conguenulla luptatum urnamorbi.', 'Ante nostra vero nihil eu odio.', 'Invidunt interdum condimentum ametduis, leopraesent tempus placerat aaenean ad.']
