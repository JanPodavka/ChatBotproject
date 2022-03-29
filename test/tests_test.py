import app



def testing():
    """
       ret 5
    """
    assert app.test_tests(5, 4) == 5


def testing_no():
    """
        ret 0
    """
    assert app.test_tests(4, 5) == 0
