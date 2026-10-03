import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'name': 'Ada', 'ticket': 'vip', 'checked_in': False}, {'name': 'Lin', 'ticket': 'standard', 'checked_in': True}, {'name': 'Sam', 'ticket': 'standard', 'checked_in': False}]


class TestC6(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.normalize_ticket(' VIP '), 'vip')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.normalize_ticket('Student'), 'student')
        self.assertEqual(app.normalize_ticket(' standard '), 'standard')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        for value in ['', ' ', 'premium']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                app.normalize_ticket(value)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

