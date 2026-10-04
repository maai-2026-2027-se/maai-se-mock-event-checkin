import unittest

import app


class TestStudentC2(unittest.TestCase):
    def test_sorts_checked_in_names_stably_by_casefolded_name(self):
        attendees = [
            {'name': 'ß', 'ticket': 'vip', 'checked_in': True},
            {'name': 'Beta', 'ticket': 'standard', 'checked_in': True},
            {'name': 'A', 'ticket': 'student', 'checked_in': True},
            {'name': 'SS', 'ticket': 'standard', 'checked_in': True},
            {'name': 'a', 'ticket': 'vip', 'checked_in': True},
            {'name': 'Not checked in', 'ticket': 'standard', 'checked_in': False},
        ]

        self.assertEqual(app.checked_in_names(attendees), ['A', 'a', 'Beta', 'ß', 'SS'])


if __name__ == '__main__':
    unittest.main()
