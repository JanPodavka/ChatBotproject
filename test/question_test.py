import random
import urllib
from datetime import datetime
from app import get_answer
from app import course_recommendation
from app import get_recomendation_data
import pytz
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

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
    assert get_answer("") == uncorrect_answer


def test_time_positive():
    time_zone = pytz.timezone('Europe/Prague')
    t = datetime.now(time_zone)
    current_time = t.strftime("%H:%M:%S")
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
    assert get_answer("") == uncorrect_answer


def test_course_negative():
    assert get_answer("jaky je kursz") == uncorrect_answer
    assert get_answer("kolik je za euro") == uncorrect_answer
    assert get_answer("") == uncorrect_answer
    assert get_answer("kolik stoji euro") == uncorrect_answer
    assert get_answer("jaky je kurz dolaru") == uncorrect_answer
    assert get_answer("jaky je kursk?") == uncorrect_answer


def test_course_positive():
    url = 'https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt?date={0:dd\.MM\.yyyy}'
    req = urllib.request.Request(url)
    req.add_header('x-api-key', 'i562s3R0gL3DbL0Pr6D0o1JjsTSAUgA9a1KlNhtB')
    response = urllib.request.urlopen(req)
    data = str(response.read()).split("\\n")
    course = [s for s in data if "EUR" in s][0].split("|")[4]
    date = data[0].split(" ")[0].split("'")[1]
    current_answer = "Aktualni kurz ke dni " + date + " je " + course + " CZE/EUR"
    assert get_answer("jaky je kurz eura?") == current_answer
    assert get_answer("jaky je kurz eura") == current_answer
    assert get_answer("jaký je kurz eura?") == current_answer
    assert get_answer("jaký je kurz eura") == current_answer
    assert get_answer("Jaký je kurz eura") == current_answer
    assert get_answer("Jaký je kurz eura?") == current_answer


def test_help_positive():
    correct_answer = 'Jaký je čas?<br>Jaký je kurz?<br>Jak se jmenuješ'
    assert get_answer("help") == correct_answer
    assert get_answer("Help") == correct_answer
    assert get_answer("help?") == correct_answer
    assert get_answer("Help?") == correct_answer


def test_help_negative():
    assert get_answer("Pomoooc?") == uncorrect_answer
    assert get_answer("") == uncorrect_answer
    assert get_answer("Help me") == uncorrect_answer
    assert get_answer("Jake mohu mít otázky") == uncorrect_answer
    assert get_answer("Pomoz mi") == uncorrect_answer
    assert get_answer("Help plllz") == uncorrect_answer


def test_history_courses_negative():
    assert get_answer("jaka je historie kurzu?") == uncorrect_answer
    assert get_answer("historie kurzu?") == uncorrect_answer
    assert get_answer("jaky je historie kurzu eura") == uncorrect_answer
    assert get_answer("") == uncorrect_answer
    assert get_answer("Pomoz mi, za kolik bylo euro") == uncorrect_answer


def get_data(year):
    url = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/vybrane.txt?od=01.01.' + year + '&do=31.05.' + year + '&mena=EUR&format=txt'
    req = urllib.request.Request(url)
    req.add_header('x-api-key', 'i562s3R0gL3DbL0Pr6D0o1JjsTSAUgA9a1KlNhtB')
    response = urllib.request.urlopen(req)
    data = str(response.read()).split("\\n")
    del data[0]
    del data[0]
    del data[len(data) - 1]
    return data


def get_history_courses_data(count_days):
    curr_year = datetime.today().year
    curr_day = datetime.now().strftime('%d')
    curr_month = datetime.now().strftime('%m')
    url = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/vybrane.txt?od=01.01.' + str(curr_year-1) + '&do='+curr_day+'.'+curr_month+'.' + str(curr_year) + '&mena=EUR&format=txt'
    req = urllib.request.Request(url)
    req.add_header('x-api-key', 'i562s3R0gL3DbL0Pr6D0o1JjsTSAUgA9a1KlNhtB')
    response = urllib.request.urlopen(req)
    data = str(response.read()).split("\\n")
    data = data[2:len(data) - 1]
    data = data[-count_days:]
    ret_data = "Kurz za poslednich " + str(count_days) + " dni:<br>"
    for day in data:
        ret_data += day.replace("|", " ") + ' CZE/EUR<br>'
    return ret_data


