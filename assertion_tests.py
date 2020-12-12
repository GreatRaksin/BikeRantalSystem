import unittest


def circle(r):
    pi = 3.14
    res = pi * r * 2
    return res


class TestSum(unittest.TestCase):


def test_circle(result):
    assert circle(5) == result, ''


def test_sum():
    assert sum([1, 2, 3]) == 6, 'should be 6'
    print(True)


def test_sum_tuple():
    assert sum((1, 2, 3)) == 6, 'should be 6'


if __name__ == '__main__':
    test_sum()
    test_sum_tuple()
    test_circle(78.5)
    print('Everything is ok')
