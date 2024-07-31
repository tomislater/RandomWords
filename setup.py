# -*- coding: utf-8 -*-

import sys

from setuptools import setup
try:
    from setuptools.command.test import test as TestCommand
except ImportError:
    # setuptools.command.test has been removed.
    # The `setup` call is only necessary when defining this `cmdclass`, since
    # building the project is no longer dependend on that.
    # Therefore, there's no more to do here.
    sys.exit()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict-markers', '--verbose', '--tb=long']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


# Use `PyTest` as a `cmdclass`.
setup(
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    test_suite='random_words.test.test_random_words',
    extras_require={ 'testing': ['pytest'] }
)
