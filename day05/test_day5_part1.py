import unittest
import day5_part1 as day5

class TestDay5Part1(unittest.TestCase):

    def test_get_row_range_front(self):
        result = day5.get_new_range('F', 0, 127)
        self.assertListEqual([0, 63], result)

        result = day5.get_new_range('F', 0, 63)
        self.assertListEqual([0, 31], result)

        result = day5.get_new_range('F', 0, 31)
        self.assertListEqual([0, 15], result)

        result = day5.get_new_range('F', 0, 15)
        self.assertListEqual([0, 7], result)

        result = day5.get_new_range('F', 0, 7)
        self.assertListEqual([0, 3], result)

        result = day5.get_new_range('F', 0, 3)
        self.assertListEqual([0, 1], result)

        result = day5.get_new_range('F', 0, 1)
        self.assertListEqual([0, 0], result)

    def test_get_row_range_back(self):

        result = day5.get_new_range('B', 0, 127)
        self.assertListEqual([64, 127], result)

        result = day5.get_new_range('B', 64, 127)
        self.assertListEqual([96, 127], result)

        result = day5.get_new_range('B', 96, 127)
        self.assertListEqual([112, 127], result)

    def test_get_col_range_left(self):

        result = day5.get_new_range('L', 0, 7)
        self.assertListEqual([0, 3], result)

        result = day5.get_new_range('L', 0, 3)
        self.assertListEqual([0, 1], result)

        result = day5.get_new_range('L', 0, 1)
        self.assertListEqual([0, 0], result)

        result = day5.get_new_range('L', 4, 7)
        self.assertListEqual([4, 5], result)

    def test_get_col_range_right(self):

        result = day5.get_new_range('R', 0, 7)
        self.assertListEqual([4, 7], result)

        result = day5.get_new_range('R', 4, 7)
        self.assertListEqual([6, 7], result)

        result = day5.get_new_range('R', 6, 7)
        self.assertListEqual([7, 7], result)

    def test_get_row_id(self):

        test_data = [{'bp':'BFFFBBFRRR', 'row_id':70},
                     {'bp':'FFFBBBFRRR', 'row_id':14},
                     {'bp':'BBFFBBFRLL', 'row_id':102}]

        for record in test_data:
            row_id = day5.get_row_id(record['bp'])
            self.assertEqual(record['row_id'], row_id)

    def test_get_col_id(self):

        test_data = [{'bp':'BFFFBBFRRR', 'col_id':7},
                     {'bp':'FFFBBBFRRR', 'col_id':7},
                     {'bp':'BBFFBBFRLL', 'col_id':4}]

        for record in test_data:
            col_id = day5.get_col_id(record['bp'])
            self.assertEqual(record['col_id'], col_id)

if __name__ == '__main__':
    unittest.main()