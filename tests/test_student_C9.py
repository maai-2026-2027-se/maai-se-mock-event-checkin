import copy
import csv
import io
import unittest

import app

HEADER = "name,ticket,checked_in\n"


class TestStudentC9(unittest.TestCase):
    def test_empty_list_is_header_only(self):
        self.assertEqual(app.to_csv([]), HEADER)

    def test_rows_keep_input_order_and_encode_checked_in(self):
        attendees = [
            {"name": "Zoe", "ticket": "student", "checked_in": True},
            {"name": "Ada", "ticket": "vip", "checked_in": False},
        ]
        self.assertEqual(app.to_csv(attendees), HEADER + "Zoe,student,1\nAda,vip,0\n")

    def test_uses_lf_line_endings_with_final_newline(self):
        text = app.to_csv([{"name": "Ada", "ticket": "vip", "checked_in": True}])
        self.assertNotIn("\r", text)
        self.assertTrue(text.endswith("\n"))

    def test_quotes_commas_quotes_and_newlines(self):
        attendees = [
            {"name": "Lee, Ann", "ticket": "standard", "checked_in": False},
            {"name": 'Say "hi"', "ticket": "vip", "checked_in": True},
            {"name": "Two\nLines", "ticket": "student", "checked_in": False},
        ]
        expected = HEADER + '"Lee, Ann",standard,0\n"Say ""hi""",vip,1\n"Two\nLines",student,0\n'
        self.assertEqual(app.to_csv(attendees), expected)

    def test_round_trips_through_csv_reader(self):
        attendees = [{"name": 'O"Neil, Pat', "ticket": "vip", "checked_in": True}]
        rows = list(csv.reader(io.StringIO(app.to_csv(attendees))))
        self.assertEqual(rows, [["name", "ticket", "checked_in"], ['O"Neil, Pat', "vip", "1"]])

    def test_input_is_not_mutated(self):
        attendees = [{"name": "Ada", "ticket": "vip", "checked_in": False}]
        original = copy.deepcopy(attendees)
        app.to_csv(attendees)
        self.assertEqual(attendees, original)


if __name__ == "__main__":
    unittest.main()
