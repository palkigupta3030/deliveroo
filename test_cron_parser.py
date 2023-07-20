import unittest
from cron_parser import parse_cron_expression, expand_field

class TestCronParser(unittest.TestCase):
    def test_parse_cron_expression(self):
        cron_expression = "*/15 0 1,15 * 1-5 /usr/bin/find"
        expected_result = {
            'minute': [0, 15, 30, 45],
            'hour': [0],
            'day of month': [1, 15],
            'month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'day of week': [1, 2, 3, 4, 5],
            'command': '/usr/bin/find'
        }
        self.assertEqual(parse_cron_expression(cron_expression), expected_result)

    def test_expand_field(self):
        self.assertEqual(expand_field("*/15", 0, 59), [0, 15, 30, 45])
        self.assertEqual(expand_field("1,2,3-5,10/2", 0, 12), [1, 2, 3, 4, 5, 10, 12])

if __name__ == "__main__":
    unittest.main()
