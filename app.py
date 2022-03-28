def test_tests(a, b):
    if a > b:
        return 5
    else:
        return 0


if __name__ == '__main__':
    print(test_tests(5, 4))
    print(test_tests(4, 5))
    print(test_tests(7, 5))
