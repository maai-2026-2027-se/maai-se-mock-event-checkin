import copy
import unittest

import app


class TestStudentC8(unittest.TestCase):
    def test_filters_by_ticket_and_includes_arrived_and_not_arrived(self):
        rows = [
            {'name': 'Zoe', 'ticket': 'student', 'checked_in': True},
            {'name': 'Bob', 'ticket': 'vip', 'checked_in': False},
            {'name': 'amy', 'ticket': 'student', 'checked_in': False},
        ]
        original = copy.deepcopy(rows)
        self.assertEqual(app.guest_list(rows, ' Student\n'), [rows[2], rows[0]])
        self.assertEqual(rows, original)

    def test_ties_keep_input_order(self):
        rows = [dict(name=n, ticket='vip', checked_in=False) for n in ['B', 'a', 'b', 'A']]
        self.assertEqual(app.guest_list(rows, 'vip'), [rows[1], rows[3], rows[0], rows[2]])

    def test_unknown_ticket_raises_even_with_matching_or_empty_list(self):
        for attendees in ([], [dict(name='Ada', ticket='vip', checked_in=False)]):
            with self.subTest(attendees=attendees), self.assertRaises(ValueError):
                app.guest_list(attendees, '')
