import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'name': 'Ada', 'ticket': 'vip', 'checked_in': False}, {'name': 'Lin', 'ticket': 'standard', 'checked_in': True}, {'name': 'Sam', 'ticket': 'standard', 'checked_in': False}]


class TestC8(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.guest_list(list(reversed(EXAMPLE)), ' STANDARD '), [EXAMPLE[1], EXAMPLE[2]])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.guest_list(EXAMPLE, 'student'), [])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        with self.assertRaises(ValueError):
            app.guest_list([], 'other')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_4(self):
        original = copy.deepcopy(EXAMPLE)
        rows = [dict(name=n, ticket='vip', checked_in=False) for n in ['z', 'a', 'A']]
        self.assertEqual(app.guest_list(rows, 'vip'), [rows[1], rows[2], rows[0]])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

