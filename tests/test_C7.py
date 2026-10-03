import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'name': 'Ada', 'ticket': 'vip', 'checked_in': False}, {'name': 'Lin', 'ticket': 'standard', 'checked_in': True}, {'name': 'Sam', 'ticket': 'standard', 'checked_in': False}]


class TestC7(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.door_report(EXAMPLE), {'registered': 3, 'checked_in': 1, 'not_arrived': 2, 'tickets': {'vip': 1, 'standard': 2}})
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.door_report([]), {'registered': 0, 'checked_in': 0, 'not_arrived': 0, 'tickets': {}})
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.door_report(app.check_in(EXAMPLE, 'Ada'))['checked_in'], 2)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

