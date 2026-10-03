import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'name': 'Ada', 'ticket': 'vip', 'checked_in': False}, {'name': 'Lin', 'ticket': 'standard', 'checked_in': True}, {'name': 'Sam', 'ticket': 'standard', 'checked_in': False}]


class TestC1(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.ticket_counts(EXAMPLE), {'vip': 1, 'standard': 2})
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.ticket_counts([]), {})
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.ticket_counts([dict(name='A', ticket='student', checked_in=False)]), {'student': 1})
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

