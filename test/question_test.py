import time
from app import get_answer

uncorrect_answer = "nerozumím"
correct_answer_name = "Jmenuji se Chatbot"


def test_name_positive():
    assert get_answer("jak se jmenujes") == correct_answer_name
    assert get_answer("jak se jmenuješ") == correct_answer_name
    assert get_answer("Jak se jmenujes") == correct_answer_name
    assert get_answer("Jak se jmenujes?") == correct_answer_name
    assert get_answer("Jak se jmenuješ?") == correct_answer_name


def test_name_negative():
    assert get_answer("jake je tve jmeno") == uncorrect_answer
    assert get_answer("jak se menujes") == uncorrect_answer
    assert get_answer("") == uncorrect_answer
    assert get_answer("Jak te pojmenovali tvy rodice") == uncorrect_answer
    assert get_answer("jmeno tve") == uncorrect_answer


def test_time_positive():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    assert get_answer("jaky je cas?") == current_time
    assert get_answer("jaky je cas") == current_time
    assert get_answer("jaky je čas") == current_time
    assert get_answer("jaky je čas?") == current_time
    assert get_answer("Jaky je cas") == current_time
    assert get_answer("Jaky je čas?") == current_time
    assert get_answer("Jaky je cas?") == current_time
    assert get_answer("Jaky je čas") == current_time


def test_time_negative():
    assert get_answer("Mas hodinky?") == uncorrect_answer
    assert get_answer("Kolik je hodin") == uncorrect_answer
    assert get_answer("jakyjecas") == uncorrect_answer
    assert get_answer("Más slunecni hodiny") == uncorrect_answer
    assert get_answer("What time is it?") == uncorrect_answer
    assert get_answer("Čas?????????") == uncorrect_answer

