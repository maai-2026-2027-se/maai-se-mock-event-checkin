import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'name': 'Ada', 'ticket': 'vip', 'checked_in': False}, {'name': 'Lin', 'ticket': 'standard', 'checked_in': True}, {'name': 'Sam', 'ticket': 'standard', 'checked_in': False}]


class TestC4(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        rows = copy.deepcopy(EXAMPLE)
        result = app.check_in(rows, 'Ada')
        self.assertTrue(result[0]['checked_in'])
        self.assertEqual(result[1:], EXAMPLE[1:])
        self.assertEqual(rows, EXAMPLE)
        for before, after in zip(rows, result):
            self.assertIsNot(before, after)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.check_in([EXAMPLE[1]], 'Lin'), [EXAMPLE[1]])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        with self.assertRaises(KeyError):
            app.check_in(EXAMPLE, 'missing')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

