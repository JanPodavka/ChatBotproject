# imports
import locale
import re
import urllib
import nltk
import unidecode
import pytz
from datetime import datetime
from datetime import date

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

# define app routes
@app.route("/")
def test():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    question = request.args.get('msg')
    answer = get_answer(question)
    return str(answer)


def current_course():
    url = 'https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt?date={0:dd\.MM\.yyyy}'
    req = urllib.request.Request(url)
    req.add_header('x-api-key', '45TzSCfYbT9SgA28vSO9rdxQHO3YKML6M4Qi045d')
    response = urllib.request.urlopen(req)
    data = str(response.read()).replace("\\n", "\n")
    kurz = re.findall(r'EUR{1}[|]{1}[\d,]*', data)[0].split("|")[1]
    date = re.findall(r'\d{2}[.]\d{2}[.]\d{4}', data)[0]
    return date, kurz


def get_data(day, month, year):
    today = day + "." + month + "." + year
    url = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/vybrane.txt?od=01.01.' + str(year) + '&do=' + today + '&mena=EUR&format=txt'
    req = urllib.request.Request(url)
    req.add_header('x-api-key', '45TzSCfYbT9SgA28vSO9rdxQHO3YKML6M4Qi045d')
    response = urllib.request.urlopen(req)
    data = str(response.read()).split("\\n")
    del data[0]
    del data[0]
    del data[len(data) - 1]
    return data


def history_course(count_days=14):
    curr_year = datetime.now().strftime('%Y')
    curr_day = datetime.now().strftime('%d')
    curr_month = datetime.now().strftime('%m')
    data = get_data(curr_day, curr_month, curr_year)
    if len(data) < count_days:
        data = get_data(curr_day, curr_month, str(int(curr_year)-1)) + data
    data = data[-count_days:]
    ret_data = "Kurz za poslednich " + str(count_days) + " dni:<br>"
    for day in data:
        ret_data += day.replace("|", " ") + ' CZE/EUR<br>'
    return ret_data



def get_answer(question):
    norm_question = unidecode.unidecode(question.lower())
    if nltk.edit_distance(norm_question, "jaky je cas?") < 2:
        now = datetime.now(pytz.timezone('CET'))
        return now.strftime("%H:%M:%S")
    elif nltk.edit_distance(norm_question, "jaky je kurz eura?") < 2:
        date, course = current_course()
        return "Aktualni kurz ke dni " + date + " je " + course + " CZE/EUR"
    elif nltk.edit_distance(norm_question, "jak se jmenujes?") < 2:
        return "Jmenuji se Chatbot"
    elif nltk.edit_distance(norm_question, "jaka je historie kurzu eura?") < 2:
        return history_course()
    elif nltk.edit_distance(norm_question, "help?") < 2:
        return "Jaký je čas?<br>Jaký je kurz?<br>Jak se jmenuješ"
    else:
        return "nerozumím"


if __name__ == "__main__":
    app.run()