def get_recomend_courses(today_courses, hist_courses):
    recomendation_by_down = True
    for it in range(len(hist_courses)-1):
        if hist_courses[it] < hist_courses[it+1]:
            recomendation_by_down = False
            break
    mean = sum(hist_courses)/3
    recomendation_by_mean = today_courses < (mean + (10 / 100 * mean))
    recomendation = recomendation_by_down or recomendation_by_mean
    return recomendation, recomendation_by_down, recomendation_by_mean, today_courses, round(mean, 3), round(hist_courses[0] - today_courses, 3), round(today_courses - mean + (10 / 100 * mean), 3)


def test_recomen_courses():
    print()
    for i in range(10):
        courses = [None] * 4
        for it, cours in enumerate(courses):
            courses[it] = round(random.uniform(20, 30), 3)
        assert course_recommendation(courses) == get_recomend_courses(courses[3], courses[0:3])
        print("Test %d." %i )

def get_recomen_data():
    data = get_history_courses_data(4)
    data = data.split("<br>")
    del data[0]
    courses = []
    for dat in data:
        if dat != "":
            course = dat.split(" ")
            course = course[1].replace(",", ".")
            courses.append(float(course))
    return courses


def test_recomen_data():
    assert get_recomendation_data() == get_recomen_data()

def test_recomen_answer_positive():
    courses = get_recomen_data()
    recomondation, recomendation_by_down, recomendation_by_mean, today_course, mean, diff_courses, ten_percent = get_recomend_courses(courses[3], courses[0:3])
    odpoved = []
    if recomondation:
        odpoved.append("Ano, kurz eura je dnes doporucen.<br>")
    else:
        odpoved.append("Ne, kurz eura neni dnes doporucovan.<br>")
    odpoved.append("Dnesni kurz: %.3f CZE/EUR <br>" % today_course)
    odpoved.append("Prumer za posledni tři dny: %.3f CZE/EUR <br>" % mean)
    if diff_courses > 0:
        odpoved.append("Kurz vzrostl za posledni tri dny o %.3f <br>" % diff_courses)
    else:
        odpoved.append("Kurz klesl za posledni tri dny o %f <br>" % abs(diff_courses))

    if recomendation_by_down:
        odpoved.append("Kurz posledni tri dny pouze klesá. <br>")
    else:
        odpoved.append("Kurz posledni tri dny je nestabilni. <br>")

    if recomendation_by_mean:
        odpoved.append("Kurz se nezvysil o více nez 10 procent z prumeru poslednich tri dni<br>")
        odpoved.append("Kurz by se nedal doporucit pokud by vzrostl o %.3f na %.3f CZE/EUR <br>" % (ten_percent, today_course + ten_percent))
    else:
        odpoved.append("Kurz se zvysil o více nez 10 procent z prumeru za posledni tri dny<br>")
        odpoved.append("Kurz by se dal doporucit pokud by klesl o %.3f na %.3f <br>" % (ten_percent, today_course + ten_percent))

    assert get_answer("Doporucujes mi euro?") == "".join(odpoved)
    assert get_answer("Doporucujes mi euro") == "".join(odpoved)
    assert get_answer("Doporucuješ mi euro?") == "".join(odpoved)
    assert get_answer("doporucuješ mi euro") == "".join(odpoved)

def test_recomen_answer_negative():
    assert get_answer("Doporucujes euro?") == uncorrect_answer
    assert get_answer("Doporucujes mi dnes euro") == uncorrect_answer
    assert get_answer("") == uncorrect_answer
    assert get_answer("doporucuješ mi eura dnes") == uncorrect_answer