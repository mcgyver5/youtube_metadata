import unittest


class TestMetadata(unittest.TestCase):

    def test_ConvertDate(self):
        expected = '12:06'
        actual = '12:16'
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

