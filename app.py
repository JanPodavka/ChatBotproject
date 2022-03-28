"""
    testing module
"""


def test_tests(number_one, number_two):
    """
        testing workflow
    """
    if number_one > number_two: # test
        return 5
    return 0


if __name__ == '__main__':
    print(test_tests(5, 4))
    print(test_tests(4, 5))
    print(test_tests(7, 5))
    print(test_tests(7, 5))
