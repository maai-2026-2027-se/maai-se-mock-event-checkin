import unittest

import app


class TestStudentC4(unittest.TestCase):
    def test_repeated_check_in_returns_fresh_records_and_preserves_fields(self):
        attendees = [
            {'name': 'Ada', 'ticket': 'vip', 'checked_in': True, 'note': 'early'},
            {'name': 'Lin', 'ticket': 'standard', 'checked_in': False},
        ]

        result = app.check_in(attendees, 'Ada')

        self.assertEqual(
            result,
            [
                {'name': 'Ada', 'ticket': 'vip', 'checked_in': True, 'note': 'early'},
                {'name': 'Lin', 'ticket': 'standard', 'checked_in': False},
            ],
        )
        self.assertEqual(attendees[1]['checked_in'], False)
        for original, updated in zip(attendees, result):
            self.assertIsNot(original, updated)

    def test_unknown_name_raises_key_error_without_mutating_input(self):
        attendees = [{'name': 'Ada', 'ticket': 'vip', 'checked_in': False}]

        with self.assertRaises(KeyError):
            app.check_in(attendees, 'ada')

        self.assertEqual(attendees[0]['checked_in'], False)


if __name__ == '__main__':
    unittest.main()
