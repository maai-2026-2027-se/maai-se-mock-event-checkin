import copy
import unittest

import app


def attendee(name, checked_in):
    return {"name": name, "ticket": "standard", "checked_in": checked_in}


class TestStudentC5(unittest.TestCase):
    def test_registrations_count_before_check_in(self):
        # Regression: the old code subtracted only checked-in attendees.
        attendees = [attendee("Ada", False), attendee("Lin", False), attendee("Sam", True)]
        self.assertEqual(app.remaining_capacity(10, attendees), 7)

    def test_nobody_checked_in_still_uses_places(self):
        attendees = [attendee("Ada", False), attendee("Lin", False)]
        self.assertEqual(app.remaining_capacity(2, attendees), 0)

    def test_overbooked_event_returns_zero(self):
        attendees = [attendee(name, False) for name in ["Ada", "Lin", "Sam", "Kim"]]
        self.assertEqual(app.remaining_capacity(3, attendees), 0)

    def test_empty_list_returns_full_capacity(self):
        self.assertEqual(app.remaining_capacity(4, []), 4)

    def test_negative_capacity_raises(self):
        with self.assertRaises(ValueError):
            app.remaining_capacity(-1, [attendee("Ada", False)])

    def test_input_is_not_mutated(self):
        attendees = [attendee("Ada", False), attendee("Lin", True)]
        original = copy.deepcopy(attendees)
        app.remaining_capacity(5, attendees)
        self.assertEqual(attendees, original)


if __name__ == "__main__":
    unittest.main()
