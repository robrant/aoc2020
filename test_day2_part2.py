import unittest
import day2_part2

class TestDay2Part2(unittest.TestCase):

    def test_valid(self):

        test_data = [
            {'pswd':'abcdefg', 'pwsd_chr':'a', 'chr_pos_1':1, 'chr_pos_2':3},
            {'pswd':'abcdefg', 'pwsd_chr':'c', 'chr_pos_1':1, 'chr_pos_2':3}
        ]
        for data in test_data:
            res = day2_part2.validate_password(data['pswd'],
                                               data['pwsd_chr'],
                                               data['chr_pos_1'],
                                               data['chr_pos_2'])
            self.assertTrue(res)

    def test_invalid(self):

        test_data = [
            {'pswd':'abcdefg', 'pwsd_chr':'a', 'chr_pos_1':2, 'chr_pos_2':4},   # neither
            {'pswd':'abcdefgc', 'pwsd_chr':'c', 'chr_pos_1':3, 'chr_pos_2':8}   # both
        ]
        for data in test_data:
            res = day2_part2.validate_password(data['pswd'],
                                               data['pwsd_chr'],
                                               data['chr_pos_1'],
                                               data['chr_pos_2'])
            print (res)
            self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()