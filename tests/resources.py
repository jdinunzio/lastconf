# -*- coding: utf-8 -*-
"""Misc fixtures and helpers for all tests"""

import functools
import os

tests_directory = os.path.dirname(os.path.abspath(__file__))
tests_abs_path = functools.partial(os.path.join, tests_directory)
