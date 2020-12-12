import unittest


def circle(r):
    pi = 3.14
    res = pi * r ** 2
    return res


class TestSum(unittest.TestCase):

    def test_circle(self):
        self.assertEqual(circle(5), 78.5, 'should be 78.5')

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, 'should be 6')

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 6, 'should be 6')


if __name__ == '__main__':
    unittest.main()
