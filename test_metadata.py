import unittest
import metadata


class TestMetadata(unittest.TestCase):

    def test_ConvertDate(self):
        expected = '39:13'
        actual = metadata.convertDate('PT39M13S')
        self.assertEqual(expected, actual)
    
    def test_ConvertDate2912(self):
        expected = '29:12'
        actual = metadata.convertDate('PT29M12S')
        self.assertEqual(expected, actual)
if __name__ == '__main__':
    unittest.main()

