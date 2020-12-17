import unittest
import day4_part2

class TestDay4Part2(unittest.TestCase):

    def test_validate_year_valid(self):
        test_data = [
                     {"year":1920, "min":1920, "max":2002},
                     {"year":2000, "min":1920, "max":2002},
                     {"year":2002, "min":1920, "max":2002},
                     
                     {"year":2010, "min":2010, "max":2020},
                     {"year":2015, "min":2010, "max":2020},
                     {"year":2020, "min":2010, "max":2020},
                     
                     {"year":2020, "min":2020, "max":2030},
                     {"year":2025, "min":2020, "max":2030},
                     {"year":2030, "min":2020, "max":2030},
                     ]
        for record in test_data:
            res = day4_part2.validate_year(record['year'], record['min'], record['max'])
            self.assertTrue(res)

    def test_validate_year_invalid(self):
        test_data = [
                     {"year":1919, "min":1920, "max":2002},
                     {"year":2003, "min":1920, "max":2002},
                     
                     {"year":2009, "min":2010, "max":2020},
                     {"year":2021, "min":2010, "max":2020},
                     
                     {"year":2019, "min":2020, "max":2030},
                     {"year":2031, "min":2020, "max":2030}
                     ]
        for record in test_data:
            res = day4_part2.validate_year(record['year'], record['min'], record['max'])
            self.assertFalse(res)


    def test_validate_height_valid(self):
        test_data = ["60in", "190cm"]
        for record in test_data:
            self.assertTrue(day4_part2.validate_height(record))

    def test_validate_height_invalid(self):
        test_data = ["190in", "190"]
        for record in test_data:
            self.assertFalse(day4_part2.validate_height(record))


    def test_validate_colour_valid(self):
        test_data = ["#123abc"]
        for record in test_data:
            self.assertTrue(day4_part2.validate_colour(record))

    def test_validate_colour_invalid(self):
        test_data = ["#123abz", "123abc"]
        for record in test_data:
            self.assertFalse(day4_part2.validate_colour(record))


    def test_validate_ecl_valid(self):
        test_data = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        for record in test_data:
            self.assertTrue(day4_part2.validate_eye_colour(record))

    def test_validate_ecl_invalid(self):
        test_data = ['xmb', 'aaa']
        for record in test_data:
            self.assertFalse(day4_part2.validate_eye_colour(record))


    def test_validate_pid_valid(self):
        test_data = ['000000001', '987654321']
        for record in test_data:
            self.assertTrue(day4_part2.validate_pid(record))

    def test_validate_pid_invalid(self):
        test_data = ['0123456789', 'aaa0123456']
        for record in test_data:
            self.assertFalse(day4_part2.validate_pid(record))

if __name__ == '__main__':
    unittest.main()