import unittest

import app


class TestStudentC6(unittest.TestCase):
    def test_strips_and_casefolds_each_valid_label(self):
        for label, expected in [('\tSTANDARD\n', 'standard'), (' ViP', 'vip'), ('STUDENT ', 'student')]:
            with self.subTest(label=label):
                self.assertEqual(app.normalize_ticket(label), expected)

    def test_unknown_labels_are_rejected_without_aliases(self):
        for label in ['', '   ', 'premium', 'students', 'std', 'vip ticket']:
            with self.subTest(label=label), self.assertRaises(ValueError):
                app.normalize_ticket(label)
