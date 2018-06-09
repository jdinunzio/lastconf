# -*- coding: utf-8 -*-
"""Unit tests of lastconf"""

import sys
nottest = istest = lambda obj: obj  # Fake decoratos provided by nose
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

import resources


###
# Test layers
###

@nottest
def setUpModule():
    # Setups for all tests of this module
    return

@nottest
def tearDownModule():
    # Cleanups for all tests of this module
    return

###
# Test cases
###

class SomeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setups before first test of this class
        return

    @classmethod
    def tearDownClass(cls):
        # Cleanups after last test of this class
        return

    def setUp(self):
        # Setups before each test of this class
        return

    def tearDown(self):
        # Cleanups after each test of this class
        return

    def test_fake(self):
        self.assertEqual(1, 1)
        return
