import copy
import unittest

import app

GUESTS = [
    {'name': 'Mara', 'ticket': 'student', 'checked_in': True},
    {'name': 'omar', 'ticket': 'vip', 'checked_in': True},
    {'name': 'Lina', 'ticket': 'student', 'checked_in': False},
    {'name': 'Kim', 'ticket': 'student', 'checked_in': True},
]


class TestStudentC7(unittest.TestCase):
    def test_counts_add_up_and_tickets_include_everyone(self):
        original = copy.deepcopy(GUESTS)
        self.assertEqual(
            app.door_report(GUESTS),
            {'registered': 4, 'checked_in': 3, 'not_arrived': 1, 'tickets': {'student': 3, 'vip': 1}},
        )
        self.assertEqual(GUESTS, original)

    def test_nobody_arrived_yet(self):
        guests = [dict(guest, checked_in=False) for guest in GUESTS]
        report = app.door_report(guests)
        self.assertEqual(report['checked_in'], 0)
        self.assertEqual(report['not_arrived'], 4)

    def test_report_has_exactly_the_four_keys(self):
        self.assertEqual(set(app.door_report(GUESTS)), {'registered', 'checked_in', 'not_arrived', 'tickets'})


if __name__ == '__main__':
    unittest.main()
