import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'name': 'Ada', 'ticket': 'vip', 'checked_in': False}, {'name': 'Lin', 'ticket': 'standard', 'checked_in': True}, {'name': 'Sam', 'ticket': 'standard', 'checked_in': False}]


class TestC9(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.to_csv([]), 'name,ticket,checked_in\n')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.to_csv(EXAMPLE), 'name,ticket,checked_in\nAda,vip,0\nLin,standard,1\nSam,standard,0\n')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        rows = [dict(name='A, \"B\"\nC', ticket='student', checked_in=True)]
        self.assertEqual(list(csv.reader(io.StringIO(app.to_csv(rows)))), [['name', 'ticket', 'checked_in'], ['A, \"B\"\nC', 'student', '1']])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

