import unittest

import app


class TestStudentC1(unittest.TestCase):
    def test_counts_every_ticket_type_regardless_of_check_in(self):
        attendees = [
            {'name': 'Ada', 'ticket': 'vip', 'checked_in': False},
            {'name': 'Lin', 'ticket': 'standard', 'checked_in': True},
            {'name': 'Sam', 'ticket': 'vip', 'checked_in': True},
            {'name': 'Jo', 'ticket': 'student', 'checked_in': False},
        ]
        original = [dict(attendee) for attendee in attendees]

        self.assertEqual(
            app.ticket_counts(attendees),
            {'vip': 2, 'standard': 1, 'student': 1},
        )
        self.assertEqual(attendees, original)


if __name__ == '__main__':
    unittest.main()
