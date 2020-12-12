import unittest


def circle(r):
    pi = 3.14
    res = pi * r * 2
    return res


class TestSum(unittest.TestCase):

    def test_circle(self):
        assert circle(5) == 78.5, ''

    def test_sum(self):
        assert sum([1, 2, 3]) == 6, 'should be 6'
        print(True)

    def test_sum_tuple(self):
        assert sum((1, 2, 3)) == 6, 'should be 6'


if __name__ == '__main__':
    test_sum()
    test_sum_tuple()
    test_circle(78.5)
    print('Everything is ok')
