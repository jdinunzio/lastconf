# -*- coding: utf-8 -*-
from unittest import TestCase
from lastconf.dictutil import deep_merge_dict


class TestDeepMergeDict(TestCase):
    def test_new_instance(self):
        """It must return a new dict instance"""
        a = dict(x=1)
        b = dict(y=2)
        c = deep_merge_dict(a, b)
        self.assertIsNot(c, a)
        self.assertIsNot(c, b)

    def test_new_instance_deep(self):
        """It must return new dict instances deep in the structure"""
        x = dict()
        y = dict()
        a = dict(x=x)
        b = dict(y=y)
        c = deep_merge_dict(a, b)
        self.assertIsNot(c['x'], x)
        self.assertIsNot(c['y'], y)

    def test_preserve_old(self):
        """Old entries must be preserved"""
        a = dict(x=1)
        b = dict(y=2)
        c = deep_merge_dict(a, b)
        self.assertIn('x', c)
        self.assertEqual(c['x'], a['x'])

    def test_add_new(self):
        """New entries must be added"""
        a = dict(x=1)
        b = dict(y=2)
        c = deep_merge_dict(a, b)
        self.assertIn('y', c)
        self.assertEqual(c['y'], b['y'])

    def test_overwrite_new(self):
        """New simple entries must overwrite old ones"""
        a = dict(x=1, y=1)
        b = dict(y=2)
        c = deep_merge_dict(a, b)
        self.assertIn('y', c)
        self.assertEqual(c['y'], b['y'])

    def test_deep_merge(self):
        """New dict entries must merged"""
        x1 = dict(w=1, y=2)
        x2 = dict(y=3, z=4)
        a = dict(x=x1)
        b = dict(x=x2)
        c = deep_merge_dict(a, b)
        self.assertIn('x', c)
        x = c['x']
        self.assertIn('w', x)
        self.assertIn('y', x)
        self.assertIn('z', x)
        self.assertEqual(x['w'], 1)
        self.assertEqual(x['y'], 3)
        self.assertEqual(x['z'], 4)
