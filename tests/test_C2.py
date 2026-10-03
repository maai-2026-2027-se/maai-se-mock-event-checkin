import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'name': 'Ada', 'ticket': 'vip', 'checked_in': False}, {'name': 'Lin', 'ticket': 'standard', 'checked_in': True}, {'name': 'Sam', 'ticket': 'standard', 'checked_in': False}]


class TestC2(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.checked_in_names(EXAMPLE), ['Lin'])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.checked_in_names([]), [])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        rows = [dict(name=n, ticket='vip', checked_in=True) for n in ['z', 'a', 'A']]
        self.assertEqual(app.checked_in_names(rows), ['a', 'A', 'z'])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

