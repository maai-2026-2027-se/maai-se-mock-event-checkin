import copy
import unittest

import app

GUESTS = [
    {'name': 'Mara Lin', 'ticket': 'vip', 'checked_in': True},
    {'name': 'Omar', 'ticket': 'standard', 'checked_in': False},
    {'name': 'LINA', 'ticket': 'student', 'checked_in': False},
]


class TestStudentC3(unittest.TestCase):
    def test_matches_substring_anywhere_in_input_order(self):
        original = copy.deepcopy(GUESTS)
        self.assertEqual(app.find_attendees(GUESTS, '\tlIn  '), [GUESTS[0], GUESTS[2]])
        self.assertEqual(GUESTS, original)

    def test_empty_query_returns_everyone_and_empty_list_returns_empty(self):
        self.assertEqual(app.find_attendees(GUESTS, ''), GUESTS)
        self.assertEqual(app.find_attendees([], 'omar'), [])

    def test_inner_spaces_are_part_of_the_query(self):
        self.assertEqual(app.find_attendees(GUESTS, ' a l '), [GUESTS[0]])


if __name__ == '__main__':
    unittest.main()
